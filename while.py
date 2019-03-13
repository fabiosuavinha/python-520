#Python3 - While

# Exercício
# Escrevam um programa que:
# 1 - Rode indefinidamente até que o usuário digite "sair"
# 2 - Se o usuário não digitar "sair", solicite a ele:
#     => nome
#     => idade
# 3 - Salve esses dados em um dicionário
# 4 - Salve esse dicionário em uma lista com todos os usuários
# 5 - Depois mostre todos os usuários "cadastrados"


lista_usuario = []

#salvando em txt com frase
def salvar_usuario(usuario)
	lista_usuario.append(usuario)
	with open ('usuarios.txt', 'a') as usuarios:
		mensagem = f'Usuario{usuario["nome"]},voce tem {usuario["idade"]}' #e esta fazendo o curso da 4linux'
		usuarios.white(mensagem)

parado = False

#Looping ate digitar sair:
while not parado:
	condicao = input('digite "sair" para finalizar o programa: ')
	if condicao == 'sair':
		parado = True

#Criando os dados em um dicionario:
	else:
		usuario = {
		
		'nome' : input('Digite seu nome: '),
		'idade':int(input('Digite sua idade: '))
		
		}

#Salvar esses dados em um dicionário
	lista_usuario.append(usuario)
	
	for usuario in lista_usuario: #Salver esse dicionário em uma lista com todos os usuários
		print(usuario) #Mostrar todos os usuarios cadastrados

print('########## Fim do programa #########')		




#Inserindo com o for:






#lista.append(0)
#print(lista)
	

#ou loopiong infinito`
#while true:
#	pass
