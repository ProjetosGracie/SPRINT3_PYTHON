# Sistema de Gerenciamento de Recarga de Veículos Elétricos

Sistema desenvolvido em **Python** para simular o gerenciamento de um posto de recarga de veículos elétricos, permitindo controlar veículos conectados, distribuir potência, estimar o tempo de carregamento, calcular valores de cobrança e analisar informações da operação.

O projeto foi desenvolvido com foco na aplicação prática de conceitos fundamentais de **Ciência da Computação e Programação**, como funções, listas, dicionários, estruturas condicionais, estruturas de repetição, tratamento de exceções e manipulação de dados.

---

## Sobre o Projeto

O sistema simula a operação de um posto de carregamento que possui uma **limitação total de potência de 150 kW**.

A aplicação permite cadastrar veículos informando dados como:

* Placa do veículo;
* Capacidade da bateria em kWh;
* Porcentagem atual da bateria;
* Horário de conexão.

A partir dessas informações, o sistema realiza cálculos e disponibiliza funcionalidades para acompanhamento da operação.

O projeto também possui um módulo denominado **IA**, responsável por apresentar uma sugestão de horário mais econômico e realizar uma auditoria da distribuição de potência entre os veículos conectados.

---

## Funcionalidades

### 1. Conectar veículo

Permite registrar um novo veículo no posto.

Durante o cadastro são solicitados:

* Placa;
* Capacidade da bateria;
* Porcentagem da bateria;
* Horário de conexão.

O sistema também realiza validações para evitar valores inválidos, como porcentagem de bateria fora do intervalo de 0 a 100 e horários inexistentes.

Além disso, veículos com a mesma placa não podem ser cadastrados novamente.

---

### 2. Controle de potência

O sistema calcula uma distribuição de potência entre os veículos conectados considerando o limite de **150 kW do posto**.

A potência atribuída aos veículos é atualizada de acordo com a quantidade de veículos presentes na sessão.

Essa funcionalidade permite simular um cenário de **gerenciamento de demanda**, evitando que a potência total disponibilizada ultrapasse o limite definido para o posto.

---

### 3. Consulta de registros

Exibe os dados dos veículos atualmente conectados.

Entre as informações apresentadas estão:

* Placa;
* Capacidade da bateria;
* Porcentagem da bateria;
* Potência recebida;
* Horário de início;
* Horário final previsto;
* Valor a pagar, quando calculado.

---

### 4. Remoção de veículo

Permite remover um veículo da sessão informando sua placa.

Caso a placa não esteja registrada, o sistema informa que o veículo não foi encontrado.

---

### 5. Cálculo do tempo de carregamento

O sistema estima o tempo necessário para o carregamento utilizando a capacidade da bateria e a potência disponibilizada ao veículo.

A estimativa é utilizada para calcular o **horário final previsto de carregamento**.

O sistema também realiza os ajustes necessários quando:

* Os minutos ultrapassam 60;
* O horário ultrapassa 24 horas.

---

### 6. Sistema de tarifação

O valor da recarga é calculado de acordo com o horário de conexão do veículo.

As tarifas utilizadas pelo sistema são:

| Faixa de horário |      Tarifa |
| ---------------- | ----------: |
| 00h – 06h        | R$ 0,70/kWh |
| 06h – 12h        | R$ 1,20/kWh |
| 12h – 14h        | R$ 1,80/kWh |
| 14h – 18h        | R$ 1,30/kWh |
| 18h – 21h        | R$ 1,80/kWh |
| 21h – 24h        | R$ 1,30/kWh |

Com essas informações, o sistema calcula o valor correspondente ao carregamento e registra os valores para posterior consulta do faturamento.

---

### 7. Faturamento

A funcionalidade de faturamento apresenta os valores associados aos carregamentos registrados e calcula o **faturamento total do posto**.

Isso permite acompanhar de forma simples a receita gerada pelas sessões de carregamento.

---

## Módulo de IA

O projeto possui um módulo chamado **"IA (sugestão de horário + auditoria)"**.

Atualmente, esse módulo é composto por duas funcionalidades principais:

### Sugestão de horário econômico

O sistema compara as tarifas cadastradas para cada período do dia e identifica a faixa com menor custo.

A comparação é realizada percorrendo as tarifas e armazenando a menor encontrada.

Atualmente, o período mais econômico definido pelo sistema é:

**Madrugada — 00h às 06h — R$ 0,70/kWh**

A funcionalidade pode servir como base para futuras implementações de modelos de previsão ou otimização mais avançados.

### Auditoria da distribuição

O sistema compara os veículos conectados entre si, analisando:

* Diferença entre as porcentagens de bateria;
* Diferença entre as potências recebidas.

Quando dois veículos possuem níveis de bateria semelhantes, mas recebem uma diferença significativa de potência, o sistema gera um alerta.

Essa funcionalidade busca identificar possíveis inconsistências na distribuição de energia.

---

## Tecnologias utilizadas

* **Python 3**
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`for`, `while`)
* Listas
* Dicionários
* Funções
* `try/except` para tratamento de erros
* Entrada e saída de dados pelo terminal
* Operações matemáticas
* Manipulação de strings

---

## Estrutura do projeto

O projeto atualmente está concentrado em um único arquivo Python:

```text
.
├── Sprint3(1).py
└── README.md
```

O arquivo principal contém o menu da aplicação e as funções responsáveis pelo gerenciamento do sistema.

Principais funções:

```text
menu()
conectar_veiculo()
potencia_posto()
dados()
remover_veiculo()
calcular_tempo()
pagamento()
faturamento_total()
sugerir_horario_economico()
auditoria_distribuicao()
inteligencia_artificial()
```

---

## Como executar

### 1. Pré-requisitos

É necessário ter o **Python 3** instalado no computador.

Para verificar a instalação:

```bash
python3 --version
```

### 2. Executar o projeto

No terminal, acesse a pasta onde o arquivo está localizado e execute:

```bash
python3 "Sprint3(1).py"
```

O sistema será iniciado diretamente pelo terminal.

---

## Fluxo de utilização

Após iniciar o programa, será apresentado um menu:

```text
===== GERENCIAMENTO ======

1 - Conectar veículo
2 - Potencia
3 - Registros
4 - Remover veículo
5 - Faturamento
6 - IA (sugestão de horário + auditoria)
7 - Sair
```

O usuário pode selecionar a funcionalidade desejada digitando o número correspondente.

O sistema também possui tratamento de entrada inválida, evitando que o programa seja encerrado caso o usuário informe um valor que não seja um número inteiro.

---

## Conceitos de Computação aplicados

Este projeto foi desenvolvido como uma aplicação prática de conceitos estudados durante a formação em **Ciência da Computação**.

Entre os principais conceitos utilizados estão:

### Estruturas de dados

As informações dos veículos são armazenadas utilizando **dicionários**, enquanto a sessão de veículos e o histórico de faturamento utilizam **listas**.

Exemplo:

```python
veiculo_conectado = {
    "placa": placa,
    "potencia (kW)": potencia_padrao,
    "Potencia da bateria (kWh)": bateria_potencia,
    "Porcentagem": bateria_porcentagem,
    "horario inicio": horario_inicial
}
```

### Modularização

As funcionalidades foram separadas em diferentes funções, facilitando a organização e manutenção do código.

### Validação de dados

O sistema utiliza condições e tratamento de exceções para verificar entradas fornecidas pelo usuário.

### Algoritmos

O projeto utiliza algoritmos para:

* Distribuição de potência;
* Cálculo de tempo;
* Definição de tarifas;
* Identificação do horário mais econômico;
* Auditoria entre veículos.

---

## Possíveis melhorias futuras

Como evolução do projeto, algumas funcionalidades podem ser implementadas:

* Separação do projeto em múltiplos módulos;
* Persistência dos dados em arquivos ou banco de dados;
* Interface gráfica ou aplicação web;
* Sistema de autenticação;
* Histórico de carregamentos;
* Relatórios de consumo e faturamento;
* Integração com dados reais de carregadores;
* Implementação de modelos de Machine Learning para previsão de demanda;
* Otimização automática da distribuição de potência;
* Utilização de APIs para integração com sistemas externos.

Essas melhorias permitiriam transformar a simulação atual em uma aplicação mais próxima de um sistema real de gerenciamento de infraestrutura de recarga.

---

## Objetivo acadêmico

O principal objetivo do projeto é aplicar conhecimentos de programação na construção de uma solução voltada para um problema real: o **gerenciamento de energia em estações de recarga de veículos elétricos**.

Além da implementação das funcionalidades, o projeto busca desenvolver habilidades de **raciocínio lógico, organização de código, tratamento de erros e resolução de problemas utilizando programação**.

---

## Autor

**Conrado Gracie**

Estudante de **Ciência da Computação**

Projeto acadêmico desenvolvido em Python.

---
