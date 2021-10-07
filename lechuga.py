import string, numpy, time, random, sys

#Variables de entorno
solver = []

def myHash(binary_matrix,hexad_clean):
    transpose_matrix = numpy.transpose(binary_matrix)
    for i in range(len(transpose_matrix)):
        pass
    pass

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

if __name__ == "__main__":
    word = "tres tigres en un trigal aa"
    newWord = ""
    cont = 0
    Tehasheo = ''
    abecedario = string.ascii_letters + string.digits
    if len(word) < 25:
        cantidad = 25 - len(word)
        word = word+''.join(random.choice(abecedario) for j in range(0,cantidad))
       # print(len(word))
        #print(word)
    else:
        #len(word) >= 25
        intervalo = len(word) / 25
        arr = []; arr1 = []; values2hexad =[]; hexad_clean = []; binary_matrix = []
        for i in range(25):
            #print("[",int(intervalo*i),",",int(intervalo*(i+1)),"[","==",str(word[int(intervalo*i):int(intervalo*(i+1))]))
            arr.append(word[int(intervalo*i):int(intervalo*(i+1))])
            suma=0
            for j in arr[i]:
                suma = suma + ord(j)
            arr1.append(suma)
            values2hexad.append(hex(arr1[i]))
            for j in values2hexad[i::2]:
                j = j.replace('0x', '')
                hexad_clean.append(j)
                solver.append(j)
            cont+=1
        #print(hexad_clean)
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
        for i in suma1:
            mensajebin.append(i)
        print(suma1)
        module = ((448-1-len(mensajebin))%512)
        print(module)
        zeros = '0'*module 
        new_mensaje = suma1 + zeros
        print(new_mensaje)
        








        suma = ''
        for i in range(len(transpose_matrix)):
            for j in transpose_matrix[i]:
                suma += (solver[iterator]+j+solver[iterator-1]+solver[iterator-2]+solver[iterator-3]+solver[iterator-4]+solver[iterator-5])
                iterator=iterator+1
        
        print(Compactar(suma))