"""Computador de bordo fiat - Sistema simula um cumputador de bordo automotivo, medindo o nivel de combustivel e temperatura de motor! Versão 0.01 - Desenvolvido por Eduardo Vitorino - 02/10/2026"""

# Cabeçalho
print("==================================================")
print("COMPUTADOR DE BORDO - FIAT PALIO 1996".center(50))
print("==================================================")

# Dados do Cabeçalho
nivel_combustivel = float(input("Nível de combustível (L): "))
nivel_temperatura = int(input("Nível de temperatura (°C): "))

# Dados matematicos
if nivel_combustivel >= 15:
    status_tanque = "Nivel Seguro"
elif nivel_combustivel >= 5:
    status_tanque = "Aviso: Entrando na Reserva"
else:
    status_tanque = "Alerta critico: Abasteça imediatamente"

if nivel_temperatura >= 95:
    status_motor = "Perigo: Superaquecimento"
else:
    status_motor = "Temperatura normal"

# Saída de dados
print("\n==================================================")
print("DIAGNÓSTICO DO VEÍCULO".center(50))
print("==================================================")
print("\nStatus do tanque:", status_tanque)
print("Status temperatura", status_motor)
