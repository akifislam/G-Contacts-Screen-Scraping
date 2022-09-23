# This is data collector script from our EDUMAIL DIRECTORY OF GOOGLE CONTACTS
# This program will take a screenshot of our desired area from a screen and then scroll 14 down click
# Output : Generated 802 Images
# Post-Processing : OCR is used to detect text from 802 images


import time
import pyautogui

x_axis = 693
y_axis = 294
gallery_path = '/Users/akifislam/Desktop/DirectoryHacker/'
time.sleep(4)
ss_counter = 1

#Left Side #Up Side #Right Side # DownSide
region = (620,500,1110,1150)
# im1 = pyautogui.screenshot('s1.png',region=(620,500,1110,1150)) #Copy
for i in range (1,10):
    im1 = pyautogui.screenshot(f'{gallery_path}{ss_counter}.png',region=region)
    pyautogui.scroll(-14)
    ss_counter+=1
    time.sleep(1)
# from PIL import Image
# import pytesseract
#
# image = 'PATH/TO/IMAGE'
# text = pytesseract.image_to_string(Image.open('/Users/akifislam/Desktop/DirectoryHacker/1.png'), lang="eng")
# print(text)
