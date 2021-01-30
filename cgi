# CGI
ffuf -w /usr/share/SecLists/Discovery/Web-Content/CGI-XPlatform.fuzz.txt -u <URL>/ccgi-bin/FUZZ -t 50
ffuf -w /usr/share/SecLists/Discovery/Web-Content/CGIs.txt -u <URL>/ccgi-bin/FUZZ -t 50
ffuf -w /usr/share/wordlist/dirbuster/directory-list-lowercase-2.3-medium.txt -u <URL>/cgi-bin/FUZZ -e .sh,.pl,.cgi >

#! If a script is found try SHELLSHOCK.
