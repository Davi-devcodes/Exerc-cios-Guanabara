times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'São Paulo', 'RB Bragantino', 'Corinthians', 'Fluminense',
         'Ceará', 'Internacional', 'Atlético-MG', 'Grêmio', 'Vasco', 'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')

cinco = times[:5]
print('\nOs cinco primeiros colocados são:', cinco)

ultimos = times[-4:]
print('\nOs últimos quatro colocados são:', ultimos)

ordem = sorted(times)
print('\nOs times, em ordem alfabética são:', ordem)

oitavo = times.index('Juventude')
print(f'O Juventude está na {oitavo}ª colocação')
