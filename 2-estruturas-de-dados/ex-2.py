equipe = {
    'nome': 'Bruno',
    'vendas': 0,
    'subordinados': [
        {
            'nome': 'Ana',
            'vendas': 300,
            'subordinados': [
                {
                    'nome': 'Bia',
                    'vendas': 100,
                },
                {
                    'nome': 'Camila',
                    'vendas': 350,          
                }
            ]
        },
        {
            'nome': 'Diandra',
            'vendas': 450,
            'subordinados': [
                {
                    'nome': 'Maga',
                    'vendas': 200,            
                }
            ]
        },
        {
            'nome': 'Nico',
            'vendas': 500,
            'subordinados': [
                {
                    'nome': 'Lucas',
                    'vendas': 150,            
                },
                {
                    'nome': 'Vini',
                    'vendas': 100,            
                }
            ]
        }
    ]
}


ganho_subordinados = 0.05


def calcular_salario(funcionario):
    salario_subordinados = 0

    if 'subordinados' in funcionario.keys():
        for subordinado in funcionario['subordinados']:
            salario_subordinados += calcular_salario(subordinado)
    
    salario = funcionario['vendas'] + salario_subordinados * ganho_subordinados

    funcionario['salario'] = salario

    return salario


def imprimir_salarios(funcionario):
    if 'subordinados' in funcionario.keys():
        for subordinado in funcionario['subordinados']:
            imprimir_salarios(subordinado)
    
    print(funcionario['nome'] + ':', funcionario['salario'])


calcular_salario(equipe)
imprimir_salarios(equipe)