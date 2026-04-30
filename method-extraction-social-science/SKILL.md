---
name: method-extraction-social-science
description: 針對社會科學、管理學、人因工程及相關領域的實證研究方法，提供專業的提取與結構化分析。使用者可利用此工具了解論文的研究設計、測量、資料收集和統計分析方法，特別適用於調查、實驗、準實驗、面板研究、多層研究、檔案研究或混合方法研究。產生結構化輸出，語言為繁體中文，保留英文方法術語，並提供簡潔的方法解釋和基於證據的品質評估，方便使用者進行比較。
---

# 任務定位

此 skill 用於抽取、整理與分析一般社會科學、管理、人因及相關實證研究論文的資料分析方法。

核心任務不是摘要研究發現，而是重建論文的方法邏輯，包含：
- 研究設計（study design）
- 樣本與資料來源（sample and data source）
- 變數或構念操作化（operationalization）
- 量測品質（measurement quality）
- 分析流程（analysis pipeline）
- 統計分析方法（statistical techniques）
- 推論或識別邏輯（inference / identification logic）
- 穩健性與效度檢查（robustness / validity checks）
- 與既有研究在方法層次上的差異（method-level difference from prior work）

此 skill 以「單篇論文」為基本處理單位，但輸出格式必須原生支援後續多篇 comparison。

輸出語言以繁體中文為主，重要方法術語保留英文於括號中，以維持跨篇比較與方法精確性。

# 適用範圍

本 skill 適用於下列一般實證研究：
- 問卷調查（survey）
- 縱貫調查（longitudinal survey）
- 實驗（experiment）
- 準實驗（quasi-experiment）
- 次級資料或檔案資料分析（archival / secondary data）
- 面板資料研究（panel data）
- 多層次研究（multilevel study）
- 混合方法研究（mixed methods）
- 質性編碼搭配量化檢驗之研究

# 不適用範圍
- 純質性研究（pure qualitative research）
- 理論建構或概念性文章（theoretical or conceptual papers without empirical methods
- 文獻回顧（literature reviews without method extraction focus）
- 方法論文章（methodological papers that do not report empirical research methods）
- 非學術研究報告（non-academic research reports or white papers）
- 其他非實證研究類型（other non-empirical research types）

# 核心原則

## 原則 1：區分研究設計、量測設計與分析方法
不可將以下三者混為一談：
- 研究設計：survey、experiment、quasi-experiment、panel 等
- 量測設計：構念如何操作化、量表來源、題項設計、信效度檢驗
- 分析方法：regression、SEM、ANOVA、HLM、DID 等

## 原則 2：不可把研究結果當成方法
顯著性、係數方向、假說支持與否，這些是研究結果，不是 method extraction 的核心內容。除非有助於理解分析流程，否則不要以結果取代方法描述。

## 原則 3：要重建分析流程，不只是列方法名稱
若論文使用多個分析步驟，應依 pipeline 順序抽取，例如：
資料清理 -> 描述統計 -> 信度/效度檢驗 -> 相關分析 -> 主模型估計 -> 中介/調節分析 -> 穩健性分析

不可只抓出一個「主要方法」就結束。

## 原則 4：不得臆測
若論文沒有清楚報告某項資訊，必須標記為：
- 未報告（not reported）
- 不清楚（unclear）
- 低信心推定（inferred with low confidence）

不可自行腦補細節。

## 原則 5：品質判讀必須以論文證據為基礎
品質評估只能根據論文明確報告的方法資訊進行。
若資訊缺乏，應標示為「報告不清楚（reporting unclear）」，而不是直接判定方法錯誤。

## 原則 6：輸出必須可比較
請盡量使用穩定、標準化的 method labels 與固定欄位名稱，避免每篇論文都用不同講法，降低後續跨篇 comparison 的困難。

參照下列 reference files：
- 標準化方法標籤：`references/normalized-method-labels.md`
- 結構化輸出模板：`references/output-schema-template.md`
- 品質判讀規則：`references/quality-assessment-rules.md`
- 類型化欄位模板：`references/type-specific-templates.md`
- 示範輸出：`references/example-output.md`

# 執行流程

## 1. 取得檔案
檔案來源可由：
- 使用者上傳 PDF
- 使用者已指定本地資料夾
- DOI、arXiv ID、PubMed ID 等識別碼以供系統自動下載
- 直接提供論文網址（需可自動抓取）
- 若已經能連接Google Drive或其他雲端存儲，詢問使用者檔案夾名稱，直接從指定資料夾讀取

## 2. 初步篩選檔案
檔案先判斷是否可以處理，標準：
- 檔案不能讀取。
- 不是 PDF 格式。
- 非學術論文，可透過標題和關鍵字辨識。
- 超過10MB或小於100KB的檔案。

符合以上任一標準，先詢問使用者是否繼續處理？
若使用者回應不處理，先將檔案移動到 `Unprocessed_Papers` 資料夾中，並附上簡短說明（例如：無法辨識論文標題、方法類型不明確等）。

## 2.辨識方法類型（method family）
先判斷論文主要屬於哪一類：
- survey
- longitudinal survey
- experiment
- quasi-experiment
- archival / secondary data
- panel data
- multilevel study
- mixed methods
- qualitative coding with quantitative validation

若同時包含多種方法類型，請先標示主要設計，再補充次要元素。

## 3. 抽取通用方法架構
所有論文都至少要抽取以下欄位：

### A. 論文基本資訊
- title
- authors
- year
- journal / venue

### B. 研究問題與理論邏輯
- research objective
- hypotheses / propositions
- theoretical logic relevant to method choice

### C. 研究設計
- design type
- method family
- time structure
- setting
- unit of analysis

### D. 樣本與資料
- sample description
- sample size
- sampling method
- context
- data source
- data collection procedure
- missing data handling
- exclusion rules

### E. 量測設計
- key constructs / variables
- operationalization
- scale source / item source
- reliability evidence
- validity evidence
- common method bias checks if applicable

### F. 分析流程
- preprocessing
- descriptive analysis
- measurement model testing
- main model estimation
- additional tests
- robustness checks

### G. 估計與檢定
- statistical techniques
- estimation method
- inference criteria
- fit indices or model evaluation
- effect size reporting
- software used

### H. 推論或識別邏輯
- causal / analytical logic
- key assumptions
- threats to validity addressed

### I. 方法貢獻
- method-level difference from prior work
- novelty in design, measurement, or analysis

### J. 證據與信心
- whether direct evidence is available
- unclear items
- extractor inference
- overall confidence

## 4. 依研究類型補充特定欄位

### 若為問卷研究（survey）
另外補充：
- respondent type
- scale format
- questionnaire source
- EFA / CFA details
- Cronbach's alpha / composite reliability / AVE
- discriminant validity
- common method bias / common method variance checks
- SEM / PLS-SEM / regression path testing
- mediation / moderation / multigroup analysis

### 若為實驗研究（experiment）
另外補充：
- treatment / manipulation
- control condition
- assignment mechanism
- randomization
- manipulation check
- pretest / posttest structure
- dependent variable timing
- covariates
- experimental setting
- ANOVA / ANCOVA / regression specification

### 若為準實驗研究（quasi-experiment）
另外補充：
- treatment definition
- comparison group
- assignment mechanism
- identification strategy
- treatment timing
- pre-period and post-period structure
- balance checks
- pre-trend checks
- endogeneity handling
- placebo / sensitivity / robustness tests

### 若為縱貫或面板研究
另外補充：
- wave structure
- time interval
- attrition handling
- lag design
- fixed effects / random effects
- within-between logic

### 若為多層次研究
另外補充：
- nested structure
- level-1 / level-2 / level-3 variables
- aggregation logic
- ICC or multilevel justification
- centering strategy
- HLM / MLM estimation details

# 固定輸出順序

除非使用者明確要求其他格式，否則一律依下列順序輸出：

1. 論文方法概覽表（paper profile）
2. 結構化抽取 schema
3. comparison-ready 表格
4. 短篇方法解釋
5. 品質判讀
6. 未報告 / 不清楚項目

不要一開始就用長篇散文摘要。

# 輸出內容格式要求

請優先依 `references/output-schema-template.md` 的模板輸出。

## 1. 論文方法概覽表
| 欄位 | 內容 |
|---|---|
| 論文標題 | |
| 研究主題 | |
| 研究設計 | |
| 方法類型 | |
| 樣本與情境 | |
| 資料來源 | |
| 分析單位 | |
| 主要變數／構念 | |
| 主要分析方法 | |
| 主要品質檢查 | |
| 方法定位一句話 | |

## 2. 結構化抽取 schema
請使用穩定欄位名稱，輸出 JSON-style 區塊。

## 3. comparison-ready 表格
請固定包含以下面向：
- 研究目的
- 研究設計
- 方法類型
- 樣本
- 情境
- 分析單位
- 資料來源
- 量測方式
- 信度／效度
- 主要統計方法
- 分析流程
- 推論／識別邏輯
- 穩健性檢查
- 方法創新點
- 與既有研究差異
- 方法限制

## 4. 短篇方法解釋
請固定輸出三小段：

### 方法邏輯摘要
說明研究問題如何對應到研究設計、量測方式與統計方法。

### 品質判讀摘要
簡要評估設計品質、量測品質、分析品質與報告透明度。

### 跨篇比較定位
說明此篇論文在未來多篇 comparison 中應如何分類。

## 5. 品質判讀
請依 `references/quality-assessment-rules.md` 進行判讀。

請分成以下四個面向，各自評等並提供 1-3 個依據：
- design quality
- measurement quality
- analysis quality
- reporting transparency

評等可用：
- high
- medium
- low
- unclear

請清楚區分：
- 真正的方法弱點
- 只是報告不清楚

## 6. 未報告 / 不清楚項目
列出所有：
- 未報告的方法資訊
- 模糊不清的細節
- 僅能低信心推定的內容

# 輸出檔案格式要求

輸出檔案格式限定為Markdown（.md），以確保跨平台兼容性與易讀性。

# 檔案處理
以上工作完成後，若已處理論文是在本地資料夾中，並且若有權限命名與移動檔案，先請求使用者同意，再將論文檔案移動在同一資料夾中，檔案夾名稱為`Readed_Papers`，並且按照以下原則處理：
- 命名格式參照 `paper-title_method-extraction.md`。
- 不符合命名格式的檔案請移動到 `Unprocessed_Papers` 資料夾中，命名格式參照 `paper-title_method-extraction.md`，並附上簡短說明（例如：無法辨識論文標題、方法類型不明確等）。

# 多研究（multiple studies）處理規則

若論文包含 Study 1、Study 2、Study 3 等多個子研究：
1. 先逐一對每個 study 做獨立 method extraction。
2. 每個 study 都維持相同 schema。
3. 最後再補一個整合比較段，說明各 study 在研究設計、樣本、量測與分析方法上的差異與互補性。

不可直接把多個 study 混成一份單一方法摘要。

# 風格要求

- 以繁體中文為主
- 重要英文方法術語保留括號
- 優先使用表格與固定欄位
- 以可比較、可重複、可複核為優先
- 若附錄或補充材料有方法資訊，應一併納入
- 若不同段落的 method 描述彼此矛盾，需明確指出
- 不要把研究結果段落當成方法段落的替代品

# 成功標準

成功的輸出應讓讀者可以：
1. 明確理解該論文如何進行資料分析
2. 直接與其他論文進行方法層次比較
3. 判斷該論文的方法報告是否完整且具可解釋性


