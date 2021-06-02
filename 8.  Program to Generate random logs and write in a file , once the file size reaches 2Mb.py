"""8. Program to Generate random logs and write in a file , once the file size reaches 2Mb
open new file and continue writing"""

import os
file_number=0
file_size=0
while True:
    if file_size<2e+6:
        try:
            file=open('test%d.txt'%file_number,'x')
        except:
            pass
        file=open('text%d.txt'%file_number)
        text=file.read()+'hello'
        file=open('test%d.txt'%file_number,'w')
        file.write(text)

    file_size=os.start('test%d.txt'%file_number).st_size
    if file_size>2e+6:
        file_number+=1
        file_size=0
