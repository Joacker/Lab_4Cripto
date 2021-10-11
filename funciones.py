#Funciones
import string, numpy, time, random, sys, math

solver = [];

def myHash(hexad_clean, word):
    binary_matrix = []
    scale = 16; binary_line = []; iterator = 0
    for i in range(len(hexad_clean)):
        hexad_clean[i] = bin(int(hexad_clean[i], scale))[2:].zfill(8)
        binary_matrix.append([hexad_clean[i]])
    #print(binary_matrix)
    suma1 = ''; mensajebin = []
    transpose_matrix = numpy.transpose(binary_matrix)
    for i in range(len(transpose_matrix)):
        for j in transpose_matrix[i]:
            suma1 += j
    suma1 = suma1+'1'
    #print(suma1)
    module = ((448-1-len(mensajebin))%512)
    #print(module)
    zeros = '0'*module 
    new_mensaje = suma1 + zeros
    # print(new_mensaje)
    for i in new_mensaje:
        mensajebin.append(i)
    # print(mensajebin)
    longitud_hex = hex(len(word)*8)
    #print(longitud_hex)
    longitud_64bits = ""
    longitud_hex=longitud_hex.replace('0x', '')
    for i in toBinary(longitud_hex):
        longitud_64bits = longitud_64bits + str(i)    

    longitud_64bits = ('0'*64)+longitud_64bits
    #print(longitud_64bits)
    #print(BintoHex(longitud_64bits))
    mensaje_bin_1_xceros = new_mensaje + longitud_64bits
    # print(len(mensaje_bin_1_xceros))
    
    h0 = hexToBinary('0x6a09e667'.replace('0x', ''),8)
    h1 = hexToBinary('0xbb67ae85'.replace('0x', ''),8)
    h2 = hexToBinary('0x3c6ef372'.replace('0x', ''),8)
    h3 = hexToBinary('0xa54ff53a'.replace('0x', ''),8)
    h4 = hexToBinary('0x510e527f'.replace('0x', ''),8)
    h5 = hexToBinary('0x9b05688c'.replace('0x', ''),8)
    h6 = hexToBinary('0x1f83d9ab'.replace('0x', ''),8)
    h7 = hexToBinary('0x5be0cd19'.replace('0x', ''),8)


    ht = h0+h1+h2+h3+h4+h5+h6+h7
    #Dividimos el mensaje en 512 bits
    
    otherword = ''
    #print(otherword)
    otherword ='♫☼►◄↕‼¶§▬↨↑↓→∟↔▲▼123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'
    mensaje_bin_1_xceros+='0'*298
    newmessage = otherword+BintoHex(mensaje_bin_1_xceros)+BintoHex(ht)+otherword
    #print(newmessage)
    for i in solver:
        newmessage = newmessage + i
    #print(newmessage)
    
    valor = (Compactar(passGenerator(newmessage)))
    print(valor)

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