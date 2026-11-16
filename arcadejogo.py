import random
import tkinter as tk


LARGURA, ALTURA = 800, 600
FUNDO = "#11152e"


class Jogo:
	def __init__(self, janela):
		self.janela = janela
		janela.title("Caça-Estrelas")
		janela.resizable(False, False)
		self.tela = tk.Canvas(janela, width=LARGURA, height=ALTURA,
							  bg=FUNDO, highlightthickness=0)
		self.tela.pack()
		self.teclas = set()
		janela.bind("<KeyPress>", self.tecla_pressionada)
		janela.bind("<KeyRelease>", self.tecla_solte)
		self.em_jogo = False
		self.tela_inicial()

	def fundo_estrelado(self):
		random.seed(12)
		for _ in range(100):
			x, y = random.randrange(LARGURA), random.randrange(ALTURA)
			raio = random.choice((1, 1, 2))
			cor = random.choice(("#52618c", "#8495bd", "#dce7ff"))
			self.tela.create_oval(x-raio, y-raio, x+raio, y+raio,
								  fill=cor, outline="")

	def tela_inicial(self):
		self.fundo_estrelado()
		self.tela.create_text(400, 180, text="CAÇA-ESTRELAS", fill="#ffdf70",
							  font=("Helvetica", 38, "bold"))
		self.tela.create_text(400, 245, text="Pegue as estrelas e fuja dos meteoros!",
							  fill="#d5dcf5", font=("Helvetica", 16))
		self.tela.create_text(400, 355, text="Mova com as setas ou A e D",
							  fill="#aab7dc", font=("Helvetica", 15))
		self.tela.create_text(400, 420, text="ESPAÇO para começar",
							  fill="white", font=("Helvetica", 20, "bold"))
		self.janela.bind("<space>", lambda _evento: self.iniciar())

	def tecla_pressionada(self, evento):
		self.teclas.add(evento.keysym.lower())

	def tecla_solte(self, evento):
		self.teclas.discard(evento.keysym.lower())

	def iniciar(self):
		if self.em_jogo:
			return
		self.em_jogo = True
		self.tela.delete("all")
		self.fundo_estrelado()
		self.x, self.y = LARGURA // 2, ALTURA - 65
		self.pontos, self.quadro = 0, 0
		self.objetos = []
		self.nave = self.tela.create_polygon(0, 0, 0, 0, 0, 0,
			fill="#62ddf5", outline="#e0fbff", width=2)
		self.painel = self.tela.create_text(20, 18, anchor="nw",
			text="PONTOS: 0", fill="white", font=("Helvetica", 16, "bold"))
		self.atualizar()

	def criar_objeto(self):
		x = random.randint(25, LARGURA - 25)
		if random.random() < 0.7:
			figura = self.tela.create_text(x, -25, text="★", fill="#ffdf62",
				font=("Helvetica", 28, "bold"))
			tipo, velocidade, raio = "estrela", random.uniform(2.5, 4), 17
		else:
			raio = random.randint(18, 26)
			figura = self.tela.create_oval(x-raio, -raio, x+raio, raio,
				fill="#ff705e", outline="#ffc078", width=2)
			tipo, velocidade = "meteoro", random.uniform(3, 5)
		self.objetos.append([figura, x, -25, tipo, velocidade, raio])

	def atualizar(self):
		if not self.em_jogo:
			return
		self.quadro += 1
		direita = "right" in self.teclas or "d" in self.teclas
		esquerda = "left" in self.teclas or "a" in self.teclas
		self.x = max(25, min(LARGURA-25, self.x + (direita-esquerda)*7))
		self.tela.coords(self.nave, self.x, self.y-23, self.x-19, self.y+18,
						 self.x, self.y+9, self.x+19, self.y+18)

		if self.quadro % max(15, 38-self.pontos//5) == 0:
			self.criar_objeto()

		for objeto in self.objetos[:]:
			figura, x, y, tipo, velocidade, raio = objeto
			y += velocidade
			objeto[2] = y
			self.tela.move(figura, 0, velocidade)
			colidiu = abs(x-self.x) < raio+14 and abs(y-self.y) < raio+17
			if colidiu and tipo == "estrela":
				self.pontos += 1
				self.tela.delete(figura)
				self.objetos.remove(objeto)
				self.tela.itemconfig(self.painel, text=f"PONTOS: {self.pontos}")
			elif colidiu:
				self.finalizar()
				return
			elif y > ALTURA+30:
				self.tela.delete(figura)
				self.objetos.remove(objeto)
		self.janela.after(16, self.atualizar)

	def finalizar(self):
		self.em_jogo = False
		self.tela.create_rectangle(150, 205, 650, 395, fill="#171d3b",
								   outline="#6573a5", width=2)
		self.tela.create_text(400, 255, text="FIM DE JOGO", fill="#ff897b",
							  font=("Helvetica", 30, "bold"))
		self.tela.create_text(400, 310, text=f"Você pegou {self.pontos} estrelas!",
							  fill="white", font=("Helvetica", 18))
		self.tela.create_text(400, 355, text="ESPAÇO para jogar novamente",
							  fill="#c4cdef", font=("Helvetica", 14))


if __name__ == "__main__":
	raiz = tk.Tk()
	Jogo(raiz)
	raiz.mainloop()
