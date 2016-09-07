# -*- coding: utf-8 -*-
# from see import *

#the predefined fields
csv_text1 = 'Adwords PPC reklame'
csv_konto = 7321
csv_motkonto = 1920
csv_type = 'Finansbilag'

import convertor, re

def convert_adwords_date(date_text):
	#a mapping of the date to number conversion
	date_mapping = {'jan': '01',
					'feb': '02',
					'mar': '03',
					'apr': '04',
					'mai': '05',
					'jun': '06',
					'jul': '07',
					'aug': '08',
					'sep': '09',
					'okt': '10',
					'nov': '11', 
					'des': '12'}
	date_text = ''.join((date_text[:3], date_mapping[date_text[3:6]], date_text[6:])) #using the fast way to join string parts, in python, takes position 3-6 of string and then converts that to xx by using the mapping above, and then stitching the peices together
	return date_text

def extract(text_data, csv_file, backup_file):
	#clean up the text a little bit 1st
	# text_data = re.sub(r"\n\n", r'\n', text_data) #remove empty lines
	text_data = re.sub(r'(?m)^\s*', r'', text_data) #remove empty space
	#find the required text and return in correct format
	relevant_data = re.search(r'Bel.p(.*\(kr.*?\))', text_data, re.DOTALL).group(1)[1:] #get the required chunk (this is the magic :))
	rows = []
	#iterate over it, every 3 lines is one entry with line 1 the date and line 3 the kr ammount
	#use enumeratin to get x position in loop and then use modulus
	for x, line in enumerate(relevant_data.splitlines()):
		if x % 3 is 0: #this is a date line
			date = convert_adwords_date(line) #use the date convertor
		elif x % 3 is 2: #this is the kr line
			#create a new row and add it to rows, (as per the csv file spec), also format the kr string to the correct format
			rows.append([csv_type, date, None, None, csv_text1, line[4:-1].replace(" ", ""), csv_konto, None, csv_motkonto, None])
	#backup and inject the data into the csv file
	convertor.add_to_csv_file(rows, csv_file, backup_file)




