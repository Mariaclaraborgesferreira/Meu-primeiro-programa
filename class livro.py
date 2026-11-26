# Define a classe Livro, que representa uma obra no acervo da biblioteca
class Livro:
    # Método construtor: inicializa os atributos do livro ao criar um objeto
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo        # Título da obra
        self.autor = autor          # Nome do autor
        self.isbn = isbn            # Código único de identificação (ISBN)
        self.disponivel = True      # Todo livro começa disponível para empréstimo

    # Método para alterar o estado do livro para emprestado
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Livro '{self.titulo}' emprestado com sucesso!")
            return True             # Indica que a operação foi concluída
        else:
            print(f"Livro '{self.titulo}' já está emprestado!")
            return False            # Indica que o livro não pôde ser emprestado

    # Método para registrar a devolução e tornar o livro disponível novamente
    def devolver(self):
        self.disponivel = True
        print(f"Livro '{self.titulo}' devolvido!")

    # Retorna uma string formatada com os dados e o status atual do livro
    def descricao(self):
        status = "disponível" if self.disponivel else "emprestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{status}]"


# Classe base (superclasse) que representa um usuário genérico da biblioteca
class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome                    # Nome do usuário
        self.matricula = matricula          # Número de matrícula ou registro
        self.livros_emprestados = []        # Lista para armazenar os objetos Livro pegos
        self.limite = 1                     # Limite padrão de empréstimos simultâneos

    # Método responsável por validar o limite do usuário e efetivar o empréstimo
    def pegar_livro(self, livro):
        # Verifica se o usuário ainda não atingiu sua cota máxima de livros
        if len(self.livros_emprestados) < self.limite:
            # Tenta emprestar o livro; só adiciona à lista se ele estiver disponível
            if livro.emprestar():
                self.livros_emprestados.append(livro)
        else:
            print(f"{self.nome} atingiu o limite de {self.limite} livro(s).")


# Subclasse Aluno: herda atributos e métodos de Usuario
class Aluno(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)   # Chama o construtor da classe mãe (Usuario)
        self.limite = 2                     # Sobrescreve o limite: alunos podem pegar até 2 livros

    # Sobrescrita (polimorfismo) do método pegar_livro para personalizar a mensagem
    def pegar_livro(self, livro):
        print(f"[Aluno] {self.nome} tentando pegar livro...")
        super().pegar_livro(livro)          # Reaproveita a lógica de empréstimo da classe Usuario


# Subclasse Professor: também herda de Usuario, mas com regras diferentes
class Professor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)   # Chama o construtor da classe mãe (Usuario)
        self.limite = 5                     # Sobrescreve o limite: professores podem pegar até 5 livros

    # Sobrescrita (polimorfismo) do método pegar_livro para identificar o perfil
    def pegar_livro(self, livro):
        print(f"[Professor] {self.nome} tentando pegar livro...")
        super().pegar_livro(livro)          # Reaproveita a lógica de empréstimo da classe Usuario


# --- Bloco de Testes ---
# Instancia (cria) um objeto da classe Livro e um da classe Aluno
livro1 = Livro("Harry Potter", "J.K. Rowling", "123")
aluno1 = Aluno("João", "202601")

# Exibe o status inicial, realiza o empréstimo e exibe o status atualizado
print(livro1.descricao())
aluno1.pegar_livro(livro1)
print(livro1.descricao())