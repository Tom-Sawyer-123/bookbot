
def words_in_book(book):
    words = book.split()
    return(len(words))


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(words_in_book(file_contents))

main()