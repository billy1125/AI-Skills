# 繪製訓練集數據：
# x_train (橫軸): 水位變化；y_train (縱軸): 流出水量
# marker="x": 點的形狀用叉叉表示
# s=40: 設定點的大小 (size)
# c='red': 設定顏色為紅色
plt.scatter(x_train, y_train, marker="x", s=40, c='red', label="Training")

# 繪製驗證集數據：
# marker="o": 點的形狀用圓圈表示
# c='blue': 設定顏色為藍色，以便與訓練集區分
plt.scatter(x_val, y_val, marker="o", s=40, c='blue', label="Validation")

# 設定圖表的輔助資訊
plt.xlabel("change in water level", fontsize=14)          # X 軸標籤與字體大小
plt.ylabel("water flowing out of the dam", fontsize=14)   # Y 軸標籤與字體大小
plt.title("Data Distribution", fontsize=16)               # 圖表標題

# 建議加上 plt.legend() 來顯示圖例，區分紅叉與藍圈
plt.legend()

# 顯示最終圖表
plt.show()