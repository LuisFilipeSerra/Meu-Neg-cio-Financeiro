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
