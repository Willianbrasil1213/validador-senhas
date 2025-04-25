# Validador e Classificador Inteligente de Senhas

Este projeto é um validador inteligente que classifica senhas em quatro categorias com base na sua complexidade e comprimento. Ele também orienta o usuário sobre como criar senhas.

## Como funciona

O sistema classifica as senhas digitadas pelo usuário nas seguintes categorias:

### Fraca
- Contém **apenas letras** (maiúsculas ou minúsculas).
- Possui **até 5 caracteres**.

### Moderada
- De **6 a 7 caracteres**.
- Contém pelo menos:
  - 1 letra maiúscula
  - 1 letra minúscula
  - 1 número

### Forte
- De **8 a 9 caracteres**.
- Contém pelo menos:
  - 1 letra maiúscula
  - 1 letra minúscula
  - 1 número

### Muito Forte
- **Exatamente 10 caracteres**.
- Contém pelo menos:
  - 1 letra maiúscula
  - 1 letra minúscula
  - 1 número
  - 1 símbolo especial (`!@#$%^&*`)

### ❌ Inválida
- Qualquer senha que **não se encaixa nos critérios acima**.
