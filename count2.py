import docx2txt
import os
import sys
import re
import time
import PyPDF2
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def getPageCount(pdf_file):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pages = pdfReader.numPages
	return pages

def extractData(pdf_file, page):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(page)
	data = pageObj.extractText()
	return data

def getWordCount(data):

	data=data.split()
	return len(data)

def main():
	if len(sys.argv)!=2:
		print('command usage: python word_count.py FileName')
		exit(1)
	else:
		pdfFile = sys.argv[1]
	
		try:
			if os.path.exists(pdfFile):
				print("file found!")
		except OSError as err:
			print(err.reason)
			exit(1)


		#totalWords = 0
		#texts = []
		#numPages = getPageCount(pdfFile)
		#for i in range(numPages):
		#	text = extractData(pdfFile, i)
		#	totalWords+=getWordCount(text)
		#	texts.append(text)
		#time.sleep(1)

		#for i in range(len(texts)):
		#	texts[i] = texts[i].split()

		stop_words = set(stopwords.words('english'))


		resume = 'i am good in python'
		resume2 = 'this job requires proficiency in python and c++ and java'
		job_description = 'this job requires proficiency in python and c++ and java'

		resume = word_tokenize(resume)

		resume_out = []

		for w in resume:
			if w not in stop_words: 
				resume_out.append(w)

		resume = ' '.join(resume_out)
		print(resume)

		text = [job_description,resume, resume2]

		from sklearn.feature_extraction.text import CountVectorizer
		cv = CountVectorizer()
		count_matrix = cv.fit_transform(text)

		from sklearn.metrics.pairwise import cosine_similarity

		print("\nSimilarity Scores:")
		print(cosine_similarity(count_matrix))

		matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
		matchPercentage = round(matchPercentage, 2)
		print("Your resume matches about "+ str(matchPercentage)+ "% of the project description.")

if __name__ == '__main__':
	main()