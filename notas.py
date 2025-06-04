alunos = [
    {'id': 1, 'nome': 'Ana', 'turma': '8A'},
    {'id': 2, 'nome': 'Bruno', 'turma': '8B'},
    {'id': 3, 'nome': 'Carlos', 'turma': '8A'}
]
#lista fa disciplinas
disciplinas = [
    {'id': 1, 'nome': 'Matemática'},
    {'id': 2, 'nome': 'Português'}
]
notas = [
    {'aluno_id': 1, 'disciplina_id': 1, 'valor': 8.5}, # lista de notas (cada nota é ligada a um aluno e uma disciplina)
    {'aluno_id': 1, 'disciplina_id': 2, 'valor': 9.0},
    {'aluno_id': 2, 'disciplina_id': 1, 'valor': 7.0},
    {'aluno_id': 2, 'disciplina_id': 2, 'valor': 6.5},
    {'aluno_id': 3, 'disciplina_id': 1, 'valor': 9.5},
    {'aluno_id': 3, 'disciplina_id': 2, 'valor': 8.0}
]
#funçao de ordenaação
def ordenar_alunos_por_nome():
    return sorted(alunos, key=lambda aluno: aluno['nome'])
 def ordenar_notas_por_valor(notas_lista, crescente=True):
   return sorted(notas_lista, key=lambda nota: nota['valor'], reverse=not crescente)

#função de busca
def buscar_aluno_por_nome(nome):
    return [aluno for aluno in alunos if nome.lower() in aluno['nome'].lower()]
  def buscar_notas_por_disciplina(disciplina_id): #busca todas as notas de ma materia
    return [nota for nota in notas if nota['disciplina_id'] == disciplina_id]
 def buscar_notas_por_aluno(aluno_id):    #Busca todas as notas de um aluno específico.
  return [nota for nota in notas if nota['aluno_id'] == aluno_id]

def buscar_notas_na_faixa(disciplina_id, nota_min, nota_max):
    """Busca notas dentro de uma faixa de valores"""
    return [
        nota for nota in notas 
        if nota['disciplina_id'] == disciplina_id 
        and nota_min <= nota['valor'] <= nota_max
    ]
# FUNÇÕES DE RELATÓRIOS
  def gerar_ranking_disciplina(disciplina_id):  #Gera ranking de alunos em uma disciplina por nota
   notas_disc = buscar_notas_por_disciplina(disciplina_id)
    
    # Ordena notas do maior para o menor
    notas_ordenadas = ordenar_notas_por_valor(notas_disc, crescente=False)
    ranking = []        # Adiciona as informação do aluno
      for nota in notas_ordenadas:
        aluno = next(a for a in alunos if a['id'] == nota['aluno_id'])
        disciplina = next(d for d in disciplinas if d['id'] == nota['disciplina_id'])
        ranking.append({
            'aluno': aluno['nome'],
            'nota': nota['valor'],
            'disciplina': disciplina['nome']
        })
        return ranking
#EXPEMPLO
if __name__ == "__main__":
    print("\n=== ALUNOS ORDENADOS POR NOME ===")
    for aluno in ordenar_alunos_por_nome():
        print(f"{aluno['nome']} - Turma {aluno['turma']}")

    print("\n=== BUSCA: ALUNOS COM 'A' NO NOME ===")
    for aluno in buscar_aluno_por_nome('a'):
        print(aluno['nome'])

    print("\n=== NOTAS DE MATEMÁTICA ===")
    for nota in buscar_notas_por_disciplina(1):
        aluno = next(a for a in alunos if a['id'] == nota['aluno_id'])
        print(f"{aluno['nome']}: {nota['valor']}")

    print("\n=== RANKING DE MATEMÁTICA ===")
    ranking = gerar_ranking_disciplina(1)
    for i, item in enumerate(ranking, 1):
        print(f"{i}º {item['aluno']}: {item['nota']}")

    print("\n=== ALUNOS COM NOTA ENTRE 7.0 E 8.5 EM MATEMÁTICA ===")
    notas_faixa = buscar_notas_na_faixa(1, 7.0, 8.5)
    for nota in notas_faixa:
        aluno = next(a for a in alunos if a['id'] == nota['aluno_id'])
        print(f"{aluno['nome']}: {nota['valor']}")
 D
