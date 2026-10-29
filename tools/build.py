#!/usr/bin/env python3
"""把 data/ch*.txt 的單字資料轉成 JSON，嵌入 web/template.html，輸出 web/index.html。

資料格式：
  #編號|中文主題|English Theme   ← 新主題
  @分支名稱                       ← 新分支
  英文|音標|詞性|中文              ← 單字（片語的音標、詞性留空）
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def parse(path, chapter):
    themes = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            num, zh, en = line[1:].split("|")
            themes.append({"id": int(num), "ch": chapter, "zh": zh, "en": en, "branches": []})
        elif line.startswith("@"):
            themes[-1]["branches"].append({"name": line[1:], "words": []})
        else:
            w, ipa, pos, zh = line.split("|")
            themes[-1]["branches"][-1]["words"].append([w, ipa, pos, zh])
    return themes


def main():
    chapters = {1: "人物元素"}
    themes = []
    for p in sorted((ROOT / "data").glob("ch*.txt")):
        ch = int(re.search(r"ch(\d+)", p.name).group(1))
        themes += parse(p, ch)
    data = {"chapters": chapters, "themes": themes}
    tpl = (ROOT / "web" / "template.html").read_text(encoding="utf-8")
    out = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    (ROOT / "web" / "index.html").write_text(out, encoding="utf-8")
    words = sum(len(b["words"]) for t in themes for b in t["branches"])
    print(f"{len(themes)} themes, {words} words -> web/index.html")


if __name__ == "__main__":
    main()
