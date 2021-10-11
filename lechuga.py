#Imports
import string, numpy, time, random, sys, math
from AVL import treeNode, AVLTree
from funciones import Compactar, toBinary, BintoHex, hexToBinary, passGenerator, newPass

#Variables de entorno
solver = [];

#Funciones    

if __name__ == "__main__":
    word = "1010"
    hexad_clean = newPass(word)
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
    
    Tree = AVLTree()
    
    root = None
    
    root = Tree.insert(root, 1,valor)
    root = Tree.insert(root, 2,5)
    root = Tree.insert(root, 3,5)
    root = Tree.insert(root, 4,5)
    root = Tree.insert(root, 5,5)
    root = Tree.insert(root, 6,5)

    # Preorder Traversal
    print("Preorder traversal of the",
        "constructed AVL tree is")
    Tree.preOrder(root)
    print()

    
    #print(Compactar(suma))