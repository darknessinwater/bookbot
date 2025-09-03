def main():
	import sys

	if __name__ == "__main__":
		if len(sys.argv) != 2:
			print("'Usage: python3 main.py <path_to_book>'")
			sys.exit(1)

	file = sys.argv[0]
	book = sys.argv[1]

	from stats import word_count
	path_to_file = sys.argv[1]

	count = word_count(path_to_file)


	from stats import character_count
	letter_count_list = character_count(path_to_file)
	

	print("============ BOOKBOT ============")
	print()
	print(f"Analyzing book found at {path_to_file}")
	print()
	print("----------- Word Count -----------")
	print()
	print(f"Found {count} total words")
	print()
	print("-------- Character Count ---------")
	print()
	for item in letter_count_list:
		letter = item["letter"]
		num = item["num"]
		if letter.isalpha():
			print(f"{letter}: {num}")
			print()
main()

