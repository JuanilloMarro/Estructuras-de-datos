class Nodo:
    def __init__(self, elemento):
        # Parte amarilla
        self.data = elemento
        # Parte morada
        self.siguiente = None

    def get_data(self):
        return self.data


class Pila:

    def __init__(self, max=-1):
        self.tope = None
        self._size = 0
        self.max = max

    def push(self, elemento):
        if self.max == -1 or self._size < self.max:

            nuevo_nodo = Nodo(elemento)
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo
            self._size += 1
        else:
            raise Exception('Desbordamiento de pila')

    def to_list(self, references=False):
        aux = self.tope
        elementos = []
        elementos_references = []
        while True:
            if aux is None:
                break
            else:
                if type(aux.data) == str:
                    if aux.data.isdigit():
                        elementos.append(int(aux.data))

                    if not aux.data.isdigit():
                        elementos.append(aux.data)

                if not type(aux.data) == str:
                    elementos.append(aux.data)

                if references:
                    elementos_references.append(aux)

                aux = aux.siguiente

        if references:
            return elementos_references

        return elementos

    def pop(self):
        if self.tope is None:
            raise Exception('Subdesbordamiento de pila')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self._size -= 1
            return aux

    # Modificamos el método search
    def search(self, elemento):
        resultado = ''
        aux = self.tope
        while True:
            if aux is None:
                break
            else:
                if aux.data == elemento:
                    resultado += 'El nodo si se encuentra en la Pila'
                    return resultado
                else:
                    aux = aux.siguiente

        resultado += 'El nodo no se encuentra en la Pila'
        return resultado

    def get_size(self):
        return self._size

    def get_max(self):
        return self.max

    def get_head(self):
        return self.tope.data if self.tope is not None else None

    # Método que devuelve la cola de la pila
    def get_tail(self):
        if self.tope is None:
            return None
        else:
            aux = self.tope
            while True:
                if aux.siguiente is None:
                    return aux.data
                else:
                    aux = aux.siguiente

    def is_digit(self, value):
        if type(value) == str:
            if value.isdigit():
                return True
            else:
                return False
