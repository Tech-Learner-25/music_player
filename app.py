# ---- Importing important libraries ----
import tkinter as tk
from pygame import mixer
from PIL import ImageTk
from tkinter import filedialog

mixer.init()

class MusicPlayer:
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.master.title("Music Player")
        self.master.geometry('400x400')

        # ---- Creating Function to Open File ----
        def openfile():
            global filename
            filename = filedialog.askopenfilename()
            self.head['text'] = filename

        def info():
            tk.messagebox.showinfo('About Us', "Music player app created by Muhammad Zaher Rasheed")

        #---- Adding Menu icons ----
        self.menu = tk.Menu(self.master)
        self.master.configure(menu=self.menu)

        self.submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label='Open', command=openfile)
        self.submenu.add_command(label='Close', command=self.master.destroy)

        self.submenu2 = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Help', menu=self.submenu2)
        self.submenu2.add_command(label='Open', command=info)
        self.submenu2.add_command(label='Exit', command=self.master.destroy)

        #----- Actual App Design ---

        self.head = tk.Label(self.master, text= "Open Music File For Playing", font= ('Halvetica', 16))
        self.head.pack()

        self.label = tk.Label(self.master, text='Lets run it', font= ("Halvetica", 14), bg='black', fg='white')
        self.label.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Addition Music Display Image ---
        self.photo = ImageTk.PhotoImage(file='images\music-display.jpeg')
        photo = tk.Label(self.master, image=self.photo).place(x=50, y=60)

        # --- Functions for play, pause and stop music
        def play_music():
            self.scale_var.set(25)

            try:
                paused
            except:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label['text'] = 'Music Playing'
                except:
                    tk.messagebox.showerror('Error', 'File could not found')
            else:
                mixer.music.unpause()
                self.label['text'] = 'Music Resumed'

        def pause_music():
            global paused
            paused = True
            mixer.music.pause()
            self.label['text'] = 'Music Paused'

        def stop_music():
            mixer.music.stop()
            self.label['text'] = 'Music Stopped'
            self.scale_var.set(0)


        #--- Play, Pause And Stop Buttons ---
        self.play_btn = ImageTk.PhotoImage(file='images\play-music.png')
        play_btn = tk.Button(self.master, image=self.play_btn, bd=0, command=play_music).place(x=60, y=270, width=40, height=45)

        self.pause_btn = ImageTk.PhotoImage(file='images\pause-music.png')
        pause_btn = tk.Button(self.master, image=self.pause_btn, bd=0, command=pause_music).place(x=120, y=270, width=40, height=45)

        self.stop_btn = ImageTk.PhotoImage(file='images\stop-music.png')
        stop_btn = tk.Button(self.master, image=self.stop_btn, bd=0, command=stop_music).place(x=180, y=270, width=40, height=45)

        # --- function for volume up and down ----
        def volume(vol):
            global volume
            volume = int(vol)/100
            mixer.music.set_volume(volume)

            if volume == 0:
                mixer.music.stop()
                self.label['text'] = 'volume low'
            else:
                mixer.music.play()
                self.label['text'] = 'Music Playing'


        #--- Adding Scale ----
        self.scale_var = tk.IntVar()
        self.scale_var.set(25)
        self.scale = tk.Scale(self.master, variable=self.scale_var, from_=0, to=100, orient=tk.HORIZONTAL, length= 100, command=volume).place(x=240, y=270)
    def start (self):
        self.master.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayer(root)
    app.start()