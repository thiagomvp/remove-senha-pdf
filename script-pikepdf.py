import pikepdf 
import os


#  diretório dos arquivos
path = 'C:\\Users\\usuario\\Documents\\Internet\\' 

#  senha dos arquivos
senha = 'senha'

#  função remover senha do pdf
def removeSenha(full_path):
    pdf = pikepdf.Pdf.open(full_path, password=senha, allow_overwriting_input=True)
    pdf.save()
    pdf.close()

#  lista arquivos do diretório e executa a função para cada arquivo
for pdf in os.listdir(path):
    full_path = path+pdf
    removeSenha(full_path)
