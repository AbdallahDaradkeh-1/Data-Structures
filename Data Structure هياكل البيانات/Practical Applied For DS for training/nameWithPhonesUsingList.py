# Two or One Array:
# One Array: Each Two Elements are for one person

            #*
            # Each Two adjecant elements are for one person 
            # 
            # We need method to add a new person Name and Number(Both Are Required)
            # 
            # A way to Search For phone Numbers through phone
            # 
            # A way to Search For Names Through Phone Numbers
            # 
            # We will do all of this initially in the terminal
            # 
            # *#

# Let us go with only single array

# A class, so we can create as many lists we want
class NameWithPhones:
  
  # our constructor
  def __init__(self):#We will stay simple right now
    # self.name = person_name
    # self.phone = person_phone
    self.nameWithPhones = [] # The array To Store the data(Name and Phone)

  # Function To Insert Values
  def addNameWithPhone(self, p_name, p_phone):
    # We want to insert Name and Phones, but next time, how we tell to add after, yes there is a function append
    try:
      # do we have any rule, it is a must the name should be at least one charachter and not duplicate
      if len(p_name) > 1 and not self.isNameExist(p_name):
        arrayLength = len(self.nameWithPhones)
        # what about phone, it should be at least 10 numbers and maximum of 15
        if p_phone > 5 and len(str(p_phone)) < 15:
          
          # self.nameWithPhones[arrayLength] = p_name
          # self.nameWithPhones[arrayLength + 1] = p_phone # This does not Work
                                                   #Because append include doubling array size
          self.nameWithPhones.append(p_name)      #When we want to add element while out of bounds
          self.nameWithPhones.append(p_phone)

    
    except ValueError:
      print("Invalid Input!")
  
      # Let us test but create print function at first


    # I will Stop here and create isExist() function
  def isNameExist(self, p_name):
    arrayLength = len(self.nameWithPhones)
    i = 0

    while i < arrayLength:
      if self.nameWithPhones[i] == p_name:
        return True
      else:
        return False
      i += 2
  def printPhonesList(self):
    print(self.nameWithPhones)
  
  # Search for phone Number Through Name Property, When user enter value let us return all possible Name with numbers. Example: u_input: A -> output: Abdallah, 078532621  New Line Ahmad, 077553(phone)

  def searchForPhoneNumbersThroughNames(self, u_input):
    outputNums = 0
    arrayLength = len(self.nameWithPhones)
    i = 0
    while i < arrayLength:
      if self.nameWithPhones[i] == u_input:
        print(self.nameWithPhones[i], self.nameWithPhones[i+1])
        outputNums += 1
      i += 2
    if outputNums == 0:
      print("Not exist")

  def searchForPhoneNumbersListThroughNames(self, u_input): #This gives all phone numbers that are 
    outputNums = 0                                        #Similar to the input, If the input is: a
    arrayLength = len(self.nameWithPhones)                #For example: output will be: Adam, Ahmad,
    i = 0                                              #And even: Taher. But the priority to A at
    while i < arrayLength:                          #First
      if u_input.lower() in self.nameWithPhones[i].lower():
        print(self.nameWithPhones[i], self.nameWithPhones[i+1])
        outputNums += 1
      i += 2
    if outputNums == 0:
      print("Not exist")
  def deleteFromNameWithPhonesUsingName(self, u_input):
    # If u_input is exactly equal to one element, it will be deleted
    arrayLength = len(self.nameWithPhones)
    i = 0
    while i < arrayLength:
      if u_input.lower() == str(self.nameWithPhones[i]).lower():
        deletedName = self.nameWithPhones.pop(i)
        deletedPhone = self.nameWithPhones.pop(i)
        
        print(deletedName, deletedPhone, "Has Been Deleted Successfully")
        return
      i += 2
      print("No Such Element Exist")
  def deleteFromNameWithPhonesUsingNameLikely(self, u_input):
    # User enter input, if there is no such exact element, show the elements that look like the user
    # Input with numbers, user choose the number for the element he wants to delete and it is done
    arrayLength = len(self.nameWithPhones)
    i = 0
    while i < arrayLength:
      if u_input.lower()  == str(self.nameWithPhones[i]).lower():
        deletedName = self.nameWithPhones.pop(i)
        deletedPhone = self.nameWithPhones.pop(i)
        print(deletedName, deletedPhone, " Has Been Deleted Successfully!")
        return
      i += 2
    i = 0
    print("Available Phone Nubmers that look like your u_input",'"',u_input,'"' ,  "Choose One to Delete:(If you want to tdelete the first result, Choose 1 for example not the phone number itself)")

    j = 1
    similarResultsIndecies = []
    while i < arrayLength:
      if u_input.lower() in str(self.nameWithPhones[i]).lower():
        
        print(j, self.nameWithPhones[i])
        j += 1
      
        similarResultsIndecies.append(i)
      i += 2

    chosenNumber = int(input())
    
    l = 0
    indeciesArrayLength = len(similarResultsIndecies)
    if 1 <= chosenNumber and chosenNumber <= len(similarResultsIndecies):
      selectedIndex = similarResultsIndecies[chosenNumber - 1]
      deletedName = self.nameWithPhones.pop(selectedIndex)
      deletedPhone = self.nameWithPhones.pop(selectedIndex)

      print(deletedName, deletedPhone, "Has Been Deleted Successfully")
      return
    
    print("No Such Element exist")
    return
  def changeValueForNames(self, u_input):
    # We show user available elements that he can change
    print("These are Names that you can change:")
    arrayLength = len(self.nameWithPhones)
    i = 0
    j = 1
    nameList = []
    indecisList = []
    while i < arrayLength:
      nameList.append(self.nameWithPhones[i])
      indecisList.append(i)
      print(j, self.nameWithPhones[i])
      j += 1
      i += 2

    # User Choose an element from those elements to change it's value
    print("Please Choose The Number Of The Name You Want To Change:")
    chosenNameNumber = int(input())
    indecisListLength = len(indecisList)
    if chosenNameNumber < indecisListLength or chosenNameNumber > indecisListLength:
      print("Invalid Input")
      return
  

    print("Please Enter The New Value")
    try:
      newNameValue = input()
      if len(newNameValue) > 1:
        self.nameWithPhones[indecisList[chosenNameNumber - 1]] = newNameValue
    except ValueError:
      print("Invalid Input!")


    #*
    # We show user available elements that he can change
    # 
    # User Choose an element from those elements to change it's value
    # 
    # User enter the new value for the element
    # 
    # Element value got updated
    # 
    #
    # 
    #  *#

        
          

        


newPhonesList = NameWithPhones()

newPhonesList.addNameWithPhone("Abdallah", 785326279)
newPhonesList.addNameWithPhone("Ahmad", 775333398)
newPhonesList.addNameWithPhone("Ali", 785326279)
# newPhonesList.addNameWithPhone("Ali", 78a26279)

# newPhonesList.printPhonesList()

# newPhonesList.searchForPhoneNumbersListThroughNames("a")

# u_input = "Ahmad"

# print(u_input.lower())

# print("After Using Delete Method")

# newPhonesList.deleteFromNameWithPhonesUsingName("Abdallah")
# print("Printed")
# newPhonesList.printPhonesList()

# print("After Using Delete Method Second Time")

# newPhonesList.deleteFromNameWithPhonesUsingName("Ahmad")

# newPhonesList.printPhonesList()

# print("Test DeletedLikely method")

# newPhonesList.deleteFromNameWithPhonesUsingNameLikely("A")

# newPhonesList.printPhonesList()

print("Testing Change Value Method")

newPhonesList.changeValueForNames("Abdallah")

newPhonesList.printPhonesList()