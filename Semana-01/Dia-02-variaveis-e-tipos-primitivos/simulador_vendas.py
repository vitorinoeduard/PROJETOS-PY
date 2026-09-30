"""Simulador de vendas - versão 0.01 - Desenvolvido por Eduardo Vitorino"""

# Cabeçalho
print("==================================================")
print("CAIXA - TERCEIRA DIMENSÃO")
print("==================================================")

# Dados do Cabeçalho
nome_peca = input("Digite o nome da peça: ")
valor_unitario = float(input("Digite o valor unitário (R$): "))
quantidade = int(input("Digite a quantidade: "))
porcentagem_desconto = float(input("Digite o desconto (%): "))

# Dados matematicos variaveis
valor_bruto = valor_unitario * quantidade
valor_desconto = valor_bruto * (porcentagem_desconto / 100)
total_a_pagar = valor_bruto - valor_desconto
pagamento_aprovado = True

# Dados do Recibo Cliente
print("\n==================================================")
print("----RECIBO DO CLIENTE----")
print("==================================================")
print("Produto:", nome_peca)
print("Total bruto R$:", valor_bruto)
print("Desconto Aplicado R$:", valor_desconto)
print("Total a Pagar R$:", total_a_pagar)
print("Pagamento aprovado:", pagamento_aprovado)
print("==================================================")
