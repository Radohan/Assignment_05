#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# RadoslawHankiewicz, 2021-Nov-14, Updated file
#------------------------------------------#

# Declare variabls

strChoice = '' # user input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input

print('The Magic CD Inventory\n')

while True:
    
    # 1. Display menu allowing the user to choose:
    
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        
        # 5. Exit the program if the user chooses so
       
        break
    
    if strChoice == 'l':
        
        # TODO Add the functionality of loading existing data
        
        objFile = open(strFileName, "r")
        for row in objFile:
            lstRow = row.strip().split(",")
            discRow = {"ID": int(lstRow[0]), "Title": lstRow[1], "Artist": lstRow[2]}
            lstTbl.append(discRow)
            print("ID, CD Title, Artist")
            print(discRow["ID"], discRow["Title"], discRow["Artist"], sep = ', ')
        objFile.close()
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        
        # 2. Add data to the table (2d-list) each time the user wants to add data
        
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {'ID': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(lstRow)
        for row in lstTbl:
                print(*row.values(), sep = ', ')
        
    elif strChoice == 'i':
        
        # 3. Display the current data to the user each time the user wants to display the data
        
        print("ID, CD Title, Artist")
        
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            
    elif strChoice == 'd':
        
        # TODO Add functionality of deleting an entry
        
        selection = int(input("Select ID of the string you would like to delete: "))
        
        for row in lstTbl:
            if row['ID'] == selection:
                lstTbl.remove(row)
        for row in lstTbl:
                print(*row.values(), sep = ', ')        
        
    elif strChoice == 's':
        
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        
        strRow = ''
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            for values in row.values():
                strRow += str(values) + ','
            strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')
