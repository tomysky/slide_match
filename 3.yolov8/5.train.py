import ultralytics
from ultralytics import YOLO

def train_model():
    # 加载YOLOv8模型
    model = YOLO('yolov8s.pt')  # 你可以选择不同的预训练模型，如'yolov8n.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'

    # 开始训练
    model.train(
        data='./target.yaml',  # 数据集的配置文件
        epochs=600,                        # 训练的轮数
        imgsz=640,                         # 输入图像的尺寸
        batch=16,                          # 批处理大小
        device='0',                        # 使用的GPU设备编号
        patience=600
          )

    # 评估模型
    model.val()

    # 导出模型
    model.export(format='onnx')  # 你可以选择其他格式，如'onnx', 'coreml', 'tflite', 等等

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()  # 确保在Windows系统上正确启动多进程
    train_model()