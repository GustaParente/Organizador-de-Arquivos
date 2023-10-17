import os
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno

def main():
    caminho = askdirectory(title="Selecione a pasta que será organizada:")

    lista_arquivos = os.listdir(caminho)

    locais = {
        "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
        "PDFs": [".pdf", ".html"],
        "Texto": [".txt", ".doc", ".docx"],
        "Winrar": [".rar", ".zip"]
    }

    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
    
    def perguntar():
        answer = askyesno(title="Organizador de pastas", message="Arquivos organizados com sucesso!\nDeseja organizar outra pasta?")
        if answer:
            main()
    
    perguntar()

main()




        




