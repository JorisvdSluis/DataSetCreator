from PIL import Image, ImageEnhance 
import glob
import os
image_list = []

for filename in glob.glob('-50Data/LightIntensity/*.jpg'): #assuming gif
    new_filename = filename.replace("0001", "-50")
    os.rename(filename,new_filename)
for filename in glob.glob('-100Data/LightIntensity/*.jpg'): #assuming gif
    new_filename = filename.replace("0001", "-100")
    os.rename(filename,new_filename)
for filename in glob.glob('50Data/LightIntensity/*.jpg'): #assuming gif
    new_filename = filename.replace("0001", "50")
    os.rename(filename,new_filename)
for filename in glob.glob('100Data/LightIntensity/*.jpg'): #assuming gif
    new_filename = filename.replace("0001", "100")
    os.rename(filename,new_filename)

