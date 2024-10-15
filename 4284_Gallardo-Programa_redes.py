print("---------Script de conversión de números---------")
print("""
Selecciona el tipo de entrada (1-4):
1. Decimal
2. Binario
3. Octal
4. Hexadecimal
""")
op_entrada=int(input("Opción (1-4): "))
if op_entrada<1:
    print("Escoge una opción válida")
    quit()
elif op_entrada>4:
    print("Escoge una opción válida")
    quit()
else:
    op_entrada=op_entrada
print("-"*50)
print("""
Selecciona el tipo de salida (1-4):
1. Decimal
2. Binario
3. Octal
4. Hexadecimal
""")
op_salida = int(input("Opción (1-4): "))
if op_salida<1:
    print("Escoge una opción válida")
    quit()
elif op_salida>4:
    print("Escoge una opción válida")
    quit()
else:
    op_salida=op_salida
print("-"*50)
valor_dato = input("Ingresa el valor a convertir: ")
print("-"*50)
# Convertir el valor de entrada a decimal
if op_entrada == 1:
    decimal = int(valor_dato)  # Decimal
elif op_entrada == 2:
    decimal = int(valor_dato, 2)  # Binario
elif op_entrada == 3:
    decimal = int(valor_dato, 8)  # Octal
elif op_entrada == 4:
    decimal = int(valor_dato, 16)  # Hexadecimal
else:
    print("Escoja una opción válida")
    exit()
# Mostrar el valor de entrada
if op_entrada == 1:
    print(f"Decimal: {valor_dato}")
elif op_entrada == 2:
    print(f"Binario: {valor_dato}")
elif op_entrada == 3:
    print(f"Octal: {valor_dato}")
elif op_entrada == 4:
    print(f"Hexadecimal: {valor_dato}")
else:
    print("Escoja una opción váilda")
# Convertir de decimal a la base de salida
if op_salida == 1:
    print(f"Decimal: {decimal}")
elif op_salida == 2:
    print(f"Binario: {bin(decimal)[2:]}")
elif op_salida == 3:
    print(f"Octal: {oct(decimal)[2:]}")
elif op_salida == 4:
    print(f"Hexadecimal: {hex(decimal)[2:]}")
else:
    print("Escoja una opción válida")
print("-"*50)
print(f"{"-"*18}Fin del script{"-"*18}")