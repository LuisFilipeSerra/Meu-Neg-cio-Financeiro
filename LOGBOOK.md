#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** Definir um projeto que atendesse a uma necessidade real e organizar sua estrutura inicial para desenvolvimento em Python.
2. **O que implementei (commits / arquivos / links):** Escolhi o projeto Meu Negócio Financeiro, voltado para pequenos empreendedores. Criei o repositório no GitHub e os arquivos `main.py` e `README.md`. Repositório: https://github.com/LuisFilipeSerra/Meu-Neg-cio-Financeiro.
3. **Objeto(s) de conhecimento mobilizado(s):** Organização de projetos de software, versionamento de código com Git e GitHub e definição inicial de requisitos.
4. **Desvio ou erro encontrado + causa técnica:**Tive dificuldade para localizar os arquivos no VS Code porque a pasta inicialmente acessada não correspondia ao diretório em que o repositório havia sido clonado.
5. **Decisão de ajuste + fonte:**Após identificar que os arquivos estavam em um diretório diferente do esperado, localizei a pasta correta do repositório e abri o projeto no VS Code. Confirmei o ajuste verificando a presença dos arquivos `main.py` e `README.md`.
6. **Feedback recebido e o que mudei:** Recebi auxílio de Enzo Figueiredo durante a organização inicial do projeto, com orientações relacionadas à estrutura dos arquivos e ao desenvolvimento no VS Code. A partir desse apoio, consegui organizar o repositório e dar continuidade ao projeto.
7. **Próximo passo:** Trabalhar com variáveis, tipos de dados e operações aritméticas para representar receitas, despesas e saldo financeiro.
**Data do registro:** 14/11/2026 — preenchimento retrospectivo.
#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** Desenvolver uma estrutura inicial em Python para representar receitas, despesas e calcular o saldo financeiro de um pequeno negócio.
2. **O que implementei (commits / arquivos / links):** No arquivo `main.py`, criei as variáveis `total_receitas`, `total_despesas` e `saldo`. Utilizei a função `print()` para apresentar as informações financeiras no terminal. O código está disponível no repositório: https://github.com/LuisFilipeSerra/Meu-Neg-cio-Financeiro.
3. **Objeto(s) de conhecimento mobilizado(s):**  Variáveis, atribuição de valores, tipo de dado `float`, operadores aritméticos e saída de dados com a função `print()`.
4. **Desvio ou erro encontrado + causa técnica:** Inicialmente, o comando `python` não foi reconhecido pelo terminal do Windows, impedindo a execução do programa. A causa estava relacionada à disponibilidade do interpretador Python no ambiente.
5. **Decisão de ajuste + fonte:** Após verificar o ambiente, utilizei o gerenciador de instalação do Python e confirmei o funcionamento do interpretador com `py --version`. Em seguida, executei o programa utilizando `py main.py`, verificando a saída diretamente no terminal.
6. **Feedback recebido e o que mudei:** Após executar o código, confirmei que as variáveis e o cálculo do saldo apresentavam os resultados esperados. Mantive a estrutura inicial como base para as próximas funcionalidades.
7. **Próximo passo:** Implementar a entrada de valores pelo usuário e desenvolver operações que permitam registrar receitas e despesas.
**Data do registro:** 14/11/2026 — preenchimento retrospectivo.
    #### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** Aplicar operadores aritméticos para calcular o saldo financeiro de um pequeno negócio a partir das receitas e despesas informadas pelo usuário.
2. **O que implementei (commits / arquivos / links):** Atualizei o arquivo `main.py` para receber os valores de receitas e despesas com a função `input()`, converter os dados para `float` e calcular o saldo por meio da subtração. Executei um teste com R$ 3.000,00 de receitas e R$ 1.200,00 de despesas, obtendo o saldo correto de R$ 1.800,00.
3. **Objeto(s) de conhecimento mobilizado(s):** Operador aritmético de subtração (`-`), operador de atribuição (`=`), variáveis do tipo `float`, entrada e saída de dados e conversão de tipos. Os operadores relacionais e lógicos ainda não foram implementados.
4. **Desvio ou erro encontrado + causa técnica:** Não foram identificados erros durante o teste realizado. O programa executou corretamente o cálculo com os valores informados.
5. **Decisão de ajuste + fonte:**  Substituí os valores fixos pela entrada de dados com `input()` e utilizei `float()` para permitir cálculos com valores decimais. Confirmei o funcionamento por meio da execução no terminal do VS Code.
6. **Feedback recebido e o que mudei:** O teste confirmou que o cálculo do saldo estava correto. A principal melhoria foi permitir que o usuário informasse suas próprias receitas e despesas.
7. **Próximo passo:** Implementar estruturas condicionais para identificar se o saldo financeiro é positivo, negativo ou igual a zero.
**Data do registro:** 15/11/2026 — preenchimento retrospectivo.
#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** Implementar estruturas condicionais para identificar a situação financeira de um pequeno negócio com base no saldo calculado.
2. **O que implementei (commits / arquivos / links):** Atualizei o arquivo `main.py` utilizando as estruturas `if`, `elif` e `else` para classificar o saldo financeiro como positivo, negativo ou zerado. Realizei testes das três condições e confirmei que todas funcionaram corretamente  Repositório: https://github.com/LuisFilipeSerra/Meu-Neg-cio-Financeiro.
3. **Objeto(s) de conhecimento mobilizado(s):**  Estruturas condicionais `if`, `elif` e `else`, operadores relacionais (`>` e `<`), comparação de valores numéricos, variáveis e lógica de decisão.
4. **Desvio ou erro encontrado + causa técnica:**  Não foram identificados erros nos testes realizados. As três condições apresentaram os resultados esperados.
5. **Decisão de ajuste + fonte:** Acrescentei condições para comparar o saldo com zero e apresentar uma mensagem correspondente à situação financeira. Verifiquei o resultado por meio de testes executados no terminal do VS Code.
6. **Feedback recebido e o que mudei:** Os testes confirmaram o funcionamento das três condições. A implementação permitiu que o sistema apresentasse a situação financeira do negócio de acordo com o saldo calculado.
7. **Próximo passo:**  Desenvolver funcionalidades para registrar e consultar movimentações financeiras, ampliando os recursos do sistema.
**Data do registro:** 15/11/2026 — preenchimento retrospectivo.
### 🧩 CAMPO 01 — Instrumento de entrada
**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. Variáveis e tipos de dados: compreender como armazenar valores financeiros utilizando variáveis do tipo float.
2. Operadores aritméticos: realizar cálculos de receitas, despesas e saldo.
3. Estruturas condicionais: utilizar if, elif e else para identificar diferentes situações financeiras.


**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. Como impedir que o programa encerre quando alguém digitar letras em vez de números.
2. Como permitir que o usuário registre várias movimentações sem reiniciar o programa.
3. Como armazenar receitas e despesas para que não desapareçam ao fechar o sistema.
**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> Acho que o sistema ainda precisa de algumas melhorias, porque, por enquanto, ele só calcula o saldo e mostra se está positivo,negativo ou zerado. Para funcionar melhor, seria necessário permitir que o usuário registre seus gastos e ganhos, consiga consultar essas informações e fazer alterações quando precisar.
### 🧩 CAMPO 02 — Aprofundamento pós-aula

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** Documentação oficial do Python — Erros e exceções.
  https://docs.python.org/pt-br/3/tutorial/errors.html — **Contribuição:**  Explica como utilizar `try` e `except` para tratar erros. Isso pode ajudar a impedir que o sistema seja encerrado quando o usuário digitar letras no lugar de números.
- **Referência 2:** Documentação oficial do Python — Módulo JSON.
  **Contribuição:** Apresenta formas de salvar e carregar informações em arquivos JSON. Esse recurso pode ser utilizado para armazenar as movimentações financeiras e recuperá-las quando o programa for aberto novamente

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> Depois de pesquisar, percebi que o sistema precisa de mais do que apenas cadastrar e consultar informações. Também é importante evitar erros quando o usuário digita valores inválidos e garantir que os dados fiquem salvos. Por isso, pretendo utilizar tratamento de exceções e armazenamento em arquivos JSON para deixar o programa mais completo e confiável.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
|Horas de desenvolvimento e estudo | 12 horas | Tempo estimado para implementar o cadastro de movimentações, tratamento de erros e armazenamento de dados. |
|Arquivos do projeto | 3 arquivos | `main.py` para o programa, `dados.json` para armazenar movimentações e `README.md` para documentar o projeto. |
|Casos de teste | 6 testes | Verificar saldos positivos, negativos e zerados, entradas inválidas, salvamento e recuperação dos dados.