import os
import pandas as pd
import numpy as np

# 定义数据文件夹路径
data_folder = "data"
# 定义标签映射表路径
label_mapping_path = "label.csv"

# 获取文件夹中的所有子文件夹（类别）
categories = os.listdir(data_folder)

# 读取标签映射表为DataFrame
label_mapping_df = pd.read_csv(label_mapping_path, header=None, names=["Filename", "Label"])

# 初始化数据和标签列表
data_list = []
labels_list = []

# 遍历每个类别的文件夹
for category in categories:
    category_path = os.path.join(data_folder, category)

    # 遍历类别文件夹中的每个Excel文件
    for file_name in os.listdir(category_path):
        file_path = os.path.join(category_path, file_name)

        # 读取Excel文件为DataFrame
        df = pd.read_excel(file_path)

        # 将DataFrame转换为NumPy数组，并添加到数据列表
        data_list.append(df.to_numpy())

        # 获取当前文件名对应的标签
        current_label = label_mapping_df.loc[label_mapping_df["Filename"] == file_name, "Label"].values[0]

        # 添加标签到标签列表
        labels_list.append(int(current_label))

# 将数据列表和标签列表转换为NumPy数组
data = np.array(data_list)
labels = np.array(labels_list)
print(data)
print(labels)


