file = input("Введите путь к файлу: ")
Opfile = open(file)
nambers = Opfile.readlines()

for i in range(len(nambers)):
    nam = nambers[i].split('\n')
    nambers[i] = int(nam[0])

summ=0
for i in nambers:
    summ+=i
average = summ // len(nambers)

i=0
for m in nambers:
    while True:
        if m<average :
            m+=1
            i+=1
        elif m>average:
            m-=1
            i+=1
        else :break
print(i)