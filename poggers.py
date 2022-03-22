import random
sonad = []
count = 0
blanks = "-----"
with open("stufff.txt") as f:

    for line in f.readlines():
        line = line.strip()
        sonad.append(line)

suvaline = random.choice(sonad).lower()
print(suvaline)
true = False
while count < 5:
    if true != True:
        proov = input("Sisestage sõna: ")
    for i in range(5):
        if proov == suvaline and true != True:
            print("U are so smarterst")
            true = True
            break
        elif proov[i] == suvaline[i] and true == False:
            blanks[i].replace(proov[i])
    count += 1