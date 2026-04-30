# AI-Skills

一套專為學術研究與教學設計的 AI Skill 工具集，涵蓋論文寫作、文獻整理、研究方法分析與教學材料製作。所有 Skill 以結構化 prompt 設計，可部署於支援 OpenAI API 格式的 AI 平台。

---

## 目錄

- [專案簡介](#專案簡介)
- [Skill 總覽](#skill-總覽)
  - [Write Suite — 學術論文寫作套件](#write-suite--學術論文寫作套件)
  - [Method Extraction — 研究方法抽取](#method-extraction--研究方法抽取)
  - [Literature Review — 文獻整理](#literature-review--文獻整理)
  - [Teaching — 教學材料製作](#teaching--教學材料製作)
  - [Code — 程式碼說明](#code--程式碼說明)
- [設計原則](#設計原則)
- [專案結構](#專案結構)
- [授權](#授權)

---

## 專案簡介

AI-Skills 提供一系列可直接部署的 AI Skill，目標使用者為：

- 資訊管理、資訊系統及相關社會科學領域的研究者
- 準備投稿國際期刊的論文作者
- 進行系統性文獻回顧的研究團隊
- 大學教師與學生

所有 Skill 強調三個核心品質：**不捏造（no fabrication）**、**有據可查（evidence-grounded）**、**輸出可比較（comparison-ready）**。

---

## Skill 總覽

### Write Suite — 學術論文寫作套件

五個相互配合的寫作輔助工具，針對實證研究論文的不同寫作階段設計，主要適用於資訊管理與資訊系統領域，目標期刊包含 *Information & Management*、*Decision Support Systems* 等實證導向期刊。

| Skill | 主要功能 |
|---|---|
| [Abstract Title Keywords Optimizer](write-suite/abstract-title-keywords-optimizer/) | 優化論文題目、摘要、關鍵字與投稿定位 |
| [Academic Paper Translation & Polishing](write-suite/academic-paper-translation-polishing/) | 中文論文稿翻譯與英文學術潤飾 |
| [Method Results Academic Writer](write-suite/method-results-academic-writer/) | 研究方法與結果段落的學術化改寫 |
| [Reviewer Response Polisher](write-suite/reviewer-response-polisher/) | 審稿回覆與修稿說明的專業化潤飾 |
| [Theory Contribution Discussion Enhancer](write-suite/theory-contribution-discussion-enhancer/) | 理論貢獻、討論與實務意涵段落強化 |

**共同限制：** 所有 Write Suite 工具均保留原始研究設計、樣本數、統計係數、顯著性水準與假說支持結果，不更動任何研究事實。

---

### Method Extraction — 研究方法抽取

**[method-extraction-social-science](method-extraction-social-science/)**

針對社會科學、管理學與人因工程等實證研究，提取並結構化論文的研究方法設計。核心任務是重建論文的方法邏輯，而非摘要研究發現。

**適用研究類型：** 問卷調查、縱貫調查、實驗、準實驗、次級資料、面板資料、多層次研究、混合方法

**固定輸出結構：**
1. 論文方法概覽表
2. 結構化抽取 schema（JSON 格式）
3. Comparison-ready 跨篇比較表
4. 方法邏輯摘要（三段式）
5. 品質判讀（設計 / 量測 / 分析 / 報告透明度）
6. 未報告與不清楚項目清單

**參考文件：**
- [`normalized-method-labels.md`](method-extraction-social-science/references/normalized-method-labels.md) — 標準化方法術語標籤
- [`output-schema-template.md`](method-extraction-social-science/references/output-schema-template.md) — 結構化輸出模板
- [`quality-assessment-rules.md`](method-extraction-social-science/references/quality-assessment-rules.md) — 品質判讀規則
- [`type-specific-templates.md`](method-extraction-social-science/references/type-specific-templates.md) — 依研究類型的補充欄位
- [`example-output.md`](method-extraction-social-science/references/example-output.md) — 示範輸出

**輸出檔案命名規則：** 見 [`paper-title_method-extraction.md`](method-extraction-social-science/references/paper-title_method-extraction.md)

---

### Literature Review — 文獻整理

**[literature-review-organizer](literature-review-organizer/)**

整理多篇學術論文，輸出比較表、研究缺口摘要與未來研究方向建議。

**輸入來源：** PDF 檔、DOI 頁面、出版商頁面或論文直連網址

**輸出結構：**
- 論文總覽比較表（19 個欄位，含方法、樣本、理論、主要發現）
- 逐篇摘要
- 跨篇綜合分析
- 研究缺口摘要
- 未來研究方向建議

**進階選項（Deep Review）：** 變數關係分析、文獻探討草稿、研究問題與假說草案、概念架構建議

---

### Teaching — 教學材料製作

兩個專為教學場景設計的工具，輸入教材後輸出結構化筆記或練習題。

| Skill | 主要功能 |
|---|---|
| [Teaching Material Notes](teaching-material-notes/) | 將教材轉換為摘要、大綱、章節筆記或重點整理 |
| [Practice Question Generator](practice-question-generator/) | 依教材生成單選、多選、簡答題及答案解析 |

**輸入來源：** Word / PowerPoint / PDF 檔案或網頁連結（不支援 Google Drive / YouTube / Email / Slack）

---

### Code — 程式碼說明

**[code-add-comment](code-add-comment/)**

為任何程式語言的程式碼加入繁體中文注解，風格參照台灣工程團隊慣例，簡潔、行為導向。

**限制：** 僅添加注解，不修改邏輯、不進行重構或安全性建議。

---

## 設計原則

所有 Skill 共享以下設計原則：

| 原則 | 說明 |
|---|---|
| **不捏造** | 不發明來源未提及的數據、理論、方法或文獻 |
| **保留原始事實** | 統計係數、樣本數、假說方向等核心事實不得更動 |
| **有據可查** | 所有判斷與修改均需能追溯至輸入材料 |
| **輸出可比較** | 使用固定欄位與標準化術語，支援多篇或多次輸出的跨篇比較 |
| **繁體中文為主** | 重要英文術語以括號保留，兼顧中文閱讀與方法精確性 |

---

## 專案結構

```
AI-Skills/
├── write-suite/
│   ├── abstract-title-keywords-optimizer/
│   ├── academic-paper-translation-polishing/
│   ├── method-results-academic-writer/
│   ├── reviewer-response-polisher/
│   └── theory-contribution-discussion-enhancer/
├── method-extraction-social-science/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── normalized-method-labels.md
│       ├── output-schema-template.md
│       ├── quality-assessment-rules.md
│       ├── type-specific-templates.md
│       ├── example-output.md
│       └── paper-title_method-extraction.md
├── literature-review-organizer/
├── teaching-material-notes/
├── practice-question-generator/
├── code-add-comment/
└── README.md
```

每個 Skill 資料夾的標準結構：

```
skill-name/
├── SKILL.md          # Skill 定義與執行規則
├── agents/
│   └── openai.yaml   # 部署設定（display name、model、icon 等）
└── references/       # 輔助參考文件（模板、規則、示範輸出）
```

---

## 授權

MIT License © 2026 Cho-Hsun Lu
