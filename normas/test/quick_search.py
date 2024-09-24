from bs4 import BeautifulSoup
import pandas as pd

log = pd.DataFrame({
    'ALERT': [],
    'PARAMETER': [],
    'RESULT': [],
    'TITLE_OF_PAGE': [],
    'FILE': [],
})

#cphPagina_chkNM_

def read_txt(path_file):
    with open(path_file, "r", encoding="utf-8") as file:
        return file.read()

def analyze_tag(path_file, mean_tag):
    soup = BeautifulSoup(read_txt(path_file), 'html.parser')
    for tag in soup.find_all(f'{mean_tag}'):
        if tag != None:
            from result import input_row
            log.loc[len(log)] = input_row('OK', mean_tag, str(tag), soup.title.string, path_file)
        else:
            log.loc[len(log)] = input_row('ERROR', mean_tag, 'DONT EXISTS', soup.title.string, path_file)
    log.to_excel(f'{format_namefile(path_file)}.xlsx')

def format_namefile(name):
    if '.txt' in name:
        name = name.replace('.txt', '')
        return name
    elif '.html' in name:
        name = name.replace('.html', '')
        return name

def search_specify_id(path_file, id):
    soup = BeautifulSoup(read_txt(path_file), 'html.parser')
    return soup.get('id') == id

def detect_tag(text):
    if 'cphPagina_chkNM_' in text:
        text = text.replace('cphPagina_chkNM_', '')
        return text
    elif 'cphPagina_chKNM_' in text:
        text = text.replace('cphPagina_chKNM_', '')
        return text
    
def search_specify_atribute(path_file, mean_tag, attribute):
    #need a tag for search a specific attribute.
    soup = BeautifulSoup(read_txt(path_file), 'html.parser')
    for tag in soup.find_all(f'{mean_tag}'):
        if tag != None:
            if tag.get(attribute):
                from result import input_row
                log.loc[len(log)] = input_row('OK', mean_tag, str(tag), soup.title.string, path_file)
                id = tag.get('id')
                print('A tag em questão é: ', detect_tag(id))
        else:
            log.loc[len(log)] = input_row('ERROR', mean_tag, 'DONT EXISTS', soup.title.string, path_file)
    log.to_excel(f'{format_namefile(path_file)}.xlsx')

search_specify_atribute('abnt.txt', 'input','checked')
print(log)


