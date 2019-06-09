from PIL import Image, ImageEnhance 
import glob
image_list = []

for filename in glob.glob('Data/LightIntensity/*.jpg'): #assuming gif
    im=Image.open(filename)
    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(1.5)
    image_list.append(im)
    enhanced_im.save(str("50" + filename))
    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(2.0)
    image_list.append(im)
    enhanced_im.save(str("100" + filename))
    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(0.6)
    image_list.append(im)
    enhanced_im.save(str("-50" + filename))
    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(0.3)
    image_list.append(im)
    enhanced_im.save(str("-100" + filename))
print(image_list)
