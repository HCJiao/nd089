username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message incorporating the strings above.
# The message should use the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username+" accessed the site "+url+" at "+timestamp+".")

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
names = [given_name, middle_names, family_name]
name_length = sum(len(name) for name in names) + len(names)-1
# print(name_length)
# print(len(given_name+middle_names+family_name))
# Check that the name fits within the driving license character limit
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)