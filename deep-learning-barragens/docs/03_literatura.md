# Literatura

Legenda de confiança: ✅ conferido neste repositório · 📄 vem de material do grupo, a conferir no original · ⚠️ divergência/lacuna.

## 1. Seminal
- **LeCun, Y. et al. (1989).** *Backpropagation Applied to Handwritten Zip Code Recognition.* Neural Computation 1(4):541–551. doi:10.1162/neco.1989.1.4.541
  Contribuição: embutir restrições de domínio (conectividade local, pesos compartilhados) na rede e treinar ponta a ponta por retropropagação, a partir de imagens normalizadas de dígitos (USPS). Números detalhados 📄⚠️ (ver B2).
- **LeCun, Y.; Bottou, L.; Bengio, Y.; Haffner, P. (1998).** *Gradient-Based Learning Applied to Document Recognition.* Proc. IEEE 86(11):2278–2324. doi:10.1109/5.726791
  Contribuição: LeNet-5; MNIST; sistemas de múltiplos módulos treinados globalmente por gradiente (Graph Transformer Networks); leitura comercial de cheques. Estrutura/parâmetros ✅ (script); erros no MNIST 📄.
- Precursores: Hubel & Wiesel (1962); Fukushima, *Neocognitron* (1980); Rumelhart, Hinton & Williams (1986, retropropagação).

## 2. Aplicado
- **Malerba, M. E.; Wright, N.; Macreadie, P. I. (2021).** *A Continental-Scale Assessment of Density, Size, Distribution and Historical Trends of Farm Dams Using Deep Learning CNNs.* Remote Sensing 13(2):319. doi:10.3390/rs13020319
  Existência e tema ✅; uso de RGB de alta resolução ✅ (revisão por pares MDPI). 7.362 imagens, ResNet34, 80/20 e 94,8% 📄 — conferir (B1).
  Ressalvas a explicitar: a CNN **classifica**; análise histórica por WOfS; capacidade por relação estatística área–capacidade; acurácia é da validação dos autores.
- **Complementar sugerido — Teixeira, A. M. A.; Batista, L. V.; Santos, C. A. G. et al. (2024).** *Dynamic monitoring of surface area and water volume of reservoirs using satellite imagery, computer vision and deep learning.* Remote Sens. Appl.: Soc. Environ. doi:10.1016/j.rsase.2024.101205
  Segundo LeapSpace: segmentação em Sentinel-2, IoU 95% 📄. Segundo a dissertação correspondente (UFPB): CNN extrai área e o volume vem de curvas elevação-área-volume ✅(resumo). É o precedente mais próximo da nossa cadeia área→volume. Conferir (B3).
- Outros (apoio, via LeapSpace 📄): Li et al. (2023, J. Hydrology) shoreline com super-resolução; He et al. (2023, JAG) CAU-Flood Sentinel-1/2; Bonafilia et al. (2020) Sen1Floods11.
  Observação do LeapSpace: **só um** artigo é estritamente sobre barragens; descrever o conjunto como "um artigo direto + vizinhos metodológicos".

## 3. Avanços da técnica (linha do tempo)
| Ano | Marco | Ideia |
|---|---|---|
| 2012 | AlexNet (Krizhevsky et al.) | ReLU, GPU, dropout; top-5 15,3% vs 26,2% no ILSVRC-2012 |
| 2014 | VGG (Simonyan & Zisserman) | filtros 3×3 empilhados, 16–19 camadas |
| 2015 | ResNet (He et al., 2016) | conexões residuais; **backbone de Malerba** |
| 2015 | Batch Norm (Ioffe & Szegedy) | treino acelerado |
| 2015 | FCN (Long et al.) / U-Net (Ronneberger et al.) | segmentação densa; **U-Net é nossa proposta** |
| 2021 | ViT (Dosovitskiy et al.) | atenção; viés convolucional útil com poucos dados |
| 2022 | ConvNeXt (Liu et al.) | CNN modernizada competitiva com Transformers |
Críticas: invariância a deslocamento não automática (Azulay & Weiss, 2018; Zhang, 2019).
Fontes agregadoras do grupo: relatórios Consensus (✅ lidos) e "CNNs: Fundamentos" (📄, material secundário — preferir artigos originais nos slides).

## 4. Normas
IDP. *Plano de Ensino: Deep Learning e PLN.* Prof. Danny de Castro, 2026 — fonte das exigências (citado no roteiro do grupo; não incluído aqui).
