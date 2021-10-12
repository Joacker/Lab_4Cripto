#Imports
import sys, time
from AVL import AVLTree
from funciones import newPass, myHash

#Variables de entorno
size = 0

#Main   
if __name__ == "__main__":
    seguir = True; Tree = AVLTree(); root = None
    size+=1
    root = Tree.insert(root,size,'root','root')
    decision = ''
    while(seguir):
        #root = None
        word = input('Ingrese password: ')
        word = str(word)
        hexad_clean = newPass(word)
        #print(myHash(hexad_clean,word))
        if (Tree.getHeight(root)==1):
            hashedpass = myHash(hexad_clean,word)
            size+=1
            root = Tree.insert(root, size, hashedpass, word)
            print(hashedpass)  
        else:
            if(Tree.Search(root,word)):
                print('entrando a busqueda')
                print(Tree.Search(root,word)[1])
            else:
                print('agregando elementos')
                hashedpass = myHash(hexad_clean,word)
                size+=1
                root = Tree.insert(root, size, hashedpass, word)
                print(hashedpass)
        #root = Tree.insert(root, size, hashedpass, word)
        decision = input('Desea continuar ¿Si o No?\n')
        if (decision == 'No'):
            #print(Tree.preOrder(root))
            seguir = False
        word = ''