#BaseUrl Of the website
baseurl = 'http://Website.com/html/demo/'


from bs4 import BeautifulSoup
import os
import urllib
import urllib2

print '''Python script to Clone a Web Page
Author : Sai Kiran Goud
Date : 14 May 2017
'''

response = urllib2.urlopen(baseurl)
html_doc = response.read()

try :
        soup = BeautifulSoup(html_doc, 'html.parser')
        #Get All Images
        print "Process Initiated"
        print "Step 1: Getting all images."
        a = soup.find_all('img')
        for i in range(len(a)):
            directory =  a[i]['src']
            print 'Getting file = '+str(directory)
            if not os.path.exists(os.path.dirname(directory)):
                print "Creating directory"
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
            print 'Getting file = '+str(directory)
            if not os.path.exists(os.path.dirname(directory)):
                print "Creating directory"
                os.makedirs(os.path.dirname(directory))
            testfile = urllib.URLopener()
            testfile.retrieve(baseurl+directory, directory)
        print '==============Done getting CS files!=============='
        print "Step 3: Getting all JS."
        #Get all JS
        a = soup.find_all('script')
        for i in range(len(a)):
            directory =  a[i]['src']
            print 'Getting file = '+str(directory)
            if not os.path.exists(os.path.dirname(directory)):
                print "Creating directory"
                os.makedirs(os.path.dirname(directory))
            testfile = urllib.URLopener()
            testfile.retrieve(baseurl+directory, directory)
        print '==============Done getting JS Files!=============='
        print 'Script Executed sucessfully!'
except Exception as e:
    print "Exception occured = ",e
