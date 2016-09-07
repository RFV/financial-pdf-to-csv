import csv 							#to open, work and save csv data files
import shutil						#to make a backup copy file of existing csv file
import re 							#to run the actual regular expressions (the text extraction/import code)

def search_convert_date(text):
	#fast tactic to search for all posible dates then if found change it and return back
	AC_search = re.search('((januar 20)|(februar 20)|(mars 20)|(april 20)|(mai 20)|(juni 20)|(juli 20)|(august 20)|(september 20)|(oktober 20)|(november 20)|(desember 20))(\d\d)', text, re.I)
	if AC_search.group(2):    return '31.01.20%s' % AC_search.group(14)
	elif AC_search.group(3):  return '28.02.20%s' % AC_search.group(14)	
	elif AC_search.group(4):  return '31.03.20%s' % AC_search.group(14)
	elif AC_search.group(5):  return '30.04.20%s' % AC_search.group(14)
	elif AC_search.group(6):  return '31.05.20%s' % AC_search.group(14)
	elif AC_search.group(7):  return '30.06.20%s' % AC_search.group(14)
	elif AC_search.group(8):  return '31.07.20%s' % AC_search.group(14)
	elif AC_search.group(9):  return '31.08.20%s' % AC_search.group(14)
	elif AC_search.group(10): return '30.09.20%s' % AC_search.group(14)
	elif AC_search.group(11): return '31.10.20%s' % AC_search.group(14)	
	elif AC_search.group(12): return '30.11.20%s' % AC_search.group(14)	
	elif AC_search.group(14): return '31.12.20%s' % AC_search.group(14)

def add_to_csv_file(rows, csv_file, backup_file):
	if backup_file: shutil.copyfile(csv_file, backup_file) 		#if no backup_file is None then no backup will be made

	#add the extacted data to the csv file, file will open and close automatically with the python with container
	with open(csv_file, 'a') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=';', lineterminator='\n') #opens a csv writer object that is used to output the csv data to csv file
		csvwriter.writerows(rows) # write all data one shot