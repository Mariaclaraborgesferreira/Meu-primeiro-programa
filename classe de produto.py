class produto:
    def __init__(self,nome,categoria,preço,estoque):
        self.nome = nome
        self.categoria = categoria
        self.preço = preço
        self.estoque = estoque
    def exibir(self):
        print("="*70)
        print(f"Produto: {self.nome}")
        print(f"Categoria:{self.categoria}")
        print(f"Preço : {self.preço}.2f")
        print(f"estoque: {self.estoque}")
        print("="*70)
    def valor_total(self):
        return self.preço * self.estoque
    def aplicar_desconto(self,percentual):
        self.preço *= (1 - percentual /100)
        print(f"desconto aplicado! novo preço:R${self.preço}")
    def vender(self,quantidade):
        if quantidade > self.estoque:
            print("estoque insuficiente!")
        else:
            self.estoque -= quantidade
            print(f"vendido {quantidade} x {self.nome}. estoque restante: {self.estoque}")
    def repor_estoque(self,quantidade):
        self.estoque += quantidade
        print(f"novo estoque: {self.estoque}")
p1 = produto("fuba", "alimentos", 2.99,20)
p2 = produto("caneta" ,"Papelaria",1.99,30)

p1.exibir()
p2.exibir()

p1.vender(5)
p2.aplicar_desconto(50)
p1.repor_estoque(20)

print(f"\nvalor total em estoque - {p1.nome}:")

p1.exibir()
p2.exibir()