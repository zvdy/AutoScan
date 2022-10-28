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
    scan(input("Enter IP: "))
