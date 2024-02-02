#You are asked to ensure that the first and last names of people begin with a capital letter in their passports
 #For example, alison heck should be capitalised correctly as Alison Heck. A single line of input containing the full name, 
 #The string consists of alphanumeric characters and spaces.
def capitalize(f_name):
    # split the names
    names = f_name.split()
    # capitalize the first letter of each name
    capitalized_names = [name.capitalize() for name in names]
    # rejoin the names to a singe string
    capitalized_fullName = ' '.join(capitalized_names)
    print (capitalized_fullName)
    
    
capitalize('12abc')

