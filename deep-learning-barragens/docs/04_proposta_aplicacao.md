# Proposta de aplicação (método a desenvolver — não executado)

**Pergunta:** como uma CNN poderia apoiar a identificação e a quantificação de mudanças na superfície de água
de um reservatório (Ilha Solteira e/ou Jupiá) a partir de imagens de diferentes datas, e como essa área se
relaciona com cota e volume?

**Ideia central (do grupo):** cada nível do reservatório corresponde a uma área e a um volume na tabela CAV;
logo, a área medida na imagem permitiria estimar cota e volume, e o resultado seria confrontado com os dados
operacionais.

## 1. Papel de cada base
| Base | Papel no projeto |
|---|---|
| **Imagens** (Brasil MAIS; alternativa Sentinel-2/NICFI) | Entrada da CNN → máscara de água → área em cada data |
| **Tabela CAV** (cota × área × volume) | Converte área em cota e volume (interpolação), e permite checar a sensibilidade da área à cota |
| **Dados hidrológicos diários** | Série de referência (cota, volume útil, afluência, defluência, turbinada, vertida); validação das estimativas e análise da operação Ilha Solteira–Jupiá |
| **Grandezas fluviométricas** | Contexto de bacia (chuva, nível/vazão a montante) para interpretar variações; **não** para atribuir causa automaticamente |
| **Cadastro dos reservatórios** | Identificação, cotas máx./mín., volumes de referência, para contextualizar e padronizar |
| **Volume de espera recomendado** | Indicador de margem operacional/risco hidrológico (comparar volume estimado com o volume mínimo livre); **não** é segurança estrutural |

## 2. Pipeline proposto
1. **Recorte:** reservatório (ou trecho) fixo, com ≥2 datas contrastantes (cheia/estiagem), com justificativa.
2. **Imagens:** descrever bandas, resolução e datas; verificar acesso e licença (B5). Escolher datas sem nuvem.
3. **Rótulos:** pares imagem–máscara (água=1, não água=0). Opções: pré-rótulo por índice de água (NDWI/MNDWI) + revisão humana em amostra; produtos existentes como referência independente. Nível e vazão não substituem máscara.
4. **Modelo:** U-Net (codificador-decodificador com *skip connections*), candidata a investigar; encoder pré-treinado (ex.: ResNet) como possibilidade. Justificar a troca de classificação (Malerba) por segmentação: precisamos de **área**, que exige a máscara.
5. **Comparação temporal:** alinhar espacialmente; classificar pixels em água persistente / ganho / perda; calcular áreas e diferença líquida.
6. **Conversão:** área → cota → volume pela CAV; comparar com cota e volume observados nas mesmas datas.
7. **Indicador de margem:** volume estimado vs. volume de espera recomendado (leitura operacional).

## 3. Avaliação
- **Segmentação:** IoU, precisão, sensibilidade, F1 contra referência independente.
- **Área e mudança:** erro de área; mapas de ganho/perda (net ≠ total de mudança).
- **Cadeia completa:** erro entre cota/volume estimados e observados (ex.: erro absoluto médio por data).
- **Generalização:** separar treino/validação/teste por cena, data ou local; sem recortes sobrepostos entre conjuntos; considerar nuvem, sombra, resolução, desalinhamento.
- **Sensibilidade (pré-requisito):** dA/dh da CAV × erro esperado da máscara. Se o erro de área for comparável à variação de área em toda a faixa operativa, a inversão área→cota não é informativa naquele reservatório.

## 4. Exemplo ilustrativo (HIPOTÉTICO — não é resultado do grupo)
| Indicador | Valor |
|---|---|
| Área inicial / final | 2,0 km² / 1,8 km² |
| Variação líquida | −0,2 km² (−10%) |
| Perda / ganho | 0,3 km² / 0,1 km² |
| Total que mudou de classe | 0,4 km² |

## 5. Limites
- Duas datas = diferença entre observações, não tendência.
- Imagem não mede vazão nem profundidade; volume depende da CAV (que pode estar desatualizada por assoreamento — verificar data de levantamento).
- Não atribuir variações à chuva ou à operação sem análise adicional; não afirmar segurança estrutural.
- Impacto esperado = benefício potencial sujeito a qualidade de dados e validação.

## 6. Checklist de dados (preencher ao acessar)
| Base | Fonte | Período | Formato | Chave/ID | Unidades | Licença/acesso | Data de acesso |
|---|---|---|---|---|---|---|---|
| Hidrológicos diários | | | | | | | |
| Fluviométricas | | | | | | | |
| Cadastro | | | | | | | |
| CAV | | | | | | | |
| Volume de espera | | | | | | | |
| Imagens | | | | | | | |
