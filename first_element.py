# Autor: Nicolas de Oliveira Lopes Braga - Case DataSprints

# Desenvolva um script em python para retornar o primeiro valor não repetido de uma string.
# Exemplo:
# input -> 'teste'
# output -> 's'
# input -> 'engenharia de dados'
# output -> 'g'

# Função para encontrar primeiro elemento único da string.
def drop_duplicates(str_word):
    
    unique = [i for i in word if word.count( i ) == 1]

    return unique[0]

# Leitura da string já transformando em lista. 
# word = list(input("Entre com uma string: ")) # Input formatado. 
word = list(input())

# Chamada da função e tratamento de erros. 
try:
    # print(f'Primeiro elemento único: {drop_duplicates(word)}') # Print formatado. 
    print(drop_duplicates(word))
except:
    print('Input fora do padrão ou sem caracteres únicos.')