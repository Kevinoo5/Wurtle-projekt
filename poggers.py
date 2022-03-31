import random
import sqlite3

sonad = []
count = 0
id = 1
blanks = ["-","-","-","-","-"]
letters = []
notletters = []
integer = 0
inputtabel = input("Insert letter amount between 5 and 7 (with words): ")
if inputtabel == "five":
    integer = 5
elif inputtabel == "six":
    integer = 6
elif inputtabel == "seven":
    integer = 7
    
if inputtabel == "five":
    blanks = ["-","-","-","-","-"]
elif inputtabel == "six":
    blanks = ["-","-","-","-","-","-"]
elif inputtabel == "seven":
    blanks = ["-","-","-","-","-","-","-"]
    
ühendus = sqlite3.connect('data.db')
c = ühendus.cursor()

if inputtabel == "five":
    number = random.randint(1, 2315)
elif inputtabel == "six":
    number = random.randint(1, 1049)
elif inputtabel == "seven":
    number = random.randint(1, 1371)
else:
    print("El Salvador")
    exit()
        
c.execute(f"SELECT * FROM {inputtabel} WHERE ID = ?", [number])
suva = c.fetchall()
ühendus.commit()

true = False
while count < integer:
    proov = input("Word please: ")
    c.execute(f"SELECT * FROM Allowed{str(integer)} WHERE allowed = ?", [proov])
    sona = c.fetchall()
    if sona != []:
        sona = sona[-1][0]
    if proov in sona:
        for i in range(integer):
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
