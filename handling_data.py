import json
import codecs

base_json = "n_kanji_list.json"


""" def list_kanji_lvl(file_access):
    list_of_kanji = []
    with codecs.open(file_access, encoding="utf-8") as file_in:
        json_set = json.load(file_in)
        total_notes = len(json_set)
        print("Number of kanji:", total_notes)
        for keys_in in json_set:
            list_of_kanji.append(keys_in)

        return total_notes, list_of_kanji """

# TODO: Find some way to sort the records of JSON.
def fetch_kanji(json_string, jlpt_lvl):
    kanji_assigns = []
    with codecs.open(json_string, encoding="utf-8") as file_in:
        json_set = json.load(file_in)
        """ total_val = len(json_set)
        print("Number of notes:", total_val) """
        for kanji_num, values in enumerate(json_set[jlpt_lvl], start=1):  # keys_in
            grab_total = int(kanji_num)
            kanji_assigns.append(values)

        return grab_total, kanji_assigns


def view_kanji(v2, list_grab):
    unpack_item = []  # ["zero_index_0", "zero_index_1", "zero_index_2"]
    for sub in list_grab[v2]:
        print(sub)
        unpack_item.append(sub)

    return unpack_item
