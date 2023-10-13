import threading
import socket
import time
from Tkinter import *

ip = ""


root1 = Tk()

def ip_get():
    global ip
    ip = get_ip.get()
    root1.destroy()


get_ip = Entry(root1)
label = Label(root1 , text="Enter ip:")
button1 = Button(root1 , text="set ip" , command=ip_get)

label.grid()
get_ip.grid()
button1.grid()



root1.mainloop()

server = socket.socket()
server.bind((ip , 12345))
server.listen(2)
con , addr = server.accept()


root = Tk()

canvas = Canvas(root)
scrollbar = Scrollbar(root , orient="vertical" , command=canvas.yview)
frame = Frame(canvas)


def send():
    data_send = edit_Text.get()
    if data_send != "":
        con.send(data_send)
        label = Label(frame , text=data_send , bg="red" , fg="white")
        label.pack(side=TOP , fill=X)
        edit_Text.delete(0 , END)





def recv():
    while True:
        data_recv = con.recv(1024)
        label = Label(frame , text=data_recv , bg="blue" , fg="white")
        label.pack(side=TOP , fill=X)


def update():
    while True:
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
        time.sleep(2)



button = Button(root , text="Send" , command=send)
edit_Text = Entry(root)



button.pack(fill=X , side=BOTTOM)
edit_Text.pack(fill=X , side=BOTTOM)

canvas.pack(fill="both" , side="left" ,  expand=True)
scrollbar.pack(fill="y" , side="right")
canvas.create_window(0,0,anchor='nw', window=frame)
canvas.update_idletasks()


threading.Thread(target=recv).start()
threading.Thread(target=update).start()

root.geometry("400x600")
root.title("server")
root.resizable(width=False , height=False)
root.mainloop()