class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia):
        self.midias.append(midia)

    def listar_midias(self):
        print("Mídias da plataforma", self.nome)
        for midia in self.midias:
            midia.mostrar_info()
            print("---")

    def reproduzir_todas(self):
        print("Reproduzindo todas as mídias:")
        for midia in self.midias:
            midia.reproduzir()
