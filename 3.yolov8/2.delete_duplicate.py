import os
import hashlib

def calculate_hash(file_path):
    """计算文件的MD5哈希值"""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        # 分块读取文件，防止大文件占用太多内存
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def delete_duplicate_images(folder_path):
    """删除文件夹中的重复PNG图片"""
    hashes = {}  # 用于存储文件的哈希值
    duplicate_files = []  # 用于存储重复文件的路径

    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.png'):
                file_path = os.path.join(root, file_name)
                file_hash = calculate_hash(file_path)

                # 如果哈希值已存在，表示该文件是重复的
                if file_hash in hashes:
                    duplicate_files.append(file_path)
                else:
                    hashes[file_hash] = file_path

    # 删除所有重复文件
    for file_path in duplicate_files:
        os.remove(file_path)
        print(f"删除重复文件: {file_path}")

# 使用示例：指定文件夹路径
folder_path = "images"  # 替换为你要操作的文件夹路径
delete_duplicate_images(folder_path)
