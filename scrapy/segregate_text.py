
def __search__(texto, lista_analise):
    """
    Função de inicialização do processo.
    Precisará do texto que será analisado e da lista
    de elementos.

    Os indices representam o número do caracter do texto no qual o elemento começa mais
    o seu tamanho. 

    Args:
        texto(str) = texto que será analisado;

        lista_analise(list[str]) = lista com os elementos que serão
        buscados no texto;
    Return:
        resultado(list) = Retornará uma lista ( '['elemento', [indice1, indice2, indice3, ..., indiceN]]' )
    """
    return organizar_resultado(encontrar_elemento(texto, lista_analise))

def organizar_resultado(resultados):
    """_summary_

    Args:
        resultados (_type_): _description_

    Returns:
        _type_: _description_
    """
    resultado_final = []
    for resultado in resultados:
        resultado_temp = []
        indices = []
        for element in resultado:
            if type(element) == str and element not in resultado_temp:
                resultado_temp.append(element)
            if type(element) == int:
                indice_real = len(resultado_temp[0]) + element
                indices.append(indice_real)
        resultado_temp.append(indices)
        resultado_final.append(resultado_temp)
    
    return resultado_final

def encontrar_elemento(texto, lista_analise):
    result = []

    for element in lista_analise:
        match = [] # 1- Match será ['elemento'(element_list), indice(int)-> de onde começa o elemento no texto ]
        start = 0
        while True:
            start = texto.find(element, start)
            if start == -1:
                break
            match.append(element)
            match.append(start)
            start += len(element)

        result.append(match)
    
    return result
