#Imports
import sys, time, os,string, math
from funciones import Compactar,hexToBinary
from datetime import datetime, timedelta
futuredate = datetime.now() + timedelta(days=10)
#Variables de entorno
size = 0
diccionario = string.ascii_letters+string.digits+'♫☼►◄↕‼¶§▬↨↑↓→∟↔▲▼123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'

def name(n):
     return (n**2)+2*n+1

factorlargo = 0
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
            suma +=  ((valores*int(seconds))) + int(((name((ord(arr[i][j])**11)*i*j*seconds)) ** 0.3*valores*seconds*j) * ((i*(valores*i)*seconds+i)+2*(i+1)) * 11)*(largos[-1]*valores*j*seconds)
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
            palabra = str(seconds*seconds*seconds*i)+palabra+i*str(seconds*seconds)+ diccionario[(i*sumita*seconds+int(seconds**i))%len(diccionario)]

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

def Entropia(word):
    return math.log(256,2)*len(word)

if __name__ == "__main__":
    seguir = True; opcion = '';
    while seguir:
        print('Ingrese una opcion.....')
        print('(1) Ingrese palabra...')
        print('(2) Ingrese el nombre de un archivo (tiene que estar dentro del directorio)....')
        print('(3) Valor de Entropia....')
        print('Presione otra tecla para cerrar el programa...')
        opcion = input('Ingrese opcion...')
        opcion = str(opcion)
        if (opcion == '1'):

            palabra = input('Ingrese clave para ser hasheada...\n')
            word = palabra.encode("utf-8").hex()
            kPonder = 0
            for i in (hexToBinary(word)):
                kPonder+=(int(i)*(len(hexToBinary(word))//3))
            valores = kPonder
            Hashed = newHash(palabra)
            print(Hashed)
        elif (opcion == '2'):
            archivo = input('Ingrese el nombre de un archivo (que este dentro del directorio): \n')
            palabra = '';
            with open('./'+archivo, 'r',errors='ignore') as log_file_fh:
                for i in log_file_fh:
                    palabra = i
                    word = palabra.encode("utf-8").hex()
                    kPonder = 0
                    for j in (hexToBinary(word)):
                        kPonder+=(int(j)*(len(hexToBinary(word))//3))
                    valores = kPonder
                    Hashed = newHash(palabra)
                    print(Hashed)
                    factorlargo = len(Hashed)
                    #print(newHash(palabra))
                    palabra = ''
        
        elif (opcion == '3'):
            a = " "
            Hashed = newHash(" ")
            print(Entropia(Hashed))
        else:
            print('''                                                                                                                                                                                                                                                                                                          
        GGGGGGGGGGGGG                                                         iiii                                                 DDDDDDDDDDDDD        
     GGG::::::::::::G                                                        i::::i                                                D::::::::::::DDD     
   GG:::::::::::::::G                                                         iiii                                                 D:::::::::::::::DD   
  G:::::GGGGGGGG::::G                                                                                                              DDD:::::DDDDD:::::D  
 G:::::G       GGGGGGrrrrr   rrrrrrrrr   aaaaaaaaaaaaa      cccccccccccccccciiiiiii   aaaaaaaaaaaaa      ssssssssss                  D:::::D    D:::::D 
G:::::G              r::::rrr:::::::::r  a::::::::::::a   cc:::::::::::::::ci:::::i   a::::::::::::a   ss::::::::::s        ::::::   D:::::D     D:::::D
G:::::G              r:::::::::::::::::r aaaaaaaaa:::::a c:::::::::::::::::c i::::i   aaaaaaaaa:::::ass:::::::::::::s       ::::::   D:::::D     D:::::D
G:::::G    GGGGGGGGGGrr::::::rrrrr::::::r         a::::ac:::::::cccccc:::::c i::::i            a::::as::::::ssss:::::s      ::::::   D:::::D     D:::::D
G:::::G    G::::::::G r:::::r     r:::::r  aaaaaaa:::::ac::::::c     ccccccc i::::i     aaaaaaa:::::a s:::::s  ssssss                D:::::D     D:::::D
G:::::G    GGGGG::::G r:::::r     rrrrrrraa::::::::::::ac:::::c              i::::i   aa::::::::::::a   s::::::s                     D:::::D     D:::::D
G:::::G        G::::G r:::::r           a::::aaaa::::::ac:::::c              i::::i  a::::aaaa::::::a      s::::::s                  D:::::D     D:::::D
 G:::::G       G::::G r:::::r          a::::a    a:::::ac::::::c     ccccccc i::::i a::::a    a:::::assssss   s:::::s       ::::::   D:::::D    D:::::D 
  G:::::GGGGGGGG::::G r:::::r          a::::a    a:::::ac:::::::cccccc:::::ci::::::ia::::a    a:::::as:::::ssss::::::s      :::::: DDD:::::DDDDD:::::D  
   GG:::::::::::::::G r:::::r          a:::::aaaa::::::a c:::::::::::::::::ci::::::ia:::::aaaa::::::as::::::::::::::s       :::::: D:::::::::::::::DD   
     GGG::::::GGG:::G r:::::r           a::::::::::aa:::a cc:::::::::::::::ci::::::i a::::::::::aa:::as:::::::::::ss               D::::::::::::DDD     
        GGGGGG   GGGG rrrrrrr            aaaaaaaaaa  aaaa   cccccccccccccccciiiiiiii  aaaaaaaaaa  aaaa sssssssssss                 DDDDDDDDDDDDD        
                                                                                                                                                                                                                                                                                                   
                                                                                                                                                        
''')
            seguir = False
    #print(kPonder)'''
        