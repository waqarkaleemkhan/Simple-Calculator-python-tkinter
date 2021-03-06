from tkinter import *

root =Tk()
root.title("Simple Calculator")

inputField=Entry(root,width=35,borderwidth=2)
inputField.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
	current = inputField.get() #use this to enter number in proper way like calculator
	inputField.delete(0,END) #this will delete the previous number which is in the number parameter if we don;t do this it put all the previous number in the screen
	inputField.insert(0,str(current)+str(number))


def button_clear():
	inputField.delete(0,END)

def button_add():
	first_number=inputField.get()
	global f_num # we use global variable becuase we are going to accsess this from out side of the function with equal and addition function
	global math
	math="addition"
	f_num=int(first_number)
	inputField.delete(0,END)
def button_equal():
	second_number=inputField.get()
	inputField.delete(0,END)
	if math=="addition":
		inputField.insert(0,f_num+int(second_number))
	if math=="multiplication":
		inputField.insert(0,f_num*int(second_number))
	if math=="division":
		inputField.insert(0,f_num/int(second_number))
	if math=="subtraction":
		inputField.insert(0,f_num-int(second_number))
def button_mul():
	first_number=inputField.get()
	global f_num # we use global variable becuase we are going to accsess this from out side of the function with equal and addition function
	global math
	math="multiplication"
	f_num=int(first_number)
	inputField.delete(0,END)
def button_sub():
	first_number=inputField.get()
	global f_num # we use global variable becuase we are going to accsess this from out side of the function with equal and addition function
	global math
	math="subtraction"
	f_num=int(first_number)
	inputField.delete(0,END)
def button_div():
	first_number=inputField.get()
	global f_num # we use global variable becuase we are going to accsess this from out side of the function with equal and addition function
	global math
	math="division"
	f_num=int(first_number)
	inputField.delete(0,END)

button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_addition=Button(root,text="+",padx=39,pady=20,command=button_add)
button_clear=Button(root,text="Clear",padx=79,pady=20,command=button_clear)
button_equal=Button(root,text="=",padx=91,pady=20,command=button_equal)
button_mul=Button(root,text="*",padx=39,pady=20,command=button_mul)
button_div=Button(root,text="/",padx=39,pady=20,command=button_div)
button_sub=Button(root,text="-",padx=39,pady=20,command=button_sub)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_addition.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_sub.grid(row=5,column=2)
button_div.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)

root.mainloop()