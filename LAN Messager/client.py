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
from tkinter import scrolledtext, ttk, filedialog, font, messagebox
from inspect import getsourcefile
from os.path import abspath
from functools import reduce
import time
import os, json
import time, base64
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

root.geometry("700x850")
root.overrideredirect(True)
 
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


buttonframe.bind('<B1-Motion>', on_mouse_drag)
buttonframe.bind('<ButtonPress-1>', on_mouse_press)

buttonframe.pack(padx=0, pady=0, fill="x")
buttonframe.config(width=3, height=0, bg = "gainsboro", highlightthickness=1, highlightbackground="gray")

button1=Button(buttonframe, text=" × ", font=("arial", 13))
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

hennay = False
num = 3

def thread():
    global hennay, server_process, imageserver_process, num

    if not hennay:
        hennay = True

        # Start subprocesses
        server_process = subprocess.Popen(['python', 'server.py'])
        imageserver_process = subprocess.Popen(['python', 'imageserver.py'])

        hostbutton.config(text="\nSTOP HOSTING CONVO\n")
        num = num-1
        messagebox.showinfo("LAN Messager", f"Started Hosting Server on {socket.gethostname()}.")

    else:
        hennay = False

        if server_process:
            server_process.terminate()
        if imageserver_process:
            imageserver_process.terminate()

        hostbutton.config(text="\nHOST CONVERSATION\n")
        messagebox.showwarning("LAN Messager", f"Stopped Hosting Server on {socket.gethostname()}.\nYou have {num} more FREE server hosts remaining.")

server_process = False
imageserver_process = False

def quitpy():
    if server_process:
        server_process.terminate()
    if imageserver_process:
        imageserver_process.terminate()
    root.destroy()

button1.config(width=3, height=0, fg = "black", bg = "gainsboro", activebackground="red", activeforeground="white", borderwidth=0, command=quitpy)

def host():
    thread1 = threading.Thread(target=thread)
    thread1.start()



myfont = font.Font(family="SimSun", size=20, weight="bold")

hostbutton=Button(buttonframe2, text="\nHOST CONVERSATION\n", font=myfont)
hostbutton.config(width=20, height=0, fg = "gray", bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, command=host)
hostbutton.grid(row=0, column=0)


frameborder = Frame(root, bg = "gray")
frameborder.place(x=0, y=450, relwidth=1.0, relheight=0.2)

actualframe=Frame(frameborder, bg="gainsboro")
actualframe.pack(padx = 2, pady = 2, fill=tk.BOTH, expand=True)


image = PhotoImage(file="image.png")
imageframe = Label(root, image=image)
imageframe.place(x=532, y=457.5)

imageframe2 = Label(root, image=image)
imageframe2.place(x=8.5, y=457.5)

discount = Label(root, text=" 30% OFF! ", bg="red", fg="white", font = "cambria 40 bold")
discount.place(x=217, y=470)

def flash():
    while True:
        try:
            discount.config(bg="red", fg="white")
            time.sleep(0.5)
            discount.config(bg="gainsboro", fg="gray")
            time.sleep(0.4)
        except:
            pass

flashthread = threading.Thread(target=flash)
flashthread.start()


freetrial = Label(root, text = "Get a physical copy before\nyour free trial runs out!", font="cambria 16", bg="gainsboro", fg="black", anchor = "nw")
freetrial.place(x=230, y=545, anchor = "nw")










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

textbox = Entry(textboxborder, font = ("cambria 20"), width = 25, fg="gray65")

submit = Button(root, text=("SEND"), font = ("ARIAL 15"), width = 7, bg = "gainsboro", activebackground="lightgray", activeforeground="white")

openfile = Button(root, text=("+"), font = ("ARIAL 15"), width = 7, bg = "gainsboro", activebackground="lightgray", activeforeground="white")



opensockets = []
imagesused = []
image_frames = []


stop_flag = threading.Event()


def join():
    entrybutton.config(state=DISABLED)

    try:
        server_hostname = entername.get()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_hostname, 5555))
 
        opensockets.append(client_socket)
        
        client_socket.close()
        error.config(text=(""))

        if name.get() == "" or name.get() == "Enter Name":
            entrybutton.config(state=NORMAL)
            error.config(text=(">> ERROR: You have to enter a name, dumbass."))
        
        else:
            entrybutton.config(state=NORMAL)
            convo_name = name.get()
            error.config(text=(""))
            
            stop_flag.clear()

            def receive_images():
                try:
                    while not stop_flag.is_set():
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
                                
                                new_width = bg.width()
                                new_height = bg.height()

                                while new_width > 300 or new_height > 200:
                                    new_width = round(new_width*0.95)
                                    new_height = round(new_height*0.95)


                                bg = bg.subsample(bg.width() // new_width, bg.height() // new_height)


                                frame = Label(myframe, image=bg, anchor="w", compound="left")
                                frame['bg'] = "white"
                                frame.image = bg
                                frame.pack(fill="both", expand=False, padx=77)

                                image_frames.append(frame)

                                labele.pack_forget()
                                labele.pack()

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
                    while not stop_flag.is_set():
                        try:
                            try:
                                received_info = client_socket2.recv(1024).decode()
                            except:
                                continue
                            
                            parts = received_info.split("__SEPARATOR__")
                            image_size = int(parts[2])
                            message = parts[1]

                            received_data = b''

                            while len(received_data) < image_size:
                                data = client_socket2.recv(1024)
                                if not data:
                                    break
                                received_data += data

                            timestamp = int(time.time())
                            image_path = f"profile_{timestamp}.png"

                            with open(image_path, 'wb') as file:
                                file.write(received_data)
                                print(f"Profile picture saved to {image_path}")

                            try:
                                if parts[1] != "+4407925532041 call me":
                                    myframe2 = Frame(myframe, bg="white")
                                    myframe2.pack(padx=5, pady=7, anchor="nw")

                                    buttonframe1 = Frame(myframe2, width=200, bg="white")  
                                    buttonframe1.columnconfigure(0, weight=1)
                                    buttonframe1.columnconfigure(1, weight=1)

                                    buttonframe1.pack(anchor="nw", padx=12)
                                    buttonframe1.pack_propagate(False)

                                    bg = PhotoImage(file=image_path)
                                    new_width = 50
                                    new_height = 50
                                    bg = bg.subsample(bg.width() // new_width, bg.height() // new_height)

                                    profile_picture_label = Label(buttonframe1, image=bg, anchor="w")
                                    profile_picture_label['bg'] = "white"
                                    profile_picture_label.image = bg
                                    profile_picture_label.grid(row=0, column=0, rowspan=2, padx=(0, 5))  

                                    name1 = str(parts[0])

                                    input_string = message
                                    text_widget = Text(buttonframe1, wrap="word", font=("cambria 16 bold"), width=35, height=1, borderwidth=0)
                                    text_widget.insert("end", name1)
                                    text_widget.config(state=DISABLED)
                                    text_widget.grid(row=0, column=1, sticky="w")

                                    input_string = message
                                    chars_per_line = 40


                                    lines = [input_string[i:i + chars_per_line] for i in range(0, len(input_string), chars_per_line)]


                                    if len(lines) > 0:
                                        label = Text(buttonframe1, wrap="word", font=("cambria 16"), width=40, height=round((len(lines[0]) / 40)), borderwidth=0)
                                        label.insert("end", lines[0])
                                        label.config(state=DISABLED)
                                        label.grid(row=1, column=1, sticky="w")

                                    if len(lines) > 1:
                                        for i, line in enumerate(lines[1:]):
                                            text_widget = Text(myframe2, wrap="word", font=("cambria 16"), width=40, height=round((len(line) / 40)), borderwidth=0)
                                            text_widget.insert("end", line)
                                            text_widget.config(state=DISABLED)
                                            text_widget.pack(anchor="w", padx=74)
                                
                                else:                                  
                                    formatted_parts = parts[0].title()

                                    text_widget = Text(myframe, wrap="word", font=("cambria", 17), width=50, height=1, borderwidth=0, fg = "gray", bg="white")
                                    text_widget.pack(padx = 15, pady = 20)

                                    # Insert the formatted text with different tags for formatting
                                    text_widget.insert("end", formatted_parts, "bold")
                                    text_widget.insert("end", " has joined the conversation! (hello)", "italic")

                                    # Configure tags for formatting
                                    text_widget.tag_configure("bold", font=("cambria", 17, "bold"))
                                    text_widget.tag_configure("italic", font=("cambria", 17, "italic"))

                                    text_widget.config(state=DISABLED)



                                labele.pack_forget()
                                labele.pack()

                                mycanvas.update_idletasks()
                                mycanvas.config(scrollregion=mycanvas.bbox("all"))
                                mycanvas.yview_moveto(1.0)




                                def osremove():
                                    time.sleep(0.1)
                                    try:
                                        os.remove(image_path)
                                    except:
                                        pass

                                skibidi_ohio_thread = threading.Thread(target=osremove)
                                skibidi_ohio_thread.start()


                            except TclError:
                                os.remove(image_path)
                                continue

                        except (OSError, ConnectionAbortedError) as e:
                            print(f"Error receiving profile pictures: {e}")
                            break

                finally:
                    client_socket2.close()





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



            
            def send(textmessage, image):
                if textbox.get() != "" and textbox.get() != "Say Something" or image == True:
                    if enterpfp.get() != "":
                        image_path = enterpfp.get()
                        try:
                            test = PhotoImage(file=image_path)
                        except TclError:
                            image_path = "pfp.png"
                    else:
                        image_path = "pfp.png"


                    message = textmessage
                    client_socket6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    opensockets.append(client_socket6)

                    try:
                        client_socket6.connect((server_hostname, 5555))

                        with open(image_path, 'rb') as file:
                            image_data = file.read()
                        print("")

                        name1 = name.get()

                        image_size = len(image_data)
                        client_socket6.sendall(str(name1+"__SEPARATOR__"+message+"__SEPARATOR__"+str(image_size)).encode())

                        ack = client_socket6.recv(1024).decode()
                        if ack == 'ACK':
                            client_socket6.sendall(image_data)
                            print("Image sent successfully!")
                            client_socket5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            client_socket5.connect((server_hostname, 5555))
                            opensockets.append(client_socket5)



                        else:
                            print("Server did not acknowledge. Image not sent.")
                        
                        textbox.delete(0, tk.END)

                    except Exception as e:
                        print(f"Error: {e}")

                    finally:
                        try:
                            client_socket5.close()
                        except:
                            pass
                        client_socket6.close()
                
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

            enterpfp.pack()
            pfpbutton.pack()
            pfplabel.pack()
            entryborder3.pack()
            
            entryborder.pack_forget()
            entryborder2.pack_forget()
            name.pack_forget()
            entername.pack_forget()
            error.pack_forget()
            serverlabel.pack_forget()
            namelabel.pack_forget()
            entrybutton.pack_forget()

            enterpfp.pack_forget()
            pfpbutton.pack_forget()
            pfplabel.pack_forget()
            entryborder3.pack_forget()




            


            mycanvas.pack(side=RIGHT, fill="both", expand="yes")

            yscrollbar.pack(side=RIGHT, fill="y")


            wrapper.pack(fill="both", expand="yes")


            frame3.pack(fill=tk.BOTH)
            frame3['bg']="gainsboro"
            frame3.pack()

            label4.pack(pady=15)

            textboxborder.place(x=100, y = 795)

            def on_enter(event):
                send(textbox.get(), False)

            def remove_temp_text(e):
                if textbox.get()=="Say Something":
                    textbox.delete(0,"end")
                    textbox.config(fg="black")
                else:
                    pass

            def temp_text(e):
                if textbox.get()=="":
                    textbox.insert(0, "Say Something")
                    textbox.config(fg="gray65")
                else:
                    pass


            textbox.pack(pady = 2, padx = 2)
            textbox.bind("<Return>", on_enter)
            textbox.bind("<FocusIn>", remove_temp_text)
            textbox.bind("<FocusOut>", temp_text)
            


            submit.config(command=lambda: send(textbox.get(), False))
            submit.place(x=500, y = 795)

            def sendimage():
                file = str(filedialog.askopenfilenames(title="Choose PNG"))
                file = file.replace(",", "")
                file = file.replace("')", "")
                image_path = file.replace("('", "")

                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                try:
                    client_socket.connect((server_hostname, 5556))

                    with open(image_path, 'rb') as file:
                        image_data = file.read()
                    print(image_data)

                    image_size = len(image_data)
                    client_socket.sendall(str(image_size).encode())

                    ack = client_socket.recv(1024).decode()
                    if ack == 'ACK':
                        client_socket.sendall(image_data)
                        print("Image sent successfully!")
                        client_socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket3.connect((server_hostname, 5555))
                        opensockets.append(client_socket3)




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

                    whattosend = f"is sending an image..."

                    send(whattosend, True)
                    print("ok bro")



            openfile.place(x=37, y = 795)
            openfile.config(command = sendimage, width = 3)


            labele = Label(myframe, text="", font=("cambria 60"), bg="white")


            send("+4407925532041 call me", True)


            mycanvas.update_idletasks()
            mycanvas.config(scrollregion=mycanvas.bbox("all"))
            mycanvas.yview_moveto(1.0)

            textbox.delete(0,"end")
            textbox.config(fg="black")



            
            

            
            

            

            

    except OSError:
        entrybutton.config(state=NORMAL)
        error.config(text=(">> ERROR: That's not a computer connected to this network."))
        client_socket.close()
        


def startjoin():
    join1 = threading.Thread(target=join)
    join1.start()


def pfp():
    file = str(filedialog.askopenfilenames(title="Choose PNG"))
    file = file.replace(",", "")
    file = file.replace("')", "")
    image_path = file.replace("('", "")

    enterpfp.config(state=NORMAL)
    enterpfp.delete(0, tk.END)
    enterpfp.insert(tk.END, image_path)
    enterpfp.config(state=DISABLED)



entryborder = Frame(root, bg ="gray")
entryborder2 = Frame(root, bg ="gray")
entryborder3 = Frame(root, bg ="gray")

def remove_temp_text2(e):
    if name.get()=="Enter Name":
        name.delete(0,"end")
        name.config(fg="black")
    else:
        pass

def temp_text2(e):
    if name.get()=="":
        name.insert(0, "Enter Name")
        name.config(fg="gray65")
    else:
        pass


name = Entry(entryborder2, width=24, font =("cambria 16"), fg="gray65")
name.insert(0, "Enter Name")
name.bind("<FocusIn>", remove_temp_text2)
name.bind("<FocusOut>", temp_text2)

def remove_temp_text3(e):
    if entername.get()=="Enter PC":
        entername.delete(0,"end")
        entername.config(fg="black")
    else:
        pass

def temp_text3(e):
    if entername.get()=="":
        entername.insert(0, "Enter PC")
        entername.config(fg="gray65")
    else:
        pass

entername = Entry(entryborder, width=20, font =("cambria 16"), fg="gray65")
entername.insert(0, "Enter PC")
entername.bind("<FocusIn>", remove_temp_text3)
entername.bind("<FocusOut>", temp_text3)

enterpfp = Entry(entryborder3, width=17, font =("cambria 16"))
enterpfp.config(state=DISABLED)
error = Label(root, bg="white", fg="red", text=(""), font =("cambria 12"))
serverlabel = Label(root, text =("Enter Name of Host's Computer:"), font = ("cambria 16"), bg="white", fg="gray")
namelabel = Label(root, text =("Enter Name you want to display:"), font = ("cambria 16"), bg="white", fg="gray")
pfplabel = Label(root, text =("Choose a profile picture:"), font = ("cambria 16"), bg="white", fg="gray")
entrybutton = Button(root, text = ("JOIN"), font = ("arial 11"), bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, width = 4, command=startjoin)
pfpbutton = Button(root, text = ("CHOOSE"), font = ("arial 11"), bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, width = 8, command=pfp)


def startagain():
    global image_frames, labele

    stop_flag.set()



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

    frameborder.place(x=0, y=450, relwidth=1.0, relheight=0.2)
    actualframe.pack(padx = 2, pady = 2, fill=tk.BOTH, expand=True)
    imageframe.place(x=532, y=457.5)
    imageframe2.place(x=8.5, y=457.5)
    discount.place(x=217, y=470)
    freetrial.place(x=230, y=545, anchor = "nw")






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

    entryborder3.place(x=200, y=500)
    
    name.pack(pady=1, padx=1)

    serverlabel.place(x=200, y = 260)
    
    namelabel.place(x=200, y = 360)
    
    pfplabel.place(x=200, y = 460)

    pfpbutton.place(x=415, y=500)

    enterpfp.pack(padx=1, pady=1)

    frameborder.pack()
    actualframe.pack()
    imageframe.pack()
    imageframe2.pack()
    discount.pack()
    freetrial.pack()

    frameborder.pack_forget()
    actualframe.pack_forget()
    imageframe.pack_forget()
    imageframe2.pack_forget()
    discount.pack_forget()
    freetrial.pack_forget()




    

    error.place(x=10, y = 700)
    


myfont = font.Font(family="SimSun", size=20, weight="bold")

joinbutton=Button(buttonframe2, text="\nJOIN CONVERSATION\n", font=myfont)
joinbutton.config(width=20, height=0, fg = "gray", bg = "gainsboro", activebackground="lightgray", activeforeground="white", borderwidth=2, command=choose)
joinbutton.grid(row=0, column=1)



text=Label(frame1, text="_________________________________________________________________________\n\n Carbon positive since 2023:                        \n https://github.com/PengeSal/LAN-Messager\n_________________________________________________________________________", font=("arial", 16), bg="white", fg="lightgray")
text.pack(pady=25, side= TOP, anchor="w")





root.mainloop()








