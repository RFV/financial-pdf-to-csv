# -*- coding: utf-8 -*-
# from see import *

#the predefined fields
csv_type1 = 'Kundebetaling'
csv_text1 = 'paypal-samlebilag, gebyr'
csv_motkonto1 = 7770

csv_type2 = 'Manuell kundefaktura'
csv_text2 = 'paypal-samlebilag, salg'
csv_motkonto2 = 3010
csv_mva = 325

csv_konto = 23284

import convertor, re

def extract(text_data, csv_file, backup_file):
	#clean up the text a little bit 1st
	text_data = re.sub(r'(?m)^\s*', r'', text_data) #remove empty space
	#find the required text and return in correct format
	gebyrer_data = re.search(r'Gebyrer *(-[\d ,]*)', text_data, re.DOTALL).group(1).replace(" ", "") #this is the magic :))
	date = convertor.search_convert_date(text_data)
	#create the rows as they will be in the csv file
	rows = [[csv_type1, date, None, None, csv_text1, gebyrer_data,   csv_konto, None, csv_motkonto1, None]]#,
			# [csv_type2, date, None, None, csv_text2, salgsaktivitet_data, csv_konto, None, csv_motkonto2, csv_mva]]
	#expoart to csv file, with backup facility
	convertor.add_to_csv_file(rows, csv_file, backup_file)


