#!C:\Program Files\Python36\python.exe
# -*- coding: utf-8 -*-
#__name__ = "Preveade"
__version__ = 0.2
__autor__ = "dp"

import os, random
try:
    import sys
    import hashlib
    import subprocess
    import math
    import time
    import shutil
    import zipfile
    import socket
except(ImportError):
    pass
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class preveade:

    def __init__(self, *args, **kwargs):
        self.sa = False
        self.variables = {}
        self.blocks = {}
        self.path = os.getcwd()
        self.tpath = os.getcwd()
        self.timer = ""
        self.a = args
        self.s = ""
        self.connect = False
        self.nomes = {"I":1, "you":2, "she":3, "he":3, "it":3, "we":4, "you":5, "they":6, "Gimmi":3, "boss":2, "hospital":3}
        self.verbs = ["sleep", "have", "be", "move", "travel", "beat"]
        try:
            with open("story", "r") as file:
                try:
                    for coso in file.readlines()[0].split("-"):
                        if coso.split("_")[0] == "n":
                            d = coso.split("_")[1].split(":")
                            if int(d[1]) < 6 and int(d[1]) > 0:
                                self.nomes[d[0]] = int(d[1])
                            else:
                                pass
                        elif coso.split("_")[0] == "v":
                            d = coso.split("_")[1]
                            self.verbs.append(d)
                except IndexError:
                    pass
        except(FileNotFoundError):
            pass
        self.n = [argument for argument in self.nomes]
        print(self.n)
        self.mv = ["can", "will", "must", "could", "should", "would"]

    def decide(self, lists=None, *args, **kwargs):
        if lists != None:
            self.a = lists
        if  self.sa != False:
            self.a.insert(0, self.sa)
            self.a.insert(0, "e")
        for argument in args:
            self.a.append(argument)
        execut = True
        rt = []
        pitstop = 0
        num = 0
        vb = False
        timer = [0, 0, 0]
        l = False
        tl = []
        a = []
        cycles = [0]
        ll = []
        block = []
        executab = [True]
        bl = False
        continu = False
        continuum = ""
        for argument in self.a:
            while argument.endswith("\n"):
                argument = argument[0:len(argument)-1]
            if argument.startswith("|") and not argument.endswith("|"):
                continu = True
                continuum = argument
            elif argument.endswith("|") and not argument.startswith("|"):
                continu = False
                argument = continuum + " " + argument
            elif continu == True:
                continuum = continuum + " " + argument
            if continu == False:
                a.append(argument)
        self.a = a
        for argument in self.a:
            risultante = ""
            dp = self.dopo(num)
            dpdp = self.dopo(num+1)
            dpdpdp = self.dopo(num+2)
            pm = self.prima(num)
            if argument == "end":
                executab = executab[0:len(executab)-1]
                execut = executab[len(executab)-1]
            elif argument == "else":
                if False in executab[0:len(executab)-1]:
                    execut = False
                else:
                    execut = not execut
            elif execut:
                try:
                    try:
                        if argument == "}":
                            if l == True:
                                l = False
                                if dp == "var":
                                    self.a.insert(num+3, tl)
                                else:
                                    rt.append(tl)
                                tl = []
                            elif bl == True:
                                bl = False
                                self.blocks[block[0]] = block[1:len(block)]
                                block = []
                        elif l == True:
                            tl.append(argument)
                        elif bl == True:
                            block.append(argument)
                        elif argument == "gp":
                            with open("pp.py", "w") as file:
                                file.write("from tkinter import *\nroot = Tk()\nroot.attributes(\"-topmost\", True)\nroot.resizable(height=False, width=False)\nroot.overrideredirect(1)\nbtn = Button(root, text='ok', command=lambda: root.destroy()).pack()\nroot.mainloop()")
                        elif argument == "block":
                            bl = True
                        elif argument == "var":
                            try:
                                dp = self.a[num+1]
                            except IndexError:
                                pass
                            try:
                                if dpdp.startswith("|") and dpdp.endswith("|"):
                                    dpdp = dpdp[1:len(dpdp)-1]
                                    self.variables[dp] = dpdp
                                else:
                                    vb = True
                            except AttributeError:
                                self.variables[dp] = dpdp
                        elif argument == "list":
                            l = True
                        elif argument == "f":
                            self.a.insert(num+2, dp)
                        elif argument == "b":
                            try:
                                self.add_to_code(self.blocks[dp], num)
                            except KeyError:
                                rt.append("unknown block: " + dp)
                        elif argument == "print":
                            rt.append(str(dp))
                        elif argument == "if":
                            execut = False
                            if dpdp == "==":
                                if dp == dpdpdp:
                                    execut = True
                            if dpdp == "!=":
                                if dp != dpdpdp:
                                    execut = True
                            if dpdp == "<":
                                if dp < dpdpdp:
                                    execut = True
                            if dpdp == ">":
                                if dp > dpdpdp:
                                    execut = True
                            executab.append(execut)
                        elif argument == "point":
                            pitstop = num+1
                            cycles.append(pitstop)
                        elif argument == "repeat":
                            numerosecondo = num+1
                            try:
                                for x in range(int(dp)):
                                    for argo in self.a[pitstop:num]:
                                        self.a.insert(numerosecondo, argo)
                                        numerosecondo += 1
                            except ValueError:
                                rt.append("si ci aspetta un numero dopo: "+ argument)
                            if cycles[len(cycles)-1] > 0:
                                pitstop = cycles[len(cycles)-1]
                                cycles = cycles[0:len(cycles)-1]
                        elif argument == "pass":
                            continue
                        elif argument == "createimage":
                            with open("favicon.ico", "w") as file:
                                file.write("\x00\x00\x01\x00\x01\x00\x10\x10\x10\x00\x01\x00\x04\x00(\x01\x00\x00\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00€\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00frs\x00\x05ã÷\x00òÿ\x00\x00¼Ýà\x00ú…\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x05UUP\x00\x00\x10\x05P\x00\x00\x05P\x00\x00\x00\x00\x00\x00\x00\x05\x00\x05\x00\x0033\x00\x00P\x05\x00\x03\x00\x003\x00PP\x000\x00\x00\x03\x00\x05P\x03\x00\x04\x00\x000\x05P\x03\x00D \x000\x05P\x03\x00\x02 \x000\x05P\x03\x00\x00\x00\x000\x05P\x000\x00\x00\x03\x00\x05\x05\x003\x00\x003\x00P\x05\x00\x0033\x00\x00P\x00P\x00\x00\x00\x00\x05\x00\x00\x05P\x00\x00\x05P\x00\x00\x00\x05UUP\x00\x008\x1f\x00\x00'ç\x00\x00ßû\x00\x00¬=\x00\x00³Í\x00\x00sî\x00\x00lö\x00\x00lv\x00\x00nv\x00\x00oö\x00\x00wî\x00\x00³Í\x00\x00¼=\x00\x00ßû\x00\x00çç\x00\x00ø\x1f\x00\x00")
                            risultante = ""
                        elif argument == "!":
                            risultante = str(math.factorial(int(dp)))
                        elif argument == "+":
                            risultante = str(float(dp) + float(dpdp))
                        elif argument == "-":
                            risultante = str(float(dp) - float(dpdp))
                        elif argument == "*":
                            risultante = str(float(dp) * float(dpdp))
                        elif argument == "^":
                            risultante = str(float(dp) ** float(dpdp))
                        elif argument == "/":
                            try:
                                risultante = str(float(dp) / float(dpdp))
                            except ZeroDivisionError:
                                risultante = "non si puo' dividere per zero"
                        elif argument == "v":
                            risultante = str(math.sqrt(float(dp)))
                        elif argument == "%":
                            risultante = str(float(dp) % float(dpdp))
                        elif argument == "not":
                            if dp == "True":
                                dp = True
                            elif dp == "False":
                                dp = False
                            risultante = not bool(dp)
                        elif argument == "and":
                            if dp == "True":
                                dp = True
                            elif dp == "False":
                                dp = False
                            if dpdp == "True":
                                dpdp = True
                            elif dpdp == "False":
                                dpdp = False
                            risultante = bool(dp) and bool(dpdp)
                        elif argument == "or":
                            if dp == "True":
                                dp = True
                            elif dp == "False":
                                dp = False
                            if dpdp == "True":
                                dpdp = True
                            elif dpdp == "False":
                                dpdp = False
                            risultante = bool(dp) or bool(dpdp)
                        elif argument == "md5":
                            hash_object = hashlib.md5(dp.encode())
                            risultante = hash_object.hexdigest()
                        elif argument == "sha1":
                            hash_object = hashlib.sha1(dp.encode())
                            risultante = hash_object.hexdigest()
                        elif argument == "sha224":
                            hash_object = hashlib.sha224(dp.encode())
                            risultante = hash_object.hexdigest()
                        elif argument == "sha256":
                            hash_object = hashlib.sha256(dp.encode())
                            risultante = hash_object.hexdigest()
                        elif argument == "sha384":
                            hash_object = hashlib.sha384(dp.encode())
                            risultante = hash_object.hexdigest()
                        elif argument == "sha512":
                            hash_object = hashlib.sha512(dp.encode())
                            risultante = hash_object.hexdigest()
                        elif argument == "type":
                            if dp.isdecimal():
                                risultante = "num"
                            elif dp.isalnum():
                                risultante = "string"
                        elif argument == "len":
                            risultante = len(dp)
                        elif argument == ",":
                            risultante = str(dp) + str(dpdp)
                        elif argument == "stwith":
                            if str(dp).startswith(str(dpdp)):
                                risultante = True
                            else:
                                risultante = False
                        elif argument == "endwith":
                            if str(dp).endswith(str(dpdp)):
                                risultante = True
                            else:
                                risultante = False
                        elif argument == "pick":
                            try:
                                risultante = dp[int(dpdp)]
                            except IndexError:
                                rt.append("non esiste nessun elemento a quell'indice")
                        elif argument == "split":
                            risultante = dp.split(dpdp)
                        elif argument == "compare":
                            num = 0
                            numdef = 0
                            for parola in dp:
                                try:
                                    if parola == dpdp[num]:
                                        numdef += 1
                                except IndexError:
                                    break
                                num = num+1
                            risultante = str(numdef/len(dp)*100)
                        elif argument == "than":
                            risultante = dp
                        elif argument == "comtime":
                            risultante = time.time()
                        elif argument == "time":
                            risultante = time.ctime()
                        elif argument == "timer":
                            risultante = str(time.ctime()).split(" ")
                            self.timer = risultante[4].split(":")
                        elif argument == "timer_get":
                            try:
                                numerot = 0
                                risultante = ""
                                tmp = str(time.ctime()).split(" ")
                                tmp = tmp[4].split(":")
                                for elemento in self.timer:
                                    risultante = risultante + ":" + str(int(tmp[numerot])-int(elemento))
                                    numerot += 1
                            except IndexError:
                                rt.append("manca un parametro dopo: " + argument)
                        elif argument == "sleep":
                            time.sleep(int(dp))
                        elif argument == "TCPconnect":
                            self.s = socket.socket()
                            try:
                                self.s.connect((dp, int(dpdp)))
                                rt.append("Connessessione al Server: " + dp + dpdp + " effettuata.")
                            except socket.error as errore:
                                rt.append("impossibile connettersi" + errore)
                            self.connect = True
                        elif argument == "TCPclient":
                            if self.connect == True:
                                if dp == "ESC":
                                    risultante = "Sto chiudendo la connessione col Server..."
                                    self.s.close()
                                else:
                                    self.s.send(dp.encode())
                                    data = self.s.recv(4096)
                                    risultante = str(data, "utf-8")
                            else:
                                rt.append("non connesso")
                        elif argument == "TCPserver":
                            if self.connect == False:
                                try:
                                    self.s = socket.socket()
                                    self.s.bind((dp, int(dpdp)))
                                    self.s.listen(int(dpdpdp))
                                    print("Server Inizializzato. In ascolto...")
                                except socket.error as errore:
                                    print("Qualcosa è andato storto...\nSto tentando di reinizializzare il server...")
                                conn, indirizzo_client = self.s.accept()
                                print("Connessione Server - Client Stabilita: " + str(indirizzo_client))
                                import Preveade as P
                                a = P.preveade()
                                while True:
                                    richiesta = conn.recv(4096)
                                    x = richiesta.decode()
                                    print(x)
                                    if x.startswith("STOPTCPSERVER"):
                                        break
                                    risposta = ""
                                    for dan in alpha.decide(x.split(" ")):
                                        risposta = risposta + "\n" + str(dan)
                                    conn.sendall(risposta.encode())
                            else:
                                rt.append("socket gia' connesso")
                        elif argument == "file":
                            if dpdp == "write":
                                with open(dp, "w") as file:
                                    file.write(dpdpdp)
                            elif dpdp == "read":
                                try:
                                    try:
                                        with open(dp, "r") as file:
                                            for linea in file.readlines():
                                                risultante = risultante + linea
                                    except UnicodeDecodeError:
                                        rt.append("Decodifica non supportata")
                                except FileNotFoundError:
                                    rt.append("il file non esiste")
                        elif argument == "zip":
                            try:
                                try:
                                    if dpdp == "compact":
                                        f = zipfile.ZipFile(dp, 'a', zipfile.ZIP_DEFLATED)
                                        f.write(dpdpdp)
                                        f.close()
                                    elif dpdp == "decompact":
                                        a = zipfile.ZipFile(dp, 'r')
                                        npath = dp[0:len(dp)-4]
                                        path = os.getcwd()
                                        os.mkdir(npath)
                                        try:
                                            os.chdir(path + "\\" + npath)
                                        except FileNotFoundError:
                                            os.chdir(path + "/" + npath)
                                        for filename in a.namelist():
                                             data = a.read(filename)
                                             with open(filename, 'w+b') as file:
                                                 file.write(data)
                                        os.chdir(path)
                                except FileExistsError:
                                    rt.append("il file esiste gia'")
                            except FileNotFoundError:
                                rt.append("il file non esiste")
                        elif argument == "P":
                            risultante = int(dp)/int(dpdp)
                        elif argument == "md":
                            try:
                                os.mkdir(dp)
                            except FileExistsError:
                                rt.append("il file esiste gia'")
                        elif argument == "cd":
                            try:
                                os.chdir(dp)
                            except FileNotFoundError:
                                rt.append("il non file esiste")
                        elif argument == "rm":
                            try:
                                try:
                                    os.remove(dp)
                                except FileNotFoundError:
                                    try:
                                        os.removedirs(dp)
                                    except FileNotFoundError:
                                        try:
                                            shutil.rmtree(dp)
                                        except FileNotFoundError:
                                            rt.append("il file non esiste")
                            except PermissionError:
                                rt.append("non hai i permessi necessari")
                        elif argument == "rn":
                            try:
                                os.rename(dp, dpdp)
                            except FileNotFoundError:
                                rt.append("il file da rinominare non esiste")
                        elif argument == "gcwd":
                            risultante = os.getcwd()
                        elif argument == "ls":
                            risultante = str(os.listdir(os.getcwd()))
                        elif argument == "fsx":
                            for it in os.walk(dp):
                                risultante = risultante + it + "\n"
                        elif argument == "rnu":
                            risultante = str(random.randint(int(dp), int(dpdp)))
                        elif argument == "cronology":
                            for ccc in self.cronology():
                                risultante = risultante + ccc + "\n"
                        elif argument == "e":
                            if dp.endswith(".v"):
                                try:
                                    if dpdp == "super":
                                        self.sa = dp
                                    with open(dp, "r") as file:
                                        self.add_to_code(file.readlines(), num)
                                except FileNotFoundError:
                                    rt.append("il file non esiste")
                            else:
                                rt.append("questo non e' uno script per questa shell")
                        elif argument == "app":
                            dp = self.dopo(num)
                            if dp.endswith(".py"):
                                if dp in os.listdir(os.getcwd()):
                                    if sys.platform == "win32":
                                        subprocess.run(["python", dp])
                                    else:
                                        subprocess.run(["python3", dp])
                                else:
                                    rt.append("errore: lo script python non esiste")
                            else:
                                rt.append("errore: il file non e' uno script python3")
                        elif argument == "configure_interpreter":
                            with open("Preveade.py", "r", encoding="utf8") as file:
                                readed = file.readlines()
                                n = ""
                                numerod = 0
                                for linea in readed:
                                    if numerod == 0:
                                        n = dp + "\n"
                                    else:
                                        n = n + linea
                                    numerod += 1
                            with open("Preveade.py", "w", encoding="utf8") as file:
                                file.write(n)
                        elif argument == "version":
                            risultante = __version__
                        elif argument == "os":
                            risultante = sys.platform
                        elif argument == "commands":
                            risultante = "lists, }, var, f, print, if, point, repeat, pass, createimage, !, +, -, *, /, v, ^, %, md5, sha1, sha224, sha256, sha384, sha512, type, len, ,, stwith, endwith, pick, split, compare, than, comtime, time, timer\ntimer_get, sleep, TCPconnect, TCPclient, TCPserver, file, zip, md, cd, rm, rn, gcwd, ls, rnu, e, app, configure_interpreter, version, os, commands, Gimmy, Gimmy_add"
                        elif argument == "Gimmy":
                            name = self.n[random.randint(1, len(self.n)-1)]
                            propnome = self.nomes[name]
                            verb = self.verbs[random.randint(1, len(self.verbs)-1)]
                            if propnome == 3:
                                if verb.endswith("y") and not verb[len(verb)-2] in vocals:
                                    verb = verb[0:len(verb)-1] + "ies"
                                elif verb.endswith("s") or verb.endswith("sh") or verb.endswith("ch") or verb.endswith("x") or verb.endswith("z") or verb.endswith("o"):
                                    verb = verb + "es"
                                elif verb == "be":
                                    verb = "is"
                                elif verb == "have":
                                    verb = "has"
                                elif verb in self.mv:
                                    pass
                                else:
                                    verb = verb + "s"
                            frase = name + " " + verb
                            rt.append(frase)
                        elif argument == "Gimmy_add":
                            if dp == "n":
                                with open("story", "a") as file:
                                    file.write("-n_" + dpdp + ":" + dpdpdp)
                            elif dp == "v":
                                with open("story", "a") as file:
                                    file.write("-v_" + dpdp)
                        elif num == 0:
                            if argument + ".v" in os.listdir(os.getcwd()):
                                with open(argument + ".v", "r") as file:
                                    self.add_to_code(file.readlines(), num)
                            else:
                                pdsf = ""
                                for ciao in self.a[1:len(self.a)]:
                                    pdsf = pdsf + ciao + "\n"
                                with open(argument + ".v", "w") as file:
                                    file.write(pdsf)
                                rt.append(argument + " aggiunto alle funzioni per questa installazione")
                        if risultante != "":
                            if vb:
                                self.variables[pm] = risultante
                                vb = False
                            else:
                                rt.append(risultante)
                    except (AttributeError, ModuleNotFoundError):
                        rt.append("mi hai dato un tipo di dato sbagliato dopo: " + argument)
                except ModuleNotFoundError:
                    rt.append("funzionalita' " + argument + " non supportata su questa piattaforma")
            num += 1
        to = ""
        for argument in self.a:
            to = to + str(argument) + " "
        ta = " "
        for argument in rt:
            ta = ta + str(argument) +" "
        ci = to + "-->" + ta
        act = ""
        for linea in self.cronology(toappend=ci):
            act = act + linea
        for returned in rt:
            yield str(returned)

    def dopo(self, num, *args, **kwargs):
        try:
            dopo = self.a[num+1]
            try:
                while dopo.endswith("\n"):
                    dopo = dopo[0:len(dopo)-1]
                if dopo.startswith("$"):
                    try:
                        dopo = self.variables[dopo]
                    except KeyError:
                        dopo = False
            except AttributeError:
                pass
        except IndexError:
            dopo = False
        return dopo

    def prima(self, num, *args, **kwargs):
        try:
            prima = self.a[num-1]
            while prima.endswith("\n"):
                prima = prima[0:len(prima)-1]
            if prima == "=":
                prima = self.a[num-1]
                while prima.endswith("\n"):
                    prima = prima[0:len(prima)-1]
        except (IndexError, AttributeError):
            prima = False
        return prima

    def add_to_code(self, list=None, num=0, *args, **kwargs):
        if num == "END":
            num = len(self.a)
        num2 = num + 1
        num3 = num + 1
        for comm in list:
            if comm.endswith("\n"):
                comm = comm[0:len(comm)-1]
            if comm == "input":
                dop = self.dopo(num+num3)
                self.a.insert(num2, dop)
                num3 += 1
            else:
                self.a.insert(num2, comm)
            num2 += 1
            num3 += 1

    def cronology(self, toappend=None, *args, **kwargs):
        with open("cronology", "a") as file:
            if toappend != None:
                file.write(toappend + "\n")
        with open("cronology", "r")as file:
            for line in file.readlines():
                line = line[0:len(line)-1]
                yield line


def main():
    alpha = preveade()
    start = ""
    try:
        try:
            with open(sys.argv[1], "r") as file:
                for line in alpha.decide(file.readlines()):
                    start = start + line + "\n"
        except IndexError:
            with open("start.ps", "r") as file:
                for line in alpha.decide(file.readlines()):
                    start = start + line + "\n"
    except (FileNotFoundError, NameError):
        start = "benvenuto"
    print(start)
    while True:
        dain = ""
        for dan in alpha.decide(input("-->").split(" ")):
            dain = dain + str(dan) + "\n"
        print(dain)

if __name__ == "__main__":
    main()
