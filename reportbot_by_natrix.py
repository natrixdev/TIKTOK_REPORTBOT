import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.CYAN + """ __________                                  __  __________          __    
\______   \  ____  ______    ____ _______ _/  |_\______   \  ____ _/  |_  
 |       _/_/ __ \ \____ \  /  _ \\_  __ \\   __\|    |  _/ /  _ \\   __\ 
 |    |   \\  ___/ |  |_> >(  <_> )|  | \/ |  |  |    |   \(  <_> )|  |   
 |____|_  / \___  >|   __/  \____/ |__|    |__|  |______  / \____/ |__|   
        \/      \/ |__|                                 \/                
                                                                          """)
print("")
print("")
print("Github: natrixdev / natrix_dev")

print("")
print("")

x = input('Report url (get it in the console) ')
print("")
print("")

print('Bot started ...')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('Reported [BY NATRIXDEV]')

    time.sleep(10)


input()



