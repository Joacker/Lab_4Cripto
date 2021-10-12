#Imports
import sys, time
from AVL import AVLTree
from funciones import newPass, myHash

#Variables de entorno
size = 0

#Main   
if __name__ == "__main__":
    seguir = True; Tree = AVLTree(); root = None
    while(seguir):
        word = input('Ingrese password: ')
        word = str(word)
        hexad_clean = newPass(word)
        print(myHash(hexad_clean,word))
        hashedpass = myHash(hexad_clean,word)
        
        root = None
        root.
        size = size+1
        if(Tree.Search(root,word) == None):
            root = Tree.insert(root, size, hashedpass, word)
        
        seguir = False
        
        

        print("Preorder traversal of the",
            "constructed AVL tree is")
        Tree.Search(root,word)
        print()
        word = ''
    '''root = Tree.insert(root, 2,5)
    root = Tree.insert(root, 3,5)
    root = Tree.insert(root, 4,5)
    root = Tree.insert(root, 5,5)
    root = Tree.insert(root, 6,5)'''

    # Preorder Traversal

    #print(Compactar(suma))