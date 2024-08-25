import cv2

# 定义一个函数用于在图像上绘制矩形框，并显示结果
def cv_show_target(img, x1, y1, x2, y2):
    # 在图像上绘制矩形框，颜色为绿色，线条宽度为2
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # 显示处理后的图像
    cv2.imshow("res", img)
    # 等待用户按键继续
    cv2.waitKey(0)
    # 关闭所有显示的窗口
    cv2.destroyAllWindows()

# 定义一个函数用于显示图像
def cv_show(img, title="img"):
    # 显示图像
    cv2.imshow(title, img)
    # 等待用户按键继续
    cv2.waitKey(0)
    # 关闭所有显示的窗口
    cv2.destroyAllWindows()

# 加载背景图像
bg = cv2.imread('bg3.png')
# 检查图像是否成功加载
if bg is None:
    print("Error: bg.png 加载失败")
else:
    # cv_show(bg, "bg")  # 显示背景图像
    pass

# 加载目标图像
target = cv2.imread('target3.png')
# 检查图像是否成功加载
if target is None:
    print("Error: target.png 加载失败")
else:
    # cv_show(target, "target")  # 显示目标图像
    pass
# 对背景图像和目标图像进行边缘检测
bg_canny = cv2.Canny(bg, 70, 200)
target_canny = cv2.Canny(target, 70, 200)

# 显示边缘检测结果
cv_show(bg_canny, "bg_canny")
cv_show(target_canny, "target_canny")

# 在背景图像中查找与目标图像匹配的区域
res = cv2.matchTemplate(bg_canny, target_canny, cv2.TM_CCOEFF_NORMED)
# 获取匹配结果的最小值、最大值及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 打印匹配度，最大值越接近1表示匹配度越高
print(f"匹配度: {max_val}")

# 获取目标图像的尺寸（高度和宽度）
height, width = target.shape[:2]

# 计算矩形框的左上角和右下角坐标
x1, y1 = max_loc[0], max_loc[1]
x2, y2 = x1 + width, y1 + height

# 在背景图像上绘制匹配区域的矩形框，并显示最终结果
cv_show_target(bg, x1, y1, x2, y2)
