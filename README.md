# G-Contacts-Screen-Scraping
Go to [Google Contacts](contacts.google.com) from your University Mail. On the left panel, you will see 'Directory' which contains almost all the emails in your orgainzation.
But unfortunately, Google doesn't let you download all of them at once. Having all them can be great for any kind of digital marketing or other good purpose.
That's why, this repository was created to bypass Google's protection.
</br>

<div align="center">
 </br>
 <img src="./Samples/directory.png" height="200" width="563" />
 </br>

</div>

# Built with
- Python 3.9
- PyAutoGUI
- [Tesseract Open Source OCR Engine ](https://github.com/tesseract-ocr/tesseract)
- [pytesseract 0.3.10](https://pypi.org/project/pytesseract/)
- Pillow
- OpenCV

# Working Process
- Place the mouse pointer on the first page of Google Contacts Directory
- Start PyAutoGUI script which will take screenshot of each page and autotically scroll down (and so on)
- On my project, it has taken total 802 shots containing 13000+ emails
- Then Convert those images to text using Pytesseract

© Akif Islam
