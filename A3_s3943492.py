#COSC1519 Introduction to Programming
#Assessment 3 Programming Project
#Student name: Matthew Shanahan
#Student number: s3943492

def find_col_int(number): #returns a list of all items in a given column
    return[int(element[number]) for element in sort_content]

def Sing_Item_Info(sort_content): #prints the information related to any given item
    print("Show One Item Information - SELECTED")
    print("Available Items:", *find_col_int(0))
    try:
        name = input('Name: ')
        Item = List_Item_Exists(name) #check whether the inputted item matches one already in the system,
        if Item == True: #if there is a match, find the index of the match, and then print the nested_list that it correstponds to
            print(name, 'Is an Item that currently exists with info:')
            Item_Info = find_row(name) #the index method returns the position of an in item in a list that matches a string
        print(*sort_content[Item_Info]) #used the result of the index method to find the list associated with the name given by the user
    except: #if the index method has an error it should be because there were no matching items, so the item requested does not exist
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                           Item Does Not Exist!')
        print('')
        print('---------------------------------------------------------------------------------------------------------------------------')
    return

def All_Item_Info():
    print('Show all stock information - SELECTED')
    print('---------------------------------------------------------------------------------------------------------------------------')
    print('')
    print('                                                 All Information:')
    print('')
    print('---------------------------------------------------------------------------------------------------------------------------')
    for i in sort_content: #loop through sort_content and display each of its nested_lists on an individual line
        print(*i)#asterisks is used here to force the nested_lists of sort_content to display without the list formatting
    return

def List_Item_Exists(name):
    List_Item_Exists = False#set List_Item_Exists to false in case it had previously been set to true
    for i in range(len(sort_content)):
        if name == sort_content[i][0]: #if name is equal to the first value in any of sort_content's nested_lists, then List_Item_Exists must be true
            List_Item_Exists = True
            return(List_Item_Exists)

def find_row(name):
    return(find_col_int(0).index(int(name)))


def AddItem(sort_content): #add a new nested_list to sort_content
    print('Add New Item - SELECTED')
    name = (input('Name: '))#have user input name
    Item = List_Item_Exists(name)
    if Item == True: #cant make a duplicate item
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                           '+ name, 'Already Exists! Add Cancelled!')
        print('')#inform the user that it was unsuccessful
        print('---------------------------------------------------------------------------------------------------------------------------')
    else:
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                                 '+ name, 'Is a New Item')
        print('')
        print('---------------------------------------------------------------------------------------------------------------------------')
        new_item = [] #create a new list to append the new items to
        new_item.append(name)
        est_price = input('Est_Price: ')
        new_item.append(est_price)
        qty = input('QTY: ')            #append each item to a list as they are assigned
        new_item.append(qty)             #append the list to sort_content as a nestedlist to match the rest of the data
        designer = input('Designer: ')
        new_item.append(designer)
        manufacturer = input('Manufacturer: ')
        new_item.append(manufacturer)
        sort_content.append(new_item)#append new list to sort_content so that it our relational data becomes a nested_list
        sort_content = sorted(sort_content, key=lambda x:x[0]) #re-sort sort_content so that the first column appears in alphabetical order
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                 Add Successful:', name, est_price, qty, designer, manufacturer)
        print('')#inform the user  that it was successful and display  the items of the new list
        print('---------------------------------------------------------------------------------------------------------------------------')
        return
    return

def EditItem(sort_content):
    print('Update Item - SELECTED')
    new_item = []
    print("Available Items:", *find_col_int(0))
    name = input('Name: ')
    Item = List_Item_Exists(name) #check whether the inputted item matches one already in the syste,
    if Item == True: 
        print(name, 'Is an Item that currently exists with info:')
        Item_Info = find_row(name) #use index to find nested_list
        print('    Est_price: ', sort_content[Item_Info][1]) #manually iterate though the nested_list in order to show labels with data
        print('    Qty: ', sort_content[Item_Info][2])        #display the Items that will be overwritten to the user
        print('    Designer: ', sort_content[Item_Info][3])
        print('    Manufacturer: ', sort_content[Item_Info][4])
        del sort_content[Item_Info] #clearing the nested_list so that it can be replaced with new Items
        new_item.append(name)
        est_price = input('Est_Price: ')
        new_item.append(est_price)
        qty = input('QTY: ')
        new_item.append(qty)
        designer = input('Designer: ')
        new_item.append(designer)
        manufacturer = input('Manufacturer: ') #append each item to a list
        new_item.append(manufacturer)
        sort_content.append(new_item)#append list to sort_content so that it matches the format of all the nested_lists
        sort_content = sorted(sort_content, key=lambda x:x[0]) #re-sort sort_content so that the first column appears in alphabetical order
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                              Update Successfull:', name, est_price, qty, designer, manufacturer)
        print('')#save the items so they can be used to show the user what they saved
        print('---------------------------------------------------------------------------------------------------------------------------')
        return
    else:
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                           Update Failed:'+ name + 'Does Not Exist')
        print('') # inform the user if they entered a name that does not exists
        print('---------------------------------------------------------------------------------------------------------------------------')
        return

def RemoveItem(sort_content): #remove a nested_list from sort content 
    print("Available Items:", *find_col_int(0)) #show user available items to delete
    name = input('Name: ') 
    Item = List_Item_Exists(name) #check if the item exists
    if Item == True:
        row = find_row(name) #find the index of sort_content that represents the nested_list the item is a part of
        sort_content.pop(row) #delete the nested_list
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                            Remove Successful: Item Deleted')
        print('')#inform user of success
        print('---------------------------------------------------------------------------------------------------------------------------')
        return
    else:
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                            Remove Failed: Item Doesnt Exist!')
        print('')#inform user of failure
        print('---------------------------------------------------------------------------------------------------------------------------')
        return


def SaveAndExit():#save the listsinlists to .txt file in the specified format
    print('---------------------------------------------------------------------------------------------------------------------------')
    print('')
    print('                                            Save Before Exiting? Please Review Current Data')
    print('')#provide user with warning before overwriting data
    print('---------------------------------------------------------------------------------------------------------------------------')
    for i in sort_content:
        print(*i)           #iterates though lists to show users the current data that will be saved
    ExitYN = input('Y/N: ') #confirmation on exit usees both accepts both capital and lowercase letters
    if ExitYN == 'Y' or ExitYN == 'y':
        header.replace(' ', ', ')   #formatting was removed from header as it was read, this replaces the formatting before it is saved
        header.join('\n')           #adds a linebreak to the end of the header so a new line begins once in the .txt document
        with open('updated_A3_s3943492_stock.txt', 'w') as savefile:   #open the file for editing
            sort_content.insert(0, header)   #place the header as a nested_list in sort_content, however it is placed as the first list so it is the first row in the .txt document
            for nested_list in sort_content:     #loop through the values in the nested_lists, and place each nested_list on its own line, and each value at its index
                line = nested_list[0] + ', ' + nested_list[1] + ', ' + nested_list[2] + ', ' + nested_list[3] + ', ' + nested_list[4] + '\n' #put formatting back in its correct places
                savefile.write(line) #save the file and write a new line for every nested_list according to the formatting above
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                                    Changes Saved! GoodBye!')
        print('')#inform user that their changes were saved
        print('---------------------------------------------------------------------------------------------------------------------------')
        quit()#quits gracefully instead of crashing
    else:
        return


def navigation(sort_content):
    #try:
    MenuChoice = input('')
    if MenuChoice == '1':
        Sing_Item_Info(sort_content)   #if user chooses between 1 and 7, the if statement will be successful.
    elif MenuChoice == '2':           #choosing a character or a number smaller than 1 or bigger than 7 will trigger the else and inform the user that they made an invalid input, resetting the loop
        All_Item_Info()              
    elif MenuChoice == '3':
        AddItem(sort_content)
    elif MenuChoice == '4':
        EditItem(sort_content)
    elif MenuChoice == '5':
        RemoveItem(sort_content)
    elif MenuChoice == '6':
        SaveAndExit()        
    elif MenuChoice == '7':
        Exit_No_Save()
    else:
        print('This is not a valid input')

def Exit_No_Save():#exits the program without saving changes made during the session
    print('---------------------------------------------------------------------------------------------------------------------------')
    print('')
    print('                                            Exit Without Saving? WARNING: Changes will be lost!')
    print('')#informs user of the consequences of quitting
    print('---------------------------------------------------------------------------------------------------------------------------')
    ExitYN = input('Y/N: ')#asks user whether they really want to quit
    if ExitYN == 'Y' or ExitYN == 'y':
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('                                                         GoodBye!')
        print('')#quits without crashing
        print('---------------------------------------------------------------------------------------------------------------------------')
        quit()
    else:
        return

def menu(sort_content):
    inMenu = True 
    while inMenu == True: #loop the menu so that anytime a function comes back successful or unsuccessfun, the user always ends up back here
        print('')
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')#tell the users where they are
        print('                                                         Menu')
        print('')
        print('---------------------------------------------------------------------------------------------------------------------------')
        print('')
        print('1 - Show one item information')
        print('2 - Show all stock information')
        print('3 - Add Item')
        print('4 - Update Item')
        print('5 - Remove Item')
        print('6 - Save and Exit')
        print('7 - Exit Without Saving')
        navigation(sort_content)




file = 'A3_s3943492_stock.txt'
stock = open(file, 'r')
#reading file
header = stock.readline()
#saving header so it is not subject to data changes when in the menu
header = header.rstrip('\n')
header = header.replace(',',"")
#Cleaning up header so that it no longer contains formatting from when it was in the .txt file
content = [element.rstrip('\n').split() for element in stock]
content = [[element.rstrip(', ') for element in element] for element in content]
#putting the database into a list of lists so that relationships can be easlily referenced later
#also removing formatting from data so that it can be more easily and accurately modified
sort_content= sorted(content, key=lambda x:x[0])
#sorting the data so it appears in alphabetical order
stockvalue = sum(find_col_int(1))
#adding the estimated_value column to find the total stock value
primarykey = find_col_int(0)
#creating a list of the values that make up the first column for use in indexing




print('---------------------------------------------------------------------------------------------------------------------------')
print('')
print('                                                  GPU_STORAGE_SOFTWARE')
print('')
print('---------------------------------------------------------------------------------------------------------------------------')
print('')
print('---------------------------------------------------------------------------------------------------------------------------')
print('')
print('                                                     Loading Data')
print('')
print('---------------------------------------------------------------------------------------------------------------------------')
print('Loading data from file:', file)
print('Column titles are:', header.strip())
print('Items Loaded:', find_col_int(0))
print('---------------------------------------------------------------------------------------------------------------------------')
print('')
print('                                                 Showing Original Data')
print('')
print('---------------------------------------------------------------------------------------------------------------------------')
print('Showing all item information in alphabetical order')
for i in sort_content:
    print(*i)
print('')
print('Current Stock Value:', stockvalue)
menu(sort_content)