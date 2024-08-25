import os
import uuid
import cv2
from ultralytics import YOLO

def predict_and_draw_boxes(image_path, model):
    # 读取图像
    image = cv2.imread(image_path)

    # 进行预测
    results = model(image)

    # 解析和显示结果
    boxes = results[0].boxes.xyxy  # 获取所有预测框的坐标
    classes = results[0].boxes.cls  # 获取所有预测框的类别
    confidences = results[0].boxes.conf  # 获取所有预测框的置信度
    targets = []
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)  # 转换为整数坐标
        class_id = int(classes[i].item())  # 类别ID
        confidence = confidences[i].item()
        if confidence < 0.75:
            continue
        targets.append([confidence,(x1,y1), (x2, y2)])

    targets.sort(key=lambda x:x[0])
    target = targets[-1]
    cv2.rectangle(image, target[1], target[2], (255, 255, 0), 2)  # 绘制矩形框
    label = f'target {target[0]:.2f}'
    print(label)
    cv2.putText(image, label, (target[1][0],target[2][1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    # 显示结果图像
    cv2.imshow('Prediction', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    model_path = 'models/best.pt'  # 替换为你的模型路径
    model = YOLO(model_path)
    #单个图片测试
    # image_path = './images/0.png'  # 替换为你的图片路径
    # predict_and_draw_boxes(image_path, model)

    #多个图片测试
    files = os.listdir("test_images")
    for file in files:
        file = "test_images/"+file
        predict_and_draw_boxes(file, model)

if __name__ == '__main__':
    main()

