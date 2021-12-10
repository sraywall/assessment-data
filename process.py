log_file = open("um-server-01.txt")#declaring a text I/O object and assigning it by opening "um-server-01.txt"

def sales_reports(log_file):#declaring a function called sales_reports that takes in a
    for line in log_file:  #iterating through each line of the file
        line = line.rstrip() # removing return characters
        day = line[0:3] #declaring a string with first three letters of the line
        if day == "Tue": #checking if the string equals 'Tue'
            print(line) #printing the entire line

def melons_over_10(log_file):
    for line in log_file:
        line = line.rstrip()
        count = int(line.split(" ")[2])
        if count > 10:
            print(count)
            print(line)

# sales_reports(log_file) # prints all deliveries that happened on a Tuesday
melons_over_10(log_file)