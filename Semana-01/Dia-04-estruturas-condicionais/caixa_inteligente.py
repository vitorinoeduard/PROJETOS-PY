"""Caixa Automático - Terceira Dimensão - Sistema de gestão de caixa para calculo de desconto baseado no valor da compra usando estrturas condicionais- versão 0.01 - Desenvolvido por Eduardo Vitorino - 02/10/2026"""

# CABEÇALHO
print("==================================================")
print("CAIXA AUTOMÁTICO - TERCEIRA DIMENSÃO".center(50))
print("==================================================")

# ENTRADA DE DADOS CABEÇALHO
nome_cliente = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor total da compra: "))

# VARIÁVEIS MATEMÁTICAS
valor_desconto = 0.0

if valor_compra >= 500:
    valor_desconto = valor_compra * 0.20
    print("Desconto aplicado: R$", valor_desconto, "| CLIENTE OURO 20% OFF")
elif valor_compra >= 250:
    valor_desconto = valor_compra * 0.10
    print("Desconto aplicado: R$", valor_desconto, "| CLIENTE PRATA 10% OFF")
else:
    valor_desconto = 0.0
    print("Desconto não aplicado")
    

# SAIDA DE DADOS RECIBO 
print("\n==================================================")
print("RECIBO DO CLIENTE".center(50))
print("==================================================")
print("Cliente:", nome_cliente)
print("Valor da compra: R$", valor_compra)
print("Desconto aplicado: R$", valor_desconto)  
print("Total a pagar: R$", valor_compra - valor_desconto)

if valor_compra < 250:
    valor_faltante = 250 - valor_compra
    print("* Dica: Faltam apenas R$", valor_faltante, "para ganhar 10% de desconto. Que tal adicionar uma peça ao carrinho?")

