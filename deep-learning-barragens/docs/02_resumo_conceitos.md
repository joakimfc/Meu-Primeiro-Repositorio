# Resumo dos conceitos

## Do neurônio à CNN
- **Neurônio:** y = f(Σ wᵢxᵢ + b). Entradas × pesos, soma, *bias*, **ativação** (ReLU: max(0, x); LeNet-5 usou tanh escalada).
- **Imagem:** pixel = número (0–255); tons de cinza = matriz; RGB = 3 canais; imagens de satélite podem ter mais bandas (ex.: Sentinel-2 com 13).
- **Camada densa** liga cada pixel a cada neurônio: muitos parâmetros e ignora vizinhança.

## Convolução
- **Filtro (kernel):** pequena grade de pesos que percorre a imagem; em cada posição multiplica e soma → um valor do **mapa de características**. Valor alto = padrão encontrado.
- **Conexões locais** (cada unidade vê uma vizinhança) e **pesos compartilhados** (mesmo filtro em todas as posições) reduzem parâmetros e dão equivariância a deslocamentos.
- **Filtros são aprendidos**, não escolhidos à mão.
- **Tamanho de saída:** ⌊(n + 2p − k)/s⌋ + 1. Ex.: 32, k=5, p=0, s=1 → 28 (C1 da LeNet-5).
- **Stride:** passo da janela (maior = mapa menor). **Padding:** borda de zeros para preservar tamanho e tratar cantos.
- **Vários canais:** o filtro tem profundidade igual à da entrada; soma os canais num único mapa; várias filtros = vários mapas.

## Pooling e hierarquia
- **Pooling** (máximo ou média) reduz o mapa e dá certa tolerância a pequenos deslocamentos. Na LeNet-5 era média treinável.
- **Campo receptivo:** camadas profundas "enxergam" áreas maiores → de bordas a formas globais.
- **Achatamento + camada densa + softmax** produzem probabilidades de classe.

## Aprendizado
Supervisionado: imagem + rótulo → previsão → **perda** (ex.: entropia cruzada) → **retropropagação** calcula gradientes → **otimizador** (SGD/Adam) atualiza pesos, inclusive os filtros. Ajustes comuns: aumento de dados, dropout, batch normalization, transferência de aprendizado.

## Tarefas
| Pergunta | Tarefa | Saída | Exemplo |
|---|---|---|---|
| Há reservatório na imagem? | Classificação | 1 classe/imagem | Malerba (ResNet34) |
| Onde está a água? | Segmentação | 1 classe/pixel | **Nossa proposta (U-Net)** |
| Qual o nível? | Regressão | valor numérico | — |

## LeNet-5 (LeCun et al., 1998) em números
Entrada 32×32 → C1 (6@28×28) → S2 (6@14×14) → C3 (16@10×10, conexão parcial) → S4 (16@5×5) → C5 (120) → F6 (84) → 10 saídas (RBF).
**60.000 parâmetros, 340.068 conexões** (verificado em `src/lenet5_parametros.py`). C5 é "convolucional", mas com entrada 5×5 equivale a camada densa e concentra 80,2% dos parâmetros.
Observação: algumas fontes descrevem a LeNet-5 como "2 conv + 2 pooling + 3 densas"; é a mesma rede contando C5 como densa.

## Do seminal ao que usaremos
LeNet (retropropagação + pesos compartilhados) → **AlexNet** (escala, ReLU, GPU) → **ResNet** (conexões residuais, backbone de Malerba) → **U-Net** (codificador-decodificador com *skip connections*, segmentação densa) .

## Segmentação e métricas
- **IoU** = |A∩B| / |A∪B|; **precisão** (erro de inclusão), **sensibilidade/recall** (erro de omissão), **F1** = média harmônica.
- **Área** = nº de pixels de água × área do pixel (precisa de máscara georreferenciada).
- Duas máscaras podem ter a mesma área e contornos diferentes; erros em cada data podem parecer mudança.

## Grandezas hidrológicas (não confundir)
| Grandeza | Obtida de | Observação |
|---|---|---|
| Área (km²) | máscara da imagem | uma observação por data |
| Cota/nível (m) | medição; ou via CAV a partir da área | relação local |
| Volume (hm³) | CAV (cota→volume) | depende da geometria do reservatório |
| Vazão (m³/s) | operação/estações | **não** sai de uma imagem isolada |
| Volume de espera | regra operativa | margem para cheias |

## Limites das CNNs
Dependência de dados rotulados, generalização entre sensores/regiões/estações, custo de preparação, erros de borda; invariância a translação/escala/rotação **não é garantida** (Azulay & Weiss, 2018; Zhang, 2019); interpretabilidade limitada (Grad-CAM ajuda).
