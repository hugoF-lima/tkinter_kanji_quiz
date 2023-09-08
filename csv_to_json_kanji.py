import json
import pandas as pd
import codecs

full_data = (
    r"C:\Users\HF_FL\Documents\generated_csv's\kanji_outline\n5_first_50_quotes.csv"
)

test_data = "src\generated_csv\recup_st_030-CDP_serie_10_1-05-21.csv"
# partial_data = "nf-data_partial.csv"


def combine_test(dictionaries):
    combined_dict = {}
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            combined_dict.setdefault(key, []).append(value)
    return combined_dict


mapping_first = ["name"]
mapping_second = ["japanese_quote", "english", " with_hiragana"]

df = pd.read_csv(full_data, sep=";", encoding="utf-8-sig")

wrapped_list = []
for key, group in df.groupby(mapping_first):
    for jp_quote, english, hiragana in zip(
        group["japanese_quote"], group["english"], group["with_hiragana"]
    ):
        sub_item = [f"{str(jp_quote)}", f"{english}", f"{hiragana}"]
        # sub_item_k = {f"{key}": [f"Merc = {merc}", f"ICMS = {icms}", f"ST = {st}"]}

        # sub_item_a = {f"{key}": [f"'Merc' : {merc} , 'ICMS' : {icms}, 'ST' : {st}"]}
        wrapped_list.append(sub_item)

print(wrapped_list[1])
# Former scheme
""" for key, group in df.groupby(mapping_first):
    for kanji, meaning in zip(group["Kanji"], group["Meaning"]):
        sub_item = {f"{(key)}": [f"{str(kanji)}", f"{meaning}"]}
        # sub_item_k = {f"{key}": [f"Merc = {merc}", f"ICMS = {icms}", f"ST = {st}"]}

        # sub_item_a = {f"{key}": [f"'Merc' : {merc} , 'ICMS' : {icms}, 'ST' : {st}"]}
        wrapped_list.append(sub_item) """

# print(wrapped_list)

# combined_list = combine_test(wrapped_list)


# print(combined_list)
# stringfy_dict = str(combined_list)
# print(stringfy_dict[0:3])  # Neat way to inspect irregularities on str
# json_dump = json.loads(stringfy_dict)
""" json_object = json.dumps(wrapped_list, indent=4, ensure_ascii=False)

with codecs.open("n5_first_50_quotes.json", "w", encoding="utf-8") as fp:
    fp.write(json_object)
    fp.close()
 """
