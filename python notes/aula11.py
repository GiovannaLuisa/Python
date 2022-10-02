#documento do python(https://docs.python.org) Hierarchy das clases
lista = [1, 10]
arquivo = open ('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    
#zeroDivisionError sempre vai no topo pela hierarquia
except ZeroDivisionError:
    print('Nao é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar op. aritmetica')
except IndexError: 
    print('Erro ao acessar um índice invalido da lista')
except Exception as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
    
   