# from see import *; log_on(__file__) #\s*log\(.*\)

#1st import the necesary libaries
import argparse 					#to get command line arguments into the program
import subprocess					#to be able to call the external pdf to text utility
import re 							#to run the actual regular expressions (the text extraction/import code)
import os							#os needed to remove the temp txt file
import datetime 					#in order to add timestamp to the log file

import adwords, izettle, paypal, klarna
import klarnaab, boapaypal

def main(): #if this proram is called as a script then it will ask for parameters at the command line
	ap = argparse.ArgumentParser()
	ap.add_argument("-input", "-input", required = True, help = "Input txt file")
	ap.add_argument("-output", "-output", required = True, help = "Output csv file")
	ap.add_argument("-backup", "-backup", required = False, help = "Backup csv file") #if no backup is specified, then no backup will be made
	args = vars(ap.parse_args())

	input_txt = args['input']
	csv_file = args['output']
	backup_file = args['backup']

	process(input_txt, csv_file, backup_file)

def process(text_file_name, csv_file, backup_file=None):
	output=''
	log_file = open('log.txt', 'a')
	log_file.write('started import\ndate-time: %s\ninput: %s\noutput: %s\nbackup file: %s\n' % (str(datetime.datetime.now()), text_file_name, csv_file, backup_file))
	try:
		#return the text as file object (open text file and return it)
		text_file = open(text_file_name,'rU')
		#convert the file to pure text
		text_data = text_file.read() 		
		
		#detect which document type it is and directly call the correct extraction function
		document_type = detect_input_type(text_data)
		#instead of doing an if-elif call just map the correct functions to a dictionary and then call the correct function based on text, pass the text data to the function
		{'google': 					adwords.extract,
		 'paypal': 					paypal.extract,
		 'klarna': 					klarna.extract,
		 'izettle': 				izettle.extract,
		 'klarna-ab':				klarnaab.extract,
		 'boa-paypal':				boapaypal.extract}[document_type](text_data, csv_file, backup_file)

		#delete the temporary-text file
		text_file.close() 			#1st close it
		log_file.write('SUCCESS\n')
	except Exception as inst:
		log_file.write(''.join((str(inst), '\n', output)))      # the exception instance
	log_file.close()

def detect_input_type(text):
	#detect what kind of input file we have then call the correct import module
	AC_search = re.search('(Google Ireland)|(izettle)|(Klarna AS)|(PayPal)|(MELDING OM OVERF)|(MELDING OM KREDITERING BETALER)', text)
	if   AC_search.group(1): return 'google' 		#if (Google Ireland) was found return google
	elif AC_search.group(2): return 'izettle' 		#if izettle was found return izettle
	elif AC_search.group(3): return 'klarna' 		#if Klarna AS was found return klarna
	elif AC_search.group(4): return 'paypal' 		#if PayPal was found return paypal
	elif AC_search.group(5): return 'klarna-ab' 	#if MELDING OM OVERF.RING was found return klarna-ab
	elif AC_search.group(6): return 'boa-paypal' 	#if MELDING OM KREDITERING BETALER was found return boa-paypal

if __name__ == '__main__': #the usual python import and script functionality to run file as script and be able to import it
	main()
