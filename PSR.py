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

imprimir_grades()
