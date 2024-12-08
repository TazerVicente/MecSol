import numpy as np
import matplotlib.pyplot as plt

def calcular_V_M_por_secao(x, cargas_p, momentos, cargas_d, reacoes, apoios):
    V = 0
    M = 0

    # Aplicar efeitos dos apoios
    for i, (tipo, pos) in enumerate(apoios):
        if x >= pos:
            if tipo == 'eng':
                if len(reacoes) > i:
                    R1, R2 = reacoes[i]
                    V += R1  # Acumular a reação de força
                    M += R2  # Aplicar o momento do apoio engastado
            elif tipo in ['pin', 'rol']:
                if len(reacoes) > i:
                    R1, _ = reacoes[i]
                    V += R1  # Acumular a reação de força

    # Aplicar efeitos das cargas pontuais
    for carga in cargas_p:
        if x >= carga[1]:
            V -= carga[0]
            M -= carga[0] * (x - carga[1])  # Calcular o momento devido à carga pontual

    # Aplicar efeitos das cargas distribuídas
    for carga in cargas_d:
        a, b, p1, p2 = carga
        if a <= x <= b:
            if p1 == p2:  # Retangular
                w = p1
                V -= w * (x - a)
                M -= w * (x - a) * (x - (a + b) / 2)
            elif p1 < p2:  # Triangular crescente
                w = (p2 - p1) / (b - a)
                V -= (p1 * (x - a) + 0.5 * w * (x - a)**2)
                M -= p1 * (x - a)**2 / 2 + w * (x - a)**3 / 6
            elif p1 > p2:  # Triangular decrescente
                w = (p1 - p2) / (b - a)
                V -= (p1 * (x - a) - 0.5 * w * (x - a)**2)
                M -= p1 * (x - a)**2 / 2 - w * (x - a)**3 / 6
        elif x > b:
            if p1 == p2:  # Retangular
                V -= p1 * (b - a)
                M -= p1 * (b - a) * (x - (a + b) / 2)
            elif p1 < p2:  # Triangular crescente
                V -= (p1 + p2) * (b - a) / 2
                M -= (p1 + p2) * (b - a) / 2 * (x - (2 * b + a) / 3)
            elif p1 > p2:  # Triangular decrescente
                V -= (p1 + p2) * (b - a) / 2
                M -= (p1 + p2) * (b - a) / 2 * (x - (2 * a + b) / 3)

    # Aplicar efeitos dos momentos aplicados
    for momento in momentos:
        if x >= momento[1]:
            M -= momento[0]

    return V, M

def calcular_esforcos(apoios, tamanho, reacoes, cargas_p, momentos, cargas_d):
    posicoes = [pos for tipo, pos in apoios] + [0, tamanho]
    for carga in cargas_p:
        posicoes.append(carga[1])
    for momento in momentos:
        posicoes.append(momento[1])
    for carga in cargas_d:
        posicoes.append(carga[0])
        posicoes.append(carga[1])
    secoes = sorted(set(posicoes))

    equacoes_secao = []
    for i in range(len(secoes) - 1):
        xi = secoes[i]
        xf = secoes[i+1]
        Vi, Mi = calcular_V_M_por_secao(xi, cargas_p, momentos, cargas_d, reacoes, apoios)
        Vf, Mf = calcular_V_M_por_secao(xf, cargas_p, momentos, cargas_d, reacoes, apoios)
        equacoes_secao.append({
            "secao": f"{xi} <= x < {xf}",
            "V(x)": f"{Vi}",
            "M(x)": f"{Mi}"
        })

    return equacoes_secao, secoes

reacoes = [[R1, R2], [R2, R1]]
equacoes, secoes = calcular_esforcos(apoios, tamanho, reacoes, cargas_p, momento, cargas_d)

#Espaço para plotagem do gráfico
x = np.linspace(0, tamanho, 500)
V = np.zeros_like(x)
M = np.zeros_like(x)


# Calcular esforço cortante e momento fletor para cada ponto
for i in range(len(x)):
    V[i], M[i] = calcular_V_M_por_secao(x[i], cargas_p, momento, cargas_d, reacoes, apoios)

# Definir as cores para cada seção
cores_secao = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']

plt.figure(figsize=(12, 6))

# Gráfico de Esforço Cortante e a plotagem das seções em um range igual o de cima
plt.subplot(2, 1, 1)
for i in range(len(secoes) - 1):
    xi = secoes[i]
    xf = secoes[i + 1]
    x_seccao = np.linspace(xi, xf, 100)
    V_seccao = np.zeros_like(x_seccao)
    for j in range(len(x_seccao)):
        V_seccao[j], _ = calcular_V_M_por_secao(x_seccao[j], cargas_p, momento, cargas_d, reacoes, apoios)
    plt.fill_between(x_seccao, V_seccao, 0, where=(V_seccao >= 0), color=cores_secao[i % len(cores_secao)], alpha=0.3)
    plt.fill_between(x_seccao, V_seccao, 0, where=(V_seccao < 0), color=cores_secao[i % len(cores_secao)], alpha=0.3)

plt.axhline(0, color='black', linewidth=2)
plt.xlabel('Posição x')
plt.ylabel('Esforço Cortante V(x)')
plt.title('Gráfico de Esforço Cortante por Seção')
plt.grid(True)

# Gráfico de Momento Fletor e a plotagem das seções em um range igual o de cima
plt.subplot(2, 1, 2)
for i in range(len(secoes) - 1):
    xi = secoes[i]
    xf = secoes[i + 1]
    x_seccao = np.linspace(xi, xf, 100)
    M_seccao = np.zeros_like(x_seccao)
    for j in range(len(x_seccao)):
        _, M_seccao[j] = calcular_V_M_por_secao(x_seccao[j], cargas_p, momento, cargas_d, reacoes, apoios)
    plt.fill_between(x_seccao, M_seccao, 0, where=(M_seccao >= 0), color=cores_secao[i % len(cores_secao)], alpha=0.3)
    plt.fill_between(x_seccao, M_seccao, 0, where=(M_seccao < 0), color=cores_secao[i % len(cores_secao)], alpha=0.3)

plt.axhline(0, color='black', linewidth=2)
plt.ylabel('Momento Fletor M(x)')
plt.title('Gráfico de Momento Fletor por Seção')
plt.grid(True)

plt.tight_layout()
plt.show()
