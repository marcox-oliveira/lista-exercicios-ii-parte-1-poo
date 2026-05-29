from midias import Podcast, TextoNarrado, Video
from plataforma import Plataforma
def main() -> None:
    plataforma = Plataforma("EduStream")
    print("\nAdicionando mídias à plataforma...")
    aula_python = Video(
        titulo="Introdução ao Python",
        duracao=45.0,
        resolucao="1080p",
    )
    podcast_ia = Podcast(
        titulo="IA no Cotidiano",
        duracao=30.0,
        apresentador="Prof. Carlos",
    )
    narrado_poo = TextoNarrado(
        titulo="Conceitos de POO",
        duracao=20.0,
        idioma="Português",
    )
    plataforma.adicionar_midia(aula_python)
    plataforma.adicionar_midia(podcast_ia)
    plataforma.adicionar_midia(narrado_poo)
    plataforma.listar_midias()
    plataforma.reproduzir_todas()
if __name__ == "__main__":
    main()
