
def __make_text__(text, lista_intervalo):
    lista_textos = []
    for item in lista_intervalo:
        lista_textos.append([item[0], text[item[1][0]:item[1][1]]])
    
    return lista_textos