from midias import Video, Podcast, TextoNarrado
from plataforma import Plataforma

plataforma = Plataforma("EduStream")

video = Video("Introdução ao Python", 45, "1080p")
podcast = Podcast("IA no Cotidiano", 30, "Prof. Alternei")
texto = TextoNarrado("Conceitos de POO", 20, "Português")

plataforma.adicionar_midia(video)
plataforma.adicionar_midia(podcast)
plataforma.adicionar_midia(texto)

plataforma.listar_midias()

plataforma.reproduzir_todas()
