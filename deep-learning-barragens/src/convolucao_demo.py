"""Demonstração numérica da convolução, ReLU e pooling (bloco 'Técnica').

Valores DIDÁTICOS, não são resultados de nenhum experimento.
Uso: python src/convolucao_demo.py
"""


def conv2d(img, ker, bias=0, stride=1, pad=0):
    if pad:
        w = len(img[0]) + 2 * pad
        img = [[0] * w] + [[0] * pad + r + [0] * pad for r in img] + [[0] * w]
        img = [[0] * w for _ in range(pad - 1)] + img + [[0] * w for _ in range(pad - 1)]
    kh, kw = len(ker), len(ker[0])
    out = []
    for i in range(0, len(img) - kh + 1, stride):
        linha = []
        for j in range(0, len(img[0]) - kw + 1, stride):
            s = sum(img[i + a][j + b] * ker[a][b] for a in range(kh) for b in range(kw))
            linha.append(s + bias)
        out.append(linha)
    return out


def relu(m):
    return [[max(0, v) for v in r] for r in m]


def maxpool(m, k=2):
    return [[max(m[i + a][j + b] for a in range(k) for b in range(k))
             for j in range(0, len(m[0]) - k + 1, k)] for i in range(0, len(m) - k + 1, k)]


def tamanho_saida(n, k, pad=0, stride=1):
    return (n + 2 * pad - k) // stride + 1


if __name__ == "__main__":
    # Imagem 4x4 com uma borda vertical (esquerda clara, direita escura)
    img = [[9, 9, 0, 0]] * 4
    vertical = [[1, -1], [1, -1]]          # detecta transição claro->escuro
    mapa = conv2d(img, vertical)
    print("mapa de características:", mapa)
    print("após ReLU:", relu(mapa))
    print("tamanho de saída 32x32, k=5, pad=0, s=1:", tamanho_saida(32, 5))   # 28 (C1 da LeNet-5)
    print("tamanho de saída 28x28, k=5, pad=2, s=1:", tamanho_saida(28, 5, pad=2))  # 28 ('same')
    # Pooling 2x2 sobre o exemplo do material de aula
    ex = [[9, 2, 1, 5], [3, 8, 4, 0], [7, 6, 2, 3], [1, 0, 5, 4]]
    print("max pooling 2x2:", maxpool(ex))  # [[9,5],[7,5]]
    # Camada: mapa [[8,0],[0,3]] + bias -2 -> ReLU (slide da aula)
    print("slide: ", relu([[v - 2 for v in r] for r in [[8, 0], [0, 3]]]))  # [[6,0],[0,1]]
