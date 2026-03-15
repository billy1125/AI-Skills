# Python 註解風格參考

## 風格原則
- 使用繁體中文，偏台灣工程團隊常用語氣
- 句子短，不寫教科書式長句
- 以「這裡在做什麼」為主，不寫過多推論
- 不寫建議語氣，例如「建議改成」「可考慮」
- 不加入情緒字眼，例如「特別注意」「很巧妙」

## 註解放置原則
- function 上方可補一行用途說明
- 複雜條件分支前補一行區塊註解
- 明顯直觀的一行指派不逐行註解
- 資料清洗、轉換、過濾等步驟可加簡短說明

## 風格範例
```python
def normalize_users(users):
    # 整理使用者資料欄位，統一輸出格式
    normalized = []

    for user in users:
        # 忽略沒有 id 的資料
        if not user.get("id"):
            continue

        # 組合前端需要的欄位結構
        normalized.append({
            "id": user["id"],
            "name": user.get("name", "").strip(),
            "email": user.get("email", "").lower(),
        })

    return normalized