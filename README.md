# SunnyForEnglish5000

用心智圖背英文單字 5000。

- 📱 **網頁版**（手機、電腦都能用）：https://claude.ai/artifact/JnyCvc68TiiWgWC6uWyiBC
- 📖 學習計畫：[學習計畫.md](學習計畫.md)

## 檔案

| 路徑 | 內容 |
|------|------|
| `data/ch1.txt` | 第 1 章「人物元素」15 個主題、450 字（從書上照片整理） |
| `web/template.html` | 網頁版程式 |
| `web/index.html` | 產生出來的網頁（不要直接改） |
| `tools/build.py` | 把 `data/` 的單字放進網頁：`python3 tools/build.py` |

新增章節：把新的 `data/chN.txt` 放進 `data/`（格式見 `tools/build.py` 開頭說明），在 `build.py` 的 `chapters` 加上章名，再執行 build。
