import os
import glob
import numpy as np
import cv2
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="Object parent folder.")
    parser.add_argument("--object", type=str, help="face, hand, panel, lion, pan, laptop")
    args = parser.parse_args()


    min_max = {
        'face':{
            'min': 22.5,
            'max': 35.2 },
        'hand':{
            'min': 22.1,
            'max': 33.6 },
        'panel':{
            'min': 22.7,
            'max': 55.8 },
        'lion':{
            'min': 16.8,
            'max': 48.3 },
        'pan':{
            'min': 19.4,
            'max': 129.8 },
        'laptop':{
            'min': 21.6,
            'max': 40.2 },

    }

    tp = os.path.join(args.path,'thermal','*.jpg')
    imgs = glob.glob(tp)

    for img in imgs:
        i = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
        i = i/255
        fn = img.split('/')[-1]
        t = cv2.imread(os.path.join(args.path,'warped_thermal',fn),cv2.IMREAD_GRAYSCALE)
        t = t/255

        print(t.min(),i.min())
        t[t<i.min()] = i.min()
        print('#')
        temp = min_max[args.object]['min'] + t * (min_max[args.object]['max'] - min_max[args.object]['min'])


        fp = os.path.join(args.path,'warped_thermal',fn[:-4]+'.npy')
        
        np.save(fp,temp)





