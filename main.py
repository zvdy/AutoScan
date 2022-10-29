import os

def scan(ip):
    os.system("nmap -sV -sC -oN nmap.txt " + ip)
    os.system("nikto -h " + ip + " -o nikto.txt")
    os.system("dirb http://" + ip + " -o dirb.txt")
    os.system("gobuster dir -u http://" + ip + " -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.txt")
    os.system("sqlmap -u http://" + ip + " --dbs -o sqlmap.txt")
    os.system("wpscan --url http://" + ip + " -o wpscan.txt")
    os.system("whatweb http://" + ip + " -o whatweb.txt")
    os.system("nbtscan " + ip + " > nbtscan.txt")
    os.system("enum4linux " + ip + " > enum4linux.txt")
    os.system("smbmap -H " + ip + " > smbmap.txt")
    

if __name__ == "__main__":
    os.system("clear")
    print(
        """
 ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄       ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄ 
▐ ▄▀ ▀▄ █   █    █ █    █  ▐ █      █     █ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █  █ █ █ 
  █▄▄▄█ ▐  █    █  ▐   █     █      █        ▀▄   ▐ █        █▄▄▄█ ▐  █  ▀█ 
 ▄▀   █   █    █      █      ▀▄    ▄▀     ▀▄   █    █       ▄▀   █   █   █  
█   ▄▀     ▀▄▄▄▄▀   ▄▀         ▀▀▀▀        █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀  ▄▀   █   
▐   ▐              █                       ▐      █     ▐  ▐   ▐   █    ▐   
                   ▐                              ▐                ▐        
        """
    )
    # User choice 
    print("What scan would you like to run?")
    print("1. Nmap")
    print("2. Nikto")
    print("3. Dirb")
    print("4. Gobuster")
    print("5. Sqlmap")
    print("6. Wpscan")
    print("7. Whatweb")
    print("8. Nbtscan")
    print("9. Enum4linux")
    print("10. Smbmap")
    print("11. All")
    print("12. Exit")
    choice = input("Enter your choice: ")

    # User input
    while choice != "12":
        if choice == "1":
            ip = input("Enter the IP address: ")
            os.system("nmap -sV -sC -oN nmap.txt " + ip)
        elif choice == "2":
            ip = input("Enter the IP address: ")
            os.system("nikto -h " + ip + " -o nikto.txt")
        elif choice == "3":
            ip = input("Enter the IP address: ")
            os.system("dirb http://" + ip + " -o dirb.txt")
        elif choice == "4":
            ip = input("Enter the IP address: ")
            os.system("gobuster dir -u http://" + ip + " -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster.txt")
        elif choice == "5":
            ip = input("Enter the IP address: ")
            os.system("sqlmap -u http://" + ip + " --dbs -o sqlmap.txt")
        elif choice == "6":
            ip = input("Enter the IP address: ")
            os.system("wpscan --url http://" + ip + " -o wpscan.txt")
        elif choice == "7":
            ip = input("Enter the IP address: ")
            os.system("whatweb http://" + ip + " -o whatweb.txt")
        elif choice == "8":
            ip = input("Enter the IP address: ")
            os.system("nbtscan " + ip + " > nbtscan.txt")
        elif choice == "9":
            ip = input("Enter the IP address: ")
            os.system("enum4linux " + ip + " > enum4linux.txt")
        elif choice == "10":
            ip = input("Enter the IP address: ")
            os.system("smbmap -H " + ip + " > smbmap.txt")
        elif choice == "11":
            ip = input("Enter the IP address: ")
            scan(ip)
        else:
            print("Invalid choice")
        print("What scan would you like to run?")
        print("1. Nmap")
        print("2. Nikto")
        print("3. Dirb")
        print("4. Gobuster")
        print("5. Sqlmap")
        print("6. Wpscan")
        print("7. Whatweb")
        print("8. Nbtscan")
        print("9. Enum4linux")
        print("10. Smbmap")
        print("11. All")
        print("12. Exit")
        choice = input("Enter your choice: ")
        
    print("Goodbye!")
