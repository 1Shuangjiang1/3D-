import os
import csv

main_folder_path = 'data'  # 替换为你的主文件夹路径
output_file_path = 'label.csv'  # 替换为你想要保存标签映射表的路径

with open(output_file_path, mode='w', newline='') as csvfile:
    fieldnames = ['Filename', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for label_folder in os.listdir(main_folder_path):
        label_folder_path = os.path.join(main_folder_path, label_folder)

        if os.path.isdir(label_folder_path):
            label = label_folder.replace('label', '')

            file_list = sorted([file for file in os.listdir(label_folder_path) if file.startswith('move')])

            for i, file_name in enumerate(file_list, start=1):
                writer.writerow({'Filename': file_name, 'Label': label})

print(f"标签映射表已生成并保存至 {output_file_path}")
