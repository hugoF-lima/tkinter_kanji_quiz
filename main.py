from question_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from pre_process_kanji_data import return_kanji_data
from random import shuffle

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

question_bank = []


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame1 = tk.Frame(self.toplevel1)
        self.choice_box = ttk.Combobox(self.frame1)
        self.n_level_select = tk.StringVar()
        self.choice_box["values"] = [
            "N5",
            "N4",
            "N3",
            "N2",
            "N1 (1)",
            "N1 (2)",
            "N1 (3)",
            "N1 (4)",
            "N1 (5)",
        ]
        self.choice_box.configure(textvariable=self.n_level_select)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", fieldbackground="transparent", background="white")
        self.choice_box.grid(column="0", padx="10", pady="15", row="1")
        self.start_option = tk.Button(
            self.frame1, width=5, bg="Blue", fg="White", font=("ariel", 12, " bold")
        )
        self.start_option.configure(text="Start")
        self.start_option.configure(command=self.start_main)
        self.start_option.grid(column="1", padx="10", row="1")
        self.label2 = tk.Label(self.frame1)
        self.label2.configure(text="Choose JP N Level:")
        self.label2.grid(column="0", pady="15", row="0")
        self.frame1.configure(height="200", width="300")
        self.toplevel1.geometry("296x132")
        self.frame1.grid(column="0", row="0")
        self.toplevel1.configure(height="200", width="300")
        self.toplevel1.title("漢字レベルを選ぶ")

        # Main widget
        self.mainwindow = self.toplevel1

    def start_main(self):
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

        self.mainwindow.destroy()
        quiz = QuizBrain(question_bank)

        quiz_ui = QuizInterface(quiz)

        print("よし、クイゾを終わった \n You've completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_no}")
        print(type(incorrect_answers))

        # quiz = QuizBrain(question_bank)

        # quiz_ui = QuizInterface(quiz)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()

# Another idea:
# I've thought about using the terminal as input before launching main
# And getting the input there.
# If it works, transition to window
