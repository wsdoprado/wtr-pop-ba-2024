#!/opt/wtr/venv/bin/python3.10

"""
Script: exemplo4 - Estrutura de Dados em Python - Dicionários
Author: William Prado
Email: wprado@nic.br  | wsprado@outlook.com
"""

dados_aluno1 = {"nome": "William Prado", "idade": 32, "altura": 1.82, "casado": True, "filhos": ["Miguel","José"]}
dados_aluno2 = {"nome": "Eduardo Pereira", "idade": 40, "altura": 1.75, "casado": False, "filhos": []}

print(dados_aluno1)
print(dados_aluno2)

print(dados_aluno1['filhos'])
print(dados_aluno2['filhos'])

lista_alunos = [dados_aluno1,dados_aluno2]

print(lista_alunos)
