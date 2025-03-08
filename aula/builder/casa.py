class Casa:
    def __init__(self):
        self.numero_quartos = None
        self.numero_banheiros = None
        self.tem_garagem = None
        self.tem_jardim = None

    def __str__(self):
        caracteristicas = []
        if self.numero_quartos:
            caracteristicas.append(f'Número de quartos: {self.numero_quartos}')
        if self.numero_banheiros:
            caracteristicas.append(f'Número de banheiros: {self.numero_banheiros}')
        if self.tem_garagem:
            caracteristicas.append('Possui garagem')
        if self.tem_jardim:
            caracteristicas.append('Possui jardim')
        return ', '.join(caracteristicas)

class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def set_numero_quartos(self, numero_quartos):
        self.casa.numero_quartos = numero_quartos
        return self

    def set_numero_banheiros(self, numero_banheiros):
        self.casa.numero_banheiros = numero_banheiros
        return self

    def set_tem_garagem(self):
        self.casa.tem_garagem = True
        return self

    def set_tem_jardim(self):
        self.casa.tem_jardim = True
        return self

    def obter_casa(self):
        return self.casa

#Precisa instanciar o builder
builder_casa = CasaBuilder()

casa = builder_casa.set_numero_quartos(3).set_numero_banheiros(2).set_tem_garagem().obter_casa()
print(casa)


