""" 
Esse arquivo retorna um array, que representerá os elementos da linha

flag seria o produto e o text com o intervalo, é o intervalo do começo desse produto até o próximo
"""


def __build__(lista_resultado):
    lista_resultado_new = []
    
    for i in range(len(lista_resultado)):
        if i == len(lista_resultado) - 1:
            resultado = [lista_resultado[i][0], [lista_resultado[i][1][0], -1]]
            lista_resultado_new.append(resultado)
        else:
            resultado = [lista_resultado[i][0], [lista_resultado[i][1][0], lista_resultado[i+1][1][0]]]
            lista_resultado_new.append(resultado)
    
    return lista_resultado_new

def criar_texto(flag, comeco_intervalo, fim_intervalo, text):
    return [flag, text[comeco_intervalo:fim_intervalo]]