#Funciones
import string, numpy, time, random, sys, math

solver = [];

def newPass(pwd):
    hexad_clean = []; values2hexad = []; arr = []; arr1 = [];
    if (len(pwd)<25):
        suma = 0
        cantidad = 25 - len(pwd)
        abecedario = string.ascii_letters + string.digits
        word = pwd+''.join(random.choice(abecedario) for j in range(0,cantidad))
        for i in range(25):
            for j in word:
                suma = suma + ord(j)
            arr1.append(suma)
            values2hexad.append(hex(arr1[i]))
            for j in values2hexad[i::2]:
                j = j.replace('0x', '')
                hexad_clean.append(j)
                solver.append(j)

        return (hexad_clean)

    intervalo = len(pwd) / 25
    for i in range(25):
        #print("[",int(intervalo*i),",",int(intervalo*(i+1)),"[","==",str(word[int(intervalo*i):int(intervalo*(i+1))]))
        #print(word[int(intervalo*i):int(intervalo*(i+1))])
        arr.append(pwd[int(intervalo*i):int(intervalo*(i+1))])
        suma=0
        for j in arr[i]:
            suma = suma + ord(j)
        arr1.append(suma)
        values2hexad.append(hex(arr1[i]))
        for j in values2hexad[i::2]:
            j = j.replace('0x', '')
            hexad_clean.append(j)
            solver.append(j)
    #print(hexad_clean)
    return (hexad_clean)

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

def hexToBinary(a,n):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    newBinnary = ''
    #print(bin(int(a, scale))[2:].zfill(num_of_bits))
    newBinnary = bin(int(a, scale))[2:].zfill(num_of_bits)
    return (('0'*n)+newBinnary)

def passGenerator(pwd):
    cantidad = len(pwd)
    return(''.join(random.choice(pwd) for j in range(0,cantidad)))