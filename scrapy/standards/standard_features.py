import re
from padroes import list_of_patterns, list_of_yearpatterns, list_of_partpatterns, list_of_numberpatterns

"""
Este arquivo monta e separa as características fundamentais de pesquisas da norma encontrada.

Ele retorna algo parecido como: [['ABNT', 'NBR ISO'], 17025, ['1', '2'], 2017] (exemplo fictício)
                    Indices:
                            1: Tag principal e tags complementares (as tags complementares precisam estar junto para montar corretamente a norma);
                            2: Número da norma (identificação numérica);
                            3: Partes da norma (se não houver, será uma lista vazia -> if parts)
                                -> Como possui mais de uma parte, a lógica do arquivo que montará a planilha, deverá repetir a norma
                            para cada partes. Ex: ABNT NBR 17025-1:2017 - ABNT NBR 17025-2:2017;
                            4: Ano da norma;

"""

def build_standard(standard):
    main_tag, complementar_tag = detect_tag(standard)
    number = detect_number(standard)
    part = detect_part(standard)
    year = detect_year(standard)

    standard_features = ([main_tag, complementar_tag], number, part, year)
    standard_formated = format_standard(standard_features)

    # print('This is standard formated:')
    # print(standard_formated)
    return standard_formated

def format_standard(features):
    result = []
    main = features[0][0]
    if features[0][1] != " ":
        complementar = features[0][1]
    else:
        complementar = ""
    number = features[1]
    year = features[3]
    if features[2]:
        for part in features[2]:
            standard = main + " " + complementar + " " + number + "-" + part + ":" + year
            new_standard = standard.replace("  ", " ")
            result.append((main, number, year, part))
            result.append(new_standard)
    else:
        standard = main + " " + complementar + " " + number + ":" + year
        new_standard = standard.replace("  ", " ")
        result.append((main, number, year, "null"))
        result.append(new_standard)
    return result
    
def detect_tag(standard):
    possibles_tag = ['ABNT', 'ISO', 'ASTM', 'IEC', 'NBR']
    for tag in possibles_tag:
        if tag in standard:
            main_tag = tag
            complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
            complementar_tag = complementar.group().replace(tag, "")
            return main_tag, complementar_tag
    return 'disregard', 'disregard'
    # if "ABNT" in standard:
    #     main_tag = "ABNT"
    #     complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
    #     complementar_tag = complementar.group().replace("ABNT", "")
    #     return main_tag, complementar_tag

    # if "ISO" in standard:
    #     main_tag = "ISO"
    #     complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
    #     complementar_tag = complementar.group().replace("ISO", "")
    #     return main_tag, complementar_tag
    
    # if "ASTM" in standard:
    #     main_tag = "ASTM"
    #     complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
    #     complementar_tag = complementar.group().replace("ASTM", "")
    #     return main_tag, complementar_tag
    
    if "IEC" in standard:
        main_tag = "IEC"
        complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
        complementar_tag = complementar.group().replace("IEC", "")
        return main_tag, complementar_tag

def detect_number(standard):
    
    for pattern in list_of_numberpatterns:
        match = re.search(pattern, standard)
        if match:
            result = re.search(r"[A-Z]{1}\d{2,5}|\d{2,5}", match.group())
            if result: 
                return result.group()

def detect_part(standard):
    parts = []
    for pattern in list_of_partpatterns:
        match = re.search(pattern, standard)
        if match:
            number_part = re.finditer(r"\d{1}", match.group())
            if number_part:
                for number in number_part:
                    parts.append(number.group())
    return parts

def detect_year(standard):
    year_concatened = ""
    for pattern in list_of_yearpatterns:
        match = re.search(pattern, standard)
        if match:
            year_match = re.finditer(r"\d", match.group())
            if year_match:
                for year in year_match:
                    year_concatened = year_concatened + year.group()
    return year_concatened



