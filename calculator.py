""" 
basic calculator program to learn tkinter
 
John Caulfield

3/24/18
"""

import tkinter as tk

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
def cmd_numeric(n):
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr or (len(eqlist) > 1 and eqlist[-2] == "="):
		solntext.set(n)
	else:
		solntext.set(solntext.get() + n)

def cmd_operator(op):
	eqlist = solntext.get().split(" ")
	if solntext.get() == errStr:
		solntext.set(op)
	elif len(eqlist) > 1 and eqlist[-2] == "=":
		solntext.set(eqlist[-1] + " {} ".format(op))
	else:
		solntext.set(solntext.get() + " {} ".format(op))

def cmdclear():
	solntext.set("")

def is_valid_equation(equationstr):
	eqlist = equationstr.split(" ")
	for i in range(len(eqlist)):
		if eqlist[i].count(".") > 1:
			return False
		if i % 2 == 0:
			if eqlist[i] in ("+-*/") or eqlist[i][0] in ("+-*/"):
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
	if is_valid_equation(equationstr):
		solntext.set(solntext.get() + " = " + str(eval(equationstr)))
	else:
		solntext.set(errStr)

# buttons
button1 = tk.Button(master, text="1", command=lambda: cmd_numeric("1")).grid(column=0, row=1, sticky="NSEW")
button2 = tk.Button(master, text="2", command=lambda: cmd_numeric("2")).grid(column=1, row=1, sticky="NSEW")
button3 = tk.Button(master, text="3", command=lambda: cmd_numeric("3")).grid(column=2, row=1, sticky="NSEW")
buttondivide = tk.Button(master, text="/", command=lambda: cmd_operator("/")).grid(column=3, row=1, sticky="NSEW")
button4 = tk.Button(master, text="4", command=lambda: cmd_numeric("4")).grid(column=0, row=2, sticky="NSEW")
button5 = tk.Button(master, text="5", command=lambda: cmd_numeric("5")).grid(column=1, row=2, sticky="NSEW")
button6 = tk.Button(master, text="6", command=lambda: cmd_numeric("6")).grid(column=2, row=2, sticky="NSEW")
buttonmultiply = tk.Button(master, text="*", command=lambda: cmd_operator("*")).grid(column=3, row=2, sticky="NSEW")
button7 = tk.Button(master, text="7", command=lambda: cmd_numeric("7")).grid(column=0, row=3, sticky="NSEW")
button8 = tk.Button(master, text="8", command=lambda: cmd_numeric("8")).grid(column=1, row=3, sticky="NSEW")
button9 = tk.Button(master, text="9", command=lambda: cmd_numeric("9")).grid(column=2, row=3, sticky="NSEW")
buttonsubtract = tk.Button(master, text="-", command=lambda: cmd_operator("-")).grid(column=3, row=3, sticky="NSEW")
button0 = tk.Button(master, text="0", command=lambda: cmd_numeric("0")).grid(column=0, row=4, columnspan=2, sticky="NSEW")
buttondecimal = tk.Button(master, text=".", command=lambda: cmd_numeric(".")).grid(column=2, row=4, sticky="NSEW")
buttonadd = tk.Button(master, text="+", command=lambda: cmd_operator("+")).grid(column=3, row=4, sticky="NSEW")
buttonclear = tk.Button(master, text="clr", command=cmdclear).grid(column=0, row=5, columnspan=2, sticky="NSEW")
buttonequals = tk.Button(master, text="=", command=cmdequals).grid(column=2, row=5, columnspan=3, sticky="NSEW")

# set grid weights so components expand to fill window
for x in range(4):
	tk.Grid.columnconfigure(master, x, weight=1)
for y in range(5):
    tk.Grid.rowconfigure(master, y, weight=1)

def main():
	master.mainloop()
	
if __name__ == "__main__":
	main()