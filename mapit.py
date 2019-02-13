#! python3

import webbrowser,sys, pyperclip
new=2

sys.argv

#1. Check if command line arguments were passed
if len(sys.argv)>1:

    address=' '.join(sysargv[1:])

else:
    address=pyperclip.paste() # if no command line argument, takes clipboard contents

webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com/maps/place/'+address, new=new)
