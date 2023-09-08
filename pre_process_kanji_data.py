from random import shuffle, sample, choices
import handling_data
import json

source_data = r"src\n_kanji_list.json"
# source_data = r"n_kanji_list.json"
# source_old = r"C:\Users\HF_FL\Documents\Python_Scripts\10-Oct_2022\tkinter_kanji_quiz\src\n_kanji_list_old.json"


# jlpt = "N1"
def return_kanji_data(jlpt):
    num_data, returned_data = handling_data.fetch_kanji(source_data, jlpt)

    # query = "Meaning of"
    add_questions = []
    for ideogram, meaning in returned_data:
        item = f"{ideogram}, {meaning}"  # in splitlines manner
        add_questions.append(item)

    alt1 = add_questions.copy()  # turn string into list

    # move feedback to left
    alt_1_copy = alt1.copy()  # copying to sol

    question_object = []  # No prompt following
    answers = []
    for q in alt1:
        q, ans_list = q.split(",")
        question_object.append(q)
        answers.append(ans_list)

    # questionaire = []
    choice_letter = []
    letters = "abcd"

    list_of_questions = []
    # correct_score = 0
    for n in range(
        0, num_data
    ):  # n outputs 79 instead of 80, unsure if num_data is why
        try:
            correct_answer = alt_1_copy[n].split(",")[1]
            related_index = answers.index(correct_answer)
            answers.pop(related_index)
            shuffle(answers)
            # So, this is the multiple choice randomizer!
            a2, a3, a4 = sample(answers, k=3)
            x = [correct_answer, a2, a3, a4]  # this runs out of guesses to sample?
            shuffle(x)  # it raises an error...
            index_of_correct = x.index(correct_answer)
            # Some crazy inter-appending here
            choice_letter.append(letters[index_of_correct])
            question_structure = {
                "question": f"What is the meaning of: {question_object[n]}",
                "correct_answer": correct_answer,
                "incorrect_answers": [a2, a3, a4],
            }
            list_of_questions.append(question_structure)

        except ValueError as e:
            print(e)
    return list_of_questions


""" json_object = json.loads(final_data)

json_object["questions"] """

""" print(list_of_questions[1]["question"])

for question in list_of_questions:
    print(question["question"]) """
