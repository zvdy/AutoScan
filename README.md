# AutoScan :snake:
Python script that runs scans on a given ip.

This _Python_ Script runs the following scans to the user's given IP address
creating a **.txt file** for each scanning software:
___
## Nmap
`nmap -sV -sC`

## Nikto
`nikto -h IP`

## Dirb
`dirb http://IP`

## GoBuster
`gobuster dir -u http://IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt` 

## SqlMap
`sqlmap -u http://IP --dbs`

## WPScan
`wpscan --url http://IP`

## WhatWeb
`whatweb https://IP`

## NBTScan
`nbtscan IP`

## Enum4Linux
`enum4linux`

## smbMap
`smbmap -H IP`
___
### :no_entry:Note
This software is for educational & research purpose only, I'm not responsible for 
the malicious use of it by any third-party.
