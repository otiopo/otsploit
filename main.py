import socket, os, sys, time, threading, colorama, requests, json, getpass
from queue import Queue
from tkinter import *

colorama.init()

print(r"""
OTSPLOIT HAS LOADED
 ________  _________  ________  ________  ___       ________  ___  _________   
|\   __  \|\___   ___\\   ____\|\   __  \|\  \     |\   __  \|\  \|\___   ___\ 
\ \  \|\  \|___ \  \_\ \  \___|\ \  \|\  \ \  \    \ \  \|\  \ \  \|___ \  \_| 
 \ \  \\\  \   \ \  \ \ \_____  \ \   ____\ \  \    \ \  \\\  \ \  \   \ \  \  
  \ \  \\\  \   \ \  \ \|____|\  \ \  \___|\ \  \____\ \  \\\  \ \  \   \ \  \ 
   \ \_______\   \ \__\  ____\_\  \ \__\    \ \_______\ \_______\ \__\   \ \__\
    \|_______|    \|__| |\_________\|__|     \|_______|\|_______|\|__|    \|__|
                        \|_________|                                           
""")

while True:
    command = input(colorama.Fore.WHITE + f"\n{getpass.getuser()} {colorama.Fore.BLACK}| {colorama.Fore.BLUE}{socket.gethostname()} {colorama.Fore.BLACK}| {colorama.Fore.RED}{socket.gethostbyname(socket.gethostname())}{colorama.Fore.GREEN}${colorama.Fore.WHITE}")

    if command == "ScanPort":
        print("Target IpV4:")
        ipv4 = input(" : ")
        if ipv4 == "me":
            ipv4 = socket.gethostbyname(socket.gethostname())
            socket.setdefaulttimeout(0.25)
            print_lock = threading.Lock()
            print("Insert An IP or a Hostname.")
            print("-" * 70)
            try:
                print("Starting the scan on " + socket.gethostbyname(ipv4))
            except socket.gaierror:
                print("Hostname " + ipv4 + " Cloud not be found.")
                sys.exit()
            print("-" * 70)


            def portscan(port):
                protocolname = 'tcp'
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((socket.gethostbyname(ipv4), port))
                    with print_lock:
                        print(f"Port : {port} / " + f"Service : {socket.getservbyport(port, protocolname)}")
                        con.close()
                except:
                    pass
            def threader():
                while True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()


            q = Queue()
            startTime = time.time()


            def start():
                for x in range(100):
                    t = threading.Thread(target=threader)
                    t.daemon = True
                    t.start()


            start()
            for worker in range(500):
                q.put(worker)
            q.join()
            arguments_results = []


        elif ipv4 == "cancel":
            print("Cancelled!")
        else:
            socket.setdefaulttimeout(0.25)
            print_lock = threading.Lock()
            print("Insert An IP or a Hostname.")
            print("-" * 70)
            try:
                print("Starting the scan on " + socket.gethostbyname(ipv4))
            except socket.gaierror:
                print("Hostname " + ipv4 + " Cloud not be found.")
                sys.exit()
            print("-" * 70)


            def portscan(port):
                protocolname = 'tcp'
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((socket.gethostbyname(ipv4), port))
                    with print_lock:
                        print(f"Port : {port} / " + f"Service : {socket.getservbyport(port, protocolname)}")
                        con.close()
                except:
                    pass


            def threader():
                while True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()


            q = Queue()
            startTime = time.time()


            def start():
                for x in range(100):
                    t = threading.Thread(target=threader)
                    t.daemon = True
                    t.start()


            start()
            for worker in range(500):
                q.put(worker)
            q.join()
            arguments_results = []
    elif command.startswith("system "):
        syscommand = command.replace("system ", "")
        os.system(syscommand)
    elif command.startswith("pyrun "):
        file = command.replace("pyrun ", "")
        os.system("python " + file)
    elif command == "exit":
        sys.exit(69)
    elif command.startswith("urltoip "):
        url = command.replace("urltoip ", "")
        print(socket.gethostbyname(url))
    elif command.startswith("pinghost "):
        ip = command.replace("pinghost ", "")
        os.system("ping " + ip)
    elif command == "sherlock":
        port = input("port: ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostbyname(socket.gethostname()), int(port)))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            print(str(addr) + " Has Been Connected!")
    elif command == "AddStartupProgram":
        print(os.getenv("APPDATA") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    elif command == "help":
        print(colorama.Fore.GREEN + """
        OtSploit Commands!
        
        ScanPort - Scans Ports Of an IpV4/IpV6
        sherlock - Finds Who Connects To Your Device On Your Router
        urltoip <url> - Finds An Ip Of a Website
        pinghost <url/ip> - Pings The Host Of The url/ip add -t -l <bytes> To Ping The Host Until You Press Ctrl + c
        system <command> - Runs a Cmd Command
        pyrun <file path> - Runs a Python File
        """)
    elif "help" in command or "welp" in command or "halp" in command or "healp" in command or "walp" in command or "wealp" in command:
        print("Did You Mean help?")
    elif command == "init-color":
        colorama.init(convert=True)
        print("Color Inited!")
    elif command == "uninit-color":
        colorama.deinit()
        print("Color UnInited!")
    elif command == "reinit-color":
        colorama.reinit()
        print("Color ReInited!")
    elif command.startswith("HttpGet "):
        try:
            host = command.replace("HttpGet ", "")
            req = requests.get(host)
            if req.status_code == 200:
                print(colorama.Fore.GREEN + req.text)
            else:
                print(colorama.Fore.RED + req.text)
        except:
            print(colorama.Fore.RED + "HttpGet Error")
    elif command.startswith("HttpPost "):
        try:
            def reqq(data):
                req = requests.post(host, data)
                if req.status_code == 200:
                    print(colorama.Fore.GREEN + req.text)
                else:
                    print(colorama.Fore.RED + req.text)
            host = command.replace("HttpPost ", "")
            data = input("Type Data To Send: ")
            if data == "MultiLine":
                screen = Tk()
                dataBox = Text(screen)
                dataBox.pack()
                submit = Button(screen,text="SUBMIT",command=lambda:reqq(json.dumps(dataBox.get('1.0', END))))
                submit.pack()
                screen.mainloop()
        except:
            print(colorama.Fore.RED + "HttpPost Error")
            print("Please Check If The Hostname Is Correct!")
    elif command == "msfvenom-console":
        print(colorama.Fore.GREEN + "Loading Console!")
        time.sleep(0.5)
        print(colorama.Fore.YELLOW + "Fetching Data From:", os.getenv("HOMEPATH"))
        for leter in "- - - - -\nMsfVenom Console Is Fetching Data...\n- - - - -":
            sys.stdout.write(colorama.Fore.CYAN + leter)
            time.sleep(0.06)
            sys.stdout.flush()
        while True:
            msfcommand = input("\n\n" + colorama.Fore.BLUE + socket.gethostname() + colorama.Fore.WHITE + colorama.Fore.BLACK + "$" + colorama.Fore.RED + "MsfConsole" + colorama.Fore.GREEN + ">")
            if msfcommand == "exitmsf":
                print(colorama.Fore.RED + "Exited Msf Console!")
                break
            elif msfcommand.startswith("search "):
                os.system("python extracommands/msfcommands/search.py " + msfcommand)
            elif msfcommand.startswith("git"):
                os.system("python extracommands/msfcommands/git.py " + msfcommand)
            elif msfcommand.startswith("use exploit "):
                os.system("python extracommands/msfcommands/use_exploit.py " + msfcommand)
    else:
        print(colorama.Fore.RED + "Enter a Valid Command!, Say 'help' For Info" + colorama.Fore.WHITE)

