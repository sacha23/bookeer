#!/usr/bin/env python

# import required modules
import argparse
import booker

# building parser object with required args 
parser = argparse.ArgumentParser(description="Tool to convert series of webpages into single PDF")
parser.add_argument("main",help="Page to find URL series",)
parser.add_argument("start",help="URL of starting page [ inclusive ]")
parser.add_argument("end",help="URL of ending page [ inclusive ]")

# Parsing args
args = parser.parse_args()
main = args.main
start = args.start
end = args.end

print "\n"
print "main page :"+main+"\nstart page :"+start+"\nend page :"+end

url_list = booker.urllist(main,start,end)

print "\nURL's parsed successfully.....\n"
print "Downloading Webpages and making PDF\n"

booker.htmltopdf(url_list,main)

print "\nPDF saved successfully as "+main.rsplit('/',2)[1]+".pdf"+" in home directory"