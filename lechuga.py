#Imports
import string
import sys, time, os
from funciones import Compactar,hexToBinary
from datetime import datetime, timedelta
futuredate = datetime.now() + timedelta(days=10)
#Variables de entorno
size = 0
diccionario = string.ascii_letters+string.digits+'♫☼►◄↕‼¶§▬↨↑↓→∟↔▲▼123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'

def name(n):
     return (n**2)+2*n+1

tiempo = time.time()
valores = 0
seconds = futuredate.toordinal()

def Segmentation25(pwd):
    arr = []; base = 0; solver = []; largos = []
    intervalo = len(pwd) / 25
    dicIntervalo = len(diccionario) / 25
    for i in range(25):
        #print("[",int(intervalo*i),",",int(intervalo*(i+1)),"[","==",str(word[int(intervalo*i):int(intervalo*(i+1))]))
        #print(word[int(intervalo*i):int(intervalo*(i+1))])
        
        k = len((pwd[int(intervalo*i):int(intervalo*(i+1))]))

        arr.append(((pwd[int(intervalo*i):int(intervalo*(i+1))])))
        
        largos.append((len(arr[i]))*k*(i+1))
        #c = (x + n) % 26   
        suma = 0
        
        for j in range(len(arr[i])):
            suma +=  ((valores*int(seconds))) + int(((name((ord(arr[i][j])**11)*i*j*seconds)) ** 0.3*valores*seconds*j) * ((i*(valores*i)*seconds+i)+2*(i+1)) * 11)*(largos[-1]*valores*j)
            #print(suma)
            if (j == (len(arr[i]) - 1)):
                solver.append(suma*(seconds*j-1))    
        
    return solver,largos

def newHash(palabra):
    if (len(palabra)<25):
        #palabra = palabra + '0'*(25-len(palabra))
        sumita = 0
        for i in palabra:
            sumita = ord(i)
        for i in range(25):
            palabra = str(seconds)+palabra+i*str(seconds)+ diccionario[(i*sumita+int(seconds**i))%len(diccionario)]

    largos = Segmentation25(palabra)[1]
    array = Segmentation25(palabra)[0]
    array.sort()
    #print(array)
    cont = 1
    myhash=''; vector = []
    for i in range(len(array)):
        myhash += diccionario[(array[i]*largos[i-1]*(i+1))%len(diccionario)]
        #vector.append(chr(Segmentation25(myhash)[0][i])+str(Segmentation25(chr(array[i]).encode('utf-8', 'replace').decode())[0][i])*i)
        cont+=1
    
    return(Compactar(myhash))

if __name__ == "__main__":
    #print(sys.argv)
    palabra = ' '
    word = palabra.encode("utf-8").hex()
    kPonder = 0
    for i in (hexToBinary(word)):
        kPonder+=(int(i)*(len(hexToBinary(word))//3))
    valores = kPonder
    print(newHash(palabra))
    #print(kPonder)
    