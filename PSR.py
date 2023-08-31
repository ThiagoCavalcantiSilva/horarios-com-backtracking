aulas = ["C1", "IP", "GA", "IP", "IP", 
         "IC", "C1", "LM", "LM", "GA"]

turma_a = [aulas[:5], aulas[5:]]
turma_b = [["" for _ in range(5)] for _ in range(2)]
turma_c = [["" for _ in range(5)] for _ in range(2)]

turmas = [turma_a, turma_b, turma_c]

def imprimir_grades():
    for i, turma in enumerate(turmas):
        print(f"Turma {chr(ord('A') + i)}:")
        for horario in turma:
            print(horario)
        print()

# Verifica se há choque de horário em outras turmas
def ha_choque(horario, dia, aula, turmas):
    for turma in turmas:
        if turma[horario][dia] == aula:
            return True

    return False

# Verifica se a disciplina tem duas aulas no mesmo dia e na mesma turma
def aula_repetida(dia, aula, turma):
    ''' 
    Basta verificar se a aula é igual ao primeiro horário.
    Pois, nas novas turmas, a primeira iteração comparará a aula com string vazia.
    E na segunda, compara duas aulas preenchidas
    '''
    return turma[0][dia] == aula

def preencher_turma(turma, horario, dia):
    if horario >= 2:  # Todos os horários foram preenchidos
        horario = 0
        dia += 1

    if dia >= 5:  # Todos os dias foram preenchidos
        return True

    for aula in aulas_disponiveis:
        if not ha_choque(horario, dia, aula, turmas) and not aula_repetida(dia, aula, turma):
            turma[horario][dia] = aula
            aulas_disponiveis.remove(aula)
            if preencher_turma(turma, horario + 1, dia):
                return True
            
            # Backtrack
            turma[horario][dia] = ""
            aulas_disponiveis.append(aula)

    return False

# Preenchendo turma_b e turma_c
aulas_disponiveis = aulas.copy() # Estrutura usada para manter controlar aulas inseridas
preencher_turma(turma_b, 0, 0)
aulas_disponiveis = aulas.copy() # Estrutura usada para manter controlar aulas inseridas
preencher_turma(turma_c, 0, 0)

imprimir_grades()
