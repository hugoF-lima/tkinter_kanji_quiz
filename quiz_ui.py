from tkinter import (
    ttk,
    Tk,
    Canvas,
    Entry,
    StringVar,
    Label,
    Radiobutton,
    Button,
    messagebox,
    END,
    PhotoImage,
    Menu,
    Text,
)
import webbrowser
from quiz_brain import QuizBrain
from source_imgs import half_flag, icon_16

from pre_process_kanji_data import return_kanji_data
from random import shuffle
from question_model import Question

THEME_COLOR = "#375162"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Kanji Memorizer 練習")
        self.window.geometry("360x350")  # 250x390

        self.menu3 = Menu(self.window, tearoff=False)
        # submenu2 = Menu(self.menu3)
        self.menu3.add_command(label="About", command=self.display_about_msg)
        # self.menu3.add_cascade(label="Help", menu=submenu2)
        self.window.config(menu=self.menu3)

        # self.window.wm_attributes('-transparentcolor', self.window['bg'])
        # Display Title
        self.display_title()

        # Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=360, height=350)
        self.background_img = PhotoImage(data=(half_flag))
        self.canvas.create_image(280, 150, image=self.background_img)
        self.question_text = self.canvas.create_text(
            180,
            45,
            text="-",
            width=380,
            fill=THEME_COLOR,
            font=("Yu Mincho", 14),
        )

        self.ideogram_view = Entry(
            self.window,
            width=2,
            borderwidth="5",
            font="{Yu Mincho} 48 {}",
            justify="center",
            relief="raised",
        )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.ideogram_view.place(x=220, y=140)

        self.n_level_select = StringVar()

        self.display_question()
        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=("ariel", 9, "bold"))
        self.feedback.place(x=20, y=270)

        # Next and Quit Button
        self.next_and_quit_buttons()

        # Display four options(radio buttons)

        # self.window.wm_attributes("-transparentcolor", "red")

        # make the whole window transparent-ish
        # self.window.attributes('-alpha', 0.5)
        # Mainloop

        self.icon_16_img = PhotoImage(data=(icon_16))
        self.window.iconphoto("-default", self.icon_16_img)
        self.window.mainloop()

    def show_menu(self, event):
        if not self.menu_visible:
            self.menu3.post(event.x_root, event.y_root)
            self.menu_visible = True

    def hide_menu(self, event):
        if self.menu_visible:
            self.menu3.unpost()
            self.menu_visible = False

    def display_about_msg(self):
        def open_link(event):
            webbrowser.open(
                "discordapp/users/440639632141451286"
            )  # Replace with your desired URL

        about_text = "Made by someone. Click here for more information."
        message_box = messagebox.showinfo(title="About", message=about_text)
        about_textbox = Text(message_box, height=5, width=30)
        about_textbox.insert("1.0", about_text)
        about_textbox.configure(state="disabled", selectbackground="blue")
        about_textbox.pack()

        """ discord_link = "discordapp/users/440639632141451286"

        message_box = messagebox.showinfo(
            title="Autor",
            message=f"Made by Hugo Lima!\nYou can give me a shoutout to\nDiscord ID: {discord_link}\nEmail: hugolima720@protonmail.com",
        )
        about_label = Label(message_box, text=discord_link, fg="blue", cursor="hand2")
        about_label.pack()
        about_label.bind("<Button-1>", open_link) """

    def display_title(self):
        """Kanji Practice やるぞ"""

        # Title
        title = Label(
            self.window,
            text="Kanji Practice! やるぞ",
            width=22,
            bg="black",
            fg="white",
            font=("Yu Mincho", 20, "bold"),
        )

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        """To display the question"""
        q_text = self.quiz.next_question()
        question_body = q_text[:-1]
        ideogram = q_text[-1:]
        self.canvas.itemconfig(self.question_text, text=question_body)
        self.ideogram_view.delete(0, END)
        self.ideogram_view.insert(END, ideogram)

    def radio_buttons(self):
        """To create four options (radio buttons)"""
        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option (125 formerly)
        y_pos = 125

        # adding the options to the list
        while len(choice_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(
                self.window,
                text="",
                variable=self.user_answer,
                value="",
                font=("ariel", 12),
            )

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=25, y=y_pos)
            # radio_btn.grid(row=3, x=25, y=y_pos, column=0, columnspan=2, pady=50)

            # incrementing the y-axis position by 30
            y_pos += 30

        # return the radio buttons
        return choice_list

    def display_options(self):
        """To display four options"""
        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]["text"] = option
            self.opts[val]["value"] = option
            val += 1

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = "Correct answer! \U0001F44D"
        else:
            self.feedback["fg"] = "red"
            self.feedback["text"] = (
                "\u274E Oops! \n"
                f"The right answer is: \n {self.quiz.current_question.correct_answer}"
            )

        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()

            # destroys the self.window
            self.window.destroy()

    def next_and_quit_buttons(self):
        """To show next button and quit button"""

        # The first button is the Next button to move to the
        # next Question

        next_button = Button(
            self.window,
            text="Next",
            command=self.next_btn,
            width=5,
            bg="green",
            fg="white",
            font=("ariel", 12, "bold"),
        )

        # palcing the button on the screen
        next_button.place(x=20, y=43)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(
            self.window,
            text="Quit",
            command=self.window.destroy,
            width=5,
            bg="red",
            fg="white",
            font=("ariel", 12, " bold"),
        )

        # placing the Quit button on the screen
        quit_button.place(x=290, y=43)

    """ def start_main(self):
        self.has_started = False
        global question_bank
        list_of_questions = return_kanji_data(self.n_level_select.get())
        # On here, it directly loops, rather than processing beforehand.
        for question in list_of_questions:
            choices = []
            question_text = question["question"]
            correct_answer = question["correct_answer"]
            incorrect_answers = question["incorrect_answers"]
            for ans in incorrect_answers:
                choices.append(ans)
            choices.append(correct_answer)
            shuffle(choices)
            new_question = Question(question_text, correct_answer, choices)
            question_bank.append(new_question)
            self.has_started = True

        print(type(incorrect_answers)) """

    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # Shows a message box to display the result
        messagebox.showinfo(
            "Result", message="よし、クイズは終わった\n" f"{result}\n{correct}\n{wrong}"
        )


""" if __name__ == "__main__":
    quiz = QuizBrain(question_bank)

    quiz_ui = QuizInterface(quiz)

    print("よし、クイゾを終わった \n You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_no}") """
