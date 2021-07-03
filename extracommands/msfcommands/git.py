import os, sys, colorama

if sys.argv[1] == "git":
    try:
        if sys.argv[2] == "-c":
            try:
                resp = sys.argv[3]
            except:
                print(colorama.Fore.RED + "Provide a Url" + colorama.Fore.WHITE)
            try:
                os.system("git clone " + resp)
            except:
                print("Provide a Valid Url")
    except:
        print(f"""
        {colorama.Fore.BLUE}
        Msf Git Commands:
        
        {colorama.Fore.GREEN}
        git -c (git url)
        {colorama.Fore.WHITE}
        """)
