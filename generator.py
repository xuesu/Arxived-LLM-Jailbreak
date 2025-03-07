import json
import pathlib


def generate_anchor(title):
    anchor = "".join([c for c in title.lower().replace(
        " ", "-").replace("_", "") if c.isalpha() or c in "-."])
    return anchor


def collect_current_deepseek_automatic_paper_summary(paper_info_json_fpath, deepseek_json_dir):
    with open(paper_info_json_fpath, "r", encoding="utf-8") as fin:
        paper_infos = json.load(fin)
        id2info = {paper_info["href"].split(
            "/")[-1]: paper_info for paper_info in paper_infos}
    fpaths = [path for path in pathlib.Path(deepseek_json_dir).glob(
        "*.json") if path.name.endswith(".tar.gz_deepseek.json")]
    res = []
    id2anchor = dict()
    for fpath in fpaths:
        id_str = fpath.name[:fpath.name.index(".tar")]
        best_answer = ""
        with open(fpath, "r", encoding="utf-8") as fin:
            content = json.load(fin)
            for subcontent in content:
                for texts in subcontent[-1]:
                    for text in texts.split(r"</think>"):
                        if "####" in text:
                            answer = text[text.index("####"):]
                            if len(answer) > len(best_answer):
                                best_answer = answer
                            print("answer" + "-" * 100)
                            print(answer)
        if len(best_answer) > 10:
            title = id2info[id_str]['title']
            res.append(f"### {id2info[id_str]['title']}\n")
            res.append(best_answer)
            res.append("\n")
            anchor = generate_anchor(title)
            id2anchor[id_str] = anchor
    return "".join(res), id2anchor

def collect_current_gpt4o_mini_automatic_paper_summary(paper_info_json_fpath, gpt_resp_json_dir):
    with open(paper_info_json_fpath, "r", encoding="utf-8") as fin:
        paper_infos = json.load(fin)
        id2info = {paper_info["href"].split(
            "/")[-1]: paper_info for paper_info in paper_infos}
    fpaths = [path for path in pathlib.Path(gpt_resp_json_dir).glob(
        "*.json") if path.name.endswith("_gpt-4o-mini.json")]
    res = []
    id2anchor = dict()
    for fpath in fpaths:
        id_str = fpath.name[:fpath.name.index("_gpt")]
        with open(fpath, "r", encoding="utf-8") as fin:
            resp = json.load(fin)
            best_answer = resp["response"]["body"]["choices"][0]["message"]["content"]
            
        if len(best_answer) > 10:
            title = id2info[id_str]['title']
            res.append(f"### {id2info[id_str]['title']}\n")
            res.append(best_answer)
            res.append("\n")
            anchor = generate_anchor(title)
            id2anchor[id_str] = anchor
    return "".join(res), id2anchor



def change_paper_infos_into_paper_infos_all_str(paper_info_json_fpath, id2anchor):
    with open(paper_info_json_fpath, "r", encoding="utf-8") as fin:
        paper_infos = json.load(fin)
    paper_infos_all_str_parts = ["""
Arxived Date|Published Date|Published Venue|Title|Paper|Codebase|Category|Tool Names|Benchmark Names
------------|--------------|---------------|-----|-----|--------|--------|----------|---------------
"""]
    paper_infos.sort(key=lambda d: int(d["arxived_date"]))
    for paper_info in reversed(paper_infos):
        id_str = paper_info["href"].split("/")[-1]
        title_exp = paper_info['title']
        if id_str in id2anchor:
            title_exp = f"[{paper_info['title']}](#{id2anchor[id_str]})"
        line = f"{paper_info['arxived_date']}|-|{paper_info.get('published_conf')}|{title_exp}|{paper_info['href']}|{paper_info.get('github')}|-|-|-|\n"
        paper_infos_all_str_parts.append(line)
    return "".join(paper_infos_all_str_parts)


def generate_readme(paper_info_json_fpath, deepseek_json_dir):
    # automatic_paper_summary_str, id2anchor = collect_current_deepseek_automatic_paper_summary(paper_info_json_fpath, deepseek_json_dir)
    automatic_paper_summary_str, id2anchor = collect_current_gpt4o_mini_automatic_paper_summary(
        paper_info_json_fpath, deepseek_json_dir)
    paper_infos_all_str = change_paper_infos_into_paper_infos_all_str(
        paper_info_json_fpath, id2anchor)
    with open("readme_template.md", "r", encoding="utf-8") as fin:
        md_content = fin.read()
    paper_infos_all_str_label = "`TODO{paper_infos_all_str}`"
    automatic_paper_summary_str_label = "`TODO{automatic_paper_summary}`"
    assert md_content.count(paper_infos_all_str_label) == 1
    assert md_content.count(automatic_paper_summary_str_label) == 1
    md_content = md_content.replace(
        paper_infos_all_str_label, paper_infos_all_str).replace(
        automatic_paper_summary_str_label, automatic_paper_summary_str)
    with open("README.md", "w", encoding="utf-8") as fout:
        fout.write(md_content)


if __name__ == '__main__':
    generate_readme("../dump_axvir_llm_jailbreak/paper_infos.json",
                    "../dump_axvir_llm_jailbreak")
