BLACK = '\u001b[40m'
WHITE = '\u001b[48;5;231m'
END = '\u001b[0m'

for i in range(9):
    if i<=2 or i>=6:
        print(f'{BLACK}{"  " * 4}{WHITE}{"  " * 4}{BLACK}{"  " * 4}{END}')
    else:
        print(f'{WHITE}{"  " * 4}{BLACK}{"  " * 4}{WHITE}{"  " * 4}{END}')
