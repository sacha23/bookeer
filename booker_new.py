#! /usr/bin/env python

import re 
import requests 
import pdfkit
from collections import OrderedDict

def get_page(main):
	return requests.get(main).content

def extract_url(cont):
	
	extr_list = re.findall('href="(.*?)"',cont)
	return extr_list


def make_abs_url(extr_list,main):

	for a in range(len(extr_list)):
		if not re.search("http",extr_list[a]):
			extr_list[a] = main.rsplit('/',1)[0] + '/' + extr_list[a]
	return extr_list


def find_index(abs_url_list,start,end):

	try:
		st_index = abs_url_list.index(start)
	except ValueError:
		st_index = None
	try:
	    end_index = abs_url_list.index(end)
	except ValueError:
		end_index = None
	return st_index,end_index

def extract_ifr(cont):

	extr_ifr_list = re.findall('iframe.*?src="(.*?)"',cont)
	return extr_ifr_list


def htmltopdf(url_list,main):
      pdfkit.from_url(url_list,main.rsplit('/',2)[1]+".pdf")

