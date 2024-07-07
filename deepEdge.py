import cv2
import os
import glob

img_path = r'E:\before'
dest_path = r'E:\after'


i = 1
for img in glob.glob(img_path+'/*.*'):
    try:
        image = cv2.imread(img)
        resize = cv2.resize(image, (416, 416))
        os.chdir(dest_path)
        filename = 'sagar'+str(i)+'.JPEG'
        cv2.imwrite(filename, resize)
        i+=1
        
    except:
        print('{} is not saved'. format(image))
 
 