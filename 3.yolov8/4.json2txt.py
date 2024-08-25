import json
import os

output_dir = './labels'

# 标签到类别编号的映射
label_to_id = {
    'target': 0,
}

def convert_labelme_to_yolo(json_file_path, output_dir, label_to_id):
    # 打开Labelme的JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 获取图片的宽度和高度
    image_width = data['imageWidth']
    image_height = data['imageHeight']

    # 获取标注对象
    annotations = data['shapes']

    # 输出TXT文件的路径
    output_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(json_file_path))[0] + '.txt')

    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for annotation in annotations:
            label = annotation['label']
            points = annotation['points']

            # 计算标注框的中心点、宽度和高度
            x_min = min([p[0] for p in points])
            x_max = max([p[0] for p in points])
            y_min = min([p[1] for p in points])
            y_max = max([p[1] for p in points])

            x_center = (x_min + x_max) / 2 / image_width
            y_center = (y_min + y_max) / 2 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            # 获取类别编号
            class_id = label_to_id.get(label, -1)

            # 检查标签是否在映射中
            if class_id == -1:
                print(f"标签 '{label}' 未在映射中找到。")
                continue

            # 写入YOLO格式
            out_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


def create_classes_file(output_dir, label_to_id):
    # classes.txt的路径
    classes_file_path = os.path.join(output_dir, 'classes.txt')

    # 根据label_to_id字典生成classes.txt
    with open(classes_file_path, 'w', encoding='utf-8') as f:
        for label in sorted(label_to_id, key=label_to_id.get):
            f.write(f"{label}\n")


def main():
    files = os.listdir("./labels_json")
    for file in files:
        json_file_path = "./labels_json/"+file
        print(json_file_path)
        convert_labelme_to_yolo(json_file_path, output_dir, label_to_id)

    create_classes_file(output_dir, label_to_id)

if __name__ == '__main__':
    main()
