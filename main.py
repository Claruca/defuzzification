import sympy as sp

x = sp.Symbol('x')

lista = [
    (30, 36, 0.1 * x - 3),
    (36, 54, 0.6),
    (54, 56, -0.1 * x + 6),
    (56, 76, 0.4),
    (76, 76.25, -0.1 * x + 8),
    (76.25, 90, 0.375)
]


def centreOfMasa(datos):
    sum_numerador = 0
    sum_denominador = 0

    def integralDefinidaNumerador(intervA, intervB, variableFunc):
        return sp.integrate(variableFuncion * x, (x, intervaloA, intervaloB))

    def integralDefinidaDenominador(intervA, intervB, variableFunc):
        return sp.integrate(variableFuncion, (x, intervaloA, intervaloB))

    for dato in datos:
        intervaloA = dato[0]
        intervaloB = dato[1]
        variableFuncion = dato[2]
        resultNum = integralDefinidaNumerador(intervaloA, intervaloB, variableFuncion)
        resultDenom = integralDefinidaDenominador(intervaloA, intervaloB, variableFuncion)
        # print(resultNum)
        # print(resultDenom)
        sum_numerador += resultNum
        sum_denominador += resultDenom

    # print(sum_numerador)
    # print(sum_denominador)
    return round(sum_numerador / sum_denominador, 2)


print(centreOfMasa(lista))