class veiculos:
    def __init__(self,marca,velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max
    def mover (self):
        print(f"O veiculos {self.marca}esta se movendo a ate {self.velocidade_max} km\h")

class carro (Veiculo):
    def __init__ (self,marca,velocidade_max, num_porta):
        super ().__init__(marca, velocidade_max)
        self.num_portas = self.num_portas
    def mover (self):
        print(f"O carro {self.marca}com{self.num_portas}portas esta andando na estrada!")

class bicicleta (veiculo):
    def __init__ (self,marca,velocidade_max, num_marchas):
            super().__init__(marca,velocidade_max)
            self.num_marchas = num_marchas
    def mover (self): 
            print(f"a bicicleta { self.marca} com {self.num_marchas} marchas esta pedalando!")
    #teste
c = carro ( "honda",200,4)
b = bicicleta ("caloi",30,21)
c . mover ()
b . mover ()