
def words_in_book(book):
    words = book.split()
    return(len(words))

def letters_in_book(book):
    letters = book.lower()
    letter_count = {}
    for letter in letters:
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count
    
    
    return letter_count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(words_in_book(file_contents))
        print(letters_in_book(file_contents))

main()