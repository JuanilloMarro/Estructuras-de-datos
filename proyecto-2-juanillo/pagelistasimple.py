import json
from tkinter import *
from tkinter.font import Font

from structures import lista_simple

lista_simple_structure = lista_simple.LinkedList()


class PageListaSimple():
	def __init__(self):
		self.top = Toplevel()

		self.top.title('Lista Simple')

		self.top.resizable(False, False)

		self.top.geometry('1250x600')

		self.fuente = Font(family="Open Sans", size=10, weight="bold")

		# --- Visualización gráfica de la Lista Simple ---

		# Frame principal donde se encuentra el frame del título y el frame de la construcción de la Lista Simple
		self.frame_all_lista_simple = Frame(self.top)
		self.frame_all_lista_simple.config(width= 650, height=600, bg='white')
		self.frame_all_lista_simple.pack(side='left', fill="both", expand=True)

		# Frame del título y su respectivo label
		self.frame_titulo_lista_simple = Frame(self.frame_all_lista_simple)
		self.frame_titulo_lista_simple.config(bg='white', width= 650, height=150)
		self.frame_titulo_lista_simple.pack(fill="both", expand=True, padx=100, pady=50)
		self.label_titulo_lista_simple = Label(self.frame_titulo_lista_simple)
		self.label_titulo_lista_simple.config(font=self.fuente, text='Visualización de la Lista Simple', bg='white')
		self.label_titulo_lista_simple.pack()

		# Frame de la construcción de la Lista Simple
		self.frame_lista_simple = Frame(self.frame_all_lista_simple)
		self.frame_lista_simple.config(bg='white', width= 650, height=450)
		self.frame_lista_simple.pack(fill="both", expand=True)

		# Frames que contienen los números que existen dentro de la Lista Simple y su respectivo label
		self.frame_content = Frame(self.frame_lista_simple)
		self.frame_content.config(bg='white')
		self.frame_content.pack(padx=100, pady=50)
		self.label_numero = Label(self.frame_content)
		self.label_numero.pack()

		# --- Información de la Lista Simple ---

		# Frame principal donde se encuentra toda la información de la Lista Simple
		self.frame_info_lista_simple = Frame(self.top)
		self.frame_info_lista_simple.config(bg='#C8EDC8', width=350, height=750)
		self.frame_info_lista_simple.pack(side='right', fill='both')

		# Frame que contiene el título 'Información de la Lista Simple' y todos los frames correspondientes a él
		self.info_especifica_lista_simple = Frame(self.frame_info_lista_simple)
		self.info_especifica_lista_simple.config(bg='#C8EDC8')
		self.info_especifica_lista_simple.pack(pady=15, padx=5)
		self.label_title_info_lista_simple = Label(self.info_especifica_lista_simple, text='Información de la Lista Simple', bg='#C8EDC8',
												   font=self.fuente)
		self.label_title_info_lista_simple.pack()

		# Frame que contiene dos labels: el tamaño y el otro label donde se asigna el tamaño
		self.frame_tamano = Frame(self.info_especifica_lista_simple)
		self.frame_tamano.config(bg='#C8EDC8')
		self.frame_tamano.pack(pady=2.5, padx=2.5)
		self.label_tamano = Label(self.frame_tamano, text='Tamaño: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_tamanoo = Label(self.frame_tamano, text=lista_simple_structure.get_size(), bg='#C8EDC8', font=self.fuente)
		self.label_tamanoo.pack(side='right')

		# Frame que contiene dos labels: el tope y el otro label donde se asigna el tope
		self.frame_tope = Frame(self.info_especifica_lista_simple)
		self.frame_tope.config(bg='#C8EDC8')
		self.frame_tope.pack(pady=2.5, padx=2.5)
		self.label_tope = Label(self.frame_tope, text='Tope: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_topee = Label(self.frame_tope, text=lista_simple_structure.get_head(), bg='#C8EDC8', font=self.fuente)
		self.label_topee.pack(side='left')

		# Frame que contiene dos labels: el fondo y el otro label donde se asigna el fondo
		self.frame_fondo = Frame(self.info_especifica_lista_simple)
		self.frame_fondo.config(bg='#C8EDC8')
		self.frame_fondo.pack(pady=2.5, padx=2.5)
		self.label_fondo = Label(self.frame_fondo, text='Fondo: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_fondoo = Label(self.frame_fondo, text=lista_simple_structure.get_tail(), bg='#C8EDC8', font=self.fuente)
		self.label_fondoo.pack(side='left')

		# Opciones del valor ingresado por el user

		# Frame que contienen la entrada del valor ingresado por el usuario y los botones que los modifican
		self.opciones_valor = Frame(self.frame_info_lista_simple)
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

		# Frame que indica información
		self.frame_informacion = Frame(self.opciones_valor)
		self.frame_informacion.config(bg='#C8EDC8')
		self.frame_informacion.pack(pady=2.5, padx=2.5)

		self.label_informacion = Label(self.frame_informacion, bg='#C8EDC8', font=self.fuente)
		self.label_informacion.pack(side='left')

		self.label_informacion = Label(self.frame_informacion, bg='#C8EDC8', font=self.fuente)
		self.label_informacion.pack(side='right')

		# Frame que contienen los 3 botones que modifican la visualización de la Lista Simple
		self.frame_boton_opcion = Frame(self.opciones_valor)
		self.frame_boton_opcion.config(bg='#C8EDC8')
		self.frame_boton_opcion.pack(pady=2.5, padx=2.5)
		self.button_add = Button(self.frame_boton_opcion, text='Add', bg='#C8EDC8', font=self.fuente, command=self.add)
		self.button_add.pack(side='left', padx=5)
		self.button_add_last = Button(self.frame_boton_opcion, text='Add Last', bg='#C8EDC8', font=self.fuente, command=self.add_last)
		self.button_add_last.pack(side='left', padx=5)
		self.button_delete = Button(self.frame_boton_opcion, text='Delete', bg='#C8EDC8', font=self.fuente,
									command=self.delete)
		self.button_delete.pack(side='left', padx=5)
		self.button_delete_last = Button(self.frame_boton_opcion, text='Delete Last', bg='#C8EDC8', font=self.fuente,
									command=self.delete_last)
		self.button_delete_last.pack(side='left', padx=5)
		self.button_search = Button(self.frame_boton_opcion, text='Search', bg='#C8EDC8', font=self.fuente,
									command=self.search)
		self.button_search.pack(side='left', padx=5)

		# Cargar archivos

		self.frame_archivos = Frame(self.frame_info_lista_simple)
		self.frame_archivos.config(bg='#C8EDC8')
		self.frame_archivos.pack(pady=15, padx=5)

		self.titulo_general = Label(self.frame_archivos, font=self.fuente, text='Opciones de archivo', bg='#C8EDC8')
		self.titulo_general.pack()

		self.frame_nombre_archivo = Frame(self.frame_archivos)
		self.frame_nombre_archivo.config(bg='#C8EDC8')
		self.frame_nombre_archivo.pack(pady=2.5, padx=2.5)

		self.titulo = Label(self.frame_nombre_archivo)
		self.titulo.config(bg='#C8EDC8', font=self.fuente, text='Nombre archivo: ')
		self.titulo.pack(side='left')

		self.nombre = Entry(self.frame_nombre_archivo)
		self.nombre.config(font=self.fuente)
		self.nombre.pack(side='right')

		self.frame_botones_archivo = Frame(self.frame_archivos)
		self.frame_botones_archivo.config(bg='#C8EDC8')
		self.frame_botones_archivo.pack(pady=2.5, padx=2.5)

		self.button_save = Button(self.frame_botones_archivo, command=self.guardar_en_json)
		self.button_save.config(bg='#C8EDC8', text='Save', font=self.fuente)
		self.button_save.pack(side='left', padx=5)

		self.button_refresh = Button(self.frame_botones_archivo)
		self.button_refresh.config(bg='#C8EDC8', text='Refresh', font=self.fuente, command=self.actualizar_lista)
		self.button_refresh.pack(side='right', padx=5)

		self.button_delete_list = Button(self.frame_botones_archivo)
		self.button_delete_list.config(bg='#C8EDC8', text='Delete', font=self.fuente, command=self.eliminar_archivo)
		self.button_delete_list.pack(side='right', padx=5)

		self.button_charge = Button(self.frame_botones_archivo)
		self.button_charge.config(bg='#C8EDC8', text='Charge', font=self.fuente, command=self.cargar_desde_json)
		self.button_charge.pack(side='right', padx=5)

		self.frame_list = Frame(self.frame_archivos)
		self.frame_list.config(bg='#C8EDC8')
		self.frame_list.pack(pady=2.5, padx=2.5)

		self.list = Listbox(self.frame_list)
		self.list.config(font=self.fuente)
		self.list.pack()

		self.file_data = {}

	def guardar_en_json(self):
		nombre_archivo = self.nombre.get()
		datos = lista_simple_structure.to_list()

		self.file_data[nombre_archivo] = datos

		with open("json/lista_simple.json", "w") as f:
			json.dump(self.file_data, f)

		self.nombre.delete(0, END)

		self.actualizar_lista()

	def cargar_desde_json(self):
		nombre_archivo = self.list.get(ACTIVE)

		datos = self.file_data[nombre_archivo]

		self.render(datos)

	def actualizar_lista(self):
		self.list.delete(0, END)

		with open("json/lista_simple.json", "r") as f:
			self.file_data = json.load(f)

		for nombre_archivo in self.file_data.keys():
			self.list.insert(END, nombre_archivo)

	def render(self, datos):

		self.frame_lista_simple.destroy()

		self.frame_lista_simple = Frame(self.frame_all_lista_simple)
		self.frame_lista_simple.config(bg='white')
		self.frame_lista_simple.pack(side='left', pady=200)

		for item in datos:

			if item == datos[0]:
				self.frame_content = Frame(self.frame_lista_simple)
				self.frame_content.config(bg='#C8EDC8', width=7, height=3, bd=2, relief='solid')
				self.frame_content.pack(side='left')

				self.label_numero = Label(self.frame_content)
				self.label_numero.config(text=item, bg='#C8EDC8', width=7, height=3, font=self.fuente)
				self.label_numero.pack()
			else:
				self.frame_content = Frame(self.frame_lista_simple)
				self.frame_content.config(bg='white', width=7, height=3)
				self.frame_content.pack(side='left')

				self.frame_numero = Frame(self.frame_content)
				self.frame_numero.config(bg='#C8EDC8', width=7, height=3, bd=2, relief='solid')
				self.frame_numero.pack(side='right')

				self.frame_flecha = Frame(self.frame_content)
				self.frame_flecha.config(bg='white', width=7, height=3)
				self.frame_flecha.pack(side='left')

				self.label_numero = Label(self.frame_numero)
				self.label_numero.config(text=item, bg='#C8EDC8', width=7, height=3, font=self.fuente)
				self.label_numero.pack()

				self.label_flecha = Label(self.frame_flecha)
				self.label_flecha.config(text='-->', bg='white', width=7, height=3)
				self.label_flecha.pack()

	def eliminar_archivo(self):
		nombre_archivo = self.list.get(ACTIVE)

		self.file_data.pop(nombre_archivo)

		with open("json/lista_simple.json", "w") as f:
			json.dump(self.file_data, f)

		self.actualizar_lista()

	def actualizar_lista_simple(self):

		self.frame_lista_simple.destroy()

		self.frame_lista_simple = Frame(self.frame_all_lista_simple)
		self.frame_lista_simple.config(bg='white')
		self.frame_lista_simple.pack(side='left', pady=200)

		for item in lista_simple_structure.to_list():

			if item == lista_simple_structure.to_list()[0]:
				self.frame_content = Frame(self.frame_lista_simple)
				self.frame_content.config(bg='#C8EDC8', width=7, height=3, bd=2, relief='solid')
				self.frame_content.pack(side='left')

				self.label_numero = Label(self.frame_content)
				self.label_numero.config(text=item, bg='#C8EDC8', width=7, height=3, font=self.fuente)
				self.label_numero.pack()
			else:
				self.frame_content = Frame(self.frame_lista_simple)
				self.frame_content.config(bg='white', width=7, height=3)
				self.frame_content.pack(side='left')

				self.frame_numero = Frame(self.frame_content)
				self.frame_numero.config(bg='#C8EDC8', width=7, height=3, bd=2, relief='solid')
				self.frame_numero.pack(side='right')

				self.frame_flecha = Frame(self.frame_content)
				self.frame_flecha.config(bg='white', width=7, height=3)
				self.frame_flecha.pack(side='left')

				self.label_numero = Label(self.frame_numero)
				self.label_numero.config(text=item, bg='#C8EDC8', width=7, height=3, font=self.fuente)
				self.label_numero.pack()

				self.label_flecha = Label(self.frame_flecha)
				self.label_flecha.config(text='-->', bg='white', width=7, height=3)
				self.label_flecha.pack()

	def add(self):

		self.text = self.label_valor.get()

		lista_simple_structure.prepend(self.text)

		self.label_tamanoo.config(text=lista_simple_structure.get_size())
		self.label_topee.config(text=lista_simple_structure.get_head())
		self.label_fondoo.config(text=lista_simple_structure.get_tail())

		self.label_informacion.config(text='El nodo se ha agregado')
		self.label_valor.delete(0, END)

		self.actualizar_lista_simple()

	def add_last(self):

		self.text = self.label_valor.get()

		lista_simple_structure.append(self.text)

		self.label_tamanoo.config(text=lista_simple_structure.get_size())
		self.label_topee.config(text=lista_simple_structure.get_head())
		self.label_fondoo.config(text=lista_simple_structure.get_tail())

		self.label_informacion.config(text='El nodo se ha agregado')
		self.label_valor.delete(0, END)

		self.actualizar_lista_simple()

	def delete(self):

		lista_simple_structure.remove_head()

		if lista_simple_structure.get_size() == 0:
			self.label_tamanoo.config(text=lista_simple_structure.get_size())
			self.label_topee.config(text='None')
			self.label_fondoo.config(text='None')
		else:
			self.label_tamanoo.config(text=lista_simple_structure.get_size())
			self.label_topee.config(text=lista_simple_structure.get_head())
			self.label_fondoo.config(text=lista_simple_structure.get_tail())

		self.label_informacion.config(text='El nodo se ha eliminado')
		self.label_valor.delete(0, END)

		self.actualizar_lista_simple()

	def delete_last(self):

		lista_simple_structure.remove_tail()

		if lista_simple_structure.get_size() == 0:
			self.label_tamanoo.config(text=lista_simple_structure.get_size())
			self.label_topee.config(text='None')
			self.label_fondoo.config(text='None')
		else:
			self.label_tamanoo.config(text=lista_simple_structure.get_size())
			self.label_topee.config(text=lista_simple_structure.get_head())
			self.label_fondoo.config(text=lista_simple_structure.get_tail())

		self.label_informacion.config(text='El nodo se ha eliminado')
		self.label_valor.delete(0, END)

		self.actualizar_lista_simple()

	def search(self):

		self.text = self.label_valor.get()

		elemento = lista_simple_structure.search(self.text)

		self.label_informacion.config(text=elemento)