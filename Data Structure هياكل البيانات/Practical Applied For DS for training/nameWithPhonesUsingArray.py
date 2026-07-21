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
        print("Name :", p_name)
        # what about phone, it should be at least 10 numbers and maximum of 15
        if p_phone > 5 and len(str(p_phone)) < 15:

          # self.nameWithPhones[arrayLength] = p_name
          # self.nameWithPhones[arrayLength + 1] = p_phone
          self.nameWithPhones.append(p_name)
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


newPhonesList = NameWithPhones()

newPhonesList.addNameWithPhone("Abdallah", 785326279)
newPhonesList.addNameWithPhone("Ahmad", 775333398)
newPhonesList.addNameWithPhone("Ali", 785326279)
# newPhonesList.addNameWithPhone("Ali", 78a26279)

newPhonesList.printPhonesList()
  