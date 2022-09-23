# This program is a image to text converter made with Google OCR Engine
# Output : emails.txt (with only studentmail starts with 's' and end with '@ru.ac.bd'

from PIL import Image
import pytesseract
import cv2

image = 'PATH/TO/IMAGE'
mailCount = 0
with open("emails.txt", "w") as e:
    for i in range (1,803):
        print(f"Getting from SS No : {i} | Total Mail Pursed : {mailCount}")
        text = pytesseract.image_to_string(Image.open(f'/Users/akifislam/Desktop/DirectoryHacker/{i}.png'), lang="eng")
        # print(text)
        for line in str(text).splitlines():
            # print(line)
            if(str(line).__contains__("@ru.ac.bd")):
                gotEmail = line.replace("$","s")
                if(gotEmail.startswith("s")):
                    mailCount += 1
                    e.write(gotEmail+"\n")





