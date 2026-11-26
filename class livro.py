class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Livro '{self.titulo}' emprestado com sucesso!")
            return True
        else:
            print(f"Livro '{self.titulo}' já está emprestado!")
            return False

    def devolver(self):
        self.disponivel = True
        print(f"Livro '{self.titulo}' devolvido!")

    def descricao(self):
        status = "disponível" if self.disponivel else "emprestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{status}]"


class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []
        self.limite = 1

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) < self.limite:
            if livro.emprestar():
                self.livros_emprestados.append(livro)
        else:
            print(f"{self.nome} atingiu o limite de {self.limite} livro(s).")


class Aluno(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 2

    def pegar_livro(self, livro):
        print(f"[Aluno] {self.nome} tentando pegar livro...")
        super().pegar_livro(livro)


class Professor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 5

    def pegar_livro(self, livro):
        print(f"[Professor] {self.nome} tentando pegar livro...")
        super().pegar_livro(livro)


# --- Testes ---
livro1 = Livro("Harry Potter", "J.K. Rowling", "123")
aluno1 = Aluno("João", "202601")

print(livro1.descricao())
aluno1.pegar_livro(livro1)
print(livro1.descricao())
