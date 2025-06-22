# KATA 1
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias(cadena):  # Definimos una función que recibe un texto como argumento
    cadena = cadena.replace(" ", "")  # Quitamos los espacios en blanco para no contarlos
    frecuencias = {}  # Creamos un diccionario vacío donde guardaremos cuántas veces aparece cada letra
    for letra in cadena:  # Recorremos cada letra del texto
        # Si la letra ya existe en el diccionario, le sumamos 1. Si no, empezamos con 0 + 1
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias  # Devolvemos el diccionario con las frecuencias de cada letra

# Llamamos a la función con el texto "hola mundo" y mostramos el resultado
print("Kata 1:", contar_frecuencias("hola mundo"))

# KATA 2
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
def duplicar_valores(lista):  # Definimos una función que recibe una lista de números
    # Usamos map para multiplicar cada elemento x por 2. Convertimos el resultado a lista.
    return list(map(lambda x: x * 2, lista))
                
# Llamamos a la función con una lista de ejemplo y mostramos el resultado
print("Kata 2:", duplicar_valores([1, 2, 3, 4]))

# KATA 3
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras_con_objetivo(lista_palabras, objetivo):  # Recibe una lista de palabras y un texto objetivo
    # Usamos una lista por comprensión para filtrar solo las palabras que contienen el objetivo dentro
    return [palabra for palabra in lista_palabras if objetivo in palabra]

# Probamos con una lista de palabras y buscamos las que contienen "ga"
print("Kata 3:", buscar_palabras_con_objetivo(["gato", "perro", "gallina"], "ga"))

# KATA 4
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
def diferencia_listas(lista1, lista2):  # Recibimos dos listas del mismo tamaño
    # Usamos map para restar cada par de elementos (uno de cada lista)
    return list(map(lambda a, b: a - b, lista1, lista2))

# Probamos con dos listas: 10-1, 20-2, 30-3 = 9, 18, 27
print("Kata 4:", diferencia_listas([10, 20, 30], [1, 2, 3]))

# KATA 5
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_nota(lista_notas, nota_aprobado=5):  # Recibe una lista de notas y una nota mínima para aprobar
    if not lista_notas:  # Si la lista está vacía
        return (0, "suspenso")  # No hay notas, se considera suspenso
    media = sum(lista_notas) / len(lista_notas)  # Calculamos la media sumando y dividiendo por el número de notas
    estado = "aprobado" if media >= nota_aprobado else "suspenso"  # Si la media es mayor o igual a 5, aprobado
    return (media, estado)  # Devolvemos una tupla con la media y el estado

# Probamos con una lista de notas y mostramos la media y si está aprobado o no
print("Kata 5:", evaluar_nota([6, 5, 7]))

# KATA 6
# Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):  # Definimos una función que calcula el factorial
    if n == 0 or n == 1:  # Caso base: el factorial de 0 o 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva multiplicando el número por el factorial del anterior

print("Kata 6:", factorial(5))  # Probamos con el número 5

# KATA 7
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
def tuplas_a_strings(lista_tuplas):  # Recibimos una lista de tuplas
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))  # Convertimos cada tupla en string uniendo sus elementos

print("Kata 7:", tuplas_a_strings([(1, 2), ("a", "b"), (True, False)]))  # Probamos con varios tipos de tuplas

# KATA 8
# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def realizar_division(a, b):  # Definimos una función que realiza la división entre dos números
    return a / b  # Devuelve el resultado de la división

def dividir():  # Definimos la función principal que interactúa con el usuario
    try:
        a = float(input("Introduce el primer número: "))  # Pedimos al usuario el primer número y lo convertimos a float
        b = float(input("Introduce el segundo número: "))  # Pedimos el segundo número
        resultado = realizar_division(a, b)  # Llamamos a la función que hace la división y guardamos el resultado
    except ValueError:  # Captura si el usuario introduce algo que no se puede convertir a número
        mensaje = "Error: Debes introducir números válidos."  # Mensaje de error para entrada inválida
    except ZeroDivisionError:  # Captura el error de dividir entre cero
        mensaje = "Error: No se puede dividir entre cero."  # Mensaje correspondiente
    else:
        mensaje = f"Resultado: {resultado}"  # Si no hay errores, guardamos el resultado como mensaje
    finally:
        print("Kata 8:", mensaje if 'mensaje' in locals() else "Fin del programa.")  # Mostramos el mensaje final, asegurando que 'mensaje' existe

dividir()  # Ejecutamos la función

# KATA 9
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
def filtrar_mascotas(lista):  # Definimos una función que recibe una lista de nombres de mascota
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]  # Lista de mascotas que queremos excluir
    return list(filter(lambda m: m not in prohibidas, lista))  # Usamos filter para excluir las mascotas prohibidas

# Probamos la función con una lista de mascotas
print("Kata 9:", filtrar_mascotas(["Perro", "Tigre", "Gato", "Oso", "Loro"]))

# KATA 10
# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def calcular_promedio(lista):  # Definimos la función que recibe una lista de números
    if not lista:  # Si la lista está vacía
        raise ValueError("La lista está vacía")  # Lanzamos una excepción con un mensaje personalizado
    return sum(lista) / len(lista)  # Calculamos el promedio sumando los elementos y dividiendo por la cantidad

try:  # Usamos try para intentar ejecutar el cálculo del promedio
    print("Kata 10:", calcular_promedio([4, 5, 6]))  # Probamos con una lista válida
except ValueError as e:  # Capturamos el error si se lanza una excepción
    print("Error:", e)  # Mostramos el mensaje de error


# KATA 11
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def pedir_edad():  # Definimos la función para pedir edad
    try:
        edad = int(input("Introduce tu edad: "))  # Pedimos al usuario que introduzca su edad como entero
        if edad < 0 or edad > 120:  # Verificamos que esté en el rango válido
            raise ValueError("Edad fuera de rango")  # Lanzamos un error si no está en el rango
    except ValueError as e:
        print("Kata 11:", "Error:", e)  # Mostramos un mensaje de error si hay excepción
    else:
        print("Kata 11:", "Edad registrada correctamente:", edad)  # Si no hay errores, mostramos la edad
pedir_edad()

# KATA 12
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().
def longitudes_palabras(frase):  # Recibimos una frase como string
    palabras = frase.split()  # Dividimos la frase en palabras
    return list(map(len, palabras))  # Aplicamos len a cada palabra usando map

# Probamos la función con una frase de ejemplo
print("Kata 12:", longitudes_palabras("Estamos aprendiendo Python"))

# KATA 13
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def mayus_minus_unicas(cadena):  # Recibimos una cadena de caracteres
    unicas = set(cadena)  # Eliminamos letras repetidas convirtiendo a conjunto
    return list(map(lambda c: (c.upper(), c.lower()), unicas))  # Usamos map para generar las tuplas

# Probamos con una palabra
print("Kata 13:", mayus_minus_unicas("Python"))

# KATA 14
# Crea una función que retorne las palabras de una lista de palabras que comiencen con una letra en específico. Usa la función filter().
def palabras_por_letra(lista, letra):  # Recibe una lista de palabras y una letra
    return list(filter(lambda palabra: palabra.startswith(letra), lista))  # Filtramos las palabras que empiezan con la letra

# Probamos la función con varias palabras y la letra "p"
print("Kata 14:", palabras_por_letra(["perro", "gato", "pez", "tigre"], "p"))

# KATA 15
# Crea una función lambda que sume 3 a cada número de una lista dada.
def sumar_tres(lista):  # Definimos una función que recibe una lista de números
    return list(map(lambda x: x + 3, lista))  # Usamos map y una lambda para sumar 3 a cada elemento

# Probamos con una lista de ejemplo
print("Kata 15:", sumar_tres([1, 2, 3, 4]))

# KATA 16
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
def palabras_mas_largas(frase, n):  # Recibe una frase y un número entero n
    palabras = frase.split()  # Separamos la frase en palabras
    return list(filter(lambda palabra: len(palabra) > n, palabras))  # Usamos filter para quedarnos con las palabras más largas que n

# Probamos con una frase y el número 4
print("Kata 16:", palabras_mas_largas("Estamos aprendiendo Python con katas", 4))

# KATA 17
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5, 7, 2] corresponde al número 572. Usa la función reduce().
from functools import reduce  # Importamos reduce desde functools para acumulación de valores

def lista_a_numero(digitos):  # Definimos una función que recibe una lista de dígitos
    if not all(isinstance(d, int) and 0 <= d <= 9 for d in digitos):  # Validamos que todos los elementos sean enteros del 0 al 9
        raise ValueError("La lista debe contener solo dígitos del 0 al 9.")  # Lanzamos un error si no es así
    return reduce(lambda x, y: x * 10 + y, digitos)  # Combinamos los dígitos en un solo número decimal

try:
    print("Kata 17:", lista_a_numero([5, 7, 2]))  # Probamos la función con una lista de ejemplo
except ValueError as e:
    print("Kata 17:", "Error:", e)  # Mostramos el mensaje de error si se lanza

# KATA 18
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter().
def estudiantes_destacados(estudiantes):  # Recibimos una lista de diccionarios con info de estudiantes
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))  # Filtramos los que tienen >= 90

# Probamos con una lista de estudiantes
lista_estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 92},
    {"nombre": "Marta", "edad": 19, "calificacion": 95},
]
print("Kata 18:", estudiantes_destacados(lista_estudiantes))

# KATA 19
# Crea una función lambda que filtre los números impares de una lista dada.
def filtrar_impares(lista):  # Recibe una lista de números
    return list(filter(lambda x: x % 2 != 0, lista))  # Usamos filter y una lambda para quedarnos con los impares

# Probamos con una lista de ejemplo
print("Kata 19:", filtrar_impares([1, 2, 3, 4, 5, 6, 7]))

# KATA 20
# Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter().
def filtrar_enteros(lista):  # Recibimos una lista mixta
    return list(filter(lambda x: isinstance(x, int), lista))  # Usamos filter para quedarnos solo con los enteros

# Probamos con una lista mixta
print("Kata 20:", filtrar_enteros([1, "hola", 3, "mundo", 5]))

# KATA 21
# Crea una función que calcule el cubo de un número dado mediante una función lambda.
def cubo(numero):  # Recibe un número como parámetro
    return (lambda x: x ** 3)(numero)  # Usa una función lambda que eleva el número al cubo

# Probamos con el número 4
print("Kata 21:", cubo(4))

# KATA 22
# Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().
from functools import reduce

def producto_total(lista):  # Recibe una lista de números
    return reduce(lambda x, y: x * y, lista)  # Usa reduce para multiplicar todos los elementos de la lista

# Probamos con una lista de ejemplo
print("Kata 22:", producto_total([2, 3, 4]))

# KATA 23
# Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(lista):  # Recibe una lista de strings
    return reduce(lambda a, b: a + b, lista)  # Usa reduce para concatenar todas las palabras

# Probamos con una lista de palabras
print("Kata 23:", concatenar_palabras(["Hola", " ", "mundo", "!"]))

# KATA 24
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().
def diferencia_total(lista):  # Definimos una función que recibe una lista de números
    if not lista:  # Si la lista está vacía
        return 0  # Devolvemos 0 para evitar errores
    return max(lista) - min(lista)  # Calculamos la diferencia entre el valor máximo y el mínimo

print("Kata 24:", diferencia_total([100, 30, 20]))  # Probamos la función

# KATA 25
# Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):  # Recibe una cadena de texto
    return len(cadena)  # Devuelve la longitud total de la cadena

# Probamos con un texto de ejemplo
print("Kata 25:", contar_caracteres("Python es genial"))

# KATA 26
# Crea una función lambda que calcule el resto de la división entre dos números dados.
def calcular_resto(a, b):  # Recibe dos números
    return (lambda x, y: x % y)(a, b)  # Usa una lambda para obtener el resto de la división

# Probamos con 4 y 2
print("Kata 26:", calcular_resto(4, 2))

# KATA 27
# Crea una función que calcule el promedio de una lista de números.
def promedio(lista):  # Recibe una lista de números
    return sum(lista) / len(lista) if lista else 0  # Calcula el promedio o devuelve 0 si la lista está vacía

# Probamos con una lista de ejemplo
print("Kata 27:", promedio([5, 10, 15]))

# KATA 28
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):  # Recibe una lista
    vistos = set()  # Usamos un conjunto para guardar los elementos ya vistos
    for elemento in lista:  # Recorremos la lista
        if elemento in vistos:  # Si el elemento ya fue visto, es el primer duplicado
            return elemento
        vistos.add(elemento)  # Si no, lo añadimos al conjunto
    return None  # Si no hay duplicados, devolvemos None

# Probamos con una lista que contiene duplicados
print("Kata 28:", primer_duplicado([1, 2, 3, 2, 4]))

# KATA 29
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar(texto):  # Recibe cualquier variable
    texto = str(texto)  # Convertimos la variable a string
    return '#' * (len(texto) - 4) + texto[-4:] if len(texto) > 4 else texto  # Reemplazamos todo excepto los últimos 4

# Probamos con un número de ejemplo
print("Kata 29:", enmascarar("123456789"))

# KATA 30
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):  # Recibe dos palabras
    return sorted(palabra1.lower()) == sorted(palabra2.lower())  # Compara las letras ordenadas en minúscula

# Probamos con dos palabras anagramas
print("Kata 30:", son_anagramas("roma", "amor"))

# KATA 31
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    nombres = input("Introduce una lista de nombres separados por comas: ").split(",")  # Pedimos al usuario que introduzca una lista de nombres separados por comas y la convertimos en lista
    nombres = [nombre.strip() for nombre in nombres]  # Eliminamos los espacios extra en cada nombre de la lista
    nombre_buscar = input("Introduce el nombre a buscar: ").strip()  # Solicitamos el nombre que desea buscar y quitamos espacios
    if nombre_buscar in nombres:  # Verificamos si el nombre está en la lista
        print("Kata 31:", f"{nombre_buscar} fue encontrado en la lista.")  # Si está, mostramos un mensaje que fue encontrado
    else:
        raise ValueError(f"{nombre_buscar} no está en la lista.")  # Si no está, lanzamos una excepción con un mensaje

buscar_nombre()  # Ejecutamos la función

# KATA 32
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre_completo, lista_empleados):  # Definimos la función que toma un nombre y una lista de empleados
    for empleado in lista_empleados:  # Recorremos la lista de empleados
        if empleado["nombre"] == nombre_completo:  # Si encontramos el nombre buscado
            return empleado["puesto"]  # Devolvemos el puesto correspondiente
    return "La persona no trabaja aquí."  # Si no lo encontramos, devolvemos un mensaje indicándolo

empleados = [  # Creamos una lista de diccionarios con empleados y sus puestos
    {"nombre": "Ana Pérez", "puesto": "Gerente"},
    {"nombre": "Luis Gómez", "puesto": "Desarrollador"}
]

print("Kata 32:", buscar_empleado("Luis Gómez", empleados))  # Probamos la función buscando un empleado existente

# KATA 33
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def sumar_listas(lista1, lista2):  # Definimos la función que recibe dos listas como parámetros
    return list(map(lambda x, y: x + y, lista1, lista2))  # Usamos map con una función lambda para sumar cada par de elementos en la misma posición

print("Kata 33:", sumar_listas([1, 2, 3], [4, 5, 6]))  # Probamos la función con dos listas)

# KATA 34
# Crea la clase Árbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    def __init__(self):  # Constructor del árbol
        self.tronco = 1  # Longitud inicial del tronco
        self.ramas = []  # Lista de ramas (vacía al inicio)

    def crecer_tronco(self):  # Método para aumentar el tronco
        self.tronco += 1

    def nueva_rama(self):  # Añadir una rama nueva con longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):  # Aumentar la longitud de todas las ramas
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, index):  # Eliminar una rama por índice
        if 0 <= index < len(self.ramas):
            del self.ramas[index]

    def info_arbol(self):  # Devuelve un resumen del estado del árbol
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

    def __str__(self):  # Representación legible del objeto
        return f"Árbol -> Tronco: {self.tronco}, Ramas: {len(self.ramas)}, Longitudes: {self.ramas}"

# Prueba de uso del árbol
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print("Kata 34:", arbol)

# KATA 36
# Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):  # Método constructor que inicializa nombre, saldo y tipo de cuenta
        self.nombre = nombre  # Almacena el nombre del usuario
        self.saldo = saldo  # Almacena el saldo inicial del usuario
        self.cuenta_corriente = cuenta_corriente  # Almacena si el usuario tiene cuenta corriente

    def retirar_dinero(self, cantidad):  # Método para retirar dinero del saldo
        if cantidad <= 0:  # Comprobamos que la cantidad sea positiva
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:  # Verificamos que haya saldo suficiente
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad  # Descontamos la cantidad

    def transferir_dinero(self, otro_usuario, cantidad):  # Método para transferir dinero entre usuarios
        if cantidad <= 0:  # Comprobamos que la cantidad sea positiva
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > otro_usuario.saldo:  # Verificamos que el otro usuario tenga saldo suficiente
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        otro_usuario.saldo -= cantidad  # Restamos la cantidad del saldo del otro usuario
        self.saldo += cantidad  # Sumamos la cantidad al saldo del usuario actual

    def agregar_dinero(self, cantidad):  # Método para aumentar el saldo del usuario
        if cantidad <= 0:  # Comprobamos que la cantidad sea positiva
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad  # Añadimos la cantidad al saldo

    def __str__(self):  # Representación legible del usuario
        tipo_cuenta = "con cuenta corriente" if self.cuenta_corriente else "sin cuenta corriente"
        return f"{self.nombre}: {self.saldo} unidades ({tipo_cuenta})"

# Prueba de uso:
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(30)
alicia.transferir_dinero(bob, 80)
alicia.retirar_dinero(50)

print("Kata 36 - Alicia:", alicia)
print("Kata 36 - Bob:", bob)

# KATA 37
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

# 1. Función para contar el número de veces que aparece cada palabra en el texto.
def contar_palabras(texto):  # Recibe el texto como parámetro
    palabras = texto.split()  # Separamos el texto por espacios
    resultado = {}  # Creamos un diccionario vacío
    for palabra in palabras:  # Recorremos cada palabra
        resultado[palabra] = resultado.get(palabra, 0) + 1  # Contamos cuántas veces aparece cada palabra
    return resultado  # Devolvemos el diccionario

# 2. Función para reemplazar una palabra por otra
def reemplazar_palabras(texto, palabra_original, palabra_nueva):  # Recibe el texto y las dos palabras
    return texto.replace(palabra_original, palabra_nueva)  # Reemplaza la palabra original por la nueva

# 3. Función para eliminar una palabra del texto
def eliminar_palabra(texto, palabra):  # Recibe el texto y la palabra a eliminar
    return " ".join([p for p in texto.split() if p != palabra])  # Devuelve el texto sin esa palabra

# 4. Función principal que llama a las anteriores según la opción seleccionada
def procesar_texto(texto, opcion, *args):  # Recibe el texto, la opción y argumentos variables
    if opcion == "contar":
        return contar_palabras(texto)  # Llama a la función contar
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])  # Llama a la función reemplazar
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])  # Llama a la función eliminar
    else:
        return "Opción inválida"  # Si no coincide ninguna opción

# Comprobamos el funcionamiento completo de la función procesar_texto
texto_ejemplo = "hola mundo hola"
print("Kata 37 - contar:", procesar_texto(texto_ejemplo, "contar"))
print("Kata 37 - reemplazar:", procesar_texto(texto_ejemplo, "reemplazar", "mundo", "Python"))
print("Kata 37 - eliminar:", procesar_texto(texto_ejemplo, "eliminar", "hola"))

# KATA 38
# Saber si es de día, tarde o noche según la hora dada por el usuario. Si la hora está entre: 6 a 12 = Es de día / 13 a 20 = Es tarde / 21 a 5 = Es de noche.

hora = int(input("Introduce la hora (0-23): "))  # Solicitamos una hora al usuario

if hora < 0 or hora > 23:  # Validamos que esté en el rango correcto
    print("Kata 38:", "Hora no válida. Debe estar entre 0 y 23.")
else:
    if 6 <= hora <= 12:
        print("Kata 38:", "Es de día")  # Si está entre 6 y 12
    elif 13 <= hora <= 20:
        print("Kata 38:", "Es tarde")  # Entre 13 y 20
    else:
        print("Kata 38:", "Es de noche")  # Entre 21 y 5

# KATA 39
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:c - 0 - 69 = insuficiente / - 70 - 79 = bien / - 80 - 89 = muy bien / - 90 - 100 = excelente

# Pedimos al usuario que introduzca su calificación numérica
nota = int(input("Introduce tu calificación (0-100): "))  # Convertimos a número entero

# Verificamos que la nota esté en el rango válido
if nota < 0 or nota > 100:
    print("Kata 39:", "Nota no válida. Debe estar entre 0 y 100.")  # Mensaje de error si está fuera del rango

# Si la nota está entre 0 y 69 = Insuficiente
elif 0 <= nota <= 69:
    print("Kata 39:", "Tu calificación es: Insuficiente")

# Si la nota está entre 70 y 79 = Bien
elif 70 <= nota <= 79:
    print("Kata 39:", "Tu calificación es: Bien")

# Si la nota está entre 80 y 89 = Muy bien
elif 80 <= nota <= 89:
    print("Kata 39:", "Tu calificación es: Muy bien")

# Si la nota está entre 90 y 100 = Excelente
else:
    print("Kata 39:", "Tu calificación es: Excelente")

# KATA 40
# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectángulo" , "circulo" o "triángulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# Importamos la librería math para usar el número Pi
import math

# Creamos la función que recibe dos parámetros:
# figura = tipo de figura (str)
# datos = tupla con los datos necesarios (base, altura, radio, etc)
def calcular_area(figura, datos):

    # Convertimos figura a minúsculas por si lo escriben en mayúscula
    figura = figura.lower()

    # Si la figura es un rectángulo
    if figura == "rectángulo":
        base, altura = datos  # Desempaquetamos base y altura
        area = base * altura  # Fórmula del área del rectángulo

    # Si la figura es un círculo
    elif figura == "círculo":
        radio, = datos  # Desempaquetamos el radio (la coma indica que es una tupla de 1 solo valor)
        area = math.pi * radio ** 2       # Fórmula del área del círculo

    # Si la figura es un triángulo
    elif figura == "triángulo":
        base, altura = datos                          # Desempaquetamos base y altura
        area = (base * altura) / 2                    # Fórmula del área del triángulo

    # Si la figura no es válida
    else:
        raise ValueError("Figura no válida")          # Lanzamos un error

    return area                                       # Devolvemos el área calculada


# Casos de prueba

# Área de un rectángulo de base 10 y altura 5
print("Kata 40 - área de un rectángulo de base 10 y altura 5:", calcular_area("rectángulo", (10, 5)))

# Área de un círculo de radio 7
print("Kata 40 - área de un círculo de radio 7:", calcular_area("círculo", (7,)))

# Área de un triángulo de base 8 y altura 4
print("Kata 40 - área de un triángulo de base 8 y altura 4:", calcular_area("triángulo", (8, 4)))

# KATA 41
# En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.

# Pedimos al usuario que introduzca el precio original del artículo
precio_original = float(input("Introduce el precio original del artículo (€): "))

# Preguntamos al usuario si tiene cupón de descuento
respuesta = input("¿Tienes un cupón de descuento? (sí o no): ")

# Si la respuesta es "sí"
if respuesta.lower() == "sí":
    
    # Pedimos el valor del cupón de descuento
    descuento = float(input("Introduce el valor del cupón de descuento (€): "))

    # Verificamos si el descuento es válido (mayor a 0)
    if descuento > 0:
        precio_final = precio_original - descuento  # Restamos el descuento al precio original
        
        # Si el precio final es menor que 0, lo dejamos en 0 (no puede haber precios negativos)
        if precio_final < 0:
            precio_final = 0
    else:
        # Si el descuento no es válido (menor o igual a 0), no se aplica
        print("Kata 41:", "Cupón de descuento no válido.")
        precio_final = precio_original

# Si la respuesta es "no"
elif respuesta.lower() == "no":
    precio_final = precio_original  # No se aplica descuento

# Si la respuesta no es válida (ni sí ni no)
else:
    print("Kata 41:", "Respuesta no válida. No se aplica descuento.")
    precio_final = precio_original

# Mostramos el precio final
print("Kata 41:", f"El precio final de tu compra es: {precio_final} €")