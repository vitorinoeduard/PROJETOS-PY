""" Sistema de Painel de Afiliados do grupo Black Wolf, usando estruturas de dados básicas como tuplas, dicionários e conjuntos. versão 1.0 - desenvolvido por: Eduardo Vitorino - 01/10/2026"""

# Cabeçalho Painel Afiliados
print("=======================================")
print("PAINEL DE AFLIADOS - BLACK WOLF".center(40))
print("=======================================")

# Lógica do sistema
plataformas_parceira = ("Amazon", "mercado livre")

campanha_atual = {
    "nome": "Black Wolf",
    "publico": "Masculino",
    "comissão": 8.5,
}
cupom_reserva = campanha_atual.get("cupom ativo", "BlackWolf10")

cliques_por_nicho = ["fitness", "tecnologia", "fitness", "vestuário", "tecnologia", "tecnologia"]
cliques_por_nicho.append("vestuário")

nichos_unicos = set(cliques_por_nicho)

# Saida de dados
print("\n------CONFIGURAÇÃO DE CAMPANHA------")
print("Plataformas Autorizadas:", plataformas_parceira)
print("Campanha Atual:", campanha_atual["nome"], "- Especial de Natal")
print("Público-Alvo:", campanha_atual["publico"])
print("Comissão:", campanha_atual["comissão"], "%")
print("Cupom Aplicado:", cupom_reserva)
print("\n------RELATÓRIO DE TRÁFEGO------")
print("Histórico de Cliques:", cliques_por_nicho)
print("Nichos Únicos com engajamento:", nichos_unicos)
print("=======================================")