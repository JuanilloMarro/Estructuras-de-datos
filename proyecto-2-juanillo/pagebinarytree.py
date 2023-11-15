import json
from tkinter import *
from tkinter.font import Font
from structures import binarytree

tree = binarytree.BinaryTree()

class PageBinaryTree():
	def __init__(self):
		self.top = Toplevel()

		self.top.title('Binary Tree')

		self.top.resizable(False, False)

		self.top.geometry('1250x750')

		self.fuente = Font(family="Open Sans", size=10, weight="bold")

		self.frame_all_arbol = Frame(self.top)
		self.frame_all_arbol.config(width=650, height=750)
		self.frame_all_arbol.pack(side='left', fill="both", expand=True)

		self.frame_titulo_arbol = Frame(self.frame_all_arbol)
		self.frame_titulo_arbol.config(width=650, height=50)
		self.frame_titulo_arbol.pack(fill="both", expand=True, padx=100, pady=50)
		self.label_titulo_cola = Label(self.frame_titulo_arbol)
		self.label_titulo_cola.config(font=self.fuente, text='Visualización del Arbol Binario')
		self.label_titulo_cola.pack()

		self.frame_tree = Frame(self.frame_all_arbol)
		self.frame_tree.config(width= 650, height=700)
		self.frame_tree.pack(fill="both", expand=True)

		# --- Información de la Arbol ---

		# Frame principal donde se encuentra toda la información del Arbol
		self.frame_info_arbol = Frame(self.top)
		self.frame_info_arbol.config(bg='#C8EDC8', width=350, height=750)
		self.frame_info_arbol.pack(side='right', fill='both')

		# Frame que contiene el título 'Información de la Pila' y todos los frames correspondientes a él
		self.info_especifica_arbol = Frame(self.frame_info_arbol)
		self.info_especifica_arbol.config(bg='#C8EDC8')
		self.info_especifica_arbol.pack(pady=15, padx=5)
		self.label_title_info_cola = Label(self.info_especifica_arbol, text='Información de la Arbol Binario', bg='#C8EDC8',
										   font=self.fuente)
		self.label_title_info_cola.pack()

		# Frame que contiene dos labels: el maximo y el otro label donde se asigna el maximo
		self.frame_root = Frame(self.info_especifica_arbol)
		self.frame_root.config(bg='#C8EDC8')
		self.frame_root.pack(pady=2.5, padx=2.5)
		self.label_max = Label(self.frame_root, text='Raiz: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_root = Label(self.frame_root, text=str(tree.get_root()), bg='#C8EDC8', font=self.fuente)
		self.label_root.pack(side='right')

		# Frame que contiene dos labels: el tamaño y el otro label donde se asigna el tamaño
		self.frame_tamano = Frame(self.info_especifica_arbol)
		self.frame_tamano.config(bg='#C8EDC8')
		self.frame_tamano.pack(pady=2.5, padx=2.5)
		self.label_tamano = Label(self.frame_tamano, text='Tamaño: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_tamanoo = Label(self.frame_tamano, text=str(tree.size()), bg='#C8EDC8', font=self.fuente)
		self.label_tamanoo.pack(side='right')

		# Frame que contiene dos labels: el tope y el otro label donde se asigna el tope
		self.frame_depht = Frame(self.info_especifica_arbol)
		self.frame_depht.config(bg='#C8EDC8')
		self.frame_depht.pack(pady=2.5, padx=2.5)
		self.label_tope = Label(self.frame_depht, text='Profundidad: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_depht = Label(self.frame_depht, text=str(tree.get_depth()), bg='#C8EDC8', font=self.fuente)
		self.label_depht.pack(side='left')
		# Opciones del valor ingresado por el user

		# Frame que contienen la entrada del valor ingresado por el usuario y los botones que los modifican
		self.opciones_valor = Frame(self.frame_info_arbol)
		self.opciones_valor.config(bg='#C8EDC8')
		self.opciones_valor.pack(pady=15, padx=5)

		# Frame que contiene el título 'Ingrese el valor' y la entrada del valor
		self.frame_valor = Frame(self.opciones_valor)
		self.frame_valor.config(bg='#C8EDC8')
		self.frame_valor.pack()
		self.label_titulo_valor = Label(self.frame_valor, text='Ingrese el valor: ', bg='#C8EDC8',
										font=self.fuente).pack(side='left')
		self.label_valor = Entry(self.frame_valor, font=self.fuente)
		self.label_valor.pack(side='left')
		self.label_titulo_referencia = Label(self.frame_valor, text='Referencia: ', bg='#C8EDC8',
										font=self.fuente).pack(side='left')
		self.label_referencia = Entry(self.frame_valor, font=self.fuente)
		self.label_referencia.pack(side='left')

		# Frame que indica información
		self.frame_informacion = Frame(self.opciones_valor)
		self.frame_informacion.config(bg='#C8EDC8')
		self.frame_informacion.pack(pady=2.5, padx=2.5)

		self.label_informacion = Label(self.frame_informacion, bg='#C8EDC8', font=self.fuente)
		self.label_informacion.pack(side='left')

		self.label_informacion = Label(self.frame_informacion, bg='#C8EDC8', font=self.fuente)
		self.label_informacion.pack(side='right')

		# Frame que contienen los 3 botones que modifican la visualización de la Cola
		self.frame_boton_opcion = Frame(self.opciones_valor)
		self.frame_boton_opcion.config(bg='#C8EDC8')
		self.frame_boton_opcion.pack(pady=2.5, padx=2.5)
		self.button_add = Button(self.frame_boton_opcion, text='Add', bg='#C8EDC8', font=self.fuente, command=self.add_root)
		self.button_add.pack(side='left', padx=5)
		self.button_add_left = Button(self.frame_boton_opcion, text='Add Left', bg='#C8EDC8', font=self.fuente,
								 command=self.add_left)
		self.button_add_left.pack(side='left', padx=5)
		self.button_add_right = Button(self.frame_boton_opcion, text='Add Right', bg='#C8EDC8', font=self.fuente,
								 command=self.add_right)
		self.button_add_right.pack(side='left', padx=5)
		self.button_delete = Button(self.frame_boton_opcion, text='Delete', bg='#C8EDC8', font=self.fuente)
		self.button_delete.pack(side='left', padx=5)
		self.button_search = Button(self.frame_boton_opcion, text='Search', bg='#C8EDC8', font=self.fuente)
		self.button_search.pack(side='left', padx=5)



	def add_root(self):

		self.text = self.label_valor.get()

		tree.insert_left(self.text)

		self.label_root.config(text=tree.get_root())
		self.label_tamanoo.config(text=tree.size())
		self.label_depht.config(text=tree.get_depth())

	def add_left(self):

		self.element = self.label_valor.get()
		self.reference = self.label_referencia.get()

		tree.insert_left(self.element, self.reference)

		self.label_root.config(text=tree.get_root())
		self.label_tamanoo.config(text=tree.size())
		self.label_depht.config(text=tree.get_depth())


	def add_right(self):
		self.element = self.label_valor.get()
		self.reference = self.label_referencia.get()

		tree.insert_right(self.element, self.reference)

		self.label_root.config(text=tree.get_root())
		self.label_tamanoo.config(text=tree.size())
		self.label_depht.config(text=tree.get_depth())

	def remove(self):
		pass

	def search(self):
		pass