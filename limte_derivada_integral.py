from sympy import symbols, sqrt, log, diff, integrate, limit, oo, lambdify
import matplotlib.pyplot as plt
import numpy as np
import re

def direcao_limite():
    direcao = input("Para qual valor x deve tender? (infinito, -infinito ou outro valor numérico): ").strip().lower()
    if direcao == "infinito":
        return oo
    elif direcao == "-infinito":
        return -oo
    else:
        try:
            return float(direcao)
        except ValueError:
            print("Valor inválido. Usando infinito como padrão.")
            return oo


def passa_pra_math(string_funcao):
    # Para exponenciação
    string_funcao = string_funcao.replace('^', '**')

    # Para raízes
    string_funcao = string_funcao.replace('\\sqrt{', 'sqrt(')
    string_funcao = re.sub(r'\\sqrt\[(\d+)\]\{', lambda m: '(' + m.group(1) + ')**(1/', string_funcao)

    # Para logaritmos
    string_funcao = string_funcao.replace('ln(', 'log(')
    # string_funcao = string_funcao.replace('log(', 'log10(')  

    return string_funcao

x = symbols('x')

while True:
    string_funcao = input("Digite a função f(x): ")
    string_funcao = passa_pra_math(string_funcao)
    func = eval(string_funcao)

    # Limite
    direcao = direcao_limite()
    try:
        lim = limit(func, x, direcao)
        print(f"Limite quando x tende a {direcao}:", lim)
    except Exception as e:
        print("Não foi possível calcular o limite.")

    # Derivada
    try:
        derivada = diff(func, x)
        print("Derivada:", derivada)
    except Exception as e:
        print("Não foi possível calcular a derivada.")

    # Integral
    try:
        integral = integrate(func, x)
        print("Integral:", integral)
    except Exception as e:
        print("Não foi possível calcular a integral.")


    # Gráfico
    f_lambdified = lambdify(x, func, "numpy")
    df_lambdified = lambdify(x, derivada, "numpy")
    F_lambdified = lambdify(x, integral, "numpy")

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)
    dy_vals = df_lambdified(x_vals)
    Y_vals = F_lambdified(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.plot(x_vals, dy_vals, label="f'(x)")
    plt.plot(x_vals, Y_vals, label='∫f(x)dx')
    plt.legend()
    plt.show()

    cont = input("Deseja calcular outra função? (s/n) ")
    if cont.lower() != 's':
        break
