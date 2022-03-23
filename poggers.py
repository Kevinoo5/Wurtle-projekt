import random
sonad = []
count = 0
blanks = ["-","-","-","-","-"]
letters = []
with open("stufff.txt") as f:

    for line in f.readlines():
        line = line.strip()
        sonad.append(line)

suvaline = random.choice(sonad).lower()
true = False
while count < 5:
    proov = input("Sisestage sõna: ")
    if len(proov) == 5:
        for i in range(5):
            if proov == suvaline:
                print("U are so smarterst")
                true = True
                exit()
            elif proov[i] == suvaline[i] and true == False:
                blanks[i] = proov[i]
                count += 1
        for letter in proov:
            letters.append(letter)
        print(letters)
        print("Correct letters: " + letters[i])
        print("".join(blanks))
print(suvaline)
