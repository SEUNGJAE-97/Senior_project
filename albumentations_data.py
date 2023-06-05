import albumentations as A
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import sklearn 
import joblib
import os
import imgaug
from glob import glob


def load_img(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image    

def comparison(actual_image, transformed_image, titles=None):
    if titles == None:
        titles = ['Actual Image', 'Transformed Image']
        
    fig, ax = plt.subplots(1, 2, figsize=(17, 17))
    ax[0].set_title(titles[0])
    if len(actual_image.shape) == 2:
        ax[0].imshow(actual_image, cmap='gray')
    else:
        ax[0].matshow(actual_image)
    ax[0].axis('off')

    ax[1].set_title(titles[1])
    if len(transformed_image.shape) == 2:
        ax[1].imshow(transformed_image, cmap='gray')
    else:
        ax[1].matshow(transformed_image)
    ax[1].axis('off')
    plt.show()

def save_al_img(file_name, path):
    A.save(file_name, path)

from albumentations import (
    HorizontalFlip, IAAPerspective, ShiftScaleRotate, CLAHE, RandomRotate90,
    Transpose, ShiftScaleRotate, Blur, OpticalDistortion, GridDistortion, HueSaturationValue,
    IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, IAAPiecewiseAffine,
    IAASharpen, IAAEmboss, RandomBrightnessContrast, Flip, OneOf, Compose
)

height = 150
width = 150

train_transeforms = Compose([
        A.Resize(200,450),
        RandomRotate90(),
        Flip(),
        Transpose(),
        OneOf([
            IAAAdditiveGaussianNoise(),
            GaussNoise(),
        ], p=0.2),
        OneOf([
            MotionBlur(p=0.2),
            MedianBlur(blur_limit=3, p=0.1),
            Blur(blur_limit=3, p=0.1),
        ], p=0.2),
        ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        OneOf([
            OpticalDistortion(p=0.3),
            GridDistortion(p=0.1),
            IAAPiecewiseAffine(p=0.3),
        ], p=0.2),
        OneOf([
            CLAHE(clip_limit=2),
            IAASharpen(),
            IAAEmboss(),
            RandomBrightnessContrast(),
        ], p=0.3),
        HueSaturationValue(p=0.3),
        OneOf([
            A.CoarseDropout(always_apply=False, p=0.5, max_holes=20, max_height=15, max_width=15, min_holes=1, min_height=8, min_width=8)
        ], p=0.2),
        OneOf([
            A.ElasticTransform(always_apply=False, p=0.5, alpha=0.20000000298023224, sigma=3.359999895095825, alpha_affine=2.009999990463257, interpolation=1, border_mode=1, value=(0, 0, 0), mask_value=None, approximate=False)
        ], p = 0.3),
        OneOf([
            HorizontalFlip(always_apply= False, p=0.5)

        ],p=0.2)
    ], p= 1.0)

folder = os.listdir('image/')
imgs = glob('image/*/*.png')

# 1. for-loop : folder
for fd in range(len(folder)):
    path = 'image/'+str(folder[fd])
    file_list = os.listdir(path)
    # 선택된 폴더 내의 이미지 갯수 만큼 반복
    for ig in range(len(file_list)):
        #이미지 선택 
        img_path = path + '/' +str(file_list[ig])
        image= load_img(img_path)
        #print(img_path)
        # transform & save transfromed img
        for i in range(30):
            transformed_img = train_transeforms(image= image)['image']
            # save path
            save_path = path + '/' + str(folder[ig]) + '_' + str(ig)+'_'+str(i)+'.png'
            print(save_path)
            # save
            cv2.imwrite(save_path, transformed_img)