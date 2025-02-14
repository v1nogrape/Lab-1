BLUE = '\u001b[48;5;12m'
PURPLE = '\u001b[48;5;13m'
END = '\u001b[0m'

f = open('sequence.txt', 'r')
bolshe = []
menshe = []
for x in f:
    if float(x)>0:
        bolshe.append(x)
    if float(x)<0:
        menshe.append(x)

proc_b=(len(bolshe)/(len(bolshe)+len(menshe)))*100
proc_m=(len(menshe)/(len(bolshe)+len(menshe)))*100

print(f'{proc_m}{" % "}{BLUE}{"  " * int(proc_m // 5)}{PURPLE}{"  " * int(proc_b// 5)}{END}{" "}{proc_b}{" %"}{END}')
print(f'{BLUE}{" " *2}{END}{" - количество чисел меньше 0"}')
print(f'{PURPLE}{" " *2}{END}{" - количество чисел больше 0"}')

f.close()