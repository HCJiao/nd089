vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
letter_number_pairs = {'a': 1,'b': 8,'c': 3,'f': 3,'h': 8,'i': 2,'l': 4,'p': 2,'q': 1,'s': 5,'u': 9,'w': 0,'y': 5,'z': 2}

def original_method(vowels, consonants, letter_number_pairs):
    vowel_value_sum     = sum(value for (letter, value) in letter_number_pairs.items() if letter in vowels)
    consonant_value_sum = sum(value for (letter, value) in letter_number_pairs.items() if letter in consonants)
    return vowel_value_sum, consonant_value_sum

def stack_overflow_O_1_method(vowels, consonants, letter_number_pairs):
    a, b = 0, 0
    vowels = set(vowels)
    for k, v in letter_number_pairs.items():
        if k in vowels:
            a += v
        else:
            b += v
    return (a,b)

vowel_value_sum, consonant_value_sum = stack_overflow_O_1_method(vowels, consonants, letter_number_pairs)
print(vowel_value_sum, consonant_value_sum)