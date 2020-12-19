import os
import shutil
# 1 - listar as pastas de arquivos temporários do Windows
# 2 - fazer o script exclui esses arquivos e migrar para outras pastas
# 3 - exibir a mensagem de limpeza concluída

lista_de_pastas = ['C:\\Windows\\Temp','C:\\Windows\\Prefetch','C:\\Users\\EDVALDO\\AppData\\Local\\Temp']
arquivos_excluidos = 0
print('Limpeza Iniciada, por favor Aguarde !!!!')
for pasta in lista_de_pastas:
    os.chdir(pasta)
    lista = os.listdir('.')
    for file in lista:
        try:
            os.chmod(file, 0o777)
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)
            arquivos_excluidos += 1
        except Exception as erro:
            print(f'{file} -> {erro}')

print('Limpeza Finalizada!!!')
print(arquivos_excluidos,' arquivos excluídos')
    
