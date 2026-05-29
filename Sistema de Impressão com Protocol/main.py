from itens import Boleto, Etiqueta, RelatorioSimples
from impressao import processar_impressao

boleto = Boleto("12345-6", 150.00)
etiqueta = Etiqueta("João Silva", "Rua das Flores, 42")
relatorio = RelatorioSimples("Vendas do Mês")

print("---")
processar_impressao(boleto)
print("---")
processar_impressao(etiqueta)
print("---")
processar_impressao(relatorio)
print("---")
