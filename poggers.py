import tkinter as tk
import random
import sqlite3
from tkinter import messagebox

root= tk.Tk()
root.title('Wurtle')
root.configure(bg='bisque4')
canvas1 = tk.Canvas(root, width = 400, height = 300, bg='bisque4')
canvas1.pack()

sonad = []
id = 1
blanks = ["-","-","-","-","-"]
letters = []
notletters = []
integer = 0

def letter5():
    count = ["try"]
    word = tk.Entry(root, width=20)
    def get_word():
        true = False
        while len(count) < 7:
            proov = word.get()
            if len(proov) != 5:
                messagebox.showwarning("showwarning", "OH NO!!! This is not in the list")
                word.delete(0, 10)
                return None
                break
            c.execute(f"SELECT * FROM Allowed5 WHERE allowed = ?", [proov])
            sona = c.fetchall()
            if len(count) >= 5:
                messagebox.showinfo("WORD", "The word was: "+suva[0][1])
                c.close()
                ühendus.close()
                exit()
            if sona != []:
                sona = sona[-1][0]
            if proov in sona:
                for i in range(integer):
                    if proov == suva[0][1]:
                        messagebox.showinfo("U won!", "U so smartest! Be proud of yourself!")
                        true = True
                        exit()
                    elif proov[i] == suva[0][1][i] and true == False:
                        blanks[i] = proov[i]
                for letter in proov:
                    if letter not in letters and letter in suva[0][1]:
                        letters.append(letter)
                    elif letter not in notletters and letter not in suva[0][1]:
                        notletters.append(letter)
                count.append("try")
                inc_letters = tk.Label(root, text=('Answer includes: '+','.join(letters)), bg='khaki')
                x_letters = tk.Label(root, text=("Answer doesn't include: "+','.join(notletters)), bg='IndianRed3')
                a = tk.Label(root, text=("".join(blanks)), bg='PaleGreen1')
                canvas1.create_window(200,200,window=inc_letters)
                canvas1.create_window(200,220,window=x_letters)
                canvas1.create_window(200,240,window=a)
                word.delete(0, 10)
                return None
            else:
                messagebox.showwarning("showwarning", "OH NO!!! This is not in the list")
                word.delete(0, 20)
                break
            


    s = tk.Label(root, text='Word please:', bg='tomato4', fg='white')
    enter = tk.Button(text='Enter', bg='bisque2', command=get_word)
    canvas1.create_window(200, 140, window=word)
    canvas1.create_window(200, 120, window=s)
    canvas1.create_window(200, 170, window=enter)
    integer = 5
    blanks = ["-","-","-","-","-"]
    ühendus = sqlite3.connect('data.db')
    c = ühendus.cursor()
    number = random.randint(1, 2315)
    c.execute(f"SELECT * FROM five WHERE ID = ?", [number])
    suva = c.fetchall()
    ühendus.commit()
    
def letter6():
    count = ["try"]
    word = tk.Entry(root)
    def get_word():
        true = False
        while len(count) < 8:
            proov = word.get()
            if len(proov) != 6:
                messagebox.showwarning("showwarning", "OH NO!!! This is not in the list")
                word.delete(0, 10)
                return None
                break
            c.execute(f"SELECT * FROM Allowed6 WHERE allowed = ?", [proov])
            sona = c.fetchall()
            if len(count) >= 6:
                messagebox.showinfo("WORD", "The word was: "+suva[0][1])
                c.close()
                ühendus.close()
                exit()
            if sona != []:
                sona = sona[-1][0]
            if proov in sona:
                for i in range(integer):
                    if proov == suva[0][1]:
                        messagebox.showinfo("U won!", "U so smartest! Be proud of yourself!")
                        true = True
                        exit()
                    elif proov[i] == suva[0][1][i] and true == False:
                        blanks[i] = proov[i]
                for letter in proov:
                    if letter not in letters and letter in suva[0][1]:
                        letters.append(letter)
                    elif letter not in notletters and letter not in suva[0][1]:
                        notletters.append(letter)
                count.append("try")
                inc_letters = tk.Label(root, text=('Answer includes: '+','.join(letters)), bg='khaki')
                x_letters = tk.Label(root, text=("Answer doesn't include: "+','.join(notletters)), bg='IndianRed3')
                a = tk.Label(root, text=("".join(blanks)), bg='PaleGreen1')
                canvas1.create_window(200,200,window=inc_letters)
                canvas1.create_window(200,220,window=x_letters)
                canvas1.create_window(200,240,window=a)
                word.delete(0, 10)
                return None
            else:
                messagebox.showwarning("showwarning", "OH NO!!! This is not in the list")
                word.delete(0, 20)
                break
        
    s = tk.Label(root, text='Word please:', bg='tomato4', fg='white')
    enter = tk.Button(text='Enter', bg='lavender', command=get_word)
    canvas1.create_window(200, 140, window=word)
    canvas1.create_window(200, 120, window=s)
    canvas1.create_window(200, 170, window=enter)
    integer = 6
    blanks = ["-","-","-","-","-","-"]
    ühendus = sqlite3.connect('data.db')
    c = ühendus.cursor()
    number = random.randint(1, 1049)
    c.execute(f"SELECT * FROM six WHERE ID = ?", [number])
    suva = c.fetchall()
    ühendus.commit()
    
def letter7():
    count = ["try"]
    word = tk.Entry(root)
    def get_word():
        true = False
        while len(count) < 9:
            proov = word.get()
            if len(proov) != 7:
                messagebox.showwarning("showwarning", "OH NO!!! This is not in the list")
                word.delete(0, 10)
                return None
                break
            c.execute(f"SELECT * FROM Allowed7 WHERE allowed = ?", [proov])
            sona = c.fetchall()
            if len(count) >= 7:
                messagebox.showinfo("WORD", "The word was: "+suva[0][1])
                c.close()
                ühendus.close()
                exit()
            if sona != []:
                sona = sona[-1][0]
            if proov in sona:
                for i in range(integer):
                    if proov == suva[0][1]:
                        messagebox.showinfo("U won!", "U so smartest! Be proud of yourself!")
                        true = True
                        exit()
                    elif proov[i] == suva[0][1][i] and true == False:
                        blanks[i] = proov[i]
                for letter in proov:
                    if letter not in letters and letter in suva[0][1]:
                        letters.append(letter)
                    elif letter not in notletters and letter not in suva[0][1]:
                        notletters.append(letter)
                        
                count.append("try")
                inc_letters = tk.Label(root, text=('Answer includes: '+','.join(letters)), bg='khaki')
                x_letters = tk.Label(root, text=("Answer doesn't include: "+','.join(notletters)), bg='IndianRed3')
                a = tk.Label(root, text=("".join(blanks)), bg='PaleGreen1')
                canvas1.create_window(200,200,window=inc_letters)
                canvas1.create_window(200,220,window=x_letters)
                canvas1.create_window(200,240,window=a)
                word.delete(0, 10)
                return None
            else:
                messagebox.showwarning("showwarning", "OH NO!!! This is not in the list")
                word.delete(0, 20)
                break
        
    s = tk.Label(root, text='Word please:', bg='tomato4', fg='white')
    enter = tk.Button(text='Enter', bg='LightBlue1', command=get_word)
    canvas1.create_window(200, 140, window=word)
    canvas1.create_window(200, 120, window=s)
    canvas1.create_window(200, 170, window=enter)
    integer = 7
    blanks = ["-","-","-","-","-","-","-"]
    ühendus = sqlite3.connect('data.db')
    c = ühendus.cursor()
    number = random.randint(1, 1371)
    c.execute(f"SELECT * FROM seven WHERE ID = ?", [number])
    suva = c.fetchall()
    ühendus.commit()
    

    
button1 = tk.Button(text='FIVE', bg = 'bisque2', command=letter5)
button2 = tk.Button(text='SIX', bg = 'lavender', command=letter6)
button3 = tk.Button(text='SEVEN', bg = 'LightBlue1', command=letter7)
label1 = tk.Label(root, text='How many letters?', bg='tomato4', fg='white')
canvas1.create_window(200, 20, window=label1)
canvas1.create_window(150, 50, window=button1)
canvas1.create_window(200,50, window=button2)
canvas1.create_window(250, 50, window=button3)

root.mainloop()