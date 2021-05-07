# -*- encoding: utf-8 -*-

import cv2
import numpy as np


def image_square_transform(src_img_file, base_img_file, new_img_path_file) -> None:
    """
    对图像做投影变换。将源图片src_img_file，经过投影变换，贴到基础图片base_img_file中，生成新的图片。
    :param src_img_file: 源图片
    :param base_img_file: 基础图片
    :param new_img_path_file: 生成图片保存地址及文件名
    """
    # 参数信息
    print("输入参数：")
    print(f"源图片\t src_img_file \t\t -> {src_img_file}")
    print(f"基础图片\t base_img_file \t\t -> {base_img_file}")
    print(f"生成图片\t new_img_path_file\t -> {new_img_path_file}")

    # mask坐标列表
    mask_pos = []

    # mask点击取坐标事件
    def on_left_click_mask(event, x, y, flags, param) -> None:
        if event == cv2.EVENT_LBUTTONDOWN:
            mask_pos.append([x, y])
            print(f"点击位置坐标：({x}, {y})")

    # 源图片
    src_img = cv2.imread(src_img_file)
    src_height, src_width, _ = src_img.shape
    src_pos = np.array([[0, 0], [0, src_height], [src_width, src_height], [src_width, 0]], np.float32)
    print("展示源图片，双击标题可使图片放大或缩小。")
    cv2.namedWindow("src_img")
    cv2.imshow("src_img", src_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("源图位置坐标列表：src_pos", "->", src_pos.tolist())

    # 基础图片
    base_img = cv2.imread(base_img_file)
    base_height, base_width, _ = base_img.shape
    print("展示基础图片，手动点击图片中需要覆盖的四边形的坐标，点击的顺序是 U 形笔画的顺序。双击标题可使图片放大或缩小。")
    cv2.namedWindow("base_img")
    cv2.setMouseCallback("base_img", on_left_click_mask)
    cv2.imshow("base_img", base_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("点击位置坐标列表：mask_pos", "->", mask_pos)

    # 判断选择的区域是否符合要求
    if len(mask_pos) != 4:
        print("没有在基础图片中选择合适的坐标，请重试。")
        return

    # 计算投影变换矩阵（从src变换到mask）
    transform_matrix = cv2.getPerspectiveTransform(src_pos, np.array(mask_pos, np.float32))
    # 投影变换：将原图片src_img做变换，生成新的图片（同base_img大小）
    src_transform_img = cv2.warpPerspective(src_img, transform_matrix, (base_width, base_height))

    # 生成mask图片（矩形，同src_img大小），图片中的值全部为255
    mask_square = 255 * np.ones_like(src_img)
    # 投影变换：将mask图片做变，生成新的mask图片（同base_img大小）。图片中选择区域内的值为255，区域外的值为0。
    mask_area = cv2.warpPerspective(mask_square, transform_matrix, (base_width, base_height))

    # 生成新的图片new_img：将src_transform_img贴到base_img中，区域内以src_transform_img为准，区域外以base_img为准
    # new_img = np.maximum(base_img, mask_area) - mask_area + src_transform_img
    # base_img[mask_area > 0] = 0
    # new_img = base_img + src_transform_img
    new_img = base_img.copy()
    new_img[mask_area > 0] = src_transform_img[mask_area > 0]
    cv2.imshow("new_img", new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(new_img_path_file, new_img)
