#Imports
import string, numpy, time, random, sys, math

#Variables de Entorno
solver = [];

#Funciones

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

def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

def BintoHex(a):
    hstr = '%0*X' % ((len(a) + 3) // 4, int(a, 2))
    return hstr

def hexToBinary(a):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    newBinnary = ''
    #print(bin(int(a, scale))[2:].zfill(num_of_bits))
    newBinnary = bin(int(a, scale))[2:].zfill(num_of_bits)
    return (newBinnary)

def Entropia(pwd):
    pass