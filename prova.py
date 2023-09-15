import random

estados_eua ={  
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

estados = list(estados_eua.keys())
capitais = list(estados_eua.values())

def criarAtv():
    respostas = []
    atividade = ""
    estados_utilizados = []

    for numero_questao in range(1, 51):
        while True:
            posicao_estados_capitais = random.randint(0, len(estados) - 1)
            estado = estados[posicao_estados_capitais]

            if estado not in estados_utilizados:
                estados_utilizados.append(estado)
                break

        opcoes = [capitais[posicao_estados_capitais]]

        while len(opcoes) < 4:
            capital_aleatoria = random.choice(capitais)
            if capital_aleatoria not in opcoes:
                opcoes.append(capital_aleatoria)

        random.shuffle(opcoes)

        resposta_correta = opcoes.index(capitais[posicao_estados_capitais])

        atividade += f'{numero_questao}) Qual é a capital do estado {estado}?\n'
        for i, opcao in enumerate(opcoes):
            atividade += f'{chr(97 + i)}) {opcao}\n'

        atividade += '\n'

        respostas.append({f'{numero_questao}) Estado de {estado}': f'Resposta correta: {chr(97 + resposta_correta)}){capitais[posicao_estados_capitais]}'})

    return atividade, respostas