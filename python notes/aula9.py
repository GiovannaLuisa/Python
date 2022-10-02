
def escrever_arquivo(texto):
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()
    
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    for x in aluno_nota:
        print(x)
    
if __name__ == '__main__':
    media_notas('notas.txt')
   #escrever_arquivo('Primeira linha.\n')
  # aluno = 'Felipe, 7,10,5,5'
  # atualizar_arquivo('notas.txt', aluno)
   #ler_arquivo('teste.txt')