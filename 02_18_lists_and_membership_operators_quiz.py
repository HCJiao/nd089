def list_indexing():
	month = 8

	days_in_month = [
		31,	# January
		28,	# February
		31,	# March
		30,	# April
		31,	# May
		30,	# June
		31,	# July
		31,	# August
		30,	# September
		31,	# October
		30,	# November
		31	# December
	]

	num_days = days_in_month[month-1]
	print(num_days)

def list_slicing():
	eclipse_dates  = [
		'June 21, 2001',
		'December 4, 2002',
		'November 23, 2003',
		'March 29, 2006',
		'August 1, 2008',
		'July 22, 2009',
		'July 11, 2010',
		'November 13, 2012',
		'March 20, 2015',
		'March 9, 2016'
	]
	print(eclipse_dates[-3:])	# Print last 3 elements

def sentences():
	sentence1 = "I wish to register a complaint."
	sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

	sentence2[6]="!"
	print(sentence2)

	sentence2[0]="Our Majesty"
	print(sentence2)

	# sentence1[30]="!"
	# print(sentence1)

	sentence2[0:2]=["We", "want"]
	print(sentence2)


# list_indexing()
# list_slicing()
sentences()