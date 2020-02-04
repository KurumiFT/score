first = input("Введите выигрыши/проигрыши первой комманды(через запятую,матчи разделяются точкой): ").split(".")
second = input("Введите выигрыши/проигрыши второй команды(через запятую,матчи разделяются точкой): ").split(".")

offset = float(input("Введите Offset: "))

def getMax(arr,index):
    max = 0
    for i in arr:
        if int(i.split(",")[index]) > max:
            max = int(i.split(",")[index])
    return max

def getSumm(arr):
    summ = 0
    for i in arr:
        summ += i
    return summ

def getMin(arr,index):
    max = 999
    for i in arr:
        if int(i.split(",")[index]) < max:
            max = int(i.split(",")[index])
    return max

firstattack = []
fisrtdefend = []
secondattack = []
seconddefend = []

for i in first:
    firstattack.append(int(i.split(",")[0]))
    fisrtdefend.append(int(i.split(",")[1]))

for i in second:
    secondattack.append(int(i.split(",")[0]))
    seconddefend.append(int(i.split(",")[1]))

firstattack.pop(firstattack.index(getMax(first,0)))
firstattack.pop(firstattack.index(getMin(first,0)))
fisrtdefend.pop(fisrtdefend.index(getMax(first,1)))
fisrtdefend.pop(fisrtdefend.index(getMin(first,1)))

secondattack.pop(secondattack.index(getMax(second,0)))
secondattack.pop(secondattack.index(getMin(second,0)))
seconddefend.pop(seconddefend.index(getMax(second,1)))
seconddefend.pop(seconddefend.index(getMin(second,1)))

fattack = getSumm(firstattack)/3
sattack = getSumm(secondattack)/3

fdefend = getSumm(fisrtdefend)/3
sdefend = getSumm(seconddefend)/3

score_one = fattack + sdefend - offset
score_two = sattack + fdefend - offset

print("Ожидаемый счёт первых: "+str(score_one))
print("Ожидаемый счёт вторых: "+str(score_two))
