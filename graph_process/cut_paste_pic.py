"""
定义了计算机图像处理常用的函数方法，基于OpenCV计算机视觉库实现
"""

import os

import cv2 as cv
import numpy as np


# 读取文件夹中所有的图片文件，自定义采样的像素尺寸进行采样，并返回读取结果
def read_img(file_path, h, w, imgs=[]):
    paths = os.listdir(file_path)
    if len(paths) == 0:
        return
    for path in paths:
        if path.endswith('.png'):
            img = cv.imread(file_path + '/' + path)
            temp_shape = img.shape
            x, y = temp_shape[0] // h, temp_shape[1] // w
            if x == 0:
                x = 1
            if y == 0:
                y = 1
            if len(temp_shape) == 2:
                imgs.append(img[::x, ::y])
            else:
                imgs.append(img[::x, ::y, :])
        elif os.path.isdir(file_path + '/' + path):
            read_img(file_path + '/' + path, h, w, imgs)
        else:
            pass
    return imgs


# 读取一张图片(可以传入路径或者传入图片)，按需求，大了裁剪小了填充黑色
def cut_picture(img_path, img_shape):
    global img
    if isinstance(img_path, str):
        img = cv.imread(img_path)
    else:
        img = img_path.copy()
    if img_shape[0] >= img.shape[0]:
        if img_shape[1] >= img.shape[1]:
            temp = np.zeros((img_shape[0], img_shape[1], img.shape[2]), dtype=np.uint8)
            top = (img_shape[0] - img.shape[0]) // 2
            left = (img_shape[1] - img.shape[1]) // 2
            temp[top:top + img.shape[0], left:left + img.shape[1], :] = img
            return temp
        else:
            temp = np.zeros((img_shape[0], img_shape[1], img.shape[2]), dtype=np.uint8)
            top = (img_shape[0] - img.shape[0]) // 2
            temp[top:top + img.shape[0], :, :] = img[:, 0:img_shape[1], :]
            return temp
    else:
        if img_shape[1] >= img.shape[1]:
            temp = np.zeros((img_shape[0], img_shape[1], img.shape[2]), dtype=np.uint8)
            left = (img_shape[1] - img.shape[1]) // 2
            temp[:, left:left + img.shape[1], :] = img[0:img_shape[0], :, :]
            return temp
        else:
            temp = img[0:img_shape[0], 0:img_shape[1], :]
            return temp


# 读取所有图片统计尺寸，将所有图片填充为最大那张图片的大小
def pad_img(imgs):
    temp_shape = [0, 0]
    for img in imgs:
        if img.shape[0] > temp_shape[0]:
            temp_shape[0] = img.shape[0]
        if img.shape[1] > temp_shape[1]:
            temp_shape[1] = img.shape[1]
    temp_img = []
    for img in imgs:
        temp = cut_picture(img, temp_shape)
        temp_img.append(temp)
    return temp_img


# 将所有尺寸大小相同的图片排列成矩阵，可以自定义一行最多多少张图片，不足的位置会自定填充黑底
def arrange_img(imgs_in, width):
    imgs = pad_img(imgs_in)
    single_shape = imgs[0].shape
    total = len(imgs)
    high = total // width
    stay = total % width
    if stay != 0:
        high += 1
        padding = [np.zeros(single_shape, dtype=np.uint8)] * (width - stay)
        imgs.extend(padding)
    if len(single_shape) == 2:
        ret = np.zeros((single_shape[0] * high, single_shape[1] * width), dtype=np.uint8)
        for i in range(len(imgs)):
            h, l = i // width, i % width
            ret[h * single_shape[0]:(h + 1) * single_shape[0], l * single_shape[1]:(l + 1) * single_shape[1]] = imgs[i]
        return ret
    else:
        ret = np.zeros((single_shape[0] * high, single_shape[1] * width, 3), dtype=np.uint8)
        for i in range(len(imgs)):
            h, l = i // width, i % width
            ret[h * single_shape[0]:(h + 1) * single_shape[0], l * single_shape[1]:(l + 1) * single_shape[1], :] = imgs[
                i]
        return ret


# 读取指定文件夹中所有图片文件按指定规格采样和排列并保存到指定文件夹
def read_all_graph(root_path, width, h, w, path_des):
    img = arrange_img(read_img(root_path, h, w), width)
    cv.imwrite(path_des, img)
    cv.imshow('1', img)
    cv.waitKey(0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 6:
        print('参数输入错误：')
        print(' 1、需要输入五个参数')
        print(' 2、（参数1， 参数2，参数3， 参数4，参数5）')
        print(' 3、参数说明：')
        print('     参数1：需要处理的图片所在的文件夹的根路径')
        print('     参数2：保存后的图片名字')
        print('     参数3、参数4：图片采样后的尺寸大小(行高，列高)')
        print('     参数5：每行放的图片数量')
    else:
        root_path, des = sys.argv[1], sys.argv[1] + '/' + sys.argv[2]
        read_all_graph(root_path, int(sys.argv[5]), int(sys.argv[3]), int(sys.argv[4]), des)
