from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("Tic Tac Toe by RIO")

click = True

def checker(buttons):
    global click
    if buttons['text']== " " and click:
        buttons['text']= "X"
        click = False
    elif buttons['text'] == " " and click == False:
        buttons['text']= "O"
        click = True

    if (
        button1['text']=="X" and button2['text']=="X" and button3['text']=="X" or
        button1['text']=="X" and button4['text']=="X" and button7['text']=="X" or
        button1['text']=="X" and button5['text']=="X" and button9['text']=="X" or
        button2['text']=="X" and button5['text']=="X" and button8['text']=="X" or
        button3['text']=="X" and button6['text']=="X" and button9['text']=="X" or
        button4['text']=="X" and button5['text']=="X" and button6['text']=="X" or
        button7['text']=="X" and button8['text']=="X" and button9['text']=="X" or
        button3['text']=="X" and button5['text']=="X" and button7['text']=="X" 
    ):
        tkinter.messagebox.showinfo("CONGRATULATIONS","Winner is X")
    elif(
        button1['text']=="O" and button2['text']=="O" and button3['text']=="O" or
        button1['text']=="O" and button4['text']=="O" and button7['text']=="O" or
        button1['text']=="O" and button5['text']=="O" and button9['text']=="O" or
        button2['text']=="O" and button5['text']=="O" and button8['text']=="O" or
        button3['text']=="O" and button6['text']=="O" and button9['text']=="O" or
        button4['text']=="O" and button5['text']=="O" and button6['text']=="O" or
        button7['text']=="O" and button8['text']=="O" and button9['text']=="O" or
        button3['text']=="O" and button5['text']=="O" and button7['text']=="O"
    ):
        tkinter.messagebox.showinfo("CONGRATULATIONS","Winner is O")




buttons = StringVar()

button1 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button1),bd=10)
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button2),bd=10)
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button3),bd=10)
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button4),bd=10)
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button5),bd=10)
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button6),bd=10)
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button7),bd=10)
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8= Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button8),bd=10)
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9 = Button(root,text=" ",font=("Arial 40"),bg="Brown",fg="white",height=2,width=4,command=lambda:checker(button9),bd=10)
button9.grid(row=3,column=2,sticky=S+N+E+W)



root.mainloop()