#Sujeito observável
#Esta sendo observado pelos Usuarios e Grupos
#Responsável por notificar todos os Usuarios inscritos
class Mensageiro:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def enviar_mensagem_para_todos_observadores_inscritos(self, remetente, mensagem):
        for observador in self.observadores:
            observador.enviar_mensagem(remetente, mensagem)

#Observador Usuário
#Implementa o metodo receber_notificacao que é chamado sempre que o Mensageiro envia uma mensagem
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def enviar_mensagem(self, remetente, mensagem):
        print(f'[{self.nome}] Nova mensagem de {remetente}: {mensagem}')

#Observador Grupo - pelo visto não é não porque não está dentro da lista de observadores do Mensageiro
#Implementa o metodo receber_notificacao que é chamado sempre que o Mensageiro envia uma mensagem
class Grupo:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def enviar_mensagem(self, remetente, mensagem):
        print(f'Grupo {self.nome}: Nova mensagem de {remetente}: {mensagem}')


#Instanciar o Mensageiro
mensageiro = Mensageiro()

#Criando usuários
usuario1 = Usuario('Maria')
usuario2 = Usuario('João')
usuario3 = Usuario('Camila')

#Criando grupos
grupo1 = Grupo('Família')
grupo2= Grupo('Trabalho')

#Adicionando observadores ao Mensageiro
#Agora os usuários se tornam observadores do Mensageiro
#Agora o Mensageiro sabe quem são seus observadores e pode enviar mensagem para eles
mensageiro.adicionar_observador(usuario1)
mensageiro.adicionar_observador(usuario2)
mensageiro.adicionar_observador(usuario3)

#Adicionando membros ao grupo
#Os grupos não estão observando diretamente o Mensageiro, pois não são adicionados a lista de observadores
#Assim o grupo só recebe mensagem se alguem chamar o enviar_mensagem diretamente nele
#Neste contexto o grupo não faz parte do mecanismo de observação do Mensageiro
grupo1.adicionar_membro(usuario1)
grupo1.adicionar_membro(usuario2)

grupo2.adicionar_membro(usuario2)
grupo2.adicionar_membro(usuario3)

#Ficou:
#Observadores do Mensageiro = Maria, Joao e Camila
#Grupo1 = Maria e Joao
#Grupo2 = Joao e Camila

#Enviando mensagens

#O mensageiro irá enviar a mensagem para todos os observadores inscritos, no caso Maria, Joao e Camila
mensageiro.enviar_mensagem_para_todos_observadores_inscritos('Admin', 'Bem-vindos ao nosso aplicativo de mensagens!')

#Será enviado a mensagem do Admin para todos os presente no grupo1, no caso Maria e João
grupo1.enviar_mensagem('Admin', 'Nova reunião marcada para amanhã.')

#Serpa enviado a mensagem de Alice para o usuario3, no caso Camila
usuario3.enviar_mensagem('Alice', 'Oi, tudo bem?')