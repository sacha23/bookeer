#!/usr/bin/env python

# TBD : iframe capture and extracting correct info iframe eg:"http://www.pitt.edu/~naraehan/python2/index.html"
        






# import required modules

#import argparse 
#import sys

import re 
import requests 
import pdfkit
from collections import OrderedDict


# building parser object with required args 
'''parser = argparse.ArgumentParser(description="Tool to convert series of webpages into single PDF")
parser.add_argument("main",help="Page to find URL series",)
parser.add_argument("start",help="URL of starting page [ inclusive ]")
parser.add_argument("end",help="URL of ending page [ inclusive ]")

# Parsing args
args = parser.parse_args()
main = args.main
start = args.start
end = args.end 


#main  = sys.argv[1]#"http://www.alsa-project.org/~tiwai/writing-an-alsa-driver/index.html"
#start = sys.argv[2]#"http://www.alsa-project.org/~tiwai/writing-an-alsa-driver/pr01.html"
#end   = sys.argv[3]#"http://www.alsa-project.org/~tiwai/writing-an-alsa-driver/ch17.html"

print "\n"
print "main page :"+sys.argv[1]+"\nstart page :"+sys.argv[2]+"\nend page :"+sys.argv[3]
'''
def urllist( main, start, end):

        '''This function returns the final list of URL's
Arg's: main   Page to find URL series 
       start  URL of starting page [ inclusive ]
       end    URL of ending page   [ inclusive ]'''
        if(re.search("http[s]?://.*?html",main)):
               in_file = requests.get(main).content
               all_url_list = re.findall('[hH][rR][eE][fF]="(.*?html)', in_file)
            #  print urllist[:10]
               for a in range(0,len(all_url_list)):
               	     all_url_list[a] = main.rsplit('/',1)[0] + '/' + all_url_list[a]
        else: 
            in_file = open(main,'r').read()
            all_url_list = re.findall('href=(.*?html)',in_file)
     #  print len(urllist)
        uniq_url_list = list(OrderedDict.fromkeys(all_url_list))
        s_index = uniq_url_list.index(start)
        e_index = uniq_url_list.index(end)
        url_list = uniq_url_list[ s_index: e_index+1]
     #  print len(urllist)
     #  print len(url_list)
        return url_list

'''url_list = urllist(main,start,end)
print "\nURL's parsed successfully.....\n"
print "Downloading Webpages and making PDF\n" '''

def htmltopdf(url_list,main):
      pdfkit.from_url(url_list,main.rsplit('/',2)[1]+".pdf")

#print "\nPDF saved successfully as "+main.rsplit('/',2)[1]+".pdf"+" in home directory"



