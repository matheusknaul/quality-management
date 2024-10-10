from data_sync import __getData__

keys_entry = __getData__()

# return of __getData__
# entrada = [tag, number, part, year] <- return of __getData__
# saída = [código da norma completo, descrição, status (aqui inclui quanto o status da norma, quanto o status da verificação), data da última verificação]

# Segundo o GPT, o web driver não possui histórico ou dados de navegação, isso significa que, se conseguirmos dar quit em cada seção, poderemos pular a etapa
#de validar o checkbox.

#

from check_automation import __main__

__main__(keys_entry)
