#bin/python3

usuarios = [
  
  {
    'id': 1,
    'nome': 'Lucas',
    'idade': 25,
  },

  {
    'id': 2,
    'nome': 'Claudia',
    'idade': 20
  },

  {
    'id': 3,
    'nome': 'Siclano',
    'idade': 10
  },

  {
    'id': 4,
    'nome': 'Matusalem',
    'idade': 3129863981263981263981263
  },
  
]





for usuario in usuarios:
#    print(usuarios)
        for chave in usuario:
            if usuario['idade'] < 20 or usuario['id'] == 2 : #acessar idade usuario['idade'] , acessar id usario['id']
                print(usuario[chave])

exit()

                  
            
        
#Lista = usuarios
#Dicionario = usuario

#usuario[1]{'id'}

#Lucas = usuarios[0]
#print(Lucas)
        
exit()
