def seleccionar_opcion(tipo):
    print(f"\nSelecciona el tipo de {tipo} (1-4):")
    print("1. Decimal\n2. Binario\n3. Octal\n4. Hexadecimal")
    while True:
        try:
            opcion = int(input("Opción (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, selecciona una opción válida (1-4).")
        except ValueError:
            print("Entrada inválida. Ingresa un número entre 1 y 4.")

def convertir_a_decimal(valor, base):
    try:
        return int(valor, base)
    except ValueError:
        print(f"El valor ingresado no es válido para la base {base}.")
        quit()

def convertir_desde_decimal(valor, base):
    if base == 2:
        return bin(valor)[2:]
    elif base == 8:
        return oct(valor)[2:]
    elif base == 16:
        return hex(valor)[2:]
    else:
        return str(valor)

def main():
    print("---------Script de conversión de números---------")
    op_entrada = seleccionar_opcion("entrada")
    op_salida = seleccionar_opcion("salida")
    
    bases = {1: 10, 2: 2, 3: 8, 4: 16}
    nombres = {1: "Decimal", 2: "Binario", 3: "Octal", 4: "Hexadecimal"}
    
    valor_dato = input("\nIngresa el valor a convertir: ")
    print("-" * 50)
    
    # Convertir a decimal
    decimal = convertir_a_decimal(valor_dato, bases[op_entrada])
    
    # Mostrar resultados
    print(f"{nombres[op_entrada]}: {valor_dato}")
    resultado = convertir_desde_decimal(decimal, bases[op_salida])
    print(f"{nombres[op_salida]}: {resultado}")
    print("-" * 50)
    print(f"{'-' * 18} Fin del script {'-' * 18}")

if __name__ == "__main__":
    main()
