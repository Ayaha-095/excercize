def great(name: str, time: str):
    greeting = ''
    if time == 'morning':
        greeting = 'さん、おはようございます。'
    elif time == 'noon':
        greeting = 'さん、こんにちは。'
    elif time == 'evening':
        greeting = 'さん、こんばんは。'
    else:
        greeting = 'さん、morning　/　noon　/　evening　を引数としてください'
    print(name, greeting)


great('Miura', 'noon')
