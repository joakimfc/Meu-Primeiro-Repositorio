"""Confere as contagens de parâmetros e conexões da LeNet-5 (LeCun et al., 1998).

Uso: python src/lenet5_parametros.py
Objetivo: validar os números usados nos slides (60.000 parâmetros; 340.068 conexões),
que vêm de material secundário e devem ser conferidos contra o artigo original.
"""

# Tabela de conexões de C3 (Tabela I do artigo de 1998): quantos mapas de S2
# cada um dos 16 mapas de C3 recebe. 6 mapas com 3, 9 com 4 (6 contíguos + 3
# descontínuos) e 1 com 6 -> 6*3 + 6*4 + 3*4 + 1*6 = 60 ligações mapa-a-mapa.
C3_ENTRADAS = [3] * 6 + [4] * 6 + [4] * 3 + [6] * 1

K = 5  # núcleo 5x5


def camadas():
    c1_p = 6 * (K * K * 1 + 1)
    c1_c = c1_p * 28 * 28
    s2_p = 6 * 2                       # 1 coeficiente + 1 bias por mapa
    s2_c = 6 * (2 * 2 + 1) * 14 * 14
    c3_p = sum(n * K * K + 1 for n in C3_ENTRADAS)
    c3_c = c3_p * 10 * 10
    s4_p = 16 * 2
    s4_c = 16 * (2 * 2 + 1) * 5 * 5
    c5_p = 120 * (16 * K * K + 1)      # C5 é conv 5x5 sobre mapas 5x5 = densa
    c5_c = c5_p
    f6_p = 84 * (120 + 1)
    f6_c = f6_p
    return [
        ("C1", c1_p, c1_c), ("S2", s2_p, s2_c), ("C3", c3_p, c3_c),
        ("S4", s4_p, s4_c), ("C5", c5_p, c5_c), ("F6", f6_p, f6_c),
    ]


if __name__ == "__main__":
    tp = tc = 0
    print(f"{'camada':<6}{'parâmetros':>12}{'conexões':>12}")
    for nome, p, c in camadas():
        tp += p
        tc += c
        print(f"{nome:<6}{p:>12,}{c:>12,}".replace(",", "."))
    print(f"{'total':<6}{tp:>12,}{tc:>12,}".replace(",", "."))
    assert tp == 60_000, tp
    assert tc == 340_068, tc
    esp_p = sum(p for n, p, _ in camadas() if n in ("C1", "S2", "C3", "S4"))
    esp_c = sum(c for n, _, c in camadas() if n in ("C1", "S2", "C3", "S4"))
    print(f"C1-S4: {esp_p/tp:.2%} dos parâmetros, {esp_c/tc:.2%} das conexões")
    print("OK: bate com 60.000 parâmetros e 340.068 conexões (saída RBF, 840 fixas, fora da conta).")
