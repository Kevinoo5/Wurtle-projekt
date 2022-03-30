import random
import sqlite3

sonad = []
count = 0
id = 1
blanks = ["-","-","-","-","-"]
letters = []
notletters = []


ühendus = sqlite3.connect('data.db')
c = ühendus.cursor()
number = random.randint(1,2315)      
        
c.execute("SELECT * FROM Wurtel WHERE ID = ?", [number])
suva = c.fetchall()

ühendus.commit()

true = False
while count < 5:
    proov = input("Word please: ")
    c.execute("SELECT * FROM Allowed WHERE allowed = ?", [proov])
    sona = c.fetchall()
    if sona != []:
        sona = sona[-1][0]
    if proov in sona:
        for i in range(5):
            if proov == suva[0][1]:
                print("U are so smarterst")
                true = True
                exit()
            elif proov[i] == suva[0][1][i] and true == False:
                blanks[i] = proov[i]
        for letter in proov:
            if letter not in letters and letter in suva[0][1]:
                letters.append(letter)
            elif letter not in notletters and letter not in suva[0][1]:
                notletters.append(letter)
        count += 1
        print("Answer includes: " + ",".join(letters))
        print("Answer doesn't include: " + ",".join(notletters))
        print("".join(blanks))
print(suva[0][1])
c.close()
ühendus.close()
