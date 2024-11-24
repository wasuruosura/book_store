def main():
    try:
        # Initialize book list
        booksList = []
        infile = open("theBooksListUpdate.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("The <BooksListUpdate.txt> file is not found")
        print("Starting a new Books List!")
        booksList = []

    choice = 0
    while choice != 5:  # Updated to include an additional option
        print("\n*** Books Manager ***")
        print("1) Add Book")
        print("2) Lookup a Book")
        print("3) Display Books")
        print("4) Update Book")  # New option for updating
        print("5) Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nAdding a book...")
            nBook = input("Enter the name of the Book: ")
            nAuthor = input("Enter the name of the Author: ")
            nPages = input("Enter the number of Pages: ")
            booksList.append([nBook, nAuthor, nPages])
            print(f"Book '{nBook}' added successfully.")

        elif choice == 2:
            print("\nLooking up for a Book...")
            keyword = input("Enter a search term: ")
            found = False
            for book in booksList:
                if keyword in book:
                    print(book)
                    found = True
            if not found:
                print("No books found with that keyword.")

        elif choice == 3:
            print("\nDisplaying all Books...")
            if not booksList:
                print("No books to display.")
            else:
                for index, book in enumerate(booksList, start=1):
                    print(f"{index}. {book}")

        elif choice == 4:  # Update book functionality
            print("\nUpdating a book...")
            search_term = input("Enter the name of the Book to update: ")
            for book in booksList:
                if search_term.lower() == book[0].lower():  # Match by book name
                    print(f"Book found: {book}")
                    print("What do you want to update?")
                    print("1) Book Name")
                    print("2) Author Name")
                    print("3) Number of Pages")
                    update_choice = int(input("Enter your choice: "))

                    if update_choice == 1:
                        new_name = input("Enter the new Book Name: ")
                        book[0] = new_name
                        print("Book name updated successfully.")
                    elif update_choice == 2:
                        new_author = input("Enter the new Author Name: ")
                        book[1] = new_author
                        print("Author name updated successfully.")
                    elif update_choice == 3:
                        new_pages = input("Enter the new Number of Pages: ")
                        book[2] = new_pages
                        print("Number of pages updated successfully.")
                    else:
                        print("Invalid choice.")
                    break
            else:
                print("Book not found.")

        elif choice == 5:
            print("\nQuitting program...")
            print("Program Terminated!")

    # Saving to external txt file
    outfile = open("theBooksListUpdate.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()
