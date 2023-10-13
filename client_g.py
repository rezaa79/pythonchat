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





client = socket.socket()
client.connect((ip , 12345))

root = Tk()


def send():
    data_send = get_text.get()
    if data_send != "":
        client.send(data_send)
        labal = Label(root , text=data_send , bg="red" , fg="white")
        labal.pack(fill=X , side=TOP)
        get_text.delete(0 , END)

def recv():
    while True:
        data_recv = client.recv(1024)
        label = Label(root , text=data_recv , bg="blue" , fg="white")
        label.pack(fill=X , side=TOP)


button = Button(root , text="Send" , command=send)
get_text = Entry(root)

button.pack(fill=X , side=BOTTOM)
get_text.pack(fill=X , side=BOTTOM)

threading.Thread(target=recv).start()

root.geometry("400x600")
root.title("client")
root.resizable(width=False , height=False)


root.mainloop()