import time

# Exemplo 1

def meu_decorator(funcao):
    def wrapper():
        print('A função será executada agora')
        funcao()
        print('A função foi executada')

    return wrapper()

@meu_decorator
def minha_funcao():
    print('Essa é a função original')


minha_funcao()

# Exemplo 2
#
# def medir_tempo(funcao):
#     def wrapper(*args, **kwargs):
#         inicio_tempo = time.time()
#         resultado = funcao(*args, **kwargs)
#         final_tempo = time.time()
#         print(f'A função {funcao.__name__} demorou {final_tempo - inicio_tempo} segundos para ser executada')
#         return resultado
#
#     return wrapper
#
#
# @medir_tempo
# def funcao_tempo_espera(tempo_espera):
#     time.sleep(tempo_espera) #Irá esperar a quantidade de segundos passada como parâmetro
#     print('A função foi executada')
#
# funcao_tempo_espera(2)

