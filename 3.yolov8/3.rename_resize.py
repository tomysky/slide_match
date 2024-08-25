import os
import cv2


def rename_and_resize_images(folder_path, new_size=(640, 640)):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    img_count = 0  # 用于生成新文件名的计数器

    # 遍历文件夹中的所有文件
    for file_name in files:
        # 构造完整文件路径
        file_path = os.path.join(folder_path, file_name)

        # 检查是否为图片文件（你可以根据需要增加其他图片格式）
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 读取图片
            img = cv2.imread(file_path)

            if img is not None:
                # 调整图片大小为640x640
                resized_img = cv2.resize(img, new_size)

                # 构造新的文件名，数字从0开始，文件格式保持不变
                new_file_name = f"{img_count}.png"
                new_file_path = os.path.join(folder_path, new_file_name)

                # 保存重新命名和调整大小后的图片
                cv2.imwrite(new_file_path, resized_img)

                # 删除原始文件
                os.remove(file_path)

                print(f"已处理并重命名: {file_name} -> {new_file_name}")

                # 更新计数器
                img_count += 1


# 使用示例：指定文件夹路径
folder_path = "images"  # 替换为你要操作的文件夹路径
rename_and_resize_images(folder_path)
