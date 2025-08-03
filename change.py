import os

# 標註資料夾
label_folder = "/Users/outingan/Desktop/2025_field_robot/dataset/train/labels"

# 定義類別映射
class_map = {
    "18": "3",
    "19": "2",
    "20": "1",
    "21": "0"
}

# 處理所有 .txt 檔案
for filename in os.listdir(label_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_folder, filename)

        # 讀取每一行
        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts and parts[0] in class_map:
                parts[0] = class_map[parts[0]]  # 替換類別編號
                new_lines.append(" ".join(parts))
            else:
                new_lines.append(line.strip())  # 不在轉換範圍內的保持原樣

        # 覆蓋寫入修改後的內容
        with open(file_path, "w") as f:
            f.write("\n".join(new_lines) + "\n")

        print(f"✅ 處理完成: {filename}")

print("🎉 所有標註檔案的類別標籤已更新！")