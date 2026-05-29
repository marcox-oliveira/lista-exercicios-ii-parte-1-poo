from armazenador import Armazenador
class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado):
        print("Salvando em arquivo local:", dado)

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        print("Salvando no banco de dados:", dado)
