from stats import word_count, char_count, sort_on

import sys



def get_book_text(filepath):

    with open(filepath) as f:

        file_contents = f.read()
            
    return file_contents


def main():

    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    whole_text = get_book_text(sys.argv[1])

    num_words = word_count(whole_text)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")






    counted_char = char_count(whole_text)

    sorted_stats = sort_on(counted_char)



    for item in sorted_stats:

        if item["char"].isalpha():

            print(f"{item['char']}: {item['num']}")


    print("============= END ===============")




main()
