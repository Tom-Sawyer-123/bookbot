
def words_in_book(book):
    words = book.split()
    return(len(words))

def letters_in_book(book):
    letters = book.lower()
    letter_count = {}
    for letter in letters:
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


def book_report(words, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in document")



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_in_book(file_contents)} words found in document")
        print("")
        for k,v in sorted(letters_in_book(file_contents).items(), key=lambda p:p[1], reverse=True):
            if k.isalpha():
                print(f"The '{k}' character was printed {v} times")

main()