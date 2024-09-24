from datetime import datetime, timedelta

class Data:
    def data_numero(self, data):
        try:
            # Verificar se data é uma string, se for, converter para datetime
            if isinstance(data, str):
                data = self.trocar_tipo(data, 'datetime.datetime')
                
            data_base = datetime(1899, 12, 30)
            delta = data - data_base

            if data > datetime(1900, 2, 28):
                delta_days = delta.days + 1
            else:
                delta_days = delta.days

            return int(delta_days)
        
        except ValueError as ve:
            print(f'Erro ao converter a data: formato de data inválido - {ve}')
        except TypeError as te:
            print(f'Erro ao converter a data: tipo de dado inválido - {te}')
        except Exception as e:
            print(f'Erro inesperado ao converter a data: {e}')
        return None
    
    def transformar_data(self, numero):
        data_base = datetime(1899, 12, 30)

        if numero >= 60:
            numero -= 1
        
        data_resultante = data_base + timedelta(days=numero)
        return data_resultante.strftime("%d/%m/%Y")
    
    def data_hoje(self):
        data_atual = datetime.now().date()
        return data_atual.strftime("%d/%m/%Y")

    def data_hoje_numero(self):
        data_atual = datetime.now().date()
        data_formatada = data_atual.strftime("%d%m%Y")
        return self.data_numero(datetime.strptime(data_formatada, "%d%m%Y"))

    def trocar_tipo(self, objeto, tipo_requisitado):
        if tipo_requisitado == 'datetime.datetime' and isinstance(objeto, str):
            data_objeto = datetime.strptime(objeto, "%d/%m/%Y")
            return data_objeto
        
        return objeto  # Retornar o objeto inalterado se não for string

    def tipo_para_string(self, objeto):
        tipo = type(objeto)
        if tipo is int:
            return "int"
        elif tipo is float:
            return "float"
        elif tipo is str:
            return "str"
        elif tipo is list:
            return "list"
        elif tipo is tuple:
            return "tuple"
        elif tipo is dict:
            return "dict"
        elif tipo is set:
            return "set"
        elif tipo is bool:
            return "bool"
        elif tipo is datetime:
            return "datetime"
        else:
            return "desconhecido"

