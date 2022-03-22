### Dicionário é uma coleção desordenada de objetos
# Representado por chaves
# O dicionário utliza o formato json

# Exemplo de dicionários

dic01 = {'chave': 'valor'}

estados_siglas = {"SC": "Santa Catarina", "PR":"Paraná",
"RS":"Rio Grande do Sul","SP":"São Paulo"}

print(estados_siglas)

for d in estados_siglas.values():
    print(d)
    
for d in estados_siglas.keys():
    print(d)
    
