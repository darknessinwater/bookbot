def word_count(path_to_file):
	with open(path_to_file) as f:
        	file_contents = f.read()
        	words = file_contents.split()
        	count = len(words)
        	return count

def character_count(path_to_file):
	with open(path_to_file) as f:
		file_contents = str.lower(f.read())
		letter_count = {}
		for letter in file_contents:
			if letter.isalpha():
				letter_count[letter] = letter_count.get(letter, 0) + 1

	letter_count_list = []
	for letter in letter_count:
		num = letter_count[letter]
		letter_count_list.append({"letter": letter, "num": num})
	letter_count_list.sort(reverse=True, key=sort_on)
	return letter_count_list

def sort_on(items):
	return items["num"]
