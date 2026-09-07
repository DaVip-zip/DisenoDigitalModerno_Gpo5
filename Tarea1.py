"""
FACULTAD DE INGENIERÍA - UNAM
Diseño Digital Moderno (Semestre 2027-1)
Tarea 1: Sistemas Numéricos, Conversiones y Aritmética
Profesor: Dr. Oscar Fuentes

Estudiante: Hebber Omar Dominguez Hernandez
            Trujillo Morales Mario Alberto
            Juarez Castillo Romario Uriel
            Carbajal Lopez Jose David
Fecha: Septiembre 2026
"""

# Digitos que vamos a usar
DIGITOS = "0123456789ABCDEF"


# ==========================================================
# CONVERSION DE BASES
# ==========================================================

def valor(c):
    c = c.upper()
    return DIGITOS.index(c)


def caracter(n):
    return DIGITOS[n]


# Revisa si el numero sirve
def validar(numero, base):

    numero = numero.strip().upper()

    if numero == "":
        return False

    # Caso especial para base 1
    if base == 1:
        for c in numero:
            if c != "1":
                return False
        return True

    puntos = 0

    for c in numero:

        if c == ".":
            puntos += 1

            if puntos > 1:
                return False

        else:

            if c not in DIGITOS:
                return False

            if valor(c) >= base:
                return False

    if numero == ".":
        return False

    return True


# Pasa una base a decimal
def a_decimal(numero, base):

    numero = numero.strip().upper()

    # Base 1
    if base == 1:
        return len(numero)

    if "." in numero:
        partes = numero.split(".")
        entero = partes[0]
        decimal = partes[1]
    else:
        entero = numero
        decimal = ""

    resultado = 0

    # Parte entera
    for c in entero:
        resultado = resultado * base + valor(c)

    # Parte decimal
    if decimal != "":
        posicion = 1

        for c in decimal:
            resultado += valor(c) / (base ** posicion)
            posicion += 1

    return resultado


# Pasa decimal a otra base
def de_decimal(numero, base):

    if base == 1:

        if numero == 0:
            return "0"

        return "1" * int(numero)

    # Parte entera
    entero = int(numero)

    if entero == 0:
        resultado_entero = "0"
    else:

        resultado_entero = ""
        n = entero

        while n > 0:

            residuo = n % base
            resultado_entero = DIGITOS[residuo] + resultado_entero
            n = n // base

    # Parte decimal
    decimal = numero - entero

    if decimal == 0:
        return resultado_entero

    resultado_decimal = ""
    contador = 0

    while decimal > 0 and contador < 6:

        decimal = decimal * base
        digito = int(decimal)

        resultado_decimal += DIGITOS[digito]

        decimal = decimal - digito
        contador += 1

    return resultado_entero + "." + resultado_decimal


# Cambia de una base a otra
def convertir(numero, base1, base2):

    decimal = a_decimal(numero, base1)
    resultado = de_decimal(decimal, base2)

    return resultado


# ==========================================================
# BINARIO DE 6 BITS
# ==========================================================

# Suma un bit
def sumar_bit(a, b, acarreo):

    total = a + b + acarreo

    if total == 0:
        return 0, 0

    if total == 1:
        return 1, 0

    if total == 2:
        return 0, 1

    return 1, 1


# Suma dos numeros de 6 bits
def suma_binaria(a, b):

    resultado = ""
    acarreo = 0

    for i in range(5, -1, -1):

        bit_a = int(a[i])
        bit_b = int(b[i])

        bit, acarreo = sumar_bit(
            bit_a,
            bit_b,
            acarreo
        )

        resultado = str(bit) + resultado

    return resultado


# Complemento a dos
def complemento_dos(bits):

    # Primero se cambian los bits
    invertido = ""

    for bit in bits:

        if bit == "0":
            invertido += "1"
        else:
            invertido += "0"

    # Despues se suma 1
    resultado = list(invertido)
    acarreo = 1

    for i in range(5, -1, -1):

        if acarreo == 0:
            break

        if resultado[i] == "0":
            resultado[i] = "1"
            acarreo = 0
        else:
            resultado[i] = "0"

    return "".join(resultado)


# Segundo metodo
def complemento_segundo(bits):

    bits = list(bits)

    # Busca el primer 1
    posicion = -1

    for i in range(5, -1, -1):

        if bits[i] == "1":
            posicion = i
            break

    if posicion == -1:
        return "".join(bits)

    # Cambia lo que esta a la izquierda
    for i in range(posicion - 1, -1, -1):

        if bits[i] == "0":
            bits[i] = "1"
        else:
            bits[i] = "0"

    return "".join(bits)


# Convierte decimal a 6 bits
def decimal_a_binario(numero):

    if numero < -32 or numero > 31:
        return None

    if numero >= 0:
        return format(numero, "06b")

    numero = 64 + numero

    return format(numero, "06b")


# Convierte 6 bits a decimal
def binario_a_decimal(bits):

    if bits[0] == "0":
        return int(bits, 2)

    complemento = complemento_dos(bits)

    return -int(complemento, 2)


# ==========================================================
# OPERACIONES BINARIAS
# ==========================================================

def resta_binaria(a, b, metodo):

    if metodo == 1:

        complemento = complemento_dos(b)

        print("\nComplemento a dos:")
        print("Numero:      ", b)

        invertido = ""

        for bit in b:

            if bit == "0":
                invertido += "1"
            else:
                invertido += "0"

        print("Invertido:  ", invertido)
        print("+ 1:         ", complemento)

    else:

        complemento = complemento_segundo(b)

        print("\nSegundo metodo:")
        print("Numero:      ", b)
        print("Resultado:  ", complemento)

    resultado = suma_binaria(a, complemento)

    return resultado


# ==========================================================
# OPERACIONES EN OTRAS BASES
# ==========================================================

def operacion_base(num1, num2, base, operador):

    valor1 = a_decimal(num1, base)
    valor2 = a_decimal(num2, base)

    if operador == "+":

        resultado = valor1 + valor2

    else:

        resultado = valor1 - valor2

    if resultado < 0:

        resultado = abs(resultado)

        return "-" + de_decimal(resultado, base)

    return de_decimal(resultado, base)


# ==========================================================
# PROBLEMA 1
# ==========================================================

def problema_conversion():

    errores = 0

    print("\n==============================================")
    print("        PROBLEMA 1: CONVERSION DE BASES")
    print("==============================================")

    # Base inicial
    while True:

        try:

            base1 = int(
                input("\nIngrese la base de origen (1 a 16): ")
            )

            if base1 < 1 or base1 > 16:

                errores += 1
                print("Error: la base debe estar entre 1 y 16.")

                if errores >= 3:
                    print("bro...")
                    errores = 0

                continue

            break

        except ValueError:

            errores += 1
            print("Error: escribe un numero.")

            if errores >= 3:
                print("bro...")
                errores = 0

    # Numero
    while True:

        numero = input(
            f"Ingrese el numero en base {base1}: "
        ).strip().upper()

        if not validar(numero, base1):

            errores += 1

            print(
                "Error: el numero no corresponde a esa base."
            )

            if errores >= 3:
                print("bro...")
                errores = 0

            continue

        break

    # Base final
    while True:

        try:

            base2 = int(
                input("Ingrese la base de destino (1 a 16): ")
            )

            if base2 < 1 or base2 > 16:

                errores += 1
                print("Error: la base debe estar entre 1 y 16.")

                if errores >= 3:
                    print("bro...")
                    errores = 0

                continue

            break

        except ValueError:

            errores += 1
            print("Error: escribe un numero.")

            if errores >= 3:
                print("bro...")
                errores = 0

    decimal = a_decimal(numero, base1)
    resultado = convertir(numero, base1, base2)

    print("\n--------------- RESULTADO ---------------")

    print(
        f"({numero}) base {base1} = "
        f"({decimal}) base 10"
    )

    print(
        f"({numero}) base {base1} = "
        f"({resultado}) base {base2}"
    )


# ==========================================================
# PROBLEMA 2
# ==========================================================

def problema_binario():

    errores = 0

    print("\n==============================================")
    print("        PROBLEMA 2: SUMADOR DE 6 BITS")
    print("==============================================")

    print("\nSe usan 6 bits:")
    print("1 bit de signo + 5 bits de datos")

    while True:

        try:

            num1 = int(
                input("\nPrimer numero decimal (-32 a 31): ")
            )

            num2 = int(
                input("Segundo numero decimal (-32 a 31): ")
            )

            if num1 < -32 or num1 > 31:
                print("Error: el primer numero esta fuera del rango.")
                continue

            if num2 < -32 or num2 > 31:
                print("Error: el segundo numero esta fuera del rango.")
                continue

            break

        except ValueError:

            errores += 1
            print("Error: escribe numeros enteros.")

            if errores >= 3:
                print("bro...")
                errores = 0

    bin1 = decimal_a_binario(num1)
    bin2 = decimal_a_binario(num2)

    print("\n----------------------------------------------")
    print("REPRESENTACION")
    print("----------------------------------------------")

    print(f"{num1} = {bin1}")
    print(f"{num2} = {bin2}")

    print("\n1. Sumar")
    print("2. Restar")

    while True:

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":

            resultado = suma_binaria(bin1, bin2)

            print("\n----------------------------------------------")
            print("SUMA")
            print("----------------------------------------------")

            print("  ", bin1)
            print("+ ", bin2)
            print("--------")
            print("  ", resultado)

            # Validacion de overflow usando la regla del bit de signo
            signo_a = bin1[0]
            signo_b = bin2[0]
            signo_r = resultado[0]

            overflow = (signo_a == signo_b) and (signo_a != signo_r)

            if overflow:

                print("\nError: overflow.")
                print("El resultado no cabe en 6 bits.")

            else:

                decimal = binario_a_decimal(resultado)
                print("\nResultado:", decimal)

            break

        elif opcion == "2":

            print("\nMetodo de resta:")
            print("1. Complemento a dos")
            print("2. Segundo metodo")

            while True:

                try:
                    metodo = int(
                        input("Selecciona el metodo: ")
                    )

                    if metodo == 1 or metodo == 2:
                        break

                    print("Error: selecciona 1 o 2.")

                except ValueError:

                    print("Error: escribe 1 o 2.")

            print("\n----------------------------------------------")
            print("RESTA")
            print("----------------------------------------------")

            print("  ", bin1)
            print("- ", bin2)

            complemento = ""

            if metodo == 1:

                complemento = complemento_dos(bin2)

                print("\nComplemento:")
                print(bin2)
                print(complemento)

            else:

                complemento = complemento_segundo(bin2)

                print("\nComplemento:")
                print(bin2)
                print(complemento)

            resultado = suma_binaria(
                bin1,
                complemento
            )

            print("\nSuma:")
            print("  ", bin1)
            print("+ ", complemento)
            print("--------")
            print("  ", resultado)

            # Validacion de overflow usando la regla del bit de signo
            signo_a = bin1[0]
            signo_b = complemento[0]
            signo_r = resultado[0]

            overflow = (signo_a == signo_b) and (signo_a != signo_r)

            if overflow:

                print("\nError: overflow.")
                print("El resultado no cabe en 6 bits.")

            else:

                decimal = binario_a_decimal(resultado)
                print("\nResultado:", decimal)

            # Procedimiento inverso
            if resultado[0] == "1":

                print("\nProcedimiento inverso:")

                if metodo == 1:

                    recuperado = complemento_dos(
                        resultado
                    )

                else:

                    recuperado = complemento_segundo(
                        resultado
                    )

                print("Resultado:   ", resultado)
                print("Complemento: ", recuperado)
                print("Valor:        -", int(recuperado, 2))

            break

        else:

            print("Error: selecciona 1 o 2.")


# ==========================================================
# OPERACIONES EN LA BASE ELEGIDA
# ==========================================================

def operaciones_generales():

    errores = 0

    print("\n==============================================")
    print("           OPERACIONES ENTRE BASES")
    print("==============================================")

    while True:

        try:

            base = int(
                input("\n¿En que base quieres operar? (1 a 16): ")
            )

            if base < 1 or base > 16:

                errores += 1
                print("Error: base fuera de rango.")

                if errores >= 3:
                    print("bro...")
                    errores = 0

                continue

            break

        except ValueError:

            errores += 1
            print("Error: escribe una base valida.")

            if errores >= 3:
                print("bro...")
                errores = 0

    if base == 2:

        # Usa el modo especial de 6 bits
        problema_binario()
        return

    while True:

        num1 = input(
            f"\nPrimer numero en base {base}: "
        ).upper()

        if not validar(num1, base):

            errores += 1
            print("Error: numero no valido.")

            if errores >= 3:
                print("bro...")
                errores = 0

            continue

        break

    while True:

        num2 = input(
            f"Segundo numero en base {base}: "
        ).upper()

        if not validar(num2, base):

            errores += 1
            print("Error: numero no valido.")

            if errores >= 3:
                print("bro...")
                errores = 0

            continue

        break

    print("\n1. Sumar")
    print("2. Restar")

    opcion = input("Selecciona: ")

    if opcion == "1":

        resultado = operacion_base(
            num1,
            num2,
            base,
            "+"
        )

        print(
            f"\n{num1} + {num2} = {resultado}"
        )

    elif opcion == "2":

        resultado = operacion_base(
            num1,
            num2,
            base,
            "-"
        )

        print(
            f"\n{num1} - {num2} = {resultado}"
        )

    else:

        print("Error: opcion no valida.")


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("   FACULTAD DE INGENIERÍA - UNAM")
        print("   DISEÑO DIGITAL MODERNO")
        print("=" * 60)
        print("Tarea 1: Sistemas Numéricos, Conversiones y Aritmética")
        print()
        print("1. Conversion de bases")
        print("2. Operaciones binarias de 6 bits")
        print("3. Operaciones en otras bases")
        print("4. Salir")

        opcion = input(
            "\nSelecciona una opcion: "
        )

        if opcion == "1":

            problema_conversion()

        elif opcion == "2":

            problema_binario()

        elif opcion == "3":

            operaciones_generales()

        elif opcion == "4":

            print("\nPrograma terminado.")
            break

        else:

            print("\nError: selecciona una opcion del 1 al 4.")


# Empieza el programa
if __name__ == "__main__":
    main()