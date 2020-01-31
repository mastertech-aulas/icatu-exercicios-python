gabarito = [ "a", "a", "b", "a","a"]
peso_gabarito = [3, 2, 1, 1, 3]

alunos = {
    "joão": ("c", "d", "a", "b","d"),
    "maria": ("a", "b", "a", "a", "d"),
}

for nome in alunos:
    aluno = alunos[nome]

    ponto = 0
    for item in range(len(gabarito)):
        if gabarito[item] == aluno[item]:
            ponto += peso_gabarito[item]
        
    print(nome, ponto)