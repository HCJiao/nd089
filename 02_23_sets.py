import random
def ex1():
	countries = [
		"Angola",
		"Maldives",
		"India",
		"United States",
		"India",
		"Denmark",
		"Sweden",
		"Ghana",
		"Argentina",
		"Dominica",
		"Chad",
		"Indonesia",
		"Iraq",
		"Federated States of Micronesia",
		"Taiwan (see Republic of China)",
		"Antigua and Barbuda",
		"Iceland",
		"Thailand",
		"Cambodia",
		"Brunei",
		"People's Republic of China",
		"Botswana",
		"Albania",
		"Tuvalu",
		"Saudi Arabia",
		"Uzbekistan",
		"Pakistan",
		"Namibia",
		"Japan",
		"Dominican Republic",
		"Dominica",
		"Central African Republic",
		"Czech Republic",
		"Georgia",
		"Grenada",
		"Ghana",
		"Bulgaria",
		"Hungary",
		"Tajikistan",
		"Indonesia",
		"South Sudan",
		"Malaysia",
		"Burundi",
		"Ghana",
		"Yemen",
		"Zambia",
		"Turkmenistan",
		"Paraguay",
		"Kiribati",
		"Gabon",
		"Switzerland",
		"Taiwan (see Republic of China)",
		"Myanmar (formerly Burma)",
		"Taiwan (see Republic of China)",
		"Sri Lanka",
		"Cambodia",
		"Niue",
		"Paraguay",
		"South Africa",
		"Trinidad and Tobago",
		"Cuba",
		"Saudi Arabia",
		"Kiribati",
		"Taiwan (see Republic of China)",
		"Saint Kitts and Nevis",
		"Colombia",
		"Chile",
		"Gabon",
		"Nauru",
		"Poland",
		"Uganda",
		"Sweden",
		"Equatorial Guinea",
		"Liberia",
		"Vietnam",
		"Zimbabwe",
		"Niue",
		"South Korea",
		"Georgia",
		"Burundi",
		"India",
		"Eritrea",
		"Uzbekistan",
		"Serbia",
		"Brazil",
		"Estonia",
		"Tanzania",
		"Paraguay",
		"Equatorial Guinea",
		"Bangladesh",
		"San Marino",
		"Mozambique",
		"Honduras",
		"Liberia",
		"Saint Kitts and Nevis",
		"Aruba",
		"Spain",
		"Ecuador",
		"Malta",
		"Antigua and Barbuda",
		"Saint Vincent and the Grenadines",
		"Peru",
		"Sweden",
		"Haiti",
		"Mexico",
		"Brunei",
		"Vatican City (Holy See)",
		"Niger",
		"North Korea",
		"Cuba",
		"Bhutan",
		"Spain",
		"Iraq",
		"Egypt",
		"Monaco",
		"Namibia",
		"Morocco",
		"Trinidad and Tobago",
		"Netherlands",
		"Tanzania",
		"Malta",
		"Honduras",
		"Malta",
		"Romania",
		"Israel",
		"Egypt",
		"Central African Republic",
		"Côte d'Ivoire",
		"Saint Lucia",
		"Republic of Cyprus",
		"Nepal",
		"Georgia",
		"New Zealand (Aotearoa)",
		"Italy",
		"Mozambique",
		"Namibia",
		"Niue",
		"The Bahamas",
		"Oman",
		"Jamaica",
		"Ukraine",
		"Vietnam",
		"Afghanistan",
		"Seychelles",
		"South Sudan",
		"Slovenia",
		"Greece",
		"Marshall Islands",
		"Aruba",
		"Malta",
		"Egypt",
		"Ethiopia",
		"Papua New Guinea",
		"Djibouti",
		"Namibia",
		"Tuvalu",
		"Mozambique",
		"Liberia",
		"Bangladesh",
		"Kenya",
		"Somalia",
		"Senegal",
		"Barbados",
		"Greece",
		"Italy",
		"Republic of China (Taiwan)",
		"Slovenia",
		"Togo",
		"Saudi Arabia",
		"Chile",
		"South Africa",
		"Senegal",
		"Malta",
		"Saint Lucia",
		"Romania",
		"Germany",
		"Venezuela",
		"Sudan",
		"South Africa",
		"Nauru",
		"Paraguay",
		"Dominican Republic",
		"Bolivia",
		"Kyrgyzstan",
		"Mongolia",
		"Australia",
		"Hungary",
		"Niue",
		"Moldova",
		"Singapore",
		"Maldives",
		"Togo",
		"Russia",
		"Netherlands",
		"Federated States of Micronesia",
		"Eritrea",
		"Slovakia",
		"Paraguay",
		"Rwanda",
		"Saint Kitts and Nevis",
		"Chile",
		"Netherlands",
		"Côte d'Ivoire",
		"Turkey",
		"Libya",
		"Belarus",
		"Morocco",
		"Vatican City (Holy See)",
		"Vietnam",
		"Taiwan (see Republic of China)",
		"Egypt",
		"Mauritius",
		"United Arab Emirates",
		"Andorra",
		"Saint Lucia",
		"Guinea-Bissau",
		"Venezuela",
		"Bahrain",
		"Turkey",
		"Algeria",
		"Turkmenistan",
		"Chile",
		"Venezuela",
		"Palau",
		"Lithuania",
		"Niger",
		"Comoros",
		"Slovenia",
		"Indonesia",
		"Liberia",
		"Sweden",
		"Spain",
		"Zambia",
		"Mauritius",
		"Botswana",
		"Ireland",
		"Hungary",
		"Gabon",
		"Nicaragua",
		"Andorra",
		"Vietnam",
		"Laos",
		"Egypt",
		"Eritrea",
		"Belarus",
		"Maldives",
		"Lesotho",
		"Peru",
		"Armenia",
		"New Zealand (Aotearoa)",
		"Paraguay",
		"Ireland",
		"Niue",
		"Switzerland",
		"Tanzania",
		"Latvia",
		"Tunisia",
		"Seychelles",
		"India",
		"Monaco",
		"Russia",
		"Guinea",
		"Mozambique",
		"Kuwait",
		"Qatar",
		"Federated States of Micronesia",
		"Nepal",
		"Cambodia",
		"Moldova",
		"Samoa",
		"Spain",
		"Gabon",
		"Republic of China (Taiwan)",
		"Saint Lucia",
		"Vatican City (Holy See)",
		"Russia",
		"Algeria",
		"Saudi Arabia",
		"Saudi Arabia",
		"Indonesia",
		"Rwanda",
		"Tajikistan",
		"Saudi Arabia",
		"São Tomé and Príncipe",
		"Saint Kitts and Nevis",
		"Djibouti",
		"Azerbaijan",
		"Brunei",
		"Brazil",
		"Federated States of Micronesia",
		"Egypt",
		"Palau",
		"Yemen",
		"Ireland",
		"The Bahamas",
		"Spain",
		"Tuvalu",
		"Samoa",
		"Marshall Islands",
		"Bahrain",
		"Senegal",
		"Liechtenstein",
		"Zambia",
		"Lebanon",
		"El Salvador",
		"Tonga",
		"Georgia",
		"Slovakia",
		"The Bahamas",
		"Cameroon",
		"Israel",
		"Swaziland",
		"Albania",
		"Algeria",
		"Lithuania",
		"People's Republic of China",
		"Tuvalu",
		"Norway",
		"Albania",
		"Argentina",
		"New Zealand (Aotearoa)",
		"Guyana",
		"Iran",
		"Cape Verde",
		"Brunei",
		"Liechtenstein",
		"Czech Republic",
		"Myanmar (formerly Burma)",
		"Bangladesh",
		"Vietnam",
		"Mali",
		"Yemen",
		"Suriname",
		"Bolivia",
		"Sierra Leone",
		"Trinidad and Tobago",
		"Jamaica",
		"Thailand",
		"Libya",
		"Aruba",
		"Dominica",
		"Comoros",
		"Nigeria",
		"Turkey",
		"Iran",
		"Poland",
		"Burundi",
		"Palau",
		"Liechtenstein",
		"Sri Lanka",
		"El Salvador",
		"Solomon Islands",
		"Denmark",
		"Sri Lanka",
		"Estonia",
		"Saint Kitts and Nevis",
		"Finland",
		"Cuba",
		"Seychelles",
		"Grenada",
		"Monaco",
		"Brazil",
		"Cook Islands",
		"Bolivia",
		"Bangladesh",
		"Belize",
		"Sri Lanka",
		"Egypt",
		"Comoros",
		"Seychelles",
		"Saint Kitts and Nevis",
		"Eritrea",
		"East Timor",
		"Malawi",
		"Poland",
		"Taiwan (see Republic of China)",
		"Burundi",
		"Tuvalu",
		"Belgium",
		"Mexico",
		"Central African Republic",
		"Kyrgyzstan",
		"Ghana",
		"Myanmar (formerly Burma)",
		"India",
		"Federated States of Micronesia",
		"Austria",
		"People's Republic of China",
		"Sweden",
		"Burundi",
		"Guinea",
		"Peru",
		"Sudan",
		"Monaco",
		"Malawi",
		"Angola",
		"Niue",
		"Cook Islands",
		"People's Republic of China",
		"Kyrgyzstan",
		"Monaco",
		"Liechtenstein",
		"Uzbekistan",
		"Kyrgyzstan",
		"Argentina",
		"Republic of China (Taiwan)",
		"Estonia",
		"Brazil",
		"Netherlands",
		"Tanzania",
		"India",
		"Kiribati",
		"San Marino",
		"Ireland",
		"Mozambique",
		"Tunisia",
		"Republic of the Congo",
		"Netherlands",
		"Rwanda",
		"Djibouti",
		"Suriname",
		"Togo",
		"Poland",
		"Burkina Faso (formerly Upper Volta)",
		"Taiwan (see Republic of China)",
		"Sierra Leone",
		"South Africa",
		"Belarus",
		"Kuwait",
		"Belgium",
		"East Timor",
		"South Korea",
		"Brazil",
		"Kyrgyzstan",
		"Latvia",
		"Mauritania",
		"Zambia",
		"Egypt",
		"Bahrain",
		"Peru",
		"Sudan",
		"Madagascar",
		"Nauru",
		"Libya",
		"Mauritania",
		"Niger",
		"South Sudan",
		"Andorra",
		"Democratic Republic of Congo",
		"Finland",
		"Sudan",
		"Kazakhstan",
		"Holy See (see Vatican City)",
		"Bolivia",
		"Brazil",
		"Vatican City (Holy See)",
		"Malaysia",
		"Moldova",
		"Nepal",
		"United Kingdom",
		"Ethiopia",
		"Botswana",
		"Trinidad and Tobago",
		"South Africa",
		"Marshall Islands",
		"Chad",
		"Antigua and Barbuda",
		"Holy See (see Vatican City)",
		"Honduras",
		"Guinea-Bissau",
		"Central African Republic",
		"Libya",
		"Madagascar",
		"Tuvalu",
		"Federated States of Micronesia",
		"Brazil",
		"Luxembourg",
		"Zambia",
		"Algeria",
		"Indonesia",
		"France",
		"Indonesia",
		"Kuwait",
		"Niue",
		"Honduras",
		"Armenia",
		"Holy See (see Vatican City)",
		"Moldova",
		"Qatar",
		"Singapore",
		"Lebanon",
		"Liberia",
		"Marshall Islands",
		"Zambia",
		"Maldives",
		"Jamaica",
		"Kuwait",
		"Fiji",
		"Bolivia",
		"Grenada",
		"Zambia",
		"Bosnia and Herzegovina",
		"Liechtenstein",
		"Holy See (see Vatican City)",
		"Niger",
		"Denmark",
		"Luxembourg",
		"Republic of Cyprus",
		"Maldives",
		"Côte d'Ivoire",
		"Portugal",
		"Vatican City (Holy See)",
		"Republic of China (Taiwan)",
		"Thailand",
		"Belize",
		"Vatican City (Holy See)",
		"Serbia",
		"Laos",
		"Estonia",
		"Central African Republic",
		"Indonesia",
		"New Zealand (Aotearoa)",
		"Suriname",
		"Bhutan",
		"Afghanistan",
		"Philippines",
		"Thailand",
		"Cook Islands",
		"Romania",
		"Ireland",
		"Japan",
		"Czech Republic",
		"Rwanda",
		"Senegal",
		"Lithuania",
		"Benin",
		"Dominica",
		"Australia",
		"Republic of the Congo",
		"Brazil",
		"Albania",
		"Luxembourg",
		"Monaco",
		"Bulgaria",
		"Turkmenistan",
		"Belize",
		"Armenia",
		"Somalia",
		"Suriname",
		"Côte d'Ivoire",
		"Nicaragua",
		"Benin",
		"Venezuela",
		"Equatorial Guinea",
		"Maldives",
		"Niger",
		"Myanmar (formerly Burma)",
		"Côte d'Ivoire",
		"Grenada",
		"South Sudan",
		"Togo",
		"Greece",
		"Republic of Macedonia",
		"São Tomé and Príncipe",
		"Nepal",
		"Malaysia",
		"Guyana",
		"Armenia",
		"Dominican Republic",
		"Venezuela",
		"Tonga",
		"Saint Kitts and Nevis",
		"Burkina Faso (formerly Upper Volta)",
		"Tunisia",
		"Sierra Leone",
		"Denmark",
		"Chile",
		"Guatemala",
		"Albania",
		"Haiti",
		"Liechtenstein",
		"Bhutan",
		"Belize",
		"Rwanda",
		"Germany",
		"Jamaica",
		"Niger",
		"Ecuador",
		"Rwanda",
		"Moldova",
		"Samoa",
		"Benin",
		"Saint Lucia",
		"Tonga",
		"Mali",
		"Portugal",
		"Marshall Islands",
		"Mozambique",
		"Malaysia",
		"Slovenia",
		"Sweden",
		"The Gambia",
		"Uruguay",
		"Vietnam",
		"Mauritania",
		"Rwanda",
		"Hungary",
		"Vatican City (Holy See)",
		"São Tomé and Príncipe",
		"Kiribati",
		"Vietnam",
		"Haiti",
		"Guinea",
		"Burkina Faso (formerly Upper Volta)",
		"Czech Republic",
		"Gabon",
		"Guinea",
		"Dominica",
		"Zambia",
		"Vietnam",
		"Senegal",
		"Vanuatu",
		"Montenegro",
		"Rwanda",
		"Gabon",
		"New Zealand (Aotearoa)",
		"Sri Lanka",
		"Cambodia",
		"Niue",
		"Suriname",
		"Ecuador",
		"The Bahamas",
		"Samoa",
		"Kuwait",
		"Gabon",
		"Cook Islands",
		"Slovenia",
		"Ecuador",
		"Palau",
		"Syria",
		"Kiribati",
		"Madagascar",
		"Monaco",
		"Guinea",
		"Saint Lucia",
		"Indonesia",
		"San Marino",
		"Denmark",
		"Ecuador",
		"Armenia",
		"Fiji",
		"Singapore",
		"Ecuador",
		"Saint Kitts and Nevis",
		"Samoa",
		"Palau",
		"Ghana",
		"Jamaica",
		"Philippines",
		"Singapore",
		"Cape Verde",
		"Saint Lucia",
		"Oman",
		"Serbia",
		"Canada",
		"Qatar",
		"Norway",
		"Federated States of Micronesia",
		"Vatican City (Holy See)",
		"Brunei",
		"North Korea",
		"Botswana",
		"Thailand",
		"Jordan",
		"Ivory Coast (see Côte d'Ivoire)",
		"Spain",
		"Niue",
		"Sri Lanka",
		"Cambodia",
		"Germany",
		"Afghanistan",
		"Czech Republic",
		"Venezuela",
		"Singapore",
		"Indonesia",
		"Republic of Cyprus",
		"Iraq",
		"People's Republic of China",
		"Bulgaria",
		"Antigua and Barbuda",
		"Central African Republic",
		"Egypt",
		"Maldives",
		"Lithuania",
		"Belgium",
		"Turkmenistan",
		"Zimbabwe",
		"Uruguay",
		"Vietnam",
		"Zambia",
		"Grenada",
		"Switzerland",
		"Saint Vincent and the Grenadines",
		"Canada",
		"Sweden",
		"Federated States of Micronesia",
		"Israel",
		"Kyrgyzstan",
		"Swaziland",
		"Bulgaria",
		"Benin",
		"Ethiopia",
		"Slovakia",
		"Marshall Islands",
		"Uganda",
		"Germany",
		"Denmark",
		"Sri Lanka",
		"Eritrea",
		"Estonia",
		"South Sudan",
		"Haiti",
		"São Tomé and Príncipe",
		"Kyrgyzstan",
		"Sierra Leone",
		"Colombia",
		"Thailand",
		"Comoros",
		"Mozambique",
		"Serbia",
		"Lesotho",
		"Kazakhstan",
		"Guinea-Bissau",
		"Ecuador",
		"Gabon",
		"Paraguay",
		"Republic of China (Taiwan)",
		"Romania",
		"Mexico",
		"Dominican Republic",
		"Turkey",
		"Democratic Republic of the Congo (formerly Zaire)",
		"Trinidad and Tobago",
		"Georgia",
		"Republic of China (Taiwan)",
		"Turkey",
		"Austria",
		"Papua New Guinea",
		"Algeria",
		"Mauritania",
		"Republic of China (Taiwan)",
		"Democratic Republic of the Congo (formerly Zaire)",
		"Uzbekistan",
		"Portugal",
		"Georgia",
		"Germany",
		"Chad",
		"Egypt",
		"Eritrea",
		"Fiji",
		"Sri Lanka",
		"Burundi",
		"Syria",
		"Chile",
		"Ireland",
		"Singapore",
		"Uzbekistan",
		"United Kingdom",
		"Mauritania",
		"Togo",
		"Somalia",
		"Maldives",
		"Germany",
		"Saint Lucia",
		"Bosnia and Herzegovina",
		"Germany",
		"New Zealand (Aotearoa)"
	]
	unique_countries = [
		"Afghanistan",
		"Albania",
		"Algeria",
		"Andorra",
		"Angola",
		"Antigua and Barbuda",
		"Argentina",
		"Armenia",
		"Aruba",
		"Australia",
		"Austria",
		"Azerbaijan",
		"The Bahamas",
		"Bahrain",
		"Bangladesh",
		"Barbados",
		"Belarus",
		"Belgium",
		"Belize",
		"Benin",
		"Bermuda",
		"Bhutan",
		"Bolivia",
		"Bosnia and Herzegovina",
		"Botswana",
		"Brazil",
		"Brunei",
		"Bulgaria",
		"Burkina Faso (formerly Upper Volta)",
		"Burundi",
		"Cambodia",
		"Cameroon",
		"Canada",
		"Cape Verde",
		"Central African Republic",
		"Chad",
		"Chile",
		"People's Republic of China",
		"Republic of China (Taiwan)",
		"Cook Islands",
		"Colombia",
		"Comoros",
		"Democratic Republic of the Congo (formerly Zaire)",
		"Republic of the Congo",
		"Costa Rica",
		"Côte d'Ivoire",
		"Croatia",
		"Cuba",
		"Republic of Cyprus",
		"Czech Republic",
		"Denmark",
		"Djibouti",
		"Dominica",
		"Dominican Republic",
		"Democratic Republic of Congo",
		"East Timor",
		"Ecuador",
		"Egypt",
		"El Salvador",
		"Equatorial Guinea",
		"Eritrea",
		"Estonia",
		"Ethiopia",
		"Fiji",
		"Finland",
		"France",
		"Gabon",
		"The Gambia",
		"Georgia",
		"Germany",
		"Ghana",
		"Greece",
		"Grenada",
		"Guatemala",
		"Guinea",
		"Guinea-Bissau",
		"Guyana",
		"Haiti",
		"Holy See (see Vatican City)",
		"Honduras",
		"Hungary",
		"Iceland",
		"India",
		"Indonesia",
		"Iran",
		"Iraq",
		"Ireland",
		"Israel",
		"Italy",
		"Ivory Coast (see Côte d'Ivoire)",
		"Jamaica",
		"Japan",
		"Jordan",
		"Kazakhstan",
		"Kenya",
		"Kiribati",
		"Kuwait",
		"Kyrgyzstan",
		"Laos",
		"Latvia",
		"Lebanon",
		"Lesotho",
		"Liberia",
		"Libya",
		"Liechtenstein",
		"Lithuania",
		"Luxembourg",
		"Republic of Macedonia",
		"Madagascar",
		"Malawi",
		"Malaysia",
		"Maldives",
		"Mali",
		"Malta",
		"Marshall Islands",
		"Mauritania",
		"Mauritius",
		"Mexico",
		"Federated States of Micronesia",
		"Moldova",
		"Monaco",
		"Mongolia",
		"Montenegro",
		"Morocco",
		"Mozambique",
		"Myanmar (formerly Burma)",
		"Namibia",
		"Nauru",
		"Nepal",
		"Netherlands",
		"New Zealand (Aotearoa)",
		"Nicaragua",
		"Niger",
		"Nigeria",
		"Niue",
		"North Korea",
		"Norway",
		"Oman",
		"Pakistan",
		"Palau",
		"Panama",
		"Papua New Guinea",
		"Paraguay",
		"Peru",
		"Philippines",
		"Poland",
		"Portugal",
		"Qatar",
		"Romania",
		"Russia",
		"Rwanda",
		"Saint Kitts and Nevis",
		"Saint Lucia",
		"Saint Vincent and the Grenadines",
		"Samoa",
		"San Marino",
		"São Tomé and Príncipe",
		"Saudi Arabia",
		"Senegal",
		"Serbia",
		"Seychelles",
		"Sierra Leone",
		"Singapore",
		"Slovakia",
		"Slovenia",
		"Solomon Islands",
		"Somalia",
		"South Africa",
		"South Korea",
		"South Sudan",
		"Spain",
		"Sri Lanka",
		"Sudan",
		"Suriname",
		"Swaziland",
		"Sweden",
		"Switzerland",
		"Syria",
		"Taiwan (see Republic of China)",
		"Tajikistan",
		"Tanzania",
		"Thailand",
		"Togo",
		"Tonga",
		"Trinidad and Tobago",
		"Tunisia",
		"Turkey",
		"Turkmenistan",
		"Tuvalu",
		"Uganda",
		"Ukraine",
		"United Arab Emirates",
		"United Kingdom",
		"United States",
		"Uruguay",
		"Uzbekistan",
		"Vanuatu",
		"Vatican City (Holy See)",
		"Venezuela",
		"Vietnam",
		"Yemen",
		"Zambia",
		"Zimbabwe"
	]
	country_set = set(countries)
	print(len(countries))
	# print(countries[:5])
	print(len(country_set))
	print('India' in countries)
	print('India' in country_set)
	country_set.add("Rectanglia")
	print(len(country_set))
ex1()