#imports tkinter
from tkinter import *
from tkinter import filedialog
import os

#opens the window, sets the title, and size
root = Tk()
root.title("Multi-Game-Player")
root.geometry("1280x800")

#adds a photo
photo = PhotoImage(file="mpg.png")
label = Label(root, image = photo)
label.pack()

play_game = PhotoImage(file='opengame.png')

exit_image = PhotoImage(file = 'exit.png')

img_label = Label(image=play_game)
#img_label.pack(pady=20)


#defining to open any program
def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    #opens the files
    os.system('"%s"' % my_program)





    
#buttons to open the program and exit the GUI
my_button = Button(root, image=play_game, command=open_program, borderwidth=0,)
my_button.pack(pady=0,)
my_button.place(x=800, y=300) 

exit_button = Button(root, image=exit_image, command=root.destroy, borderwidth=0)
exit_button.pack(pady=20)
exit_button.place(x=800, y=600)




#adding labels to act as a button 
my_label = Label(root, text = "")
my_label.pack(pady=20)

my_label2 = Label(image=exit_image)
#my_label2.pack(pady=20)

root.mainloop()