import math

# Função para calcular a distância entre dois pontos
def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# Função para verificar se dois pontos estão no mesmo quadrante
def mesmo_quadrante(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if (x1 * x2 > 0) and (y1 * y2 > 0):
        return True
    else:
        return False

# Solicitar ao usuário que insira os pares ordenados
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Criar os pares ordenados
ponto1 = (x1, y1)
ponto2 = (x2, y2)

# Calcular a distância entre os pontos
distancia = calcular_distancia(ponto1, ponto2)

# Verificar se os pontos estão no mesmo quadrante
if mesmo_quadrante(ponto1, ponto2):
    mesmo_quadrante_str = "sim"
else:
    mesmo_quadrante_str = "não"

# Exibir os resultados
print(f"A distância entre os pontos {ponto1} e {ponto2} é {distancia:.2f}.")
print(f"Os pontos estão no mesmo quadrante? {mesmo_quadrante_str}")
