# Dicionário de produtos fictícios e suas categorias
produtos = {
    'furadeira eletrica': 'Ferramentas Elétricas e Máquinas',
    'maquina de solda': 'Ferramentas Elétricas e Máquinas' ,
    'tinta Automotiva': 'Funilaria e Pintura',
    'aspirador': 'Jardinagem' ,
    'compressor de ar':'Ferramentas Elétricas e Máquinas', 
    'marteletes eletricos':'Ferramentas Elétricas e Máquinas', 
    'alicate para solda':'Funilaria e Pintura', 
    'eletrodo e Arames':'Funilaria e Pintura', 
}



# Solicitar ao usuário que escolha produtos separados por vírgula
escolha_usuario = input("Escolha produtos (separados por vírgula): ").strip().split(",")

# Inicializar uma lista vazia para armazenar as categorias dos produtos escolhidos
categorias_escolhidas = []

# Verificar as categorias dos produtos escolhidos usando o operador lógico 'and'
todos_mesma_categoria = True

for produto in escolha_usuario:
    produto = produto.strip()
    if produto in produtos:
        categoria = produtos[produto]
        categorias_escolhidas.append(categoria)
    else:
        todos_mesma_categoria = False  # Se um produto não for encontrado, definir como False

# Exibir o resultado
if todos_mesma_categoria and categorias_escolhidas:
    primeira_categoria = categorias_escolhidas[0]
    if all(categoria == primeira_categoria for categoria in categorias_escolhidas):
        print(f"Você escolheu produtos da categoria: {primeira_categoria}.")
    else:
        print(f"Você escolheu produtos de categorias diferentes.")
else:
    print("Nenhum produto válido foi escolhido.")
