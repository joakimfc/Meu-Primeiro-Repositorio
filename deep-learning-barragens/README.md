# CNNs para monitoramento de reservatórios — Trabalho final de Deep Learning

Mestrado em Ciências de Dados e IA (IDP) · Disciplina *Deep Learning e PLN* · Opção 1:
técnica + literatura empírica + proposta de caso real · apresentação de 30 min, grupo de 3–4.

## Fio condutor
**LeCun (1989/1998)** → o que é uma CNN e por que funciona  
**Malerba et al. (2021)** (+ Teixeira et al., 2024, complementar) → CNN em imagens de satélite de reservatórios  
**Nossa proposta** → segmentação multitemporal de Ilha Solteira e Jupiá, convertendo área em cota/volume pela tabela CAV e confrontando com os dados operacionais

> A proposta é **método a desenvolver**. Nada aqui é resultado do grupo; valores ilustrativos são sempre rotulados.

## Conteúdo
| Arquivo | O que tem |
|---|---|
| [docs/00_decisoes_e_pendencias.md](docs/00_decisoes_e_pendencias.md) | Decisões a tomar, riscos e itens a verificar **antes** de montar os slides |
| [docs/01_plano_apresentacao.md](docs/01_plano_apresentacao.md) | Roteiro slide a slide (12 + 10 + 8 min), divisão de tarefas |
| [docs/02_resumo_conceitos.md](docs/02_resumo_conceitos.md) | Resumo dos conceitos de CNN |
| [docs/03_literatura.md](docs/03_literatura.md) | Seminal, aplicado, avanços; o que cada fonte sustenta e o que falta conferir |
| [docs/04_proposta_aplicacao.md](docs/04_proposta_aplicacao.md) | Proposta: dados, pipeline, arquitetura, avaliação, limites |
| [src/lenet5_parametros.py](src/lenet5_parametros.py) | Confere 60.000 parâmetros / 340.068 conexões da LeNet-5 |
| [src/convolucao_demo.py](src/convolucao_demo.py) | Convolução, ReLU, pooling e tamanho de saída em Python puro |

```bash
python src/lenet5_parametros.py
python src/convolucao_demo.py
```
