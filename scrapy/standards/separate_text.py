import re
from padroes import list_of_patterns, list_of_yearpatterns, list_of_partpatterns, list_of_numberpatterns

def __separate__(text):
    lista_resultados = search_patterns(text)
    lista_interval = set_interval(lista_resultados, text)
    return format_standard(lista_interval)

def search_patterns(text):
    lista_de_matchs = []

    # Ordenar os padrões pela complexidade (padrões maiores primeiro)
    list_of_patterns_sorted = sorted(list_of_patterns, key=lambda p: -len(p))

    for pattern in list_of_patterns_sorted:
        resultados = re.finditer(pattern, text)
        for match in resultados:
            title, start, end = match.group(), match.start(), match.end()
            
            sobreposto = False

            # Verifica se a nova norma detectada está sobrepondo uma já existente
            for item in lista_de_matchs:
                start_anterior = item[1][0]
                end_anterior = item[1][1]

                # Verificar se há sobreposição com o intervalo de um item já detectado
                if start >= start_anterior and end <= end_anterior:
                    sobreposto = True
                    break

            # Se não houver sobreposição, adicionamos a nova norma
            if not sobreposto:
                lista_de_matchs.append([title, [start, end]])

    return lista_de_matchs

def set_interval(list_results, text):
    lista_ordenada = sort_list(list_results)
    result = []

    for i, norma_atual in enumerate(lista_ordenada):
        start_norma_atual = norma_atual[1][0]
        nome_norma_atual = norma_atual[0]

        # Determina o intervalo do texto anterior à norma atual
        if i == 0:
            # Se for a primeira norma, pegue o texto desde o início
            bloco_anterior = text[:start_norma_atual].strip()
        else:
            # Não lembro mais o que essa porra faz
            end_norma_anterior = lista_ordenada[i-1][1][1]
            bloco_anterior = text[end_norma_anterior:start_norma_atual].strip()

        # Adiciona o bloco de texto e a norma à lista de resultados
        result.append([bloco_anterior, nome_norma_atual])

    return result
    
def format_standard(list_results):
    lista_result = []
    for result in list_results:
        from standard_features import build_standard
        # new_result.append(result[0])
        lista_result.append(build_standard(result[1]))

    return lista_result

def sort_list(list_results):
    lista_ordenada = sorted(list_results, key=lambda x: x[1][0])
    return lista_ordenada
