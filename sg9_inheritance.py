class Publication: #Creates the Parent Class, Publication
  def __init__(self, title, author): #Creates the main objects
    self.title = title #Sets the title
    self.author = author #Sets the author
#Create 5 base functions that can be used by other classes
  def get_title(): #Retrieves the title
    return self.title

  def get_author(): #Retrives the title
    return self.author

  def set_title(self, title): #Overrides the current title with a new one
    self.title = title

  def set_author(self, author): #Overrides the current author with a new one
    self.author = author

  def display_info(self): #Displays the current title and author attributes
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")

class Book(Publication): #Creates a new child class derived from the class "Publication", essentially inheriting the parent class.
  def __init__(self, title, author, number_pages): #Adds "number_pages" to the current object roster
    super().__init__(title, author)
    self.number_pages = number_pages #Sets the new object
#Create 2 new functions involving the new "number_pages" object
  def get_number_of_pages(self): #Retrieves the number of pages, or the integer inside the object
    return self.number_pages

  def set_number_of_pages(self, number_pages): #Ovverides the current integer inside "number_pages"
    if number_pages < 0:
      print("Number of pages must be positive") #If the integer being set is negative, prints a warning and doesn't override the current integer inside "number_pages"
    else:
      self.number_pages = number_pages #Else, override the current integer for a new, positive one

class Magazine(Publication): #Creates a new child class also derived from the class "Publication, inheriting the parent class but not its sibling child class
  def __init__(self, title, author, issue_number): #Adds "issue_number" to the current roster, but doesn't contain "number_pages" from it's sibling class
    super().__init__(title, author)
    self.issue_number = issue_number #Sets the new object

  def get_issue_number(self): #Retrieves the issue number, or the integer inside the object
    return self.issue_number

  def set_issue_number(self, issue_number): #Ovverides the current integer inside "issue_number"
    if issue_number < 0:
      print("Issue Number must be positive") #Similar to its sibling function counterpart, if the integer being set is negative, prints a warning and doesn't override the current integer "issue_number"
    else:
      self.issue_number = issue_number #Else, override the current integer for a new, positive one

#Create the variables containing the classes
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") #Sets the value of the objects inside the "Publication" class
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310) #Sets the value of the objects inside the "Book" class
mag1 = Magazine("National Geographic", "Various Authors", 202) #Sets the value of the objects inside the "Magazine" class

print("Publication Information: ") 
pub1.display_info() #Displays the current information inside the objects within the "Publication" class
pub1.set_title("On Anarchism") #sets a new title
pub1.set_author("Penguin Books") #sets a new author
print("\nNew Publication Information: ")
pub1.display_info() #Will display the new information after setting a new title and author


print("\nBook Information: ")
book1.set_number_of_pages(-310) #Will try to override the integer inside "number_pages", but fails because of a countermeasure
book1.display_info() #Displays the current information insde the objects within the "Book" class
print(book1.get_number_of_pages()) #Gets the number of pages and displays it
book1.set_title("Don Quixote") #sets a new title
book1.set_author("Miguel de Cervantes") #sets a new author
book1.set_number_of_pages(860) #Tries to override the integer inside "number_pages" and succeeds
print("\nNew Book Information: ")
book1.display_info() #Displays the new information after setting a new title and author
print(book1.get_number_of_pages()) #Displays the new set number of pages, or integer in "number_pages"

print("\nMagazine Information: ")
mag1.set_issue_number(-540) #Will try to override the integer inside "issue_number", but fails because of a countermeasure
mag1.display_info() #Displays the current information insde the objects within the "Magazine" class
print(mag1.get_issue_number()) #Gets the issue number and displays it
mag1.set_title("Time") #sets a new title
mag1.set_author("TIME USA") #sets a new author
print("\nNew Magazine Information: ")
mag1.display_info() #Displays the new information after setting a new title and author
print(mag1.get_issue_number()) #Displays the new set issue number, or integer in "issue_number"
