#!/usr/bin/env python

# import required modules
import argparse
import booker_new
from os import getcwd

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

#url_list = booker.urllist(main,start,end)

cont = booker_new.get_page(main)
extr_list = booker_new.extract_url(cont)
abs_url_list = booker_new.make_abs_url(extr_list,main)
st_index,end_index = booker_new.find_index(abs_url_list,start,end)

if not (st_index and end_index):
	ifr_list = booker_new.extract_ifr(main)
	for main in ifr_list:
		cont = booker_new.get_page(main)
		extr_list = booker_new.extract_url(cont)
		abs_url_list = booker_new.make_abs_url(extr_list,main)
		st_index,end_index = booker_new.find_index(abs_url_list,start,end)
		if st_index and end_index:
			break
print abs_url_list
print st_index
print end_index
if not (st_index):
	print 'Oops!..Starting URL not found on main page.'
if not (end_index):
	print 'Oops!..Ending URL not found on main page.'
if (st_index and end_index):
	
	print "\nURL's parsed successfully.....\n"
	print "Downloading Webpages and making PDF\n"
	booker_new.htmltopdf(abs_url_list[st_index:end_index+1],main)
	print "\nPDF saved successfully as "+main.rsplit('/',2)[1]+".pdf"+" in " + getcwd() + " directory"