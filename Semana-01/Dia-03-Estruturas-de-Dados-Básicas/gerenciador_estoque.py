"""Sistema de Gerenciamento de Estoque, Usando atributos basicos de estruturas de dados em Python.
Este script demonstra o uso de tuplas, dicionários, listas e conjuntos para gerenciar estoque. - Versão 1.0 - Desenvolvido por: Eduardo Vitorino - Data: 01/10/2026"""

# Cabeçalho do gerenciador_estoque
print("=================================================")
print("SISTEMA DE ESTOQUE - TERCEIRA DIMENSÃO".center(50))
print("=================================================")

# Dados processados
categoria_loja = ("Jeans", "Camisas", "Acessórios")

produto_atual = {
    "nome": "Camisa Sallo",
    "preco": 129.90,
    "estoque": 20,
}

desconto_aplicado = produto_atual.get("desconto", 0.0)

carrinho = []
carrinho.append("Camisa Sallo")
carrinho.append("Cinto")

historico_cliques = ["Jeans", "Camisas", "Acessórios", "Camisas", "Acessórios", "Jeans", "Camisas"]
buscas_unicas = set(historico_cliques)

# Saida de dados
print("Categoria da loja:", categoria_loja)

print("\n---------DETALHES DO PRODUTO----------")
print("Produto:", produto_atual["nome"])
print("Preço:R$", produto_atual["preco"])
print("Estoque:", produto_atual["estoque"], "unidades")
print("Desconto aplicado:", desconto_aplicado)

print("\n---------CARRINHO DO CLIENTE----------")
print("Itens no carrinho:", carrinho)

print("\n---------ANÁLISE DE BUSCAS----------")
print("Categorias mais visitadas:", buscas_unicas)