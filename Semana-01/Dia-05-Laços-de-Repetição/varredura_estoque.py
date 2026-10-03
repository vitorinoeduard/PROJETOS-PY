""" Sistema desenvolvido para auditoria de estoque e fechamento total de caixa, usando estrutura de laços - versao 2.0 - Desenvolvido por Eduardo Vitorino - 03/10/2026"""

# CABEÇALHO
print("==================================================")
print("AUDITORIA DE ESTOQUE - TERCEIRA DIMENSÃO".center(50))
print("==================================================")

# DADOS MATEMATICOS
vendas_dia = [159.90, 69.90, 299.90, 89.90, 129.90]
estoque = [
    {"nome": "Calça Jeans Patogê", "quantidade": 8},
    {"nome": "Camiseta Sallo", "quantidade": 2},
    {"nome": "Cinto de Couro", "quantidade": 0},
    {"nome": "Bermuda Nicoboco", "quantidade": 5}
]

total_vendas = 0.0
for vendas in vendas_dia:
    total_vendas += vendas

# DADOS SAIDA RELATORIO
print("\n", "---------RELATÓRIO DE ESTOQUE---------".center(50))

for item in estoque:
    nome = item["nome"]
    qtd = item["quantidade"]

    if qtd == 0:
        status = f"[CRITICO] {nome} (ESGOTADO)"
    elif qtd <= 3:
        status = f"[ESTOQUE BAIXO] {nome} ({qtd} unidades)"
    else:
        status = f"[OK] {nome} ({qtd} unidades)"
        
    print(status)

# DADOS TOTAL
print("\n", "---------FECHAMENTO DE CAIXA---------".center(50))
print("Total vendido no dia: R$", total_vendas)   
