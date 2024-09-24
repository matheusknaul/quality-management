from bs4 import BeautifulSoup


#por padrão, todas as tags recebem False = Não precisa ser "deschecada", caso True, significa que a tag precisa ser "deschecada"


def read_txt(path_file):
    with open(path_file, "r", encoding="utf-8") as file:
        return file.read()

def detect_tag(text):
    if 'cphPagina_chkNM_' in text:
        text = text.replace('cphPagina_chkNM_', '')
        return text
    elif 'cphPagina_chKNM_' in text:
        text = text.replace('cphPagina_chKNM_', '')
        return text  

def confirm_checkbox(html, desired_tag):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all('input'):
        if tag != None:
            if tag.get('checked'):
                id = tag.get('id')
                if detect_tag(id) == 'Ativo':
                    pass
                if detect_tag(id) == desired_tag.upper():
                    return False
    return True

def search_checkbox(html, mean_tag):

    result = {
        'ABNT': False,
        'ASTM': False,
        'ISO': False
    }

    #função usada para única e exclusivamente busca do atributo "checked" nas tags do checkbox da página de busca
    soup = BeautifulSoup(html, 'html.parser')
    #primeiro ele vai buscar todas as tags input que estão dentro da página
    for tag in soup.find_all('input'):
        if tag != None:
            if tag.get('checked'):          
                id = tag.get('id')
                print('A mean_tag é', mean_tag)
                print('A tag em questão é: ', detect_tag(id))
                if detect_tag(id) == mean_tag.upper():
                    result[f'{detect_tag(id).upper()}'] = False
                    print('É igual!')
                else:
                    result[f'{detect_tag(id).upper()}'] = True
                    print('Num é igual')
    return result

