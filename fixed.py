import datetime
import json
import os


def parse_datetime(s):
    "24 December, 2024"
    words = s.split()
    if not len(words) == 3:
        print(s)
        return ""
    day = int(words[0])
    month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
             "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}[words[1].strip(",")]
    yr = int(words[2])
    return datetime.datetime(year=yr, month=month, day=day).strftime("%Y%m%d")


def correct_paper_infos(paper_info_json_fpath):
    with open(paper_info_json_fpath, "r", encoding="utf-8") as fin:
        paper_infos = json.load(fin)
    for paper_info in paper_infos:
        if not paper_info["arxived_date"].isdigit():
            paper_info["arxived_date"] = parse_datetime(
                paper_info["arxived_date"])
            if not paper_info["arxived_date"]:
                print(paper_info)
    with open(paper_info_json_fpath+".new", "w", encoding="utf-8") as fout:
        json.dump(paper_infos, fout)


def just_print_it(paper_details_json_fpath):
    with open(paper_details_json_fpath, "r", encoding="utf-8") as fin:
        paper_info = json.load(fin)
    for rec in paper_info:
        print(rec[0], rec[1])
        for subrec in rec[2]:
            print(subrec)


def split_openai_batch_json(openai_batch_res_jsonl, model_name, adir):
    with open(openai_batch_res_jsonl, "r", encoding="utf-8") as fin:
        for line in fin.readlines():
            if len(line.strip()) == 0:
                continue
            resp = json.loads(line)
            with open(os.path.join(adir, resp["custom_id"] + "_" + model_name + ".json"), "w", encoding="utf-8") as fout:
                print(line)
                fout.write(line)


if __name__ == '__main__':
    just_print_it(
        r"../dump_axvir_llm_jailbreak/2305.03495.tar.gz_deepseek.json")
    # correct_paper_infos("../dump_axvir_llm_jailbreak/paper_infos.json")
    # correct_paper_infos("../dump_axvir_llm_bias/paper_infos.json")
