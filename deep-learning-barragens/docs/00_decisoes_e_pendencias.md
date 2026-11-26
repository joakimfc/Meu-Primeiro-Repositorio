# Decisões, riscos e pendências

## A. Decisões para o grupo
1. **Artigo seminal.** Recomendação: **LeCun et al. (1998)** como principal (traz a LeNet-5 e é a referência
   que o roteiro da disciplina indica), com **LeCun et al. (1989)** como origem (primeira CNN treinada por
   retropropagação). Confirmar com o professor se um ou os dois.
2. **Artigo aplicado.** Malerba et al. (2021) é o candidato do roteiro. Sugestão de **complementar**:
   **Teixeira et al. (2024)**, que faz justamente *área por CNN → volume por curva cota-área-volume* em
   reservatórios brasileiros (UFPB). Ver pendência B3.
3. **Tarefa da proposta.** Segmentação (U-Net) em vez da classificação de Malerba — justificar a mudança.
4. **Onde fica o repositório.** Este material está em subpasta do repositório da disciplina
   *Transformação Digital*. Se preferirem, mover para um repositório próprio.

## B. Itens a verificar antes de apresentar
| # | Item | Situação |
|---|---|---|
| B1 | Números de Malerba (7.362 imagens, 400 rotuladas, ResNet34, 80/20, 94,8%, 558 reservatórios) | Vêm do roteiro do grupo. A busca web confirmou o artigo e que usa RGB de alta resolução, **mas não os números**. Conferir nas seções 2.1–2.3 do PDF original (MDPI). |
| B2 | LeCun 1989: 9.298 dígitos, 7.291/2.007, 5,0% de erro no teste, 1% com 12,1% de rejeição | Vêm do relatório "CNNs: Fundamentos". O Consensus cita **~9% de rejeição** (relatório companheiro, outro texto). **Divergência** — conferir no original antes de usar. |
| B3 | Teixeira et al. (2024) | A busca achou a **dissertação** (UFPB, "Monitoramento Dinâmico do Volume Hídrico em Reservatórios Utilizando Imagens de Satélite e Redes Neurais Convolucionais"), mas não um artigo com o título do LeapSpace. Confirmar o artigo (RSASE, 2024), arquitetura e métricas. |
| B4 | LeNet-5 (60.000 parâmetros; 340.068 conexões; 0,95% / 0,8% no MNIST) | Parâmetros e conexões **reproduzidos** por `src/lenet5_parametros.py`. Erros no MNIST: conferir no artigo de 1998. |
| B5 | Brasil MAIS | É um programa do Ministério da Justiça e Segurança Pública (imagens diárias e mosaicos mensais, >130 satélites). Fontes consultadas indicam **acesso restrito a instituições habilitadas** — resolução, periodicidade e licença para uso acadêmico **não confirmadas**. |
| B6 | Dados ONS/ANA (5 bases) | Ainda não inspecionados: conferir período, formato, ID de usina e unidades. |

## C. Riscos técnicos da proposta
- **Sensibilidade área→cota.** Em reservatórios com pouca variação operativa de nível (a verificar para Jupiá),
  a área muda pouco entre cotas; o erro de contorno da máscara (≈1 pixel de borda) pode superar o sinal.
  *Teste antes de treinar:* calcular dA/dh na tabela CAV e comparar com o erro esperado de área.
  Ilha Solteira, com deplecionamento maior, tende a ser o caso mais favorável (hipótese a checar na CAV).
- **Acesso ao Brasil MAIS** (B5). Plano B: Sentinel-2 (10 m, revisita ~5 dias) ou mosaicos NICFI/Planet (~4,8 m).
- **Rótulos.** Não há máscaras prontas: opções são limiar espectral (NDWI/MNDWI) como rótulo fraco + revisão
  humana, ou pré-rótulos de produtos existentes. Nível e vazão **não substituem** máscara espacial.
- **Nuvem e sombra** nas datas; alinhamento entre imagens; vazamento entre treino e teste (separar por cena/data/local).
- **Alcance da conclusão.** Mapear superfície de água apoia monitoramento hídrico; **não demonstra segurança
  estrutural** nem atribui causas (chuva × operação) automaticamente.
