import json
import pathlib

def collect_current_deepseek_automatic_paper_summary(paper_info_json_fpath, deepseek_json_dir):
    with open(paper_info_json_fpath, "r", encoding="utf-8") as fin:
        paper_infos = json.load(fin)
        id2info = {paper_info["href"].split("/")[-1]: paper_info for paper_info in paper_infos}
    fpaths = [path for path in pathlib.Path(deepseek_json_dir).glob("*.json") if path.name.endswith(".tar.gz_deepseek.json")]
    res = []
    for fpath in fpaths:
        id_str = fpath.name[:fpath.name.index(".tar")]
        best_answer = ""
        with open(fpath, "r", encoding="utf-8") as fin:
            content = json.load(fin)
            for subcontent in content:
                answer = ""
                for text in subcontent[-1]:
                    if r"</think>" in text:
                        print(text)
                        text = text[text.rindex("</think>") + len("</think>"):]
                    if "#### **" in text:
                        answer += text[text.index("#### **"):]
                if len(answer) > len(best_answer):
                    best_answer = answer
        if len(best_answer) > 10:
            res.append(f"### {id2info[id_str]['title']}\n")
            res.append(best_answer)
            res.append("\n")

    return "".join(res)


def change_paper_infos_into_paper_infos_all_str(paper_info_json_fpath):
    with open(paper_info_json_fpath, "r", encoding="utf-8") as fin:
        paper_infos = json.load(fin)
    paper_infos_all_str_parts = ["""
Arxived Date|Published Date|Published Venue|Title|Paper|Codebase|Category|Tool Names|Benchmark Names
------------|--------------|---------------|-----|-----|--------|--------|----------|---------------
"""]
    paper_infos.sort(key=lambda d: int(d["arxived_date"]))
    for paper_info in reversed(paper_infos):
        line = f"{paper_info['arxived_date']}|-|{paper_info.get('published_conf')}|{paper_info['title']}|{paper_info['href']}|{paper_info.get('github')}|-|-|-|\n"
        paper_infos_all_str_parts.append(line)
    return "".join(paper_infos_all_str_parts)


def generate_readme(paper_info_json_fpath, deepseek_json_dir):
    paper_infos_all_str = change_paper_infos_into_paper_infos_all_str(
        paper_info_json_fpath)
    automatic_paper_summary_str = collect_current_deepseek_automatic_paper_summary(paper_info_json_fpath, deepseek_json_dir)
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
    generate_readme("../dump_axvir_llm_jailbreak/paper_infos.json", "../dump_axvir_llm_jailbreak")
