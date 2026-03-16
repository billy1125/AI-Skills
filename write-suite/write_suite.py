from pathlib import Path

base = Path('/mnt/data/paper-ai-suite')

skills = {
    'academic-paper-translation-polishing': {
        'yaml': 'interface:\n  display_name: "Academic Paper Translation Polishing"\n  short_description: "中文論文翻譯、英文潤飾與投稿版優化"\n',
        'skill': '''---
name: academic-paper-translation-polishing
description: translate chinese academic paper drafts into polished english for information management, information systems, and empirical business research. use when the user provides chinese academic text, paper sections, or full manuscripts and needs bilingual comparison, accurate translation, journal-style polishing, revision rationale, and a submission-ready english version while preserving original meaning, terminology, and data.
---

# Academic Paper Translation and Polishing
# 學術論文翻譯與潤飾

This skill translates Chinese academic writing into polished English suitable for submission-oriented writing in information management and information systems research.
本技能用於將中文學術寫作翻譯並潤飾為適合投稿的英文版本，特別適用於資訊管理與資訊系統研究。

The target style is practical, empirical, and readable, closer to journals such as Information & Management, Decision Support Systems, and Electronic Commerce Research.
目標風格偏向務實、實證導向、可讀性高，接近 Information & Management、Decision Support Systems、Electronic Commerce Research 常見寫法。

## Core Rules
## 核心規則

1. Preserve the original meaning exactly.  
   準確保留原意，不改動研究主張、推論方向與結論。

2. Do not alter numbers, variable names, hypotheses, coefficients, significance levels, sample sizes, or findings.  
   不可更動數值、變數名稱、假說、係數、顯著性、樣本數與研究結果。

3. Preserve technical terminology in its accepted academic form.  
   保留術語的學術慣用表達。

4. Improve academic tone, clarity, concision, and logical flow.  
   改善學術語氣、清晰度、精簡度與邏輯連接。

5. Avoid literal translation when natural academic English is better.  
   避免逐字直譯，優先使用自然且符合期刊風格的學術英文。

## Preferred Style
## 偏好風格

Prefer wording commonly seen in empirical information management papers:
優先使用資訊管理實證論文常見表達：

- this study examines
- this study investigates
- the results indicate that
- the findings suggest that
- prior research has shown
- this study contributes by
- from a managerial perspective
- the empirical results provide evidence that

Avoid overly ornate or philosophical wording.
避免過度華麗、抽象或理論炫技式用語。

## Workflow
## 工作流程

When the user provides text, follow this order:
當使用者提供文本時，依以下順序處理：

### Step 1. Identify the writing unit
### 步驟 1：辨識文本類型

Determine whether the text is:
判斷文本屬於：

- title / 題目
- abstract / 摘要
- introduction / 前言
- literature review / 文獻探討
- method / 研究方法
- results / 研究結果
- discussion / 討論
- conclusion / 結論
- reviewer response / 回覆審稿人
- full manuscript / 全文

### Step 2. Produce a faithful translation
### 步驟 2：產出忠實翻譯

Translate the Chinese text into accurate English without changing meaning.
將中文轉為忠實英文，不改變原意。

### Step 3. Produce a polished submission-oriented version
### 步驟 3：產出投稿導向潤飾版

Rewrite the English into stronger academic prose with better:
將英文再潤飾為更適合投稿的版本，提升：

- clarity / 清晰度
- concision / 精簡度
- readability / 可讀性
- coherence / 連貫性
- discipline-appropriate academic tone / 領域適配的學術語氣

### Step 4. Explain revision logic
### 步驟 4：說明修改理由

Briefly explain major improvements in Chinese.
以中文簡要說明關鍵修改理由。

## Required Output Format
## 固定輸出格式

Unless the user requests otherwise, always use this structure:
除非使用者另有要求，固定使用以下格式：

### 1. 原文 Original
[貼上中文原文]

### 2. 直譯版 Direct Translation
[忠實英文翻譯]

### 3. 潤飾版 Polished Academic Version
[更適合投稿的英文版本]

### 4. 修改說明 Revision Notes
Use concise bullet points in Chinese.
以中文條列重點說明，例如：

- 將口語表達改為較常見的學術動詞
- 簡化冗長句構，提升可讀性
- 強化因果或邏輯連接詞
- 調整語氣，使其更符合實證研究論文風格

## Domain Guidance
## 領域指引

For information management and information systems papers, prefer terminology commonly used in:
對資訊管理與資訊系統論文，優先採用下列常見術語慣例：

- information systems
- information management
- digital transformation
- platform governance
- business analytics
- user adoption
- continuance intention
- organizational performance
- firm performance
- knowledge sharing
- technology acceptance
- trust
- perceived usefulness
- perceived ease of use
- innovation capability
- supply chain integration
- e-commerce
- fintech
- artificial intelligence adoption

Do not replace accepted domain terms with casual synonyms.
不要把已固定的領域術語改成口語近義詞。

## Long Text Handling
## 長文本處理

For long sections or full papers:
對於長段落或全文：

1. process paragraph by paragraph
2. keep terminology consistent across paragraphs
3. preserve section intent
4. flag ambiguous source wording when necessary

若中文原文本身表意模糊，可指出「原文此處可能有歧義」，但不要自行改寫成新的研究結論。

## Quality Threshold
## 品質門檻

The polished version should sound suitable for practical, empirical journals rather than highly abstract theory-heavy journals.
潤飾版應更像務實、實證型期刊，而非高度抽象或理論堆疊型期刊。

Prefer:
優先：

- direct claims
- clear variable relationships
- concise reporting language
- readable transitions

Avoid:
避免：

- inflated rhetoric
- vague grand claims
- unnecessary complexity
'''
    },
    'abstract-title-keywords-optimizer': {
        'yaml': 'interface:\n  display_name: "Abstract Title Keywords Optimizer"\n  short_description: "題目、摘要、關鍵字與投稿定位優化"\n',
        'skill': '''---
name: abstract-title-keywords-optimizer
description: optimize academic titles, abstracts, keywords, and contribution-focused summaries for information management and empirical information systems research. use when the user needs chinese or english title and abstract refinement, stronger journal-style phrasing, clearer research positioning, and bilingual output aligned with practical empirical journals such as information and management, decision support systems, and electronic commerce research.
---

# Abstract Title Keywords Optimizer
# 題目摘要關鍵字優化器

This skill improves titles, abstracts, keywords, and short contribution summaries for empirical papers in information management and information systems.
本技能專門優化資訊管理與資訊系統實證論文的題目、摘要、關鍵字與研究亮點摘要。

## Purpose
## 目的

Help the user make the paper easier to understand, easier to evaluate, and more aligned with submission-oriented writing.
協助使用者讓論文更容易被理解、被審閱，並更符合投稿導向寫法。

## Core Rules
## 核心規則

1. Preserve the original research design, variables, findings, and contribution claims.  
   保留原本研究設計、變數、發現與貢獻主張。

2. Do not invent theories, methods, or findings.  
   不可虛構理論、方法或結果。

3. Prefer practical and readable title and abstract wording.  
   題目與摘要優先清楚、務實、易讀。

4. Make the research question, method, findings, and contribution explicit.  
   清楚標示研究問題、方法、主要發現與貢獻。

## Title Optimization Rules
## 題目優化規則

A good title should be:
好的題目應具備：

- specific / 具體
- readable / 易讀
- informative / 資訊充分
- not overly long / 不過長
- aligned with the actual method or context / 與研究方法或情境一致

Prefer these title patterns:
優先使用這些題目結構：

- The impact of X on Y: Evidence from ...
- Understanding X in the context of ...
- Examining the relationship between X and Y
- How X influences Y: An empirical study of ...
- Investigating X and Y in ...

Avoid:
避免：

- vague broad titles
- poetic titles
- overly clever wordplay
- titles that claim more than the paper proves

## Abstract Optimization Rules
## 摘要優化規則

A strong abstract should clearly cover:
好的摘要應明確包含：

1. background or problem context
2. research purpose
3. method or data
4. key findings
5. contribution or implication

When rewriting abstracts:
重寫摘要時：

- remove redundancy
- clarify variable relationships
- state method and sample clearly when available
- make findings explicit
- end with contribution or implication

## Keywords Optimization Rules
## 關鍵字優化規則

Prefer keywords that are:
關鍵字應：

- discipline-relevant
- searchable
- conceptually precise
- not merely repeated from the title unless appropriate

For information management papers, prefer combinations of:
對資訊管理論文，常見可優先考慮：

- digital transformation
- information systems
- business analytics
- organizational performance
- technology adoption
- user behavior
- e-commerce
- platform governance
- artificial intelligence
- trust
- continuance intention
- innovation capability

## Required Output Format
## 固定輸出格式

If the user provides a draft title or abstract, return:
若使用者提供題目或摘要草稿，輸出：

### 1. 原始版本 Original
[原文]

### 2. 優化建議版 Optimized Version
[英文優化版]

### 3. 備選版本 Alternative Version
[另一個偏不同風格的版本]

### 4. 修改理由 Revision Notes
用中文簡述修改邏輯，包括：
- 題目更聚焦
- 摘要結構更完整
- 關鍵字更適合檢索
- 學術語氣更自然

If keywords are requested, also return:
若有關鍵字需求，另附：

### 5. 建議關鍵字 Suggested Keywords
- keyword 1
- keyword 2
- keyword 3
- keyword 4
- keyword 5

## Style Preference
## 風格偏好

The style should be more readable and practical than highly theoretical journals.
風格應比高度理論型期刊更可讀、更務實。

Prefer concise, direct statements over abstract positioning language.
優先精簡直接，不堆疊空泛定位語句。
'''
    },
    'reviewer-response-polisher': {
        'yaml': 'interface:\n  display_name: "Reviewer Response Polisher"\n  short_description: "回覆審稿人與修稿說明專業化"\n',
        'skill': '''---
name: reviewer-response-polisher
description: polish reviewer response letters and point-by-point rebuttals for academic papers in information management and information systems. use when the user provides chinese or english responses to reviewers and needs a more professional, respectful, precise, and submission-ready version with bilingual explanation while preserving the original substantive response and revision claims.
---

# Reviewer Response Polisher
# 回覆審稿人潤飾器

This skill rewrites reviewer responses into a professional, respectful, clear, and submission-ready style.
本技能將回覆審稿人的文字潤飾為專業、禮貌、清楚且可投稿的版本。

## Core Goal
## 核心目標

Help the author sound:
協助作者呈現出：

- respectful but not submissive / 尊重但不卑微
- confident but not defensive / 有根據但不防禦性過強
- precise and traceable / 精確且可對照
- cooperative and revision-oriented / 展現配合修正的態度

## Core Rules
## 核心規則

1. Preserve the actual response content.  
   保留原本實質回應內容。

2. Do not fabricate revisions that were not made.  
   不可虛構未進行的修正。

3. Do not exaggerate agreement if the author is only partially accepting the comment.  
   若只是部分接受意見，不可假裝完全同意。

4. When disagreeing, use calm and evidence-based phrasing.  
   若不同意審稿意見，語氣需冷靜、有理有據。

## Preferred Tone
## 建議語氣

Prefer expressions such as:
優先使用以下表達：

- We thank the reviewer for this insightful comment.
- We appreciate this valuable suggestion.
- In response to this comment, we have revised ...
- We have clarified this point in the revised manuscript.
- We respectfully note that ...
- To address this concern, we now ...
- We agree that this issue required clearer explanation.

Avoid:
避免：

- emotional language
- defensive language
- over-apologizing
- vague statements without revision trace

## Response Strategy
## 回覆策略

For each reviewer comment:
對每則審稿意見：

1. acknowledge the comment politely
2. state the action taken
3. summarize the revision
4. point to where the revision appears if available
5. if disagreeing, explain the rationale carefully

## Handling Disagreement
## 處理不同意見

When the author does not fully agree, use wording like:
當作者不完全同意時，可用：

- We appreciate the reviewer’s perspective. However, ...
- We respectfully suggest that ...
- We agree in part and have clarified ...
- While we understand this concern, our study focuses on ...

Never sound confrontational.
不可帶有對抗語氣。

## Required Output Format
## 固定輸出格式

### 1. 原始回覆 Original Response
[原文]

### 2. 潤飾版 Polished Response
[英文潤飾版]

### 3. 修改說明 Revision Notes
用中文說明：
- 語氣更禮貌
- 回應更明確
- 更像 point-by-point rebuttal
- 不同意時更具學術說服力

If the user provides reviewer comments together with draft responses, organize as:
若使用者同時提供審稿意見與回覆草稿，格式整理為：

Reviewer Comment
[comment]

Polished Response
[response]

Revision Notes
[中文說明]

## Journal Style Preference
## 期刊風格偏好

Use a professional but practical tone.
採用專業但務實的語氣。

Do not make responses sound overly legalistic or overly emotional.
不要讓回覆像法律辯駁，也不要過度情緒化。
'''
    },
    'theory-contribution-discussion-enhancer': {
        'yaml': 'interface:\n  display_name: "Theory Contribution Discussion Enhancer"\n  short_description: "理論貢獻、討論與實務意涵強化"\n',
        'skill': '''---
name: theory-contribution-discussion-enhancer
description: strengthen theory, contribution, discussion, and implication sections for information management and information systems research. use when the user needs help rewriting chinese or english discussion paragraphs, theoretical contributions, practical implications, or conclusion sections into clearer, more persuasive, and submission-ready academic prose with bilingual explanation while preserving the original claims and evidence.
---

# Theory Contribution Discussion Enhancer
# 理論貢獻與討論段落強化器

This skill improves discussion, theoretical contribution, practical implication, and conclusion writing for empirical papers.
本技能用於強化實證研究中的討論、理論貢獻、實務意涵與結論段落。

## Goal
## 目標

Help the user express contribution more clearly without overstating the findings.
協助使用者更清楚表達研究貢獻，同時避免過度宣稱。

## Core Rules
## 核心規則

1. Do not invent contributions unsupported by the findings.  
   不可創造未被研究結果支持的貢獻。

2. Distinguish clearly between findings, theoretical contribution, and practical implication.  
   清楚區分研究發現、理論貢獻與實務意涵。

3. Keep claims proportional to the evidence.  
   主張強度需與證據強度相符。

4. Use readable and practical academic language.  
   使用清楚、務實、可讀的學術語言。

## What to Improve
## 強化重點

Improve the user's writing by:
可從以下幾方面強化：

- clarifying what the study adds to prior literature
- distinguishing confirmation from extension
- showing why the findings matter
- linking results back to theory
- translating vague value statements into precise contributions
- improving transitions between findings and implications

## Contribution Writing Guidance
## 貢獻寫作指引

Prefer contribution statements like:
優先使用這類貢獻句型：

- This study contributes to the literature by ...
- Our findings extend prior research by ...
- This study provides empirical evidence that ...
- From a theoretical perspective, the results suggest ...
- From a managerial perspective, the findings indicate ...

Avoid vague claims like:
避免空泛說法：

- This study is very important
- This study fills many gaps
- This study provides huge contributions

## Discussion Writing Guidance
## 討論段落指引

A good discussion should:
好的 discussion 應：

1. restate key findings selectively
2. interpret what they mean
3. compare them with prior research if relevant
4. explain why they matter
5. note boundary conditions when appropriate

## Practical Implication Guidance
## 實務意涵指引

Practical implications should be action-oriented.
實務意涵應具可操作性。

Prefer:
優先：

- managers should consider ...
- firms may benefit from ...
- practitioners can improve ... by ...
- platform operators should pay attention to ...

Avoid generic advice with no link to the findings.
避免與研究結果脫節的空泛建議。

## Required Output Format
## 固定輸出格式

### 1. 原文 Original
[原文]

### 2. 強化版 Enhanced Version
[英文強化版]

### 3. 修改說明 Revision Notes
以中文說明：
- 哪裡更具貢獻感
- 哪裡強化了理論連結
- 哪裡使實務意涵更具體
- 哪裡避免了過度宣稱

## Style Preference
## 風格偏好

Target the style of practical empirical journals, not theory-maximizing journals.
以務實型實證期刊風格為主，不追求過度理論化。

Prefer clarity over density.
清楚勝於堆疊。
'''
    },
    'method-results-academic-writer': {
        'yaml': 'interface:\n  display_name: "Method Results Academic Writer"\n  short_description: "研究方法、假說與結果段落英文化"\n',
        'skill': '''---
name: method-results-academic-writer
description: write and polish method and results sections for empirical papers in information management and information systems. use when the user provides chinese or english drafts about research design, measures, data collection, hypotheses, statistical analysis, or findings and needs clearer, more rigorous, and submission-ready academic writing with bilingual explanation while preserving the original design, data, and statistical meaning.
---

# Method Results Academic Writer
# 研究方法與結果寫作器

This skill improves the writing of method and results sections for empirical academic papers.
本技能專門優化實證研究論文中的研究方法與研究結果段落。

## Scope
## 適用範圍

Use for:
適用於：

- research design / 研究設計
- sample and data collection / 樣本與資料蒐集
- measures / 變數與量表
- hypothesis statements / 假說陳述
- analysis procedure / 分析程序
- regression / SEM / PLS-SEM / mediation / moderation reporting
- findings and hypothesis support statements / 結果報告與假說支持情形

## Core Rules
## 核心規則

1. Preserve methodological facts exactly.  
   精確保留方法事實。

2. Do not alter sample size, model type, coefficients, p-values, fit indices, or support status.  
   不可更動樣本數、模型類型、係數、p 值、配適指標與假說支持情況。

3. Make the wording more rigorous, concise, and readable.  
   提升嚴謹度、精簡度與可讀性。

4. Avoid over-interpreting the results in the results section.  
   在 results 段落避免過度解讀。

## Method Writing Guidance
## 方法段落指引

Method writing should be:
方法段落應：

- clear
- procedural
- replicable
- logically ordered

Prefer structures such as:
可優先採用：

- Data were collected from ...
- The sample consisted of ...
- We measured X using ...
- All items were adapted from prior studies.
- We used a three-step procedure to ...
- To test the hypotheses, we employed ...

## Results Writing Guidance
## 結果段落指引

Results writing should:
結果段落應：

- report findings accurately
- distinguish reporting from interpretation
- state hypothesis support clearly
- use discipline-standard reporting phrases

Preferred phrases:
優先用語：

- The results show that ...
- The analysis indicates that ...
- Hypothesis 1 was supported.
- The effect of X on Y was positive and significant.
- The interaction term was significant, suggesting that ...
- The mediation analysis revealed that ...

Avoid:
避免：

- dramatic wording
- exaggerated interpretation
- repeating every table value in prose unless needed

## Hypothesis Writing Guidance
## 假說寫作指引

When the user provides rough hypotheses, rewrite them to be concise and academically standard.
當使用者提供粗略假說時，將其改寫為精簡、學術標準的形式。

Example patterns:
例如：

- X positively affects Y.
- X is positively associated with Y.
- Y mediates the relationship between X and Z.
- Z moderates the relationship between X and Y.

## Required Output Format
## 固定輸出格式

### 1. 原文 Original
[原文]

### 2. 潤飾版 Polished Version
[英文潤飾版]

### 3. 修改說明 Revision Notes
以中文說明：
- 哪裡更嚴謹
- 哪裡更符合方法或結果寫法
- 哪裡去除了口語或重複
- 哪裡改善了統計敘述表達

If the user is writing hypotheses, also provide:
若是寫假說，可另附：

### 4. 假說格式建議 Hypothesis Formatting Suggestion
[更標準的 H1, H2, H3 表述]

## Section-Specific Reminders
## 章節特定提醒

For method sections:
方法段落：

- prioritize procedural clarity
- make measurement and sampling descriptions concise
- preserve instrument source information if present

For results sections:
結果段落：

- report what the analysis found
- avoid moving too much implication into the results section
- keep interpretation proportional to evidence
'''
    }
}

readme = '''# Paper AI Suite

A bundled project containing five standalone academic writing skills for information management and information systems research.

## Included skills

1. academic-paper-translation-polishing
2. abstract-title-keywords-optimizer
3. reviewer-response-polisher
4. theory-contribution-discussion-enhancer
5. method-results-academic-writer

## Notes

- Each skill is independently packageable and uploadable.
- Each packaged archive is named `skill.zip` inside that skill's `dist/` folder.
- This suite archive is a convenience bundle for download and local organization. It is not a single uploadable skill because the platform expects one skill per packaged archive.
'''

(base / 'README.md').write_text(readme, encoding='utf-8')

for name, data in skills.items():
    skill_dir = base / name
    (skill_dir / 'SKILL.md').write_text(data['skill'], encoding='utf-8')
    (skill_dir / 'agents' / 'openai.yaml').write_text(data['yaml'], encoding='utf-8')
    for sub in ['scripts', 'references', 'assets']:
        p = skill_dir / sub
        if p.exists():
            for child in p.rglob('*'):
                if child.is_file():
                    child.unlink()
            for child in sorted(p.rglob('*'), reverse=True):
                if child.is_dir():
                    child.rmdir()
            p.rmdir()

print('wrote suite')
