# Plano da apresentação (30 min)

Formato livre, grupo de 3–4 pessoas, sem exigência de código. Foco: clareza e fundamentação.
Regra: tudo da proposta no **condicional**; números ilustrativos com selo "HIPOTÉTICO".

| Bloco | Tempo | Quem (definir) | Entrega |
|---|---|---|---|
| 1. Técnica (CNN + LeCun + avanços) | 12 min | Pessoa A | A turma entende componentes e treinamento |
| 2. Uso real (Malerba + complemento) | 10 min | Pessoa B | Problema, dados, método, métricas, resultados, crítica |
| 3. Proposta nova | 8 min | Pessoas C/D | Aplicação, dados, arquitetura, avaliação, impacto |

## Bloco 1 — Técnica (12 min, ~7 slides)
1. **Pergunta guia** (1 min): como uma máquina "enxerga" um reservatório? Tabela classificação/segmentação/regressão.
2. **Do neurônio à imagem** (2 min): soma ponderada + bias + ativação; imagem = matriz de números; RGB = 3 canais.
3. **Convolução** (2 min): filtro 2×2 percorrendo a imagem → mapa de características (exemplo 8/0/0/3 da aula; `src/convolucao_demo.py`).
4. **O que torna a CNN especial** (1,5 min): conexões locais + pesos compartilhados vs. camada densa. Usar a LeNet-5: C1–S4 têm 82,9% das conexões e 2,9% dos parâmetros.
5. **Camadas e aprendizado** (2,5 min): ReLU, stride, padding, pooling → previsão → perda → retropropagação → atualização dos filtros.
6. **LeCun (1989 → 1998)** (2 min): zip codes/USPS → LeNet-5, MNIST, treino ponta a ponta. Arquitetura: entrada 32×32 → C1 → S2 → C3 → S4 → C5 → F6 → saída.
7. **Avanços, em uma linha do tempo** (1 min, e fecha o bloco): AlexNet 2012 (ReLU, GPU, dropout) → VGG (3×3 empilhado) → **ResNet** (conexões residuais; é o backbone de Malerba) → **U-Net** (codificador-decodificador; é a nossa proposta) → ConvNeXt (CNN modernizada). Limites: dados rotulados, generalização, e invariância a deslocamento **não é automática** (Azulay & Weiss, 2018).

## Bloco 2 — Uso real (10 min, ~6 slides)
1. **Malerba et al. (2021)** — problema: inventário de pequenos reservatórios rurais na Austrália (registros incorretos, não documentados).
2. **Dados**: imagens RGB de alta resolução; rotulagem inicial pequena → classificação assistida pelo modelo + correção humana. *(números: conferir B1)*
3. **Método**: ResNet34 pré-treinada no ImageNet, aprendizado por transferência, "dam"/"not dam".
4. **Avaliação e resultado**: 80/20; acurácia relatada pelos autores (**do experimento deles, não de reservatórios brasileiros**).
5. **Ponto metodológico central**: a CNN **classifica imagens**, não gera máscara; histórico usa WOfS e capacidade vem de relação estatística área–capacidade (558 reservatórios).
6. **Crítica + complemento (Teixeira et al., 2024)**: o que a métrica mede, papel da correção humana, diferença Austrália × Brasil; no complemento, CNN de área + curva cota-área-volume — o elo para a nossa proposta.

## Bloco 3 — Proposta (8 min, ~5 slides)
1. **Pergunta**: como uma CNN poderia apoiar a identificação e quantificação de mudanças na superfície de água de Ilha Solteira e Jupiá?
2. **Dados** (esquema "5 bases + imagens"): imagens (Brasil MAIS/Sentinel-2) → máscara → área; CAV converte área↔cota↔volume; hidrológicos diários e fluviométricos **validam**; cadastro contextualiza; volume de espera = indicador de margem operacional.
3. **Arquitetura**: U-Net (segmentação), por quê e diferença para Malerba.
4. **Avaliação**: IoU/F1/precisão/sensibilidade; erro de área; separação por cena/data/local; validação cruzada com cota e volume observados.
5. **Impacto esperado e limites**: apoio ao monitoramento hídrico; **não** prova segurança estrutural; duas datas ≠ tendência. Exemplo "HIPOTÉTICO" (2,0→1,8 km²) apenas para ilustrar perda/ganho.

## Cuidados de apresentação
- Separar sempre: *resultado do artigo* / *interpretação do grupo* / *proposta*.
- Slides de aula (Gemini Notebook) podem ser reaproveitados só se o grupo concordar; citar a origem.
- Ensaiar com cronômetro; reservar 1 min de folga.

## Próximos passos
1. Resolver pendências B1–B6 ([00](00_decisoes_e_pendencias.md)).
2. Dividir blocos e fechar rascunho dos slides.
3. Teste de sensibilidade área×cota na CAV (se os dados já estiverem acessíveis) — apenas para embasar a proposta.
4. Ensaio geral.
