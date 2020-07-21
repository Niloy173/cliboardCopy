import time,pyperclip,os
# pypeclip module for copy/paste
contentvalue = ''
from contextlib import redirect_stdout # for the textdocument
D = time.strftime("%D")
r =time.strftime("%r")

# copy any text or anything related data while runing the program
while True:
    time.sleep(.6)
    if pyperclip.paste() != 'None':
        data = pyperclip.paste()
        if data not in contentvalue:
            contentvalue = pyperclip.paste()
            with open('clipboard.txt','a') as f:
                with redirect_stdout(f):
                    f.write("----------"+D+""+r+"----------------\n")
                    print(contentvalue+'\n')


