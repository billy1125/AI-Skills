# 檔案命名規則

所有 method extraction 處理後產出的論文檔案，統一依此規則命名。

---

## 基本格式

```
YYYY_AuthorLastName_MethodFamily_KeywordShort_method-extraction.md
```

| 欄位 | 說明 | 格式要求 |
|---|---|---|
| `YYYY` | 論文發表年份 | 4 位數字，如 `2023` |
| `AuthorLastName` | 第一作者姓氏 | 英文姓氏以 PascalCase；中文姓氏以拼音，如 `Chen`、`Wang` |
| `MethodFamily` | 研究方法類型（見下方對照表） | 固定標籤，小寫 |
| `KeywordShort` | 論文主題關鍵字 | 1-2 個英文詞，小寫，以 `-` 連接，如 `job-stress` |
| `method-extraction` | 固定後綴，識別檔案類型 | 固定不變 |

---

## MethodFamily 固定標籤對照表

| 論文設計類型 | 檔案標籤 |
|---|---|
| 問卷調查 | `survey` |
| 縱貫調查 | `longitudinal` |
| 實驗 | `experiment` |
| 準實驗 | `quasi-experiment` |
| 次級 / 檔案資料 | `archival` |
| 面板資料 | `panel` |
| 多層次研究 | `multilevel` |
| 混合方法 | `mixed-methods` |
| 質性編碼搭配量化 | `qualitative-quant` |

若論文同時包含多種設計，以**主要設計**為標籤，次要設計不出現在檔名中。

---

## 命名範例

| 情境 | 範例檔名 |
|---|---|
| 2023 年 Chen 的問卷調查，主題為工作壓力 | `2023_Chen_survey_job-stress_method-extraction.md` |
| 2021 年 Wang 的實驗，主題為決策偏誤 | `2021_Wang_experiment_decision-bias_method-extraction.md` |
| 2024 年 Lin 的準實驗，主題為政策效果 | `2024_Lin_quasi-experiment_policy-effect_method-extraction.md` |
| 2020 年 Smith 的面板研究，主題為組織績效 | `2020_Smith_panel_org-performance_method-extraction.md` |
| 2022 年 Lee 的多層次研究，主題為團隊創新 | `2022_Lee_multilevel_team-innovation_method-extraction.md` |

---

## 衝突處理規則

### 同一作者同一年有多篇
在 `AuthorLastName` 後加小寫字母 `a`、`b`、`c` 區別：

```
2023_Chen_a_survey_job-stress_method-extraction.md
2023_Chen_b_survey_burnout_method-extraction.md
```

### 論文包含多個子研究（Study 1, 2, 3）
**不**為每個 study 建立獨立檔案，統一收在同一份輸出檔中，檔名維持單篇格式。
（多 study 的處理規則見 SKILL.md「多研究處理規則」段）

---

## 跨篇比較輸出

若需要將多篇論文合併為 comparison 輸出，另存為：

```
comparison_MethodFamily_Topic_YYYY-YYYY.md
```

範例：
```
comparison_survey_job-stress_2018-2024.md
comparison_experiment_fairness_2020-2023.md
```

---

## 注意事項

- 檔名全部使用**英文與數字**，不使用中文、空格或特殊符號。
- 連接詞統一用 `-`（hyphen），欄位分隔統一用 `_`（underscore）。
- `KeywordShort` 以論文核心依變項或主題為準，不使用理論名稱（如不用 `JD-R`，改用 `job-demand`）。
- 作者為機構或匿名時，以期刊縮寫代替，如 `MISQ`、`AMJ`。
