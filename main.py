#!C:\Program Files\Python36\python.exe
import Preveade, os, sys, pyaudio, wave
from tkinter import *
from tkinter.colorchooser import *
from tkinter import ttk
import planetmapping


class recording:

    def __init__(self, filename="file.wav"):
        if filename.endswith("\n"):
            filename = filename[0:len(filename)-1]
        self.filename = filename

    def rec(self):
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 5
        if not self.filename.endswith(".wav"):
            self.filename = self.filename + ".wav"
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        print("recording...")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("finished recording")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        waveFile = wave.open(self.filename, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()


class CA:

    def __init__(self, master):
        self.color = "black"
        self.ok = False
        self.incanvas = ""
        self.canvas = Canvas(master, height=300, width=500, bg="white")
        self.pop = Menu(master, tearoff=0)
        self.pop.add_command(label="save", command=self.save_c)
        self.pop.add_command(label="open", command=self.open_c)
        self.canvas.bind("<Control-s>", self.save_c)
        self.canvas.bind("<Control-o>", self.open_c)
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.bind("<Button-3>", self.do_popup_c)
        self.ent = Entry(master)
        self.ent.bind("<Button-3>", self.do_popup_c)
        self.ent.bind("<Control-s>", self.save_c)
        self.ent.bind("<Control-o>", self.open_c)
        self.canvas.pack()
        self.ent.pack(side=BOTTOM)

    def do_popup_c(self, event):
        try:
            self.pop.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.pop.grab_release()

    def save_c(self, event=None):
        try:
            try:
                with open(self.ent.get(), "w") as file:
                    file.write(self.incanvas)
            except PermissionError:
                self.ent.insert(0, "Permission deniered")
        except OSError:
            self.ent.insert(0, "Imppossible to save")

    def open_c(self, event=None):
        try:
            try:
                with open(self.ent.get(), "r") as file:
                    inf = file.readlines()[0]
                    splitted = inf.split("-")
                    n = 0
                while n <= len(splitted):
                    selected = splitted[n]
                    try:
                        self.xco = int(splitted[n+1])
                        self.yco = int(splitted[n+2])
                    except IndexError:
                        pass
                    if selected == "line":
                        self.canvas.create_line(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]) , fill=splitted[n+5])
                        n += 6
                    elif selected == "foval":
                        self.canvas.create_oval(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]), fill=splitted[n+5])
                        n += 6
                    elif selected == "oval":
                        self.canvas.create_oval(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]))
                        n += 5
                    elif selected == "frectangle":
                        self.canvas.create_rectangle(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]), fill=splitted[n+5])
                        n += 6
                    elif selected == "rectangle":
                        self.canvas.create_rectangle(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]))
                        n += 5
                    elif selected == "farc":
                        self.canvas.create_arc(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]), fill=splitted[n+5])
                        n += 6
                    elif selected == "arc":
                        self.canvas.create_arc(self.xco, self.yco, int(splitted[n+3]), int(splitted[n+4]))
                        n += 5
                    else:
                        self.canvas.create_text(self.xco, self.yco, text=selected, fill=splitted[n+3])
                        n += 4
            except PermissionError:
                self.ent.insert(0, "Permission deniered")
        except FileNotFoundError:
            self.ent.insert(0, "File not found")

    def callback(self, event=None):
        selected = self.ent.get()
        if selected == "chcolor":
            self.color = askcolor()[0]
            print(self.color)
        elif self.ok == False:
            self.xco = event.x
            self.yco = event.y
            self.ok = True
        else:
            if selected == "line":
                self.canvas.create_line(self.xco, self.yco, event.x, event.y, fill=self.color)
                self.incanvas = self.incanvas + "line-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-" + self.color  + "-"
            elif selected == "foval":
                self.canvas.create_oval(self.xco, self.yco, event.x, event.y, fill=self.color)
                self.incanvas = self.incanvas + "foval-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-" + self.color  + "-"
            elif selected == "oval":
                self.canvas.create_oval(self.xco, self.yco, event.x, event.y)
                self.incanvas = self.incanvas + "oval-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-"
            elif selected == "frectangle":
                self.canvas.create_rectangle(self.xco, self.yco, event.x, event.y, fill=self.color)
                self.incanvas = self.incanvas + "frectangle-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-" + self.color  + "-"
            elif selected == "rectangle":
                self.canvas.create_rectangle(self.xco, self.yco, event.x, event.y)
                self.incanvas = self.incanvas + "rectangle-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-"
            elif selected == "farc":
                self.canvas.create_arc(self.xco, self.yco, event.x, event.y, fill=self.color)
                self.incanvas = self.incanvas + "farc-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-" + self.color  + "-"
            elif selected == "arc":
                self.canvas.create_arc(self.xco, self.yco, event.x, event.y)
                self.incanvas = self.incanvas + "arc-" + str(self.xco) + "-" + str(self.yco) + "-" + str(event.x) + "-" + str(event.y) + "-"
            else:
                self.canvas.create_text(event.x, event.y, text=selected, fill=self.color)
                self.incanvas = self.incanvas + selected + "-" + str(event.x) + "-" + str(event.y) + "-" + self.color  + "-"
            self.ok = False


class planetmapping:

    def __init__(self, master, *args, **kwargs):
        self.ax = ""
        self.ay = ""
        self.ok = True
        self.p = True
        self.i = []
        self.frame = Frame(master, bg="white")
        self.l1 = Label(self.frame, text=">>>")
        self.v1 = StringVar()
        self.e1 = Entry(self.frame, textvariable=self.v1, width=50)
        self.b1 = Button(self.frame, text="canc", command=self.c)
        self.canvas = Canvas(self.frame, height=500, width=850, bg="#0084FF")
        self.canvas.bind("<Button-1>", self.callback)
        self.s1 = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.s2 = Scrollbar(self.frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.canvas["yscrollcommand"] = self.s1.set
        self.canvas["xscrollcommand"] = self.s2.set
        self.lf1 = LabelFrame(self.frame, text="dimensions")
        self.l2 = Label(self.lf1, text="height")
        self.v2 = IntVar()
        self.e2 = Entry(self.lf1, textvariable=self.v2)
        self.l3 = Label(self.lf1, text="width")
        self.v3 = IntVar()
        self.e3 = Entry(self.lf1, textvariable=self.v3)
        self.b2 = Button(self.lf1, text="resize", command=self.r)
        self.l4 = Label(self.frame, text="")
        self.lf2 = LabelFrame(self.frame, text="options")
        self.b3 = Button(self.lf2, text="Salva", command=self.s)
        self.b4 = Button(self.lf2, text="Apri", command=self.a)
        self.b5 = Button(self.lf2, text="esporta come png", command=self.e)
        self.frame.pack()
        self.l1.grid(row=0, column=0)
        self.e1.grid(row=0, column=1)
        self.b1.grid(row=0, column=2)
        self.canvas.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.s1.grid(row=1, column=3, sticky="nsew")
        self.s2.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.lf1.grid(row=3, column=0, columnspan=3)
        self.l2.grid(row=0, column=0)
        self.e2.grid(row=0, column=1)
        self.l3.grid(row=0, column=2)
        self.e3.grid(row=0, column=3)
        self.b2.grid(row=0, column=4)
        self.l4.grid(row=4, column=0, columnspan=3)
        self.lf2.grid(row=5, column=0, columnspan=3)
        self.b3.grid(row=0, column=0)
        self.b4.grid(row=0, column=1)
        self.b5.grid(row=0, column=2)

    def callback(self, event):
        x = event.x
        y = event.y
        if self.ok == True:
            if self.ax != "" and self.ay != "":
                self.canvas.create_line(self.ax, self.ay, x, self.ay)
                self.canvas.create_line(x, self.ay, x, y, arrow=LAST)
                self.i.append(["l", self.ax, self.ay, x, self.ay, "n"])
                self.i.append(["l", x, self.ay, x, y, "y"])
                z = y - self.ay
                if z < 0:
                    y = y - 5
                elif z > 0:
                    y = y + 5
            self.canvas.create_text(x, y, text=self.v1.get())
            self.i.append(["t", x, y, self.v1.get()])
            self.ok = False
        else:
            self.ok = True
        if self.p == False:
            self.ax = x
            self.ay = y - 5
        self.p = False

    def c(self):
        self.canvas.delete(ALL)
        self.i = []

    def r(self):
        x = self.v2.get()
        y = self.v3.get()
        self.canvas.configure(height=x, width=y)

    def s(self, event=None):
        try:
            f = ""
            for argument in self.i:
                for abc in argument:
                    f = f + str(abc) + "\n"
            with open(self.v1.get(), "w") as file:
                file.write(f)
            self.l4.configure(text="saved")
        except PermissionError:
            self.l4.configure(text="permission deniered")

    def a(self, event=None):
        try:
            try:
                l = False
                t = False
                co = []
                with open(self.v1.get(), "r") as file:
                    for linea in file.readlines():
                        if linea.endswith("\n"):
                            linea = linea[0:len(linea)-1]
                        if l == True:
                            if linea == "y":
                                l = False
                                self.canvas.create_line(co[0], co[1], co[2], co[3], arrow=LAST)
                                self.i.append(["l", co[0], co[1], co[2], co[3], "y"])
                            elif linea == "n":
                                l = False
                                self.canvas.create_line(co[0], co[1], co[2], co[3])
                                self.i.append(["l", co[0], co[1], co[2], co[3], "n"])
                            else:
                                co.append(int(linea))
                        elif t == True:
                            try:
                                co.append(int(linea))
                            except ValueError:
                                self.canvas.create_text(co[0], co[1], text=linea)
                                self.i.append(["t", co[0], co[1], linea])
                                t = False
                        elif linea == "l":
                            l = True
                            co = []
                        elif linea == "t":
                            t = True
                            co = []
                self.l4.configure(text="opened")
            except PermissionError:
                self.l4.configure(text="permission deniered")
        except FileNotFoundError:
            self.l4.configure(text="can't open")

    def e(self, event=None):
        f = self.v1.get() + ".ps"
        self.canvas.postscript(file=f, colormode="color")
        with open(f, "r") as file:
            a = ""
            for linea in file.readlines():
                a = a + linea + "\n"


class IO:

    def __init__(self, master):
        self.alpha = Preveade.preveade()
        self.ok = False
        self.dx = 27
        self.dy = 3
        self.bg = "white"
        self.fg = "black"
        self.fs = "Times"
        self.fd = 10
        self.cr = "target"
        try:
            with open("main.py", "r") as file:
                readed = file.readlines()
                for linea in readed:
                    if linea.endswith("\n"):
                        linea = linea[0:len(linea)-1]
                    if linea.startswith("#\\"):
                        splitted = linea.split("\\")
                        if splitted[1] == "dx":
                            self.dx = int(splitted[2])
                        if splitted[1] == "dy":
                            self.dy = int(splitted[2])
                        if splitted[1] == "cr":
                            self.cr = splitted[2]
                        if splitted[1] == "fs":
                            self.fs = splitted[2]
                        if splitted[1] == "fd":
                            self.fd = int(splitted[2])
        except(FileNotFoundError, OSError):
            pass
        try:
            try:
                with open(sys.argv[1], "r") as file:
                    for line in self.alpha.decide(file.readlines()):
                        self.start = self.start + line + "\n"
            except IndexError:
                with open("self.start.ps", "r") as file:
                    for line in self.alpha.decide(file.readlines()):
                        self.start = self.start + line + "\n"
        except (FileNotFoundError, NameError):
            self.start = "benvenuto"
        n = 0
        self.root = Frame(master, bg=self.bg, cursor=self.cr)
        self.root.pack()
        self.popup = Menu(self.root, tearoff=0)
        self.popup.add_command(label="save", command=self.save)
        self.popup.add_command(label="open", command=self.open)
        self.popup.add_command(label="execute", command=self.execute)
        self.popup.add_command(label="record", command=self.record)
        self.popup.add_separator()
        self.popup.add_command(label="exit", command=lambda :master.quit())

    def stdio(self):
        self.e = Text(self.root, height=self.dy, width=self.dx, font=(self.fs, self.fd), bg=self.bg, fg=self.fg)
        self.l = Label(self.root, text=self.start, font=(self.fs, self.fd), bg=self.bg, fg=self.fg)
        self.e.bind("<Button-3>", self.do_popup)
        self.l.bind("<Button-3>", self.do_popup)
        self.e.bind("<F5>", self.execute)
        self.e.bind("<Control-s>", self.save)
        self.e.bind("<Control-o>", self.open)
        self.e.bind("<Control-r>", self.record)
        self.e.bind("<Control-i>", self.settings)
        self.e.pack()
        self.l.pack()

    def C(self):
        self.fn = Tk()
        self.fn.title("preveade | Canvas")
        self.fn["cursor"] = self.cr
        try:
            self.fn.wm_iconbitmap("favicon.ico")
        except TclError:
            pass
        self.fn.resizable(height=False, width=False)
        a = CA(self.fn)
        self.fn.mainloop()

    def P(self):
        self.pmp = Tk()
        self.pmp.title("preveade | Planetmapping")
        try:
            self.pmp.wm_iconbitmap("favicon.ico")
        except TclError:
            pass
        self.pmp.resizable(height=False, width=False)
        alba = planetmapping(self.pmp)
        self.pmp.mainloop()

    def save(self, event=None):
        try:
            try:
                t = self.e.get(1.0, END)
                l = t.split("!")
                with open(l[0], "w") as file:
                    file.write(l[1])
                self.l.config(text="file saved")
            except PermissionError:
                self.l.config(text="permission deniered")
        except OSError:
            self.l.config(text="impossible to save")

    def open(sefl, event=None):
        try:
            try:
                try:
                    t = self.e.get(1.0, END)
                    l = t.split("!")
                    with open(l[0], "r") as file:
                        r = ""
                        for aa in file.readlines():
                            r = r + aa
                        e.insert(0, r)
                    self.l.config(text="file saved")
                except FileNotFoundError:
                    self.l.config(text="file not found")
            except PermissionError:
                self.l.config(text="permission deniered")
        except OSError:
                self.l.config(text="impossible to open")

    def execute(self, event=None):
        t = self.e.get(1.0, END)
        if t.startswith("P"):
            self.P()
        elif t.startswith("C"):
            self.C()
        else:
            a = ""
            for argument in self.alpha.decide(t.split(" ")):
                a = a + argument + "\n"
            self.l.config(text=a)

    def record(self, event=None):
        try:
            t = self.e.get(1.0, END)
            a = recording(filename=t)
            a.rec()
            self.l.config(text="recorded")
        except PermissionError:
            self.l.config(text="permission deniered")

    def do_popup(self, event):
        try:
            self.popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup.grab_release()

    def settings(self, event=None):
        self.se = Tk()
        self.se.title("preveade | settings")
        try:
            self.se.wm_iconbitmap("favicon.ico")
        except TclError:
            pass
        self.se.resizable(height=False, width=False)
        self.dim = LabelFrame(self.se, text="dimensions")
        self.sc1 = Scale(self.dim, from_=0, to=200, orient=HORIZONTAL, label="width")
        self.sc2 = Scale(self.dim, from_=0, to=200, orient=VERTICAL, label="height")
        self.col = LabelFrame(self.se, text="style")
        self.l1 = Label(self.col, text="Cursor")
        self.vob = StringVar()
        self.box = ttk.Combobox(self.col, textvariable=self.vob)
        self.box["values"] = ("select Cursor", "shuttle", "arrow", "spider", "target")
        self.box.current(0)
        self.l2 = Label(self.col, text="Font")
        self.v1 = StringVar()
        self.vob2 = StringVar()
        self.box2 = ttk.Combobox(self.col, textvariable=self.vob2)
        self.box2["values"] = ("select char", "Times", "Arial")
        self.box2.current(0)
        self.sc3 = Scale(self.col, from_=0, to=50, orient=HORIZONTAL, label="Font size")
        self.b3 = Button(self.se, text="apply", command=self.apply)
        self.dim.grid(row=0, column=0, sticky="nsew")
        self.sc1.grid(row=0, column=0)
        self.sc2.grid(row=0, column=1)
        self.col.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.l1.pack()
        self.box.pack()
        self.l2.pack()
        self.box2.pack()
        self.sc3.pack()
        self.b3.grid(row=0, column=2, sticky="nsew", rowspan=2)
        self.se.mainloop()

    def activate(self):
        self.cvsi = "1"

    def deactivate(self):
        self.cvsi = "0"

    def apply(self):
        towrite = ""
        y = int(self.sc1.get())
        x = self.sc2.get()
        z = self.sc3.get()
        cr = self.box.get()
        fs = self.box2.get()
        if x != 0:
            towrite = towrite + "\n#\\dx\\" + str(x)
        if y != 0:
            towrite = towrite + "\n#\\dy\\" + str(y)
        if z != 0:
            towrite = towrite + "\n#\\fd\\" + str(z)
        if fs != self.fs and fs != "select char":
            towrite = towrite + "\n#\\fs\\" + fs
        if cr != self.cr and cr != "select Cursor":
            towrite = towrite + "\n#\\cr\\" + cr
        if self.cvsi != self.ac:
            towrite = towrite + "\n#\\ac\\" + self.cvsi
        try:
            with open("main.py", "a") as file:
                file.write(towrite)
        except (PermissionError, OSError):
            self.l.config(text="impossible to change settings")
        self.se.destroy()

if __name__ == "__main__":
    r = Tk()
    r.title("preveade")
    try:
        r.wm_iconbitmap("favicon.ico")
    except TclError:
        pass
    r.resizable(height=False, width=False)
    a = IO(r)
    a.stdio()
    r.mainloop()
