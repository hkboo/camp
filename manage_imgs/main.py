#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:50:47 2021

@author: hkboo
"""

import os
import random
from PIL import Image


def select_random_injection_img(injection_img_dir):
    files = os.listdir(injection_img_dir)
    index = random.randrange(0, len(files))
    full_path = "{}/{}".format(injection_img_dir, files[index])
    return full_path




def attach_imgs(injection_img, target_img):
    """
    Parameters
    ----------
    injection_img : Image object
        advertisement
    target_img : Image object
        Image in NFT
    Returns
    -------
    New image object (Attached both).

    * working on only same format
    """
    in_w, in_h = injection_img.size
    ta_w, tar_h = target_img.size
    
    
    bg_w, bg_h = in_w if in_w > ta_w else ta_w, in_h + tar_h
    new_img = Image.new('RGB', (bg_w, bg_h), (255,255,255))
    new_img.paste(injection_img, (0, 0), injection_img)
    new_img.paste(target_img, (0, bg_h-tar_h), target_img)
    return new_img


def save_new_img(img_obj, img_name):
    """

    Parameters
    ----------
    img_obj : Image object
        Image object to save.
    img_name : str
        Input save path/file_name

    Returns
    -------
    TYPE
        Nothing.

    """
    return img_obj.save("{}".format(img_name))


def main():
    injection_img_dir = './data/injection_ad'
    target_img_path = './data/target_nft/test2.png'
    new_target_img_path = 'output.png'
    
    random_injection = select_random_injection_img(injection_img_dir)
    injection_img = Image.open(random_injection)
    target_img = Image.open(target_img_path)

    work = attach_imgs(injection_img, target_img)
    save_new_img(work, new_target_img_path)
    
    
main()