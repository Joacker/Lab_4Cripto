import time as t

class treeNode(object):
    def __init__(self, value, password, word):
        #value es tiempo y password
        self.value = value
        self.password = password
        self.word = word
        self.l = None
        self.r = None
        self.h = 1

class AVLTree(object):

	def insert(self, root,key,password,word):
	
		if not root:
			return treeNode(key,password,word)
		elif key < root.value:
			root.l = self.insert(root.l, key,password,word)
		else:
			root.r = self.insert(root.r, key,password,word)

		root.h = 1 + max(self.getHeight(root.l),
						self.getHeight(root.r))

		b = self.getBal(root)

		if b > 1 and key < root.l.value:
			return self.rRotate(root)

		if b < -1 and key > root.r.value:
			return self.lRotate(root)

		if b > 1 and key > root.l.value:
			root.l = self.lRotate(root.l)
			return self.rRotate(root)

		if b < -1 and key < root.r.value:
			root.r = self.rRotate(root.r)
			return self.lRotate(root)

		return root

	def lRotate(self, z):

		y = z.r
		T2 = y.l

		y.l = z
		z.r = T2

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def rRotate(self, z):

		y = z.l
		T3 = y.r

		y.r = z
		z.l = T3

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.h

	def getBal(self, root):
		if not root:
			return 0

		return self.getHeight(root.l) - self.getHeight(root.r)

	def Search(self, root, pwd):
		if not root:
			return
		if root.word == pwd:
    			#print('Ya se encuentra dentro del arbol')
    			return (root.word,root.password)
		#print("{0} ".format(root.word), end="")
		izquierda = (self.Search(root.l,pwd))
		derecha = (self.Search(root.r,pwd))
		if(izquierda):
    			return (izquierda)
		if(derecha):
    			return (derecha)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.value), end="")
		self.preOrder(root.l)
		self.preOrder(root.r)
