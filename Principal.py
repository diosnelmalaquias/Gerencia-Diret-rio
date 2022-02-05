import datetime
import cv2
import os
import shutil

from cv2 import split

#Leitura da imagem
foto = cv2.imread('img/2.jpg')

# tratamento de data e tempo
def data_hora():
    tempo = datetime.datetime.now()
    dia = tempo.day
    mes = tempo.month
    ano = tempo.year
    hora = tempo.hour
    minuto = tempo.minute
    segundo = tempo.second

    return dia, mes, ano, hora, minuto, segundo

#metodo para criar pasta
def cria_diretorio(pasta):
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    return dir

tempo = data_hora()

#cria diretorio principal para historico das imagens
nome_dir_principal = "data"

#nome diretorio para salvar as imagens
diretorio_data = cria_diretorio(nome_dir_principal)

#nome da pasta para imagens
nome_dir_img = f"{tempo[0]}-{tempo[1]}-{tempo[2]}"
diretorio_img = cria_diretorio(f'{nome_dir_principal}/{nome_dir_img}')

#nome das imagens salvas
nome_img = f"{tempo[3]}_{tempo[4]}_{tempo[5]}"
diretorio_img = cria_diretorio(f'{nome_dir_principal}/{nome_dir_img}')

def salva_img(foto):    
    #cria nome da imagem
    imagem = f"{nome_dir_principal}/{nome_dir_img}/{nome_img}.png"

    #salva imagem com formato jpg
    cv2.imwrite(imagem, foto )
    return imagem


if os.path.exists(f"{nome_dir_principal}/{nome_dir_img}"):    
    imagem_salva = salva_img(foto)

#limpa arquivos de fotos deletando arquivos mais antigos
if len(os.listdir(nome_dir_principal))>=4:
    #lista menor data das pastas
    menor_dir = min(os.listdir(nome_dir_principal))
    
    #deleta arquivo mais antigo com todas as fotos
    shutil.rmtree(f'{nome_dir_principal}/{menor_dir}')







        


    







    
    
        

