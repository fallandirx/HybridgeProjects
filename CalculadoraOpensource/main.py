from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Bienvenido/a a la calculadora open source de Hybridge")
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")
    
def main():
    while True:
        mostrar_menu()
        
        chosenOption = input("¿Cuál es tu opción?:  ")
        
        if (chosenOption == "1"):
            print("Has elegido la suma")
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print("El resultado es: ", sumar(num1, num2))
            except ValueError:
                print("Por favor, ingresa números válidos.")
        elif (chosenOption == "2"):
            print("Has elegido la resta")
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print("El resultado es: ", restar(num1, num2))
            except ValueError:
                print("Por favor, ingresa números válidos.")
        elif (chosenOption == "3"):
            print("Has elegido la multiplicación")
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print("El resultado es: ", multiplicar(num1, num2))
            except ValueError:
                print("Por favor, ingresa números válidos.")
        elif (chosenOption == "4"):
            print("Has elegido la división")
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if (num1 == 0 or num2 == 0):
                    print("No se puede dividir por 0")
                else:
                    print("El resultado es: ", dividir(num1, num2))
            except ValueError:
                print("Por favor, ingresa números válidos.")
        elif (chosenOption == "5"):
            print("Has elegido la suma avanzada")
            lista_de_numeros = []
            secuencia = 0
            
            while True:
                respuesta = input("Ingresa un número para sumar, "
                          "o escribe 'q' para terminar la suma: ")
                
                if respuesta.lower() == "q":
                    break
                    
                try:
                    respuesta_filtrada = float(respuesta)
                    secuencia += 1
                    print(f"Tu numero #{secuencia} es: {respuesta_filtrada}")
                    lista_de_numeros.append(respuesta_filtrada)
                except ValueError:
                    print("Por favor, ingresa números válidos.")
            
            print("El resultado es: ", suma_avanzada(lista_de_numeros))                
        elif (chosenOption == "6"):
            print("Gracias, adios!")
            break
        else:
            print("Por favor, ingresa una opción correcta.")

if __name__ == "__main__":
    main()