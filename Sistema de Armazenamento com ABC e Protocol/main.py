from armazenadores import ArmazenadorArquivo, ArmazenadorBanco
from nuvem import ArmazenadorNuvem
from funcoes import executar_salvamento_formal, executar_salvamento_flexivel

arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

print("--- Parte A: ABC ---")
executar_salvamento_formal(arquivo, "dados do usuario")
executar_salvamento_formal(banco, "dados do usuario")

print("--- Parte B: Protocol ---")
executar_salvamento_flexivel(arquivo, "dados do usuario")
executar_salvamento_flexivel(banco, "dados do usuario")
executar_salvamento_flexivel(nuvem, "dados do usuario")
