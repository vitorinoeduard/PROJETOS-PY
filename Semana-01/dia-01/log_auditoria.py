"""Registro de auditoria servidor - Versão 0.01 beta - Desenvolvido por Eduardo Vitorino"""

print("======================================================================")
print("REGISTRO DE AUDITORIA DE SERVIDOR")
print("======================================================================")
print("Diretório de gravação:")
print("/var/log/sistema/auditoria_2026.log")

# DADOS SERVIDOR
print("\n[EVENTO 01]", "AUTENTICAÇÃO", "UTILIZADOR: Admin", sep=" :: ", end=" -> ")
print("[AUTORIZADO]")
print("[EVENTO 02]", "FIREWALL", "Porta: 443", sep=" :: ", end=" -> ")
print("[BLINDADA]")
print("[EVENTO 03]", "BACKUP", "Base de Dados", sep=" :: ", end=" -> ")
print("[SINCRONIZADO]")
print("======================================================================")

# RESULTADO AUDITORIA
print("\nID", "MÓDULO\t", "ESTADO", sep="\t|")
print("01", "Core_Engine", "Ativo", sep="\t|")
print("02", "Security_Lab", "Ativo", sep="\t|")
