class Pila:
    def __init__(self):
        self.items = []
        self.states = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0
    
    def pushStates(self, State):
        self.states.append(State)
        
    def listStates(self):
        return self.states
    
    def remove(self):
        self.states.clear()

def es_palindromo(cadena,pila):
    
    # Crear una pila vacía
    pila.remove()
    # Procesar la mitad izquierda de la cadena y empujarla a la pila
    mitad = len(cadena) // 2
    for i in range(mitad):
        pila.pushStates(0)
        pila.push(cadena[i])

    # Verificar si la longitud de la cadena es impar
    if len(cadena) % 2 == 1:
        mitad += 1

    # Comparar la segunda mitad de la cadena con la pila
    for i in range(mitad, len(cadena)):
        pila.pushStates(1)
        if pila.is_empty() or cadena[i] != pila.pop():
            return False

    pila.pushStates(2)
    return True

# Prueba del autómata de pila para verificar si una cadena es un palíndromo
cadena1 = "abba"
cadena2 = "aba"
cadena3 = "ababa"
cadena4 = "abaa"
pila=Pila()

print(f'"{cadena1}" es un palíndromo: {es_palindromo(cadena1,pila)} el recorrido es {pila.states}')
print(f'"{cadena2}" es un palíndromo: {es_palindromo(cadena2,pila)} el recorrido es {pila.states}')
print(f'"{cadena3}" es un palíndromo: {es_palindromo(cadena3,pila)} el recorrido es {pila.states}')
print(f'"{cadena4}" es un palíndromo: {es_palindromo(cadena4,pila)} el recorrido es {pila.states}')
