names = [
	"Joey Tribbiani",
	"Monica Geller",
	"Chandler Bing",
	"Phoebe Buffay"
]
def question_1(names):
	usernames = [name.replace(" ","_").lower() for name in names]
	print(usernames)

def question_2(names):
	print(names)
	for name in names:
		name = name.lower().replace(" ", "_")
	print(names)

def question_3(names):
	usernames = [names[i].replace(" ","_").lower() for i in range(len(names))]
	print(usernames)

def question_4():
	tokens = [
		'<greeting>',
		'Hello World!',
		'</greeting>'
	]

	count = sum(
		int(token[0]=="<" and token[-1]==">") for token in tokens
	)

	print(count)

def question_5(items):
	z = ['<ul>']
	for item in items:
		z.append("<li>"+item+"</li>")
	z.append('</ul>')
	print("\n".join(z))


# question_1(names)
# question_2(names)
# question_3(names)
# question_4()
question_5(['first string', 'second string'])