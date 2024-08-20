#!/opt/wtr/venv/bin/python3.10

"""
Script: exemplo4 - Estrutura de Dados em Python - Dicionários
Author: William Prado
Email: wprado@nic.br  | wsprado@outlook.com
"""

filho1_aluno1 = {"nome": "Miguel Guedes", "idade": 5, "altura": 0.80, "casado": False}
filho2_aluno1 = {"nome": "José Guedes", "idade": 2, "altura": 0.60, "casado": False}


dados_aluno1 = {"nome": "William Prado", "idade": 32, "altura": 1.82, "casado": True, "filhos": [filho1_aluno1,filho2_aluno1]}
dados_aluno2 = {"nome": "Eduardo Pereira", "idade": 40, "altura": 1.75, "casado": False, "filhos": []}

lista_alunos = [dados_aluno1,dados_aluno2]

print(lista_alunos)

for aluno in lista_alunos:
    print(f"Aluno: {aluno['nome']} - Idade: {aluno['idade']} - Altura: {aluno['altura']}")
    for filho in aluno['filhos']:
        print(f"Nome filho: {filho['nome']} - Idade: {filho['idade']}")
