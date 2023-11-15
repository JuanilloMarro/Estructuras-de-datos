import json
from tkinter import *
from tkinter.font import Font

from structures import pila

pila_structure = pila.Pila()


class PagePila():
	def __init__(self):
		self.top = Toplevel()

		self.top.title('Pila')

		self.top.resizable(False, False)

		self.top.geometry('1000x600')

		self.fuente = Font(family="Open Sans", size=10, weight="bold")

		# --- Visualización gráfica de la Pila ---

		# Frame principal donde se encuentra el frame del título y el frame de la construcción de la Pila
		self.frame_all_pila = Frame(self.top)
		self.frame_all_pila.config(width= 650, height=600, bg='white')
		self.frame_all_pila.pack(side='left', fill="both", expand=True)

		# Frame del título y su respectivo label
		self.frame_titulo_pila = Frame(self.frame_all_pila)
		self.frame_titulo_pila.config(bg='white', width= 650, height=150)
		self.frame_titulo_pila.pack(fill="both", expand=True, padx=100, pady=50)
		self.label_titulo_pila = Label(self.frame_titulo_pila)
		self.label_titulo_pila.config(font=self.fuente, text='Visualización de la Pila', bg='white')
		self.label_titulo_pila.pack()

		# Frame de la construcción de la Pila
		self.frame_pila = Frame(self.frame_all_pila)
		self.frame_pila.config(bg='white', width= 650, height=450)
		self.frame_pila.pack(fill="both", expand=True)

		# Frames que contienen los números que existen dentro de la Pila y su respectivo label
		self.frame_content = Frame(self.frame_pila)
		self.frame_content.config(bg='white')
		self.frame_content.pack(padx=100, pady=50)
		self.label_numero = Label(self.frame_content)
		self.label_numero.pack()

		# --- Información de la Pila ---

		# Frame principal donde se encuentra toda la información de la pila
		self.frame_info_pila = Frame(self.top)
		self.frame_info_pila.config(bg='#C8EDC8', width=350, height=750)
		self.frame_info_pila.pack(side='right', fill='both')

		# Frame que contiene el título 'Información de la Pila' y todos los frames correspondientes a él
		self.info_especifica_pila = Frame(self.frame_info_pila)
		self.info_especifica_pila.config(bg='#C8EDC8')
		self.info_especifica_pila.pack(pady=15, padx=5)
		self.label_title_info_pila = Label(self.info_especifica_pila, text='Información de la Pila', bg='#C8EDC8', font=self.fuente)
		self.label_title_info_pila.pack()

		# Frame que contiene dos labels: el maximo y el otro label donde se asigna el maximo
		self.frame_max = Frame(self.info_especifica_pila)
		self.frame_max.config(bg='#C8EDC8')
		self.frame_max.pack(pady=2.5, padx=2.5)
		self.label_max = Label(self.frame_max, text='Máximo: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_maxx = Label(self.frame_max, text=pila_structure.get_max(), bg='#C8EDC8', font=self.fuente)
		self.label_maxx.pack(side='right')

		# Frame que contiene dos labels: el tamaño y el otro label donde se asigna el tamaño
		self.frame_tamano = Frame(self.info_especifica_pila)
		self.frame_tamano.config(bg='#C8EDC8')
		self.frame_tamano.pack(pady=2.5, padx=2.5)
		self.label_tamano = Label(self.frame_tamano, text='Tamaño: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_tamanoo = Label(self.frame_tamano, text=pila_structure.get_size(), bg='#C8EDC8', font=self.fuente)
		self.label_tamanoo.pack(side='right')

		# Frame que contiene dos labels: el tope y el otro label donde se asigna el tope
		self.frame_tope = Frame(self.info_especifica_pila)
		self.frame_tope.config(bg='#C8EDC8')
		self.frame_tope.pack(pady=2.5, padx=2.5)
		self.label_tope = Label(self.frame_tope, text='Tope: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_topee = Label(self.frame_tope, text=pila_structure.get_head(), bg='#C8EDC8', font=self.fuente)
		self.label_topee.pack(side='left')

		# Frame que contiene dos labels: el fondo y el otro label donde se asigna el fondo
		self.frame_fondo = Frame(self.info_especifica_pila)
		self.frame_fondo.config(bg='#C8EDC8')
		self.frame_fondo.pack(pady=2.5, padx=2.5)
		self.label_fondo = Label(self.frame_fondo, text='Fondo: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
		self.label_fondoo = Label(self.frame_fondo, text=pila_structure.get_tail(), bg='#C8EDC8', font=self.fuente)
		self.label_fondoo.pack(side='left')

		# Opciones del valor ingresado por el user

		# Frame que contienen la entrada del valor ingresado por el usuario y los botones que los modifican
		self.opciones_valor = Frame(self.frame_info_pila)
		self.opciones_valor.config(bg='#C8EDC8')
		self.opciones_valor.pack(pady=15, padx=5)

		# Frame que contiene el título 'Ingrese el valor' y la entrada del valor
		self.frame_valor = Frame(self.opciones_valor)
		self.frame_valor.config(bg='#C8EDC8')
		self.frame_valor.pack()
		self.label_titulo_valor = Label(self.frame_valor, text='Ingrese el valor: ', bg='#C8EDC8', font=self.fuente).pack(side='left')
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

		# Frame que contienen los 3 botones que modifican la visualización de la Pila
		self.frame_boton_opcion = Frame(self.opciones_valor)
		self.frame_boton_opcion.config(bg='#C8EDC8')
		self.frame_boton_opcion.pack(pady=2.5, padx=2.5)
		self.button_add = Button(self.frame_boton_opcion, text='Add', bg='#C8EDC8', font=self.fuente, command=self.add)
		self.button_add.pack(side='left', padx=5)
		self.button_delete = Button(self.frame_boton_opcion, text='Delete',  bg='#C8EDC8', font=self.fuente, command=self.delete)
		self.button_delete.pack(side='left', padx=5)
		self.button_search = Button(self.frame_boton_opcion, text='Search', bg='#C8EDC8', font=self.fuente, command=self.search)
		self.button_search.pack(side='left', padx=5)

		# Cargar archivos

		self.frame_archivos = Frame(self.frame_info_pila)
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
		self.button_charge.config(bg='#C8EDC8', text='Charge', font=self.fuente ,command=self.cargar_desde_json)
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
		datos = pila_structure.to_list()

		self.file_data[nombre_archivo] = datos

		with open("json/pila.json", "w") as f:
			json.dump(self.file_data, f)

		self.nombre.delete(0, END)

		self.actualizar_lista()

	def cargar_desde_json(self):
		nombre_archivo = self.list.get(ACTIVE)

		datos = self.file_data[nombre_archivo]

		self.render(datos)

	def actualizar_lista(self):
		self.list.delete(0, END)

		with open("json/pila.json", "r") as f:
			self.file_data = json.load(f)

		for nombre_archivo in self.file_data.keys():
			self.list.insert(END, nombre_archivo)

	def render(self, datos):

		self.frame_pila.destroy()

		self.frame_pila = Frame(self.frame_all_pila)
		self.frame_pila.config(bg='white')
		self.frame_pila.pack(side='left', padx=225, pady=50)

		for item in datos:
			self.frame_content = Frame(self.frame_pila)
			self.frame_content.config(bg='#C8EDC8', width=15, height=3, bd=2, relief='solid')
			self.frame_content.pack()

			self.label_numero = Label(self.frame_content)
			self.label_numero.config(text=item, bg='#C8EDC8', width=15, height=3, font=self.fuente)
			self.label_numero.pack()

	def eliminar_archivo(self):

		nombre_archivo = self.list.get(ACTIVE)

		self.file_data.pop(nombre_archivo)

		with open("json/pila.json", "w") as f:
			json.dump(self.file_data, f)

		self.actualizar_lista()

	def actualizar_pila(self):

		self.frame_pila.destroy()

		self.frame_pila = Frame(self.frame_all_pila)
		self.frame_pila.config(bg='white')
		self.frame_pila.pack(side='left', padx=225, pady=50)

		for item in pila_structure.to_list():
			self.frame_content = Frame(self.frame_pila)
			self.frame_content.config(bg='#C8EDC8', width=15, height=3, bd=2, relief='solid')
			self.frame_content.pack()

			self.label_numero = Label(self.frame_content)
			self.label_numero.config(text=item, bg='#C8EDC8', width=15, height=3, font=self.fuente)
			self.label_numero.pack()

	def add(self):

		self.text = self.label_valor.get()

		pila_structure.push(self.text)
		self.actualizar_pila()

		self.label_maxx.config(text=pila_structure.get_max())
		self.label_tamanoo.config(text=pila_structure.get_size())
		self.label_topee.config(text=pila_structure.get_head())
		self.label_fondoo.config(text=pila_structure.get_tail())

		self.label_informacion.config(text='El nodo se ha agregado')
		self.label_valor.delete(0, END)

	def delete(self):

		pila_structure.pop()
		self.actualizar_pila()

		if pila_structure.get_size() == 0:
			self.label_maxx.config(text=pila_structure.get_max())
			self.label_tamanoo.config(text=pila_structure.get_size())
			self.label_topee.config(text='None')
			self.label_fondoo.config(text='None')
		else:
			self.label_maxx.config(text=pila_structure.get_max())
			self.label_tamanoo.config(text=pila_structure.get_size())
			self.label_topee.config(text=pila_structure.get_head())
			self.label_fondoo.config(text=pila_structure.get_tail())

		self.label_informacion.config(text='El nodo se ha eliminado')
		self.label_valor.delete(0, END)

	def search(self):

		self.text = self.label_valor.get()

		elemento = pila_structure.search(self.text)

		self.label_informacion.config(text=elemento)
