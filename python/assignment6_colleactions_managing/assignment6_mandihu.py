__author__ = 'Die Hu, mandihu@live.unc.edu, Onyen = mandihu'

# Performs case insensitive partial string matching.
# Returns True of query_str is part of full_str (ignoring upper/lower case).
# Otherwise returns False.
def is_substring_match(query_str, full_str):
    return query_str.lower() in full_str.lower()


# Loads data for both books and movies, returning a dictionary with two keys, 'books' and 'movies', one for
# each subset of the collection.
def load_collections():

    # Load the two collections.
    book_collection, max_book_id = load_collection("books.csv")
    movie_collection, max_movie_id = load_collection("movies.csv")

    # Check for error.
    if (book_collection is None) or (movie_collection is None):
        return None, None

    # Return the composite dictionary.
    return {"books": book_collection, "movies": movie_collection}, max(max_book_id, max_movie_id)


# Loads a single collection and returns the data as a dictionary.  Upon error, None is returned.
def load_collection(file_name):
    max_id = -1
    try:
        # Create an empty collection.
        collection = []

        # Open the file and read the field names
        collection_file = open(file_name, "r")
        field_names = collection_file.readline().rstrip().split(",")

        # Read the remaining lines, splitting on commas, and creating dictionaries (one for each item)
        for item in collection_file:
            field_values = item.rstrip().split(",")
            collection_item = {}
            for index in range(len(field_values)):
                if (field_names[index] == "Available") or (field_names[index] == "Copies")\
                        or (field_names[index] == "ID"):
                    collection_item[field_names[index]] = int(field_values[index])
                else:
                    collection_item[field_names[index]] = field_values[index]
            # Add the full item to the collection.
            collection.append(collection_item)
            # Update the max ID value
            max_id = max(max_id, collection_item["ID"])

        # Close the file now that we are done reading all of the lines.
        collection_file.close()

    # Catch IO Errors, with the File Not Found error the primary possible problem to detect.
    except FileNotFoundError:
        print("File not found when attempting to read", file_name)
        return None
    except IOError:
        print("Error in data file when reading", file_name)
        collection_file.close()
        return None

    # Return the collection.
    return collection, max_id

# Display the menu of commands and get user's selection.  Returns a string with the user's requested command.
# No validation is performed.
def prompt_user_with_menu():
    print("\n\n********** Welcome to the Collection Manager. **********")
    print("COMMAND    FUNCTION")
    print("  ci         Check in an item")
    print("  co         Check out an item")
    print("  ab         Add a new book")
    print("  am         Add a new movie")
    print("  db         Display books")
    print("  dm         Display movies")
    print("  qb         Query for books")
    print("  qm         Query for movies")
    print("  x          Exit")
    return input("Please enter a command to proceed: ")

# Print all information of a book or a movie.
def print_information(file_kind, collection_item):
    if file_kind == "books":
        collection_file = open("books.csv", "r")
    elif file_kind == "movies":
        collection_file = open("movies.csv", "r")

    # Get field names of books file or movies file.
    field_names = collection_file.readline().rstrip().split(",")

    # Print ID first.
    print("ID: ", collection_item['ID'])

    # Print other information except ID.
    for i in range(len(field_names)-1):
        print(field_names[i], ": ", collection_item[field_names[i]], sep='')
    print("")


# Check in an item.
def check_in(library_collections):

    # Set id_included default as False and ask users to input an ID
    # until users input an ID which can be found in the file.
    id_included = False
    while id_included == False:

        try:
            # Ask users to input the ID they want to check in.
            id = int(input("Enter the ID for the item you want to check in: "))

            # Set check_in default as True. When the item of the ID is unable to check in, set check_in variable to
            # be False to prompt the message indicating unsuccessful checking in.
            check_in = True

            # Check the ID in books collection.
            for books in library_collections["books"]:
                if id == books['ID']:

                    # ID is found, change id_included to True to avoid ask users to input an ID again.
                    id_included = True

                    if books['Available'] < books['Copies']:
                        books['Available'] += 1
                        print("Your check in has succeeded.")
                        print_information("books", books)

                    # When item of the ID is unable to be checked in, checking in is unsuccessful.
                    else :
                        check_in = False

            # Check the ID in movies collection.
            for movies in library_collections["movies"]:
                if id == movies['ID']:

                    # ID is found, change id_included to True to avoid ask users to input an ID again.
                    id_included = True

                    if movies['Available'] < movies['Copies']:
                        movies['Available'] += 1
                        print("Your check in has succeeded.")
                        print_information("movies", movies)

                    # When item of the ID is unable to be checked in, checking in is unsuccessful.
                    else :
                        check_in = False

            # Unable to check in, prompt the message.
            if check_in == False:
                print("All copies are already available, so this item can not be checked in.")

            # Unable to find the ID, prompt the message.
            if id_included == False:
                print("ID", id, "can not be found in either books or movies collections. Please try again.")

        # ID validation.
        except ValueError:
            print("The ID must be a valid integer. Please try again.")

        else:
            if id <= 0:
                print("The ID must be positive. Please try again.")

# Check out an item.
def check_out(library_collections):

    # Set id_included default as False and ask users to input an ID
    # until users input an ID which can be found in the file.
    id_included = False

    while id_included == False:

        try:
            # Ask users to input the ID they want to check out.
            id = int(input("Enter the ID for the item you want to check out: "))

            # Set check_out default as True. When the item of the ID is unable to check out, set check_out variable to
            # be False to prompt the message indicating unsuccessful checking out.
            check_out = True

            # Check the ID in books collection.
            for books in library_collections["books"]:
                if id == books['ID']:

                    # ID is found, change id_included to True to avoid ask users to input an ID again.
                    id_included = True

                    if books['Available'] > 0:
                        books['Available'] -= 1
                        print("Your check out has succeeded.")
                        print_information("books", books)

                    # When item of the ID is unable to be checked in, checking in is unsuccessful.
                    else :
                        check_out = False

            # Check the ID in movies collection.
            for movies in library_collections["movies"]:
                if id == movies['ID']:

                     # ID is found, change id_included to True to avoid ask users to input an ID again.
                    id_included = True

                    if movies['Available'] > 0:
                        movies['Available'] -= 1
                        print("Your check out has succeeded.")
                        print_information("movies", movies)

                    # When item of the ID is unable to be checked in, checking in is unsuccessful.
                    else :
                        check_out = False

            # Unable to check out, prompt the message.
            if check_out == False:
                print("No copies of the item are available for check out.")

            # Unable to find the ID, prompt the message.
            if id_included == False:
                print("ID", id, "can not be found in either books or movies collections. Please try again.")

        # ID validation.
        except ValueError:
            print("The ID must be a valid integer. Please try again.")

        else:
            if id <= 0:
                print("The ID must be positive. Please try again.")

# Add a book.
def add_book(library_collections, max_existing_id):
    try:
        # Ask users to input the information of the book.
        print("Please enter the following attributes for the new book.")

        # Assign the ID automatically.
        id = max_existing_id + 1

        title = input("Title: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        pages = input("Pages: ")

        # Convert pages to integer to catch the ValueError if users input string instead of number.
        pages_int = int(pages)
        year = input("Year: ")

        # Convert year to integer to catch the ValueError if users input string instead of number.
        year_int = int(year)
        copies = int(input("Copies: "))
        available = int(input("Available: "))

    # Invalid pages, year, copies and available.
    except ValueError:
        print("Pages, Year, Copies, and Available should be valid integer. Adding the book is unsuccessful. ")
        return max_existing_id
    else:
        if pages_int <= 0 or year_int <= 0 or copies <= 0 or available <= 0:
            print("The Pages, Year, Copies, or Available must be a positive number.",
                  "Adding the book is unsuccessful. ")
            return max_existing_id

        elif copies < available:
            print("The Copies shouldn't be less than Available. Adding the movie is unsuccessful.")
            return max_existing_id

        else:
            # Create a dictionary to store the information of the book and add into the list of book collection.
            book_info = {"Title": title, "Author": author, "Publisher": publisher, "Pages": pages,"Year": year,"Copies": copies,\
                         "Available": available, "ID": id}
            library_collections['books'].append(book_info)

            # Print the data users input.
            print("You have entered the following data.")
            print_information("books", book_info)

            # Update max_existing_id
            max_existing_id += 1
            return max_existing_id

# Add a movie.
def add_movie(library_collections, max_existing_id):
    try:
        # Ask users to input the information of the book.
        print("Please enter the following attributes for the new movie.")

        # Assign the ID automatically.
        id = max_existing_id + 1

        title = input("Title: ")
        director = input("Director: ")
        length = input("Length: ")

        # Convert length to integer to catch the ValueError if users input string instead of number.
        length_int = int(length)
        genre = input("Genre: ")
        year = input("Year: ")

        # Convert year to integer to catch the ValueError if users input string instead of number.
        year_int = int(year)
        copies = int(input("Copies: "))
        available = int(input("Available: "))

    # Invalid length, year, copies and available.
    except ValueError:
        print("Length, Year, Copies, and Available should be valid integer. Adding the movie is unsuccessful. ")
        return max_existing_id
    else:
        if length_int <= 0 or year_int <= 0 or copies <= 0 or available <= 0:
            print("The Length, Year, Copies, or Available must be a positive number.",
                  "Adding the movie is unsuccessful. ")
            return max_existing_id

        elif copies < available:
            print("The Copies shouldn't be less than Available. Adding the movie is unsuccessful.")
            return max_existing_id

        else:
            # Create a dictionary to store the information of the movie and add into the list of movie collection.
            movie_info = {"Title": title, "Director": director, "Length": length, "Genre": genre,"Year": year,"Copies": copies,\
                          "Available": available, "ID": id}
            library_collections['movies'].append(movie_info)

            # Print the data users input.
            print("You have entered the following data.")
            print_information("movies", movie_info)

            # Update max_existing_id
            max_existing_id += 1
            return max_existing_id

# Display all books or movies with 10 items at a time.
def display_collection(library_collection):
    for i in range(len(library_collection)):
        operation = ""

        # Just display 10 items at a time and when 10 items have been display, ask users to input a command.
        if i // 10 >=1 and i % 10 == 0:
            operation = input("Press enter to show more items, or type 'm' to return to the menu.")

            # Validation.
            while operation != "" and operation != "m":
                print("Unknown command. Please try again.")
                operation = input("Press enter to show more items, or type 'm' to return to the menu.")

        if operation == "":

            # Display movies.
            if "Director" in library_collection[0].keys() and "Genre" in library_collection[0].keys():
                print_information("movies", library_collection[i])

            # Display books.
            elif "Author" in library_collection[0].keys() and "Publisher" in library_collection[0].keys():
                print_information("books", library_collection[i])

        elif operation == "m":
            break

# Query for a book or movie.
def query_collection(library_collection):
    query = input("Enter a query string to use for the search: ")

    # Set found default as True. When the query cannot match any books or movies, set it to False and prompt
    # the message indication no result of this query.
    found = False

    # Search in movies collection.
    if "Director" in library_collection[0].keys() and "Genre" in library_collection[0].keys():
        for movies in library_collection:
            if is_substring_match(query, movies['Title'])\
               or is_substring_match(query, movies['Director'])\
               or is_substring_match(query, movies['Genre']):
                print_information("movies", movies)
                found = True

    # Or search in books collection
    elif "Author" in library_collection[0].keys() and "Publisher" in library_collection[0].keys():
        for books in library_collection:
            if is_substring_match(query, books['Title'])\
               or is_substring_match(query, books['Author'])\
               or is_substring_match(query, books['Publisher']):
                print_information("books", books)
                found = True

    # When no result has been found, prompt the message.
    if found == False:
        print("No result has been found.")


# This is the main program function.  This function should (1) Load the data and
# (2) Manage the main program loop that lets the user perform the various operations (ci, co, qb, etc.)
def main():
    # Load the collections, and check for an error.
    library_collections, max_existing_id = load_collections()
    if library_collections is None:
        print("The collections could not be loaded. Exiting.")
        return
    print("The collections have loaded successfully.")

    # Display the error and get the operation code entered by the user.  We perform this continuously
    # until the user enters "x" to exit the program.
    # Calls the appropriate function that corresponds to the requested operation.
    operation = prompt_user_with_menu()
    while operation != "x":
        ###############################################################################################################
        ###############################################################################################################
        # HINTS HINTS HINTS!!! READ THE FOLLOWING SECTION OF COMMENTS!
        ###############################################################################################################
        ###############################################################################################################
        #
        # The commented-out code below gives you a some good hints about how to structure your code.
        #
        # FOR BASIC REQUIREMENTS:
        #
        # Notice that each operation is supported by a function.  That is good design, and you should use this approach.
        # Moreover, you will want to define even MORE functions to help break down these top-level user operations into
        # even smaller chunks that are easier to code.
        #
        # FOR ADVANCED REQUIREMENTS:
        #
        # Notice the "max_existing_id" variable?  When adding a new book or movie to the collection, you'll need to
        # assign the new item a unique ID number.  This variable is included to make that easier for you to achieve.
        # Remember, if you assign a new ID to a new item, be sure to keep "max_existing_id" up to date!
        #
        # Have questions? Ask on Piazza!
        #
        ###############################################################################################################
        ###############################################################################################################
        #
        #
        if (operation == "ci"):
            check_in(library_collections)
        elif (operation == "co"):
            check_out(library_collections)
        elif (operation == "ab"):
            max_existing_id = add_book(library_collections, max_existing_id)
        elif (operation == "am"):
            max_existing_id = add_movie(library_collections, max_existing_id)
        elif (operation == "db"):
             display_collection(library_collections["books"])
        elif (operation == "dm"):
             display_collection(library_collections["movies"])
        elif (operation == "qb"):
             query_collection(library_collections["books"])
        elif (operation == "qm"):
             query_collection(library_collections["movies"])
        else:
            print("Unknown command.  Please try again.")

        operation = prompt_user_with_menu()


# Start the program!
main()