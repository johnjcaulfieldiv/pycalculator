# basic calculator program to learn tkinter
# 
# John Caulfield
#
# 3/24/18

import tkinter as tk
from tkinter import Grid

# create window component
master = tk.Tk()
master.title("Calculator")
master.geometry("180x220")

# solution display label
solntext = tk.StringVar()
solntext.set("")
soln = tk.Label(master, textvariable=solntext).grid(column=0, row=0, columnspan=4, sticky="NSEW")

# string to display if improper equation is executed
errStr = "error: invalid equation"

# Functions
def cmd1():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("1")
	else:
		solntext.set(solntext.get() + "1")	
def cmd2():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("2")
	else:
		solntext.set(solntext.get() + "2")	
def cmd3():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("3")
	else:
		solntext.set(solntext.get() + "3")	
def cmd4():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("4")
	else:
		solntext.set(solntext.get() + "4")	
def cmd5():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("5")
	else:
		solntext.set(solntext.get() + "5")	
def cmd6():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("6")
	else:
		solntext.set(solntext.get() + "6")	
def cmd7():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("7")
	else:
		solntext.set(solntext.get() + "7")	
def cmd8():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("8")
	else:
		solntext.set(solntext.get() + "8")	
def cmd9():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("9")
	else:
		solntext.set(solntext.get() + "9")	
def cmd0():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set("0")
	else:
		solntext.set(solntext.get() + "0")	
def cmddecimal():
    eqlist = solntext.get().split(" ")
    if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
        solntext.set(".")
    else:
        solntext.set(solntext.get() + ".")
def cmddivide():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr:
		solntext.set("/")
	elif len(eqlist) > 1 and eqlist[-2] == "=":
		solntext.set(eqlist[-1] + " / ")
	else:
		solntext.set(solntext.get() + " / ")
def cmdmultiply():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr:
		solntext.set("*")
	elif len(eqlist) > 1 and eqlist[-2] == "=":
		solntext.set(eqlist[-1] + " * ")
	else:
		solntext.set(solntext.get() + " * ")
def cmdadd():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr:
		solntext.set("+")
	elif len(eqlist) > 1 and eqlist[-2] == "=":
		solntext.set(eqlist[-1] + " + ")
	else:
		solntext.set(solntext.get() + " + ")
def cmdsubtract():
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr:
		solntext.set("-")
	elif len(eqlist) > 1 and eqlist[-2] == "=":
		solntext.set(eqlist[-1] + " - ")
	else:
		solntext.set(solntext.get() + " - ")
def cmdclear():
	solntext.set("")
def isvalidequation(equationstr):
	eqlist = equationstr.split(" ")
	for i in range(len(eqlist)):
		if eqlist[i].count(".") > 1:
			return False
		if i % 2 == 0:
			if eqlist[i] in ("+-*/"):
				return False
		else: # i % 2 == 1
			if eqlist[i] not in ("+-*/"):
				return False
			else:				
				if eqlist[i] == "/" and eqlist[i+1] not in ("+-*/"): # check for div by zero error
					if eqlist[i+1].count(".") > 1 or float(eqlist[i+1]) == 0:
						return False
	return True	
def cmdequals():
	equationstr = solntext.get()
	if isvalidequation(equationstr):
		solntext.set(solntext.get() + " = " + str(eval(equationstr)))
	else:
		solntext.set(errStr)

# button1
button1 = tk.Button(master, text="1", command=cmd1).grid(column=0, row=1, sticky="NSEW")
# button2
button2 = tk.Button(master, text="2", command=cmd2).grid(column=1, row=1, sticky="NSEW")
# button3
button3 = tk.Button(master, text="3", command=cmd3).grid(column=2, row=1, sticky="NSEW")
# buttondivide
buttondivide = tk.Button(master, text="/", command=cmddivide).grid(column=3, row=1, sticky="NSEW")
#button4
button4 = tk.Button(master, text="4", command=cmd4).grid(column=0, row=2, sticky="NSEW")
# button5
button5 = tk.Button(master, text="5", command=cmd5).grid(column=1, row=2, sticky="NSEW")
# button6
button6 = tk.Button(master, text="6", command=cmd6).grid(column=2, row=2, sticky="NSEW")
# buttonmultiply
buttonmultiply = tk.Button(master, text="*", command=cmdmultiply).grid(column=3, row=2, sticky="NSEW")
# button7
button7 = tk.Button(master, text="7", command=cmd7).grid(column=0, row=3, sticky="NSEW")
# button8
button8 = tk.Button(master, text="8", command=cmd8).grid(column=1, row=3, sticky="NSEW")
# button9
button9 = tk.Button(master, text="9", command=cmd9).grid(column=2, row=3, sticky="NSEW")
# buttonsubtract
buttonsubtract = tk.Button(master, text="-", command=cmdsubtract).grid(column=3, row=3, sticky="NSEW")
# button0
button0 = tk.Button(master, text="0", command=cmd0).grid(column=0, row=4, columnspan=2, sticky="NSEW")
# buttondecimal
buttondecimal = tk.Button(master, text=".", command=cmddecimal).grid(column=2, row=4, sticky="NSEW")
# buttonadd
buttonadd = tk.Button(master, text="+", command=cmdadd).grid(column=3, row=4, sticky="NSEW")
# buttonclear
buttonclear = tk.Button(master, text="clr", command=cmdclear).grid(column=0, row=5, columnspan=2, sticky="NSEW")
# buttonequals
buttonequals = tk.Button(master, text="=", command=cmdequals).grid(column=2, row=5, columnspan=3, sticky="NSEW")

# set grid weights so components expand to fill window
for x in range(4):
	Grid.columnconfigure(master, x, weight=1)
for y in range(5):
    Grid.rowconfigure(master, y, weight=1)

def main():
	master.mainloop()
	
if __name__ == "__main__":
	main()