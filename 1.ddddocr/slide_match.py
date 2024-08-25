import ddddocr  # 导入 ddddocr 库，用于滑块验证码的目标检测
import cv2  # 导入 OpenCV 库，用于图像处理和显示

# 定义一个函数，用于显示背景图像并在匹配到的目标位置绘制矩形框
def cv_show(bg_path, res):
    # 读取背景图像
    img = cv2.imread(bg_path)
    # 在匹配到的位置绘制一个矩形框
    # res['target'] 包含了匹配到的目标的坐标 [x1, y1, x2, y2]
    cv2.rectangle(img,
                  (res['target'][0], res['target'][1]),  # 左上角坐标
                  (res['target'][2], res['target'][3]),  # 右下角坐标
                  (0, 255, 0),  # 颜色为绿色
                  2)  # 线条宽度为 2 像素
    # 显示结果图像
    cv2.imshow("res", img)
    # 等待用户按键，随后关闭窗口
    cv2.waitKey(0)

# 初始化 ddddocr 的滑块验证码匹配模型，禁用字符检测和OCR功能
det = ddddocr.DdddOcr(det=False, ocr=False)

# 背景图像路径
bg_path = "bg4.jpg"

# 打开并读取目标图像（滑块）文件
with open('target4.png', 'rb') as f:
    target_bytes = f.read()

# 打开并读取背景图像文件
with open(bg_path, 'rb') as f:
    background_bytes = f.read()

# 使用 ddddocr 进行滑块验证码匹配，获取匹配结果
res = det.slide_match(target_bytes, background_bytes,simple_target=True)

# 打印匹配结果，res 是一个包含匹配位置等信息的字典
print(res)

# 调用自定义函数 cv_show，在背景图像上绘制匹配到的目标矩形框，并显示
cv_show(bg_path, res)
