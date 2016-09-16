# -*- coding: utf-8 -*-
# from see import *; log_on(__file__)

#the predefined fields
csv_type = 'Kundebetaling'
csv_text = 'Klarna innbetaling'
csv_konto = 1920
csv_motkonto = 23283

import convertor, re

def extract(text_data, csv_file, backup_file):
	#clean up the text a little bit 1st
	text_data = re.sub(r'(?m)^\s*', r'', text_data) #remove empty space

	#ge the date with the new format
	date = re.search(r'\d\d/\d\d-\d{4}', text_data).group(0) #, re.DOTALL
	date = re.sub(r'(\d\d)/(\d\d)-(\d{4})', r'\1.\2.\3', date)
	
	#check for both types in the doc and depending on which one is found the relevant code will be executed below
	sumkostnader_data = re.search(r'NOK (\d*?,\d\d)', text_data, re.DOTALL)
	payload = sumkostnader_data.group(1).replace(" ", "")

	#create the rows as they will be in the csv file
	rows = [[csv_type, date, None, None, csv_text, abs(float(payload.replace(',','.'))), csv_motkonto, None, csv_konto, None]]#,
			# [csv_type2, date, None, None, csv_text2, suminntekt_data, csv_konto, None, csv_motkonto2, csv_mva]]
	#export to csv file, with backup facility
	convertor.add_to_csv_file(rows, csv_file, backup_file)


