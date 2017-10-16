#BaseUrl Of the website
#place link of the website without index.html
#eg: http://canada.tonytemplates.com/rent-a-car/index.html is the website you want to clone
#put the base URL as http://canada.tonytemplates.com/rent-a-car/
baseurl = 'REPLACE URL HERE'


from bs4 import BeautifulSoup
import os
import urllib
import urllib2

print '''Python script to Clone a Web Page
Author : Sai Kiran Goud
Date : 14 May 2017
'''
print "Connecting to server"
response = urllib2.urlopen(baseurl)
html_doc = response.read()
print "Connection Success!"
try :
        soup = BeautifulSoup(html_doc, 'html.parser')
        f = open( 'index.html', 'w' )
        f.write(str(soup))
        f.close()
        print "Initializing Index File" 
        #Get All Images
        print "Process Initiated"
        print "Step 1: Getting all images."
        a = soup.find_all('img')
        for i in range(len(a)):
            directory =  a[i]['src']
            print '\t[+]Getting file = '+str(directory)
            if not os.path.exists(os.path.dirname(directory)):
                print "    [DIR]Creating directory"
                os.makedirs(os.path.dirname(directory))
            testfile = urllib.URLopener()
            testfile.retrieve(baseurl+directory, directory)
        print '==============Done getting images!=============='
        #Get all Css
        print "Step 2: Getting all CSS."
        a = soup.find_all('link')
        for i in range(len(a)):
            directory =  a[i]['href']
            if "http" in directory or "https" in directory:
                print "------Skipped for ----- ",directory
                continue
            print '\t[+]Getting file = '+str(directory)
            if "/" not in directory:
                    print "\tNo directory. Saving file",directory
            elif not os.path.exists(os.path.dirname(directory)):
                print "    [DIR]Creating directory"
                os.makedirs(os.path.dirname(directory))
            testfile = urllib.URLopener()
            testfile.retrieve(baseurl+directory, directory)
        print '==============Done getting CS files!=============='
        print "Step 3: Getting all JS."
        #Get all JS
        a = soup.find_all('script')
        for i in range(len(a)):
            try:
                directory =  a[i]['src']
            except Exception as e:
                print "Excpetion occured in JS for",a[i]
                continue
            if "http" in directory or "https" in directory:
                print "------Skipped for ----- ",directory
                continue
            print '\t[+]Getting file = '+str(directory)
            if not os.path.exists(os.path.dirname(directory)):
                print "    [DIR]Creating directory"
                os.makedirs(os.path.dirname(directory))
            testfile = urllib.URLopener()
            testfile.retrieve(baseurl+directory, directory)
        print '==============Done getting JS Files!=============='
        print 'Script Executed sucessfully!'
except Exception as e:
    print "Exception occured = ",e
