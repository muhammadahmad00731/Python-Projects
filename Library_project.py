class Library:
    def __init__(self):
        # Initial list of books
        self.books = ["Talash", "How To Show Your Work","Rich Dad Poor Dad"]

    def show_books(self):
        (self.books).sort()
        print(f"\nThe default library is:\n{self.books}\n")

    def add_books(self):
        try:
            user_choice = int(input("Enter '1' to add a book: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if user_choice == 1:
            new_book = input("Enter Book to add: ")
            self.books.append(new_book)
            self.books.sort()
            print(f"\nThe library after appending is:\n{self.books}")
        else:
            print("Invalid Input\nNo appending")

    def total_books(self):
        print(f"\nTotal number of books = {len(self.books)}")


# Create an object of Library
object1 = Library()

# Call methods
object1.show_books()
object1.add_books()
object1.total_books()