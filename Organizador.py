# Importando as bibliotecas necessárias
import os
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno

# Função principal que vai executar o Script
def main():
    caminho = askdirectory(title="Selecione a pasta que será organizada:")
    lista_arquivos = os.listdir(caminho)

    # Definindo os tipos de arquivos que serão organizados (podendo facilmente adicionar mais tipos futuramente)
    locais = {
        "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
        "PDFs": [".pdf", ".html"],
        "Texto": [".txt", ".doc", ".docx"],
        "Winrar": [".rar", ".zip"]
    }

    # Um loop (For) que vai efetuar a organização enquanto o usuário quiser
    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
    
    # Função que pergunta ao usuário se ele quer continuar organizando outras pastas ou não
    def perguntar():
        answer = askyesno(title="Organizador de pastas", message="Arquivos organizados com sucesso!\nDeseja organizar outra pasta?")
        if answer:
            main()
    
    perguntar()

main()




        




