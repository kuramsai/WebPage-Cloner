#BaseUrl Of the website
#place link of the website without index.html
#eg: http://xyz.com/index.html is the website you want to clone
#put the base URL as http://xyz.com/
#baseurl = 'Replace this'
baseurl = 'http://webdesign-finder.com/html/energy/'


from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from urllib.request import urlretrieve
import urllib.request



print ('''Python script to Clone a Web Page
Author : Sai Kiran Goud
Date : 17 Dec 2019
''')


def report(count, size, total):
        progress = [0, 0]       
        progress[0] = count * size
        if progress[0] - progress[1] > 1000000:
            progress[1] = progress[0]
            print("Downloaded {:,}/{:,} ...".format(progress[1], total))

print ("Connecting to server")

opener = urllib.request.build_opener()
#defining headers as some servers mandiate it
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                        ('Connection', 'keep-alive')
                    ]
urllib.request.install_opener(opener)
html_doc = urllib.request.urlopen(baseurl).read()

print ("Connection Success!")
try :
        soup = BeautifulSoup(html_doc, 'html.parser')
        f = open( 'index.html', 'w' )
        f.write(str(soup))
        f.close()
        print ("Initializing Index File")
        #Get All Images
        print ("Process Initiated")
        print ("Step 1: Getting all images.")
        a = soup.find_all('img')
        for i in range(len(a)):
            directory =  a[i]['src']
            print ('\t[+]Getting file = '+str(directory))
            if not os.path.exists(os.path.dirname(directory)):
                print ("    [DIR]Creating directory")
                os.makedirs(os.path.dirname(directory))
            testfile, headers = urlretrieve(baseurl+directory, directory, reporthook=report)
        print ('==============Done getting images!==============')
        #Get all Css
        print ("Step 2: Getting all CSS.")
        a = soup.find_all('link')
        for i in range(len(a)):
            directory =  a[i]['href']
            if "http" in directory or "https" in directory:
                print ("------Skipped for ----- ",directory)
                continue
            print ('\t[+]Getting file = '+str(directory))
            if "/" not in directory:
                    print ("\tNo directory. Saving file",directory)
            elif not os.path.exists(os.path.dirname(directory)):
                print ("    [DIR]Creating directory")
                os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl+directory, directory, reporthook=report)
        print ('==============Done getting CS files!==============')
        print ("Step 3: Getting all JS.")
        #Get all JS
        a = soup.find_all('script')
        for i in range(len(a)):
            try:
                directory =  a[i]['src']
            except Exception as e:
                print ("Excpetion occured in JS for",a[i])
                continue
            if "http" in directory or "https" in directory:
                print ("------Skipped for ----- ",directory)
                continue
            print ('\t[+]Getting file = '+str(directory))
            if not os.path.exists(os.path.dirname(directory)):
                print ("    [DIR]Creating directory")
                os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl+directory, directory, reporthook=report)
        print ('==============Done getting JS Files!==============')
        print ('Script Executed sucessfully!')
except Exception as e:
    print ("Exception occured = ",e)
