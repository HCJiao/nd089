def question1():
	elements = {
		'hydrogen':{
			'number':	1,
			'weight':	1.00794,
			'symbol':	'H'
		},
		'helium':{
			'number':	2,
			'weight':	4.002602,
			'symbol':	'He'
		}
	}
	print(elements)
	elements['hydrogen']['is_noble_gas'] = False
	elements['helium']['is_noble_gas'] = True

	print(elements)
def question2():
	