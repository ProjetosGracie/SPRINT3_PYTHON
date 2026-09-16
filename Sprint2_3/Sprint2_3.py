# VARIAVEIS GLOBAIS
sessao      = []
faturamento_lista = []
potencia_padrao = 44.0
limite_posto    = 150.0

# MENU - ESCOLHER A OPCAO QUE DESEJA 
def menu():
    while True:
        print("\n===== GERENCIAMENTO ======")
        print("1 - Conectar veículo")
        print("2 - Potencia ")
        print("3 - Registros")
        print("4 - Remover veículo")
        print("5 - Faturamento")
        print("6 - IA (sugestão de horário + auditoria)")  
        print("7 - Sair")

        # CASO DIGITE ALGO ALEM DE UM NUMERO INTEIRO, DAR COMO OPCAO INVALIDA
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nOpção inválida. Digite um número.\n")
            continue

        if opcao == 1:
            conectar_veiculo()
        elif opcao == 2:
            potencia_posto()
        elif opcao == 3:
            dados()
        elif opcao == 4:
            remover_veiculo()
        elif opcao == 5:
            faturamento_total()
        elif opcao == 6:
            inteligencia_artificial()
        elif opcao == 7:
            print("Saindo do sistema...")
            break
        else:
            print("\nOpção inválida. Digite entre 1 a 7.\n")

# CONECTAR_VEICULO - CONECTA O VEICULO QUE ENTROU NO POSTO
# pergunta a potencia da bateria, porcentagem da bateria, horario que conectou 
def conectar_veiculo():

    placa = input("Informe a placa do veículo: ").upper()

    try:
     bateria_potencia = float(input("Informe a capacidade da bateria (kWh): "))
     bateria_porcentagem = float(input("Informe a porcentagem de carga da bateria (0 a 100): "))

     # Transforma a string em um numero int, para podermos fazer os calculos 
     horario_inicial = input("Informe o horário de conexão (HH:MM): ")
     horas, minutos = map(int, horario_inicial.split(":"))

     if bateria_porcentagem < 0 or bateria_porcentagem > 100:
        print("Valor inválido para a porcentagem de carga da bateria (deve estar entre 0 e 100).")
        return
     
     if bateria_potencia < 0 or bateria_potencia > 100:
        print("Valor inválido para a capacidade da bateria (deve estar entre 0 e 100).")
        return

     if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
       print("Valor inválido para o horário de conexão.")
       return  
     
    except ValueError:
        print("Valor inválido. Por favor, informe um número.")
        return
    
    if placa in [v["placa"] for v in sessao]:
        print("Veículo já conectado.\n")
    
    else:
        veiculo_conectado = {"placa": placa, "potencia (kW)": potencia_padrao,"Potencia da bateria (kWh)":bateria_potencia,"Porcentagem":bateria_porcentagem, "horario inicio": horario_inicial}
        sessao.append(veiculo_conectado) # --> adiciona o carro na lista de sessao
        print(f" ===== VEICULO {placa} CONECTADO =====\n")

        # CORREÇÃO: chama as duas funções passando apenas o veículo recém-conectado,
        # em vez de reprocessar todos os veículos já existentes na sessão.
        calcular_tempo(veiculo_conectado)
        pagamento(veiculo_conectado)


# POTENCIA_POSTO - INFORMA A POTENCIA QUE OS CARROS ESTAO UTILIZANDO E INFORMA QUANTOS CARROS ESTAO CONECTADOS 
def potencia_posto():
    n = 0
    potencia_calculada = limite_posto / (len(sessao) + 0.4)

    if not sessao:
        print("Nenhum veículo conectado.")
        return
    
    for veiculo in sessao:
        n += 1
        veiculo["potencia (kW)"] = potencia_calculada
        print(f"\n====== Registro {n} ======")
        print(f"Veículo: {veiculo['placa']}\nPotencia: {potencia_calculada:.2f} kW.")
        print("===========================\n")

    print(f"Total de veículo(s) conectado(s): {len(sessao)}\nPotencia que o(s) veiculo(s) recebeu(ao): {potencia_calculada:.2f} kW.\n")

# DADOS - DADOS DE CADA CARRO REGISTRADO, INFORMANDO A PLACA, POTENCIA DA BATERIA, POTENCIA UTILIZADA, PORCENTAGEM DA BATERIA, HORARIO DE INICIO, HORARIO FINAL, 
def dados():
    if not sessao:
        print("Nenhum veículo conectado.")
        return

    n = 1
    for veiculo in sessao:
        print(f"\n===== DADOS {n} =====")
        n += 1
        for nome, valor in veiculo.items():
            if isinstance(valor, (int, float)):
                print(f"{nome} - {valor:.2f}")
            else:
                print(f"{nome} - {valor}")
        print("=======================\n")

# REMOVER_VEICULO - REMOVER O VEICULO QUE ACABOU DE CARREGAR 
def remover_veiculo():
    if not sessao:
        print("Nenhum veículo conectado.")
        return
    
    placa_remover = input("Informe a placa do veículo a ser removido: ").upper()
    for veiculo in sessao:
            if veiculo["placa"] == placa_remover:
                sessao.remove(veiculo)
                print(f"Veículo {placa_remover} removido com sucesso.\n")
                return
            
    print(f"Veículo {placa_remover} não encontrado.\n")

# CALCULAR_TEMPO - CALCULA O TEMPO TOTAL DE UM ÚNICO VEÍCULO
def calcular_tempo(veiculo):
    horario_inicial = veiculo["horario inicio"]

    # Calcula o tempo de carregamento em horas
    tempo = veiculo["Potencia da bateria (kWh)"] / veiculo["potencia (kW)"]

    # Separa o horário inicial
    horas, minutos = map(int, horario_inicial.split(":"))

    # Separa horas e minutos do tempo de carregamento
    tempo_horas = int(tempo)
    tempo_minutos = int((tempo - tempo_horas) * 60)

    # Soma o tempo ao horário inicial
    fim_horas = horas + tempo_horas
    fim_minutos = minutos + tempo_minutos

    # Corrige quando os minutos passam de 60
    if fim_minutos >= 60:
        fim_horas += fim_minutos // 60
        fim_minutos = fim_minutos % 60

    # Corrige quando passa de 24 horas
    fim_horas = fim_horas % 24

    # Monta o horário final
    horario_termino = f"{fim_horas:02d}:{fim_minutos:02d}"

    # Salva os resultados
    veiculo["horario final previsto"] = horario_termino
    veiculo["tempo de carregamento"] = tempo

# PAGAMENTO - CALCULA O QUANTO A PESSOA TEM QUE PAGAR E FAZ AS REGRAS
def pagamento(veiculo):

    # Separa hora e minuto
    horas, minutos = map(int, veiculo["horario inicio"].split(":"))

    # MADRUGADA (00h-06h)
    if 0 <= horas < 6:
        tarifa = 0.70

    # MANHÃ (06h-12h)
    elif 6 <= horas < 12:
        tarifa = 1.20

    # PICO ALMOÇO (12h-14h)
    elif 12 <= horas < 14:
        tarifa = 1.80

    # TARDE (14h-18h)
    elif 14 <= horas < 18:
        tarifa = 1.30

    # PICO NOITE (18h-21h)
    elif 18 <= horas < 21:
        tarifa = 1.80

    # NOITE (21h-24h)
    else:
        tarifa = 1.30

  
    energia_consumida = (veiculo['Potencia da bateria (kWh)']*(100 - veiculo["Porcentagem"]))/100
    valor_pagar = energia_consumida*tarifa*veiculo['tempo de carregamento']
    veiculo['valor a pagar'] = valor_pagar
    faturamento_lista.append(veiculo)

# FATURAMENTO_TOTAL - CALCULA O FATURAMENTO TOTAL DO POSTO      
def faturamento_total():
    if not faturamento_lista:
        print("Nenhum carregamento registrado ainda.")
        return

    faturamento = 0
    n = 0
    print("\n======= CALCULANDO FATURAMENTO =======")
    for veiculo in faturamento_lista:
        faturamento += veiculo['valor a pagar']
        n += 1
        print(f"Faturamento do {n}º carregamento ({veiculo['placa']}): R$ {veiculo['valor a pagar']:.2f} ...")
    print("======================================\n")

    print("====== CALCULO CONCLUIDO ======")
    print(f"Faturamento total: R$ {faturamento:.2f}\n")

#SUGERIR_HORARIO_ECONOMICO - AQUI SUGERE O HORARIO MAIS ECONOMICO 
def sugerir_horario_economico():
    tarifas_por_faixa = {
        "Madrugada (00h-06h)": 0.70,
        "Manhã (06h-12h)": 1.20,
        "Pico almoço (12h-14h)": 1.80,
        "Tarde (14h-18h)": 1.30,
        "Pico noite (18h-21h)": 1.80,
        "Noite (21h-24h)": 1.30,
    }

    print("\n[Sugestão de horário] Comparando as tarifas de cada faixa:")

    # Percorre o dicionário manualmente pra achar a menor tarifa (sem usar min()),
    # mostrando cada comparação pra ficar visível o que está acontecendo.
    menor_tarifa = None
    faixa_mais_barata = None
    for faixa, tarifa in tarifas_por_faixa.items():
        print(f" - {faixa}: R$ {tarifa:.2f}/kWh")

        if menor_tarifa is None or tarifa < menor_tarifa:
            menor_tarifa = tarifa
            faixa_mais_barata = faixa

    print(f"Faixa mais econômica: '{faixa_mais_barata}' (R$ {menor_tarifa:.2f}/kWh). Priorize conectar veículos nesse período.")

# AUDITORIA_DISTRIBUICAO - COMPARA A DISTRIBUICAO DE POTENCIA ENTRE OS VEICULOS 
def auditoria_distribuicao():

    print("\n[Auditoria] Verificando distribuição de potência entre veículos...")
    
    encontrou_alerta = False  
    for indice_atual in range(len(sessao)):
        for indice_comparado in range(indice_atual + 1, len(sessao)):
            veiculo_atual = sessao[indice_atual]
            veiculo_comparado = sessao[indice_comparado]
            diferenca_bateria = veiculo_atual["Porcentagem"] - veiculo_comparado["Porcentagem"]

            if diferenca_bateria < 0:
                diferenca_bateria = -diferenca_bateria

            # Mesma ideia pra diferença de potência recebida por cada veículo.
            diferenca_potencia = veiculo_atual["potencia (kW)"] - veiculo_comparado["potencia (kW)"]

            if diferenca_potencia < 0:
                diferenca_potencia = -diferenca_potencia

            print(f" - Comparando {veiculo_atual['placa']} ({veiculo_atual['Porcentagem']}% de bateria) com {veiculo_comparado['placa']} ({veiculo_comparado['Porcentagem']}% de bateria)\nDiferença de bateria: {diferenca_bateria:.1f} pontos\nDiferença de potência: {diferenca_potencia:.2f} kW")

            if diferenca_bateria <= 10 and diferenca_potencia > 5:
                print(f" === ALERTA: bateria parecida, mas potência bem diferente entre {veiculo_atual['placa']} e {veiculo_comparado['placa']} ===")
                encontrou_alerta = True

    if not encontrou_alerta:
        print("Nenhuma inconsistência encontrada na distribuição atual.")


# INTELIGENCIA_ARTIFICIAL - ENGLOBA AS DUAS FUNCOES ACIMA 
def inteligencia_artificial():
    if not sessao:
        print("Nenhum veículo conectado.")
        return

    print("\n===== MÓDULO DE IA: SUGESTÃO E AUDITORIA =====")
    sugerir_horario_economico()
    auditoria_distribuicao()
    print("================================================\n")

menu()