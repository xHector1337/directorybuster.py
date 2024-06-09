import requests
import sys

if len(sys.argv) != 4:
    print('Usage: ',str(sys.argv[0]),'url','wordlist','extension')
url = str(sys.argv[1])
wordlist = sys.argv[2]
extension = str(sys.argv[3])
if 'http' not in url:
    print('Usage: ',str(sys.argv[0]),'url','wordlist','extension')
    sys.exit(1)

def bruteforcer(url,wordlist,extension):
    i = 0
    file = open(wordlist,'r')
    file_contents = file.readlines()
    while i < len(file_contents):
        line = file_contents[i].strip()
        request = requests.request('GET',url=(f'{url}{line}{extension}'))
        if 'Page not found' not in request.content.decode('utf-8'):
            print('[200]:\t',str(f'{url}{line}{extension}'))
        else:
            print('An error occured.')
            print('[400]',str(f'{url}{line}{extension}'))
        i+=1
    

bruteforcer(url=url,wordlist=wordlist,extension=extension)
