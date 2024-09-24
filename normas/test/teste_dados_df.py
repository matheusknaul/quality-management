import pandas as pd
from pandas._libs.tslibs.nattype import NaTType

_path_db = 'db_excel/dataframe.xlsx'
_data_frame = pd.read_excel(_path_db)

def verify_data_column(df, column):
    for indice, linha in df.iterrows():
        print(linha[column])
        print(type(linha[column]))

def detect_nan(df, column):
    quant_nan = []
    for indice, linha in df.iterrows():
        if pd.isnull(linha[column]):
            quant_nan.append(1)
            print(linha[column])
        else:
            new_data = str(int(linha[column]))
            print(new_data)
    print('The length of nan type in this column, is: ', len(quant_nan))

detect_nan(_data_frame, 'Ano')