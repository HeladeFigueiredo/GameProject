# Poderia ser feito com herança, mas outra opção é usar decorators

#Este é o decorator da classe
class Carro:
    def __init__(self, classe_decorada): #O parâmetro classe_decorada será a classe que Carro vai decorar, no caso Automovel
        self.classe_decorada = classe_decorada

    def __call__(self, *args, **kwargs): #Função será executada quando instanciar a classe Automovel. Recebe os argumentos que serão passados para o construtor da classe Automovel
        instancia_classe = self.classe_decorada(*args, **kwargs) #Aqui cria uma instância da classe Automovel usando os argumentos recebidos

        instancia_classe.num_rodas = 4 #Está adicionando um atributo a mais na classe Automovel
        return instancia_classe

#Esta é a classe
#Como ela é @carro, sempre que eu instanciar a classe automóvel, o função __call__ da classe Carro será chamada
@Carro
class Automovel:
    def __init__(self, modelo):
        self.modelo = modelo


novo_auto = Automovel('Gol')

print(novo_auto.modelo)
print(novo_auto.num_rodas)

#Apesar da classe Automovel não ter o atributo numero de rodas
#Este atributo foi incluido no decorators da classe