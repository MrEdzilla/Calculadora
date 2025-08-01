import os
import time
import math

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError("Não é possível dividir por zero!")
    elif operador == '^':
        result = num1 ** num2       
    return result

if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            numero1: float = float(input('Introduza o primeiro número: '))
            operacao: str = input('Introduza a operação a realizar (+ - / * ^): ').strip()
            numero2: float = float(input('Introduza o segundo número: '))

            print(f'O resultado: {calculadora(numero1, numero2, operacao)}')
            print()
            cont: str = input('Deseja continuar? (s/n): ').lower()
            if cont == 'n':
                break

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
