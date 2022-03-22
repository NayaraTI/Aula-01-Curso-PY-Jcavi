## Função enumerate retorna o indice de memória de uma estrutura de dados
# Ex: lista

animais = ["Cachorro", "Gato", "Periquito", "Elefante"]

print(list(enumerate(animais)))

## Usar um iterador ##

for i,valor in enumerate(animais):
    print(i,valor)
    
for i,valor in enumerate(animais):
    if i>1:
        break
    else:
        print(valor)