#Imports
import string, numpy, time, random, sys, math

#Variables de Entorno


#Funciones Complementarias

#Funcion que se encarga de compactar mi String en caso de que el hash resultante llegue a ser mayor a 25 caractere
def Compactar(password):    
    while len(password) > 25:
        newstring = password[len(password)-2:]
        password = password[:len(password)-2]
        num = (ord(newstring[0]) + ord(newstring[1])) % 123
        if(num < 48):
            num+=48
        newLet = chr(num)
        password += newLet
    return password

#Función con que hace la conversión de string a binario
def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

#Función que se encarga de convertir binario a hexadecimal
def BintoHex(a):
    hstr = '%0*X' % ((len(a) + 3) // 4, int(a, 2))
    return hstr

#Función que se encarga de convertir hexadecimal a binario
def hexToBinary(a):
    scale = 16 
    num_of_bits = 8
    newBinnary = ''
    #print(bin(int(a, scale))[2:].zfill(num_of_bits))
    newBinnary = bin(int(a, scale))[2:].zfill(num_of_bits)
    return (newBinnary)
