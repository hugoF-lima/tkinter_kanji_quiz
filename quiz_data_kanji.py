import codecs
from pre_process_kanji_data import final_data
import json

object_in = {
    "question": "What was Marilyn Monroe`s character&#039;s first name in the film &quot;Some Like It Hot&quot;?",
    "correct_answer": "Sugar",
    "incorrect_answers": ["Honey", "Caramel", "Candy"],
}

with codecs.open(final_data, encoding="utf-8") as file_in:
    json_set = json.load(file_in)
    print(json_set["questio"])
    """ total_val = len(json_set)
        print("Number of notes:", total_val) """
    for kanji_num, values in enumerate(json_set, start=1):  # keys_in
        grab_total = int(kanji_num)
        # kanji_assigns.append(values)

    # return grab_total, kanji_assigns
