from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

from pagepila import PagePila
from pagecola import PageCola
from pagelistasimple import PageListaSimple
from pagelistacircular import PageListaCircular
from pagelistadoble import PageListaDoble
from pagelistacirculardoble import PageListaCircularDoble
from pagebinarytree import PageBinaryTree


class MainWindow():
	def __init__(self):

		self.main_window = Tk()
		self.main_window.title('Menú')
		self.main_window.resizable(False, False)
		self.main_window.geometry('255x700')

		self.frame_menu = Frame(self.main_window)
		self.frame_menu.config(bg='#007723')
		self.frame_menu.pack(expand=True, fill='both')

		# Fuente utilizada en todo el código
		self.fuente = Font(family="Open Sans", size=10, weight="bold")

		# Contenido del Menu
		self.label_menu = Label(self.frame_menu, text='Estructuras de datos', bg='#007723', fg='#C8EDC8', font=self.fuente).pack(pady=10, padx=10) #Pad y-x son los margenes del frame hacia los objetos

		self.image_pila = Image.open('images/baterias.png')
		self.resized_pila = self.image_pila.resize((35, 35) , Image.LANCZOS)
		self.new_image_pila = ImageTk.PhotoImage(self.resized_pila)
		self.button_pila = Button(self.frame_menu, command=PagePila, image=self.new_image_pila,
								  text=' Pila', bg='#007723', fg='#C8EDC8', width=200, height=50,
								  compound='left', font=self.fuente).pack(pady=10, padx=10)

		self.image_cola = Image.open('images/embotellamiento.png')
		self.resized_cola = self.image_cola.resize((35, 35), Image.LANCZOS)
		self.new_image_cola = ImageTk.PhotoImage(self.resized_cola)
		self.button_cola = Button(self.frame_menu, command=PageCola, image=self.new_image_cola,
								  text=' Cola', bg='#007723', fg='#C8EDC8', width=200, height=50,
								  compound='left', font=self.fuente).pack(pady=10,padx=10)

		self.image_lista_simple = Image.open('images/lista-de-verificacion.png')
		self.resized_lista_simple = self.image_lista_simple.resize((35, 35), Image.LANCZOS)
		self.new_image_lista_simple = ImageTk.PhotoImage(self.resized_lista_simple)
		self.button_lista_simple = Button(self.frame_menu, command=PageListaSimple, image=self.new_image_lista_simple,
										  text=' Lista Simple', bg='#007723', fg='#C8EDC8', width=200, height=50,
										  compound='left', font=self.fuente).pack(pady=10,padx=10)

		self.image_lista_circular = Image.open('images/1f7e2.png')
		self.resized_lista_circular = self.image_lista_circular.resize((35, 35), Image.LANCZOS)
		self.new_image_lista_circular = ImageTk.PhotoImage(self.resized_lista_circular)
		self.button_lista_circular = Button(self.frame_menu, command=PageListaCircular, image=self.new_image_lista_circular,
											text=' Lista Circular', bg='#007723', fg='#C8EDC8', width=200, height=50,
											compound='left', font=self.fuente).pack(pady=10, padx=10)

		self.image_lista_doble = Image.open('images/1323734 (1).png')
		self.resized_lista_doble = self.image_lista_doble.resize((35, 35), Image.LANCZOS)
		self.new_image_lista_doble = ImageTk.PhotoImage(self.resized_lista_doble)
		self.button_lista_doble = Button(self.frame_menu, command=PageListaDoble, image=self.new_image_lista_doble,
										 text=' Lista Doble', bg='#007723', fg='#C8EDC8', width=200, height=50,
										 compound='left', font=self.fuente).pack(pady=10, padx=10)

		self.image_lista_circular_doble = Image.open('images/rec.png')
		self.resized_lista_circular_doble = self.image_lista_circular_doble.resize((35, 35), Image.LANCZOS)
		self.new_image_lista_circular_doble = ImageTk.PhotoImage(self.resized_lista_circular_doble)
		self.button_lista_circular_doble = Button(self.frame_menu, command=PageListaCircularDoble, image=self.new_image_lista_circular_doble,
										 text=' Lista Circular Doble', bg='#007723', fg='#C8EDC8', width=200, height=50,
										 compound='left', font=self.fuente).pack(pady=10, padx=10)

		self.image_arbol = Image.open('images/arbol (1).png')
		self.resized_arbol = self.image_arbol.resize((35, 35), Image.LANCZOS)
		self.new_image_arbol = ImageTk.PhotoImage(self.resized_arbol)
		self.button_arbol = Button(self.frame_menu, image=self.new_image_arbol, command=PageBinaryTree,
											text=' Arbol', bg='#007723', fg='#C8EDC8', width=200, height=50,
											compound='left', font=self.fuente).pack(pady=10, padx=10)

		self.image_arbol_busqueda = Image.open('images/arbol.png')
		self.resized_arbol_busqueda = self.image_arbol_busqueda.resize((35, 35), Image.LANCZOS)
		self.new_image_arbol_busqueda = ImageTk.PhotoImage(self.resized_arbol_busqueda)
		self.button_arbol_busqueda = Button(self.frame_menu, image=self.new_image_arbol_busqueda,
											text=' Arbol de Búsqueda', bg='#007723', fg='#C8EDC8', width=200, height=50,
											compound='left', font=self.fuente).pack(pady=10, padx=10)

		self.main_window.mainloop()

Window = MainWindow()