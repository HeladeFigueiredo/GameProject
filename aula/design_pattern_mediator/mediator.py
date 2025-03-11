#Essa é a classe mediadora
class TorreDeControle:
    def __init__(self):
        self.avioes = []

    def adicionar_aviao(self, aviao):
        self.avioes.append(aviao)
        aviao.registrar_torre(self)

    #Nesta função a torre envia a mensagem recebida de um avião para todos os outros
    def enviar_mensagem(self, aviao, mensagem):
        print(f'Torre de controle recebeu do {aviao.nome}: {mensagem}')

        for outro_aviao in self.avioes:
            if outro_aviao != aviao:
                outro_aviao.receber_mensagem(aviao, mensagem)


#Essa é a classe mediada
class Aviao:
    def __init__(self, nome):
        self.nome = nome
        self.torre = None

    def registrar_torre(self, torre):
        self.torre = torre

    def enviar_mensagem(self, mensagem):
        self.torre.enviar_mensagem(self, mensagem)

    def receber_mensagem(self, aviao, mensagem):
        print(f'{self.nome} recebeu uma mensagem de {aviao.nome}: {mensagem}')



#Instanciar a torre de controle - mediador
torre_de_controle = TorreDeControle()

#Crio os aviões
aviao1 = Aviao('Avião 1')
aviao2 = Aviao('Avião 2')
aviao3 = Aviao('Avião 3')

#Adicionar os aviões a torre de controle
torre_de_controle.adicionar_aviao(aviao1)
torre_de_controle.adicionar_aviao(aviao2)
torre_de_controle.adicionar_aviao(aviao3)

aviao1.enviar_mensagem('Vamos decolar')
aviao2.enviar_mensagem('Confirmado, prontos para decolar')
aviao3.enviar_mensagem('Aguardando autorização para decolar')
