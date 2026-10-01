"""Calculadora de treino para uso fitness. Este programa permite fazer o resumo diario de gasto calorico, com base no peso do usuario, tempo de treino e marca a quantidade ingerida de agua. - Versão 1.0 - desenvolvido por: Eduardo Vitorino 30/09/2026 """
# Cabeçalho 
print("==================================================")
print("DIÁRIO DE TREINO E HIPERTROFIA".center(50))
print("==================================================")

# Dados do Cabeçalho
peso_atual = float(input("Digite seu peso atual (kg): "))
tempo_treino = int(input("Digite aqui o tempo de treino em minutos: "))
consumo_agua = float(input("Digite a quantidade de agua ingerida em litros: "))

# Dados matematicos variaveis
gasto_calorico = tempo_treino * 6
meta_diaria = 4.0
agua_restante = meta_diaria - consumo_agua
meta_agua_batida = consumo_agua >= 4.0 


# Dados de saida
print("\n==================================================")
print("RESUMO DO DIA".center(50))
print("==================================================")
print("Peso atual (kg):", peso_atual)
print("Gasto Calórico estimado:", gasto_calorico, "Kcal")
print("Meta de Água diaria (4.0L) batida?", meta_agua_batida)
print("Falta beber:", agua_restante, "L para a meta.")
print("==================================================")
