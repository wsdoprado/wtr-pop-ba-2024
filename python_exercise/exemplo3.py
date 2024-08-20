#!/opt/wtr/venv/bin/python3.10

"""
Script: exemplo3 - Estrutura de Dados em Python - Listas
Author: William Prado
Email: wprado@nic.br  | wsprado@outlook.com
"""

aluno1 = "William Prado"
aluno2 = "Miguel Prado"
aluno3 = "Jose Prado"
aluno4 = "Eduardo Reis"
aluno5 = "Carlos Andre"
aluno6 = "Pedro Elias"

lista_alunos = [aluno1,aluno2,aluno3,aluno4,aluno5]
#index             0      1      2      3      4

print(lista_alunos)

print(lista_alunos[4])

for aluno in lista_alunos:
    print(aluno)

if aluno6 in lista_alunos:
    print("Aluno Encontrado")
else:
    print(f"Aluno: {aluno6} não encontrado na lista")
