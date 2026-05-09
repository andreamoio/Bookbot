from stats import counting
from stats import character_counter
from stats import sort_list 
from stats import real_function 
import sys

def get_book_text(path): 

    with open(path) as book: 
        
        return book.read()

def main():

    if len(sys.argv) != 2:

        print("Usage: python3 main.py <path_to_book>")

        sys.exit(1)

    else:

        path = sys.argv[1]
        text = get_book_text(path)

        total_number = counting(text)
    

        my_dictionary = character_counter(text)
        new_list = real_function(my_dictionary)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {total_number} total words")
        print("--------- Character Count -------")
    
    
        for item in new_list:

            if not item["char"].isalpha():
                continue

            else:
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")

main()

