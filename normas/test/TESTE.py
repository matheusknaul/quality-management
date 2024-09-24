titulo = ['1', '2', '3', '4']

string_list = f'{titulo}'
print(string_list)
string_list = string_list.replace('[','')
string_list = string_list.replace(']','')
string_list = string_list.replace("'",'')
print(string_list)