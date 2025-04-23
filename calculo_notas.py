def media(unidade1=0, unidade2=0):
    if unidade2 == 0:
        mediaA = unidade1/1
        if mediaA <= 4.9:
            resultado = "I"
            return resultado
        elif mediaA > 4.9 and mediaA <=6.9:
            resultado = "R"
            return resultado
        elif mediaA > 6.9 and mediaA <=8.9:
            resultado = "B"
            return resultado
        elif mediaA > 8.9 and mediaA <=10:
            resultado = "E"
            return resultado
        print(resultado)
    elif unidade2 != 0:
        mediaA = (unidade1 + unidade2)/2
        if mediaA <= 4.9:
            resultado = "I"
            return resultado
        elif mediaA > 4.9 and mediaA <=6.9:
            resultado = "R"
            return resultado
        elif mediaA > 6.9 and mediaA <=8.9:
            resultado = "B"
            return resultado
        elif mediaA > 8.9 and mediaA <=10:
            resultado = "E"
            return resultado
    return resultado


