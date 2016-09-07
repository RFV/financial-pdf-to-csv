# -*- coding: utf-8 -*-
# from see import *

#the predefined fields
csv_type1 = 'Kundebetaling'
csv_text1 = 'klarna-samlebilag, gebyr'
csv_motkonto1 = 7770

csv_type2 = 'Manuell kundefaktura'
csv_text2 = 'klarna-samlebilag, salg'
csv_motkonto2 = 3010
csv_mva = 325

csv_konto = 23283

import convertor, re

def extract(text_data, csv_file, backup_file):
	#clean up the text a little bit 1st
	text_data = re.sub(r'(?m)^\s*', r'', text_data) #remove empty space
	#find the required text and return in correct format
	# suminntekt_data = re.search(r'Sum inntekt\n([-\d ,]*)', text_data, re.DOTALL).group(1).replace(" ", "") #this is the magic :))
	sumkostnader_data = re.search(r'0,00 (-[\d ,]*)', text_data, re.DOTALL).group(1).replace(" ", "") #this is the magic :))
	date = re.search(r'\d\d\.\d\d\.\d{4} - (\d\d\.\d\d\.\d{4})', text_data, re.DOTALL).group(1)
	#create the rows as they will be in the csv file
	rows = [[csv_type1, date, None, None, csv_text1, sumkostnader_data,   csv_konto, None, csv_motkonto1, None]]#,
			# [csv_type2, date, None, None, csv_text2, suminntekt_data, csv_konto, None, csv_motkonto2, csv_mva]]
	#expoart to csv file, with backup facility
	convertor.add_to_csv_file(rows, csv_file, backup_file)


