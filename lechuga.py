#Imports
import sys
from AVL import AVLTree
from funciones import newPass, myHash

#Funciones    

if __name__ == "__main__":
    word = "1010"
    hexad_clean = newPass(word)
    print(myHash(hexad_clean,word))
    
    
    Tree = AVLTree()
    
    root = None
    
    root = Tree.insert(root, 1,5)
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