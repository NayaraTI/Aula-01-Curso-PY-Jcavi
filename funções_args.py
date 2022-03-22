## Funções *args utilizamos quando não sabemos a quantidade exata de parâmetros
# na função
## Args retorna os valores em tuplas

def soma(*args):
    print(args)
    
soma(1,4,5,4,76,3,32,6,3,3)

def soma_total(*args):
    total = 0
    for numero in args:
        total = numero+total
    return total

print(soma_total(3,6,9,5))

