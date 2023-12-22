import socket
import subprocess
import shutil
import tkinter as tk
import threading, webbrowser
import os
import sys
import ctypes, random
from tkinter import *
from tkinter.ttk import Style, Frame as fp
from tkinter import scrolledtext, ttk, filedialog, font
from inspect import getsourcefile
from os.path import abspath
from functools import reduce
import time
import os
import time
import importlib.util
from pip._internal import main as pipmain
import winreg as reg
from tkinter import Tk, font


root = Tk()
root['bg']="white"

def toggle(event):
    if event.type == EventType.Map:
        root.deiconify()
        root.lift()
    else:
         root.withdraw()

top = Toplevel(root)
top.geometry('0x0+10000+10000') 
top.protocol('WM_DELETE_WINDOW', root.destroy)
top.bind("<Map>", toggle)
top.bind("<Unmap>", toggle)
top.title(f"LAN Messager | {socket.gethostname()}")

#icon = PhotoImage(file = "icon.ico")
root.geometry("700x850")
root.overrideredirect(True)
#root.iconphoto(True, icon)
 
buttonframe=Frame(root)

for i in range(5):
    buttonframe.columnconfigure(1, weight=1)

def on_mouse_press(evt):
    global xp, yp
    xp = evt.x
    yp = evt.y

def on_mouse_drag(evt):
    deltax = evt.x - xp
    deltay = evt.y - yp
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

def quitpy():
    root.destroy()


buttonframe.bind('<B1-Motion>', on_mouse_drag)
buttonframe.bind('<ButtonPress-1>', on_mouse_press)

buttonframe.pack(padx=0, pady=0, fill="x")
buttonframe.config(width=3, height=0, bg = "gainsboro", highlightthickness=1, highlightbackground="gray")

button1=Button(buttonframe, text=" × ", font=("arial", 13))
button1.config(width=3, height=0, fg = "black", bg = "gainsboro", activebackground="red", activeforeground="white", borderwidth=0, command=quitpy)
button1.grid(row=0, column=7)

button3=Button(buttonframe, text=" - ", font=("arial", 13))
button3.config(width=3, height=0, fg = "black", bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=0, command=top.iconify)
button3.grid(row=0, column=6)

myfont = font.Font(family="SimSun", size=15)

text=Label(buttonframe, text=f"LAN Messager | {socket.gethostname()}", font=myfont, fg = "gray", bg = "gainsboro")
text.place(x=10,y=2)

text.bind('<B1-Motion>', on_mouse_drag)

frame1 = Frame(root, highlightthickness=1, highlightbackground="gray")
frame1['bg']="white"
frame1.pack(fill=tk.BOTH, expand=True)

text1=Label(frame1, text="\n\n", font=("arial", 16), bg="white", fg="#97d180")
text1.pack(pady=20, side= TOP, anchor="w")

bg = PhotoImage(file= "logo.png")
frame = Label(frame1, image=bg)
frame.pack(pady=25)
frame['bg']="white"
frame.pack(fill=tk.BOTH, expand=False)

def callback(url):
    webbrowser.open_new_tab(url)

frame.bind("<Button-1>", lambda e: callback("https://github.com/PengeSal/LAN-Messager"))


frame2 = Label(frame1, image=bg)


#STARTAGAINWAS HERE 


buttonframe2=Frame(frame1)
buttonframe2.config(bg="white")
buttonframe2.columnconfigure(0, weight=1)
buttonframe2.columnconfigure(1, weight=1)
buttonframe2.pack(fill=tk.BOTH)
buttonframe2.pack(fill=tk.BOTH, expand=True)
buttonframe2.pack()

def host():
    pass


myfont = font.Font(family="SimSun", size=20, weight="bold")

hostbutton=Button(buttonframe2, text="\nHOST CONVERSATION\n", font=myfont)
hostbutton.config(width=20, height=0, fg = "gray", bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, command=host)
hostbutton.grid(row=0, column=0)




wrapper=LabelFrame(frame1)
wrapper['bg']='white'
wrapper.configure(borderwidth=0)

style = ttk.Style()
style.theme_use('clam')

style.configure("Vertical.TScrollbar", gripcount=0, background="gray95", darkcolor="gainsboro", lightcolor="gainsboro", troughcolor="gainsboro", bordercolor="gray", arrowcolor="black")
            
mycanvas=Canvas(wrapper, width=600,height=200, bg="white")

yscrollbar=ttk.Scrollbar(mycanvas, orient="vertical", command=mycanvas.yview)

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas['bg']='white'
mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion= mycanvas.bbox("all")))
mycanvas.configure(borderwidth=0, highlightthickness=0)

myframe=Frame(mycanvas)
myframe['bg']='white'
myframe.configure(borderwidth=0)
mycanvas.create_window((0,0), window=myframe, anchor="w")

wrapper["bg"]="white"

frame3 = Frame(root, highlightthickness=1, highlightbackground="gray")
frame3['bg']="gainsboro"

label4 = Label(frame3, text = ("deez"), font = ("cambria 20"), fg = "gainsboro", bg="gainsboro")

textboxborder = Frame(root, bg = "gray")

textbox = Entry(textboxborder, font = ("cambria 20"), width = 25)

submit = Button(root, text=("SEND"), font = ("ARIAL 15"), width = 7, bg = "gainsboro", activebackground="lightgray", activeforeground="white")

openfile = Button(root, text=("+"), font = ("ARIAL 15"), width = 7, bg = "gainsboro", activebackground="lightgray", activeforeground="white")



opensockets = []
imagesused = []
image_frames = []


def join():
    entrybutton.config(state=DISABLED)
    try:
        server_hostname = entername.get()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_hostname, 5555))
 
        opensockets.append(client_socket)
        
        client_socket.close()
        error.config(text=(""))

        if name.get() == "":
            entrybutton.config(state=NORMAL)
            error.config(text=(">> ERROR: You have to enter a name, dumbass."))
        
        else:
            entrybutton.config(state=NORMAL)
            convo_name = name.get()
            error.config(text=(""))
            

            def receive_images():
                try:
                    while True:
                        try:
                            image_size = int(client_socket4.recv(1024).decode().replace("image:", ""))
                            received_data = b''

                            while len(received_data) < image_size:
                                data = client_socket4.recv(1024)
                                if not data:
                                    break
                                received_data += data

                            timestamp = int(time.time())
                            image_path = f"image_{timestamp}.png"

                            with open(image_path, 'wb') as file:
                                file.write(received_data)
                                print(f"Image saved to {image_path}")

                            try:
                                bg = PhotoImage(file=image_path)
                                effective_height = min(500, bg.height())

                                frame = Label(myframe, image=bg, anchor="w", compound="left", width=150, height=effective_height)
                                frame['bg'] = "white"
                                frame.image = bg
                                frame.pack(fill="both", expand=False)

                                image_frames.append(frame)

                                label = Text(myframe, wrap="word", font=("cambria 16"), width=55, height=1, borderwidth=0)
                                label.pack(anchor="w")

                                mycanvas.update_idletasks()
                                mycanvas.config(scrollregion=mycanvas.bbox("all"))
                                mycanvas.yview_moveto(1.0)

                                os.remove(image_path)

                            except TclError:
                                os.remove(image_path)
                                continue

                        except (OSError, ConnectionAbortedError) as e:
                            print(f"Error receiving images: {e}")
                            break

                finally:
                    client_socket4.close()




            def receive_messages():
                try:
                    while True:
                        data = client_socket2.recv(1024).decode("utf-8")

                        reply = data
                        input_string = f" >> {reply}"

                        chars_per_line = 75

                        lines = [input_string[i:i + chars_per_line] for i in range(0, len(input_string), chars_per_line)]

                        for line in lines:
                            label = Text(myframe, wrap="word", font=("cambria 16"), width=55, height=round((len(line) / 55)), borderwidth=0)
                            label.pack(anchor="w")
                            label.insert(tk.END, line)
                            label.config(state=DISABLED)

                        mycanvas.update_idletasks()
                        mycanvas.config(scrollregion=mycanvas.bbox("all"))
                        mycanvas.yview_moveto(1.0)

                except ConnectionAbortedError:
                    pass

            client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            opensockets.append(client_socket2)
            client_socket2.connect((server_hostname, 5555))

            receive_thread = threading.Thread(target=receive_messages)
            receive_thread.start()



            client_socket4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            opensockets.append(client_socket4)
            client_socket4.connect((server_hostname, 5556))

            image_receive_thread = threading.Thread(target=receive_images)
            image_receive_thread.start()



            def send():
                if textbox.get() != "":
                    message = textbox.get()
                    message = f"{convo_name}: {message}"
                    client_socket2.send(message.encode('utf-8'))

                    input_string = f" >> {message}"

                    
                    chars_per_line = 75

                    
                    lines = [input_string[i:i + chars_per_line] for i in range(0, len(input_string), chars_per_line)]

                    for line in lines:
                        label = Text(myframe, wrap="word", font=("cambria 16"), width = 55, height = round((len(line)/55)), borderwidth=0)
                        label.pack(anchor="w")                   
                        label.insert(tk.END, line)
                        label.config(state=DISABLED)

                    mycanvas.update_idletasks()
                    mycanvas.config(scrollregion=mycanvas.bbox("all"))
                    mycanvas.yview_moveto(1.0)

                    textbox.delete(0, tk.END)
                else:
                    pass


            
            bg = PhotoImage(file= "logo2.png")
            frame.config(image=bg)
            frame.image = bg
            frame.pack(pady=25)
            text1.pack_forget()
            text.pack_forget()
            buttonframe2.pack_forget()

            entryborder.pack()
            entryborder2.pack()
            name.pack()
            entername.pack()
            error.pack()
            serverlabel.pack()
            namelabel.pack()
            entrybutton.pack()
            
            entryborder.pack_forget()
            entryborder2.pack_forget()
            name.pack_forget()
            entername.pack_forget()
            error.pack_forget()
            serverlabel.pack_forget()
            namelabel.pack_forget()
            entrybutton.pack_forget()
            


            mycanvas.pack(side=RIGHT, fill="both", expand="yes")

            yscrollbar.pack(side=RIGHT, fill="y")


            wrapper.pack(fill="both", expand="yes")


            frame3.pack(fill=tk.BOTH)
            frame3['bg']="gainsboro"
            frame3.pack()

            label4.pack(pady=15)

            textboxborder.place(x=100, y = 795)

            def on_enter(event):
                send()

            textbox.pack(pady = 2, padx = 2)
            textbox.bind("<Return>", on_enter)


            submit.config(command=send)
            submit.place(x=500, y = 795)

            def sendimage():
                file = str(filedialog.askopenfilenames())

                file = file.replace(",", "")
                file = file.replace("')", "")
                image_path = file.replace("('", "")

                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                try:
                    client_socket.connect((server_hostname, 5556))

                    with open(image_path, 'rb') as file:
                        image_data = file.read()

                    image_size = len(image_data)
                    client_socket.sendall(str(image_size).encode())

                    ack = client_socket.recv(1024).decode()
                    if ack == 'ACK':
                        client_socket.sendall(image_data)
                        print("Image sent successfully!")
                        client_socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket3.connect((server_hostname, 5555))
                        opensockets.append(client_socket3)

                        message = f"{convo_name} is sending an image..."
                        client_socket3.send(message.encode('utf-8'))



                    else:
                        print("Server did not acknowledge. Image not sent.")

                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    try:
                        client_socket3.close()
                    except:
                        pass
                    client_socket.close()



            openfile.place(x=28, y = 795)
            openfile.config(command = sendimage, width = 3)



            message = f"{convo_name} has joined the conversation! (say hello)"
            client_socket2.send(message.encode('utf-8'))

            input_string = f" >> {message}"

            chars_per_line = 75
            
            lines = [input_string[i:i + chars_per_line] for i in range(0, len(input_string), chars_per_line)]

            for line in lines:
                label = Text(myframe, wrap="word", font=("cambria 16"), width = 55, height = round((len(line)/55)), borderwidth=0)
                label.pack(anchor="w")                   
                label.insert(tk.END, line)
                label.config(state=DISABLED)

            mycanvas.update_idletasks()
            mycanvas.config(scrollregion=mycanvas.bbox("all"))
            mycanvas.yview_moveto(1.0)
            

            
            

            

            

    except OSError:
        entrybutton.config(state=NORMAL)
        error.config(text=(">> ERROR: That's not a computer connected to this network."))
        client_socket.close()
        


def startjoin():
    join1 = threading.Thread(target=join)
    join1.start()
    


entryborder = Frame(root, bg ="gray")
entryborder2 = Frame(root, bg ="gray")
name = Entry(entryborder2, width=24, font =("cambria 16"))
entername = Entry(entryborder, width=20, font =("cambria 16"))
error = Label(root, bg="white", fg="red", text=(""), font =("cambria 12"))
serverlabel = Label(root, text =("Enter Name of Host's Computer:"), font = ("cambria 16"), bg="white", fg="gray")
namelabel = Label(root, text =("Enter Name you want to display:"), font = ("cambria 16"), bg="white", fg="gray")
entrybutton = Button(root, text = ("JOIN"), font = ("arial 11"), bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, width = 4, command=startjoin)


def startagain():
    global image_frames

    for widget in root.winfo_children():
        if widget != top:
            widget.pack()
            widget.pack_forget()

    for socket in opensockets:
        socket.close()


    buttonframe.pack(padx=0, pady=0, fill="x")
    text.place(x=10, y=2)
    frame1.pack(fill=tk.BOTH, expand=True)
    wrapper.pack_forget()
    frame.pack_forget()

    text1.pack(pady=20, side=TOP, anchor="w")
    frame2.image = bg
    frame2.pack(pady=25)
    frame2['bg'] = "white"
    frame2.pack(fill=tk.BOTH, expand=False)

    def callback(url):
        webbrowser.open_new_tab(url)

    frame2.bind("<Button-1>", lambda e: callback("https://github.com/PengeSal/LAN-Messager"))

    buttonframe2.pack(fill=tk.BOTH)
    buttonframe2.pack(fill=tk.BOTH, expand=True)
    buttonframe2.pack()
    hostbutton.grid(row=0, column=0)
    text.pack(pady=20, side=TOP, anchor="w")
    joinbutton.grid(row=0, column=1)






def choose():
    try:
        frame2.pack_forget()
    except NameError:
        pass


    home = Button(root, text = ("←"), font = ("arial 38 bold"), command = startagain, borderwidth = 0, bg = "white", fg = "gray", activebackground = "white", activeforeground = "lightgray")
    home.place(x=25, y=32)
    
    bg = PhotoImage(file= "logo2.png")
    frame.config(image=bg)
    frame.image = bg
    frame.pack(pady=25)
    text1.pack_forget()
    text.pack_forget()
    buttonframe2.pack_forget()


    entryborder.place(x=200, y=300)

    entername.pack(pady=1, padx=1)

    entrybutton.place(x=450, y=300)

    entryborder2.place(x=200, y=400)
    
    name.pack(pady=1, padx=1)

    serverlabel.place(x=200, y = 260)
    
    namelabel.place(x=200, y = 360)

    error.place(x=10, y = 560)
    




myfont = font.Font(family="SimSun", size=20, weight="bold")

joinbutton=Button(buttonframe2, text="\nJOIN CONVERSATION\n", font=myfont)
joinbutton.config(width=20, height=0, fg = "gray", bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, command=choose)
joinbutton.grid(row=0, column=1)



text=Label(frame1, text="_________________________________________________________________________\n\n Carbon positive since 2023:                        \n https://github.com/PengeSal/LAN-Messager\n_________________________________________________________________________", font=("arial", 16), bg="white", fg="lightgray")
text.pack(pady=25, side= TOP, anchor="w")





root.mainloop()



















