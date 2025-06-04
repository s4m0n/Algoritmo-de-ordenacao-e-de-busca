from dados import Aluno, Disciplina, Nota

class SistemaNotas:
    def __init__(self):
        self.alunos = []
        self.disciplinas = []
        self.notas = []
  def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
      def adicionar_nota(self, nota):
        self.notas.append(nota)
       def ordenar_notas_por_valor(self, crescente=True):
        """Ordena notas por valor usando Bubble Sort"""
        n = len(self.notas)
        for i in range(n):
            for j in range(0, n-i-1):
                # Ordenação crescente ou decrescente
                if crescente:
                    condicao = self.notas[j].valor > self.notas[j+1].valor
                else:
                    condicao = self.notas[j].valor < self.notas[j+1].valor
                    
                if condicao:
                    self.notas[j], self.notas[j+1] = self.notas[j+1], self.notas[j]
    
    def ordenar_alunos_por_nome(self):
        """Ordena alunos por nome usando sorted() com lambda"""
        self.alunos = sorted(self.alunos, key=lambda aluno: aluno.nome)
    
    # ---------- ALGORITMOS DE BUSCA ----------
    
    def buscar_notas_por_aluno(self, aluno_id):
        """Busca linear por todas as notas de um aluno"""
        return [nota for nota in self.notas if nota.aluno_id == aluno_id]
    
    def buscar_alunos_por_faixa_notas(self, disciplina_id, nota_min, nota_max):
        """Busca alunos com notas em uma faixa específica"""
        resultados = []
        for nota in self.notas:
            if (nota.disciplina_id == disciplina_id and 
                nota_min <= nota.valor <= nota_max):
                aluno = next(a for a in self.alunos if a.id == nota.aluno_id)
                resultados.append((aluno, nota.valor))
        return resultados
    
    # ---------- SINERGIA ORDENAÇÃO/BUSCA ----------
    
    def buscar_e_ordenar_notas_disciplina(self, disciplina_id, decrescente=True):
        """Busca notas de uma disciplina e ordena por valor"""
        # 1. Busca as notas da disciplina
        notas_disciplina = [n for n in self.notas if n.disciplina_id == disciplina_id]
        
        # 2. Ordenação por valor (usando sorted para eficiência)
        return sorted(
            notas_disciplina, 
            key=lambda n: n.valor, 
            reverse=decrescente
        )
    
    def ranking_disciplina(self, disciplina_id):
        """Retorna ranking de alunos em uma disciplina ordenado por nota"""
        # 1. Busca todas as notas da disciplina
        notas_disc = [n for n in self.notas if n.disciplina_id == disciplina_id]
        
        # 2. Ordena as notas por valor (maior primeiro)
        notas_ordenadas = sorted(notas_disc, key=lambda n: n.valor, reverse=True)
        
        # 3. Adiciona informações do aluno
        ranking = []
        for nota in notas_ordenadas:
            aluno = next(a for a in self.alunos if a.id == nota.aluno_id)
            ranking.append((aluno, nota.valor))
        
        return ranking
