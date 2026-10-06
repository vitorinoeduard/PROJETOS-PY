"""Módulo de funções desenvolvido para treinar def/return e demais funções - Desenvolvido por Eduardo Vitorino - 0571072026"""

# CABECALHO
print("=====================================================")
print("MODULO DE FUNÇÕES - TERCEIRA DIMENSÃO".center(50))
print("=====================================================")

# DEFINIÇÃO DA FUNÇÃO
def aplicar_desconto(valor):

    if valor >= 500:
        return valor * 0.80  # 20% de desconto
    elif valor >= 250:
        return valor * 0.90  # 10% de desconto
    else:
        return valor

# ENTRADA
valor_compra = float(input("\nDigite o valor da compra: "))

valor_final = aplicar_desconto(valor_compra)

# SAIDA
print("=====================================================")
print(f"Total a pagar com desconto aplicado: R$ {valor_final:.2f}")
print("\n=====================================================")