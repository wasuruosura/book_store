def main():
    

    try:
        #initialize book list
        booksList = []
    
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError :
        print("The <BooksList.txt> file is not found")
        print("Starting a new Books List!")
        booksList = []

    choice = 0 
    while choice !=4:
        print("*** Books Manager ***")
        print("1) Add Book") 
        print("2) Lookup a Book") 
        print("3) Display Books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...") 
            nBook = input("Enter the name of the Book>>>")
            nAuthor = input("Enter the name of the Author>>>")
            nPages = input("Enter the number of the Pages>>>")
            booksList.append([nBook, nAuthor, nPages]) 

        elif choice == 2:
            print("Lookingup for a Book...")
            keyword = input("Enter a search term...")
            for book in booksList:
                if keyword in book:
                    print(book) 

        elif choice == 3: 
            print("Displaying all Books...")
            for books in range (len(booksList)):
                print(booksList[books])

        elif choice == 4:
            print("Quitting programm")
            print("Programm Terminated!")

#Saving to external txt.file
    outfile = open("theBooksList.txt", "w" )
    for book in booksList:
        outfile.write(",".join(book) + "\n" )
    outfile.close()
     


if __name__ == "__main__":
    main()