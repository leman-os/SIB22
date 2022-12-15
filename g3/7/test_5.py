import sys
import os
import base64

if (len(sys.argv)>3):
    print("Превышено количество аргументов")
else:
    if (sys.argv[1]=="crypt"):
        ansicr = sys.argv[2].encode('ascii')
        crypto = base64.b64encode(ansicr)
        print(crypto.decode('ascii'))
    elif (sys.argv[1]=="decrypt"):
        ansicr = sys.argv[2].encode('ascii')
        crypto = base64.b64decode(ansicr)
        print(crypto.decode('ascii'))
    else:
        print("Неверные параметры")