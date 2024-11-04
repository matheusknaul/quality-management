"""
Matheus Calvet - 01/10/2024

Módulo que será responsável por capturar partes do texto onde definimos
o intervalo a partir do elemento (classe, área de ensaio ou produto), com
seus respectivos indices encontrados no módulo segregate_text
"""

def organizar_indices(lista_resultado):
    nova_lista = []
    for item in lista_resultado:
        chave = item[0]
        valores = item[1]
        
        for valor in valores:
            nova_lista.append([chave, [valor]])

    nova_lista.sort(key=lambda x: x[1][0])

    return nova_lista
