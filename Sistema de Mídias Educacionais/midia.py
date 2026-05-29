from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Duração:", self.duracao, "minutos")

    @abstractmethod
    def reproduzir(self):
        pass
