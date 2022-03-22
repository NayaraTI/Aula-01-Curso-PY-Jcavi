## Permite passar um número indeterminado de parâmetros para uma função
# Mas os parâmetros são passados como identificadores de chave e valor
# A saída será em formato de dicionário


def saudacao(**kwargs):
    print(kwargs)
    
saudacao(manha= 'Bom Dia',tarde= 'Boa Tarde', noite= 'Boa Noite')

def saudacao_dia(**kwargs):
    for hora,saudacao in kwargs.items():
        print(f"Durante a {hora} dizemos {saudacao}")
        
saudacao_dia(manha='bom dia', tarde='boa tarde')


# 2 underlines ou dunder quer dizer métodos mágicos
#_next_