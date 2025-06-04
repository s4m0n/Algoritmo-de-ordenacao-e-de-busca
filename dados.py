class Aluno:
    def __init__(self, id, nome, turma):
        self.id = id
        self.nome = nome
        self.turma = turma
        
    def __repr__(self):
        return f"{self.nome} (Turma: {self.turma})"

class Disciplina:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
    def __repr__(self):
        return self.nome

class Nota:
    def __init__(self, aluno_id, disciplina_id, valor):
        self.aluno_id = aluno_id
        self.disciplina_id = disciplina_id
        self.valor = valor  # Valor da nota (0-10)
        
    def __repr__(self):
        return f"Nota: {self.valor}"
