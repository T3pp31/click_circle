import tkinter as tk      

def click(e):
    canvas.create_oval(e.x-20,e.y-20,e.x+20,e.y+20,fill="red",width=0)

root=tk.Tk()
root.geometry("600x400")

canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

canvas.bind("<Button-1>", click)

root.mainloop()
