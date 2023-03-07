#SOLUCION HOMEWORK

#1.-Crear una variable que contenga un elemento del conjunto de números enteros
####y luego imprimir por pantalla
unEntero = 5
print(unEntero)

#2.-Imprimir el tipo de dato de la constante 8.5
decimal = 8.5
print(type(8.5))

#3.-Imprimir el tipo de dato de la variable creada en el punto 1
print(type(unEntero))

#4.-Crear una variable que contenga tu nombre
miNombre = "JAC"

#5.-Crear una variable que contenga un número complejo
unComplex = 1j

#6.-Mostrar el tipo de dato de la variable crada en el punto 5
print(type(unComplex))

#7.-Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
valorPI = 3.1416

#8.-Crear una variable que contenga el valor 'True' y otra que contenga el valor True.
####¿Se trata de lo mismo?
unaVar = 'True'
otraVar = True
print(type(unaVar))
print(type(otraVar))

#9.-Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type('True'))
print(type(True))

#10.-Asignar a una variable, la suma de un número entero y otro decimal
sumaInt_Dec = 10 + 11.5

#11.-Realizar una operación de suma de números complejos
sumaComplex = 2j + 4j

#12.-Realizar una operación de suma de un número real y otro complejo
sumaComp_Real = 5 + 4j

#13.-Realizar una operación de multiplicación
multi = 8*3

#14.-Mostrar el resultado de elevar 2 a la octava potencia
octava = 2**8
print(octava)

#15.-Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
divCociente = 27/4
print(divCociente)

#16.-De la división anterior solamente mostrar la parte entera
print(int(divCociente))
divEntero = 27//4
print(divEntero)

#17.-De la división de 27 entre 4 mostrar solamente el resto
divResto = 27%4
print(divResto)

#18.-Utilizando como operandos el número 4 y los resultados 
#####obtenidos en los puntos 16 y 17. Obtener 27 como resultado  
opera = (divEntero*4)+divResto
print(opera)

#19.-Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
alfan1 = "JACes1"
alfan2 = "CAP0"
operaMas = alfan1+alfan2
print(operaMas)

#20.-Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
igual1 = "2"
igual2 = 2
print(igual1==igual2)
print(type(igual1))
print(type(igual2))

#21.-Utilizar las funciones de cambio de tipo de dato,
#####para que la validación del punto 20 resulte verdadera
print(igual1==str(igual2))
igual2 = str(igual2)
print(igual1==igual2)

#22.-¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = tuple('3,8')
print(a)
a = float('3.8')
print(a)

#23.-Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
varValor = 3
varValor -= 2
print(varValor)

#24.-Realizar la operacion 1 << 2 ¿Por qué da ese resultado?
#####¿Qué es el sistema de numeración binario?

1 << 2

#25.-Realizar la operación 2 + '2' ¿Por qué no está permitido?
#####¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

print(2+int('2'))

#26.-Realizar una operación válida entre valores de tipo entero y string

valorEnt = 3
valorStr = 'este texto se repite '
print((valorStr*valorEnt)+"x "+str(valorEnt)+" veces...")