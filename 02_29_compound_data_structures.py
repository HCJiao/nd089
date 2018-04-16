elements = {
	'hydrogen':{
		"number":	1,
		"weight":	1.00794,
		"symbol":	"H"
	},
	'helium':{
		"number":	2,
		"weight":	4.002602,
		"symbol":	"H"
	}
}

helium = elements['helium']
hydrogen_weight = elements["hydrogen"]["weight"]
print(helium)
print(elements.get('unobtainium'))
print(helium['weight'])