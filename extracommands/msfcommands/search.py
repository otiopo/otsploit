import colorama, sys, requests

try:
    exploit = sys.argv[2]
    print(colorama.Fore.BLUE + "Searching For, " + colorama.Fore.GREEN + exploit)
    try:
        response = requests.get("https://otsploit-console-extra-utilities.otiopo.repl.co/utilities/exploits.json").json()
        print(response[exploit])
        print(f"""Be Sure You Type: "use exploit "{response[exploit]}"" Then Run It""")
    except:
        print("This Exploit Is Not Here")
except:
    print(colorama.Fore.RED + "An Error Has Been Seen")
