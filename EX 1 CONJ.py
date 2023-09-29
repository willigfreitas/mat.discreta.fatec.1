#programa relacionado a conjuntos
produto = input("Digite o nome do produto: ")

# Criar dicionários para mapear produtos aos grupos
grupos = {
    'Ferramentas Elétricas e Máquinas': {'compressor de ar','maquina de solda','serra eletrica','parafusadeiras eletricas', 'esmerilhadeira','furadeira eletrica', 'tupias e plainas', 'marteletes eletricos', 'lixadeira e politriz'},
    'Funilaria e Pintura': {'alicate para solda', 'alinhador', 'eletrodo e Arames', 'martelinho de ouro', 'tasso', 'tinta automotiva', 'massa plastica'},
    'Jardinagem': {'aparadores de cerca viva', 'aparadores de grama', 'aspirador', 'soprador de folhas'}
    }


#
#


# Inicializar uma lista vazia para armazenar os grupos do produto
grupos_produto = []

# Verificar a que grupos o produto pertence usando um loop for
for grupo, produtos in grupos.items():
    if produto.lower() in produtos:
        grupos_produto.append(grupo)

# Exibir o resultado
if grupos_produto:
    print(f"O produto '{produto}' pertence ao seguinte grupo: {', '.join(grupos_produto)}.")
else:
    print(f"O produto '{produto}' não pertence a nenhum grupo conhecido.")
