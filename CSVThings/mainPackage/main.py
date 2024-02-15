# main.py

from utilsPackage.utils import *

# Call the function and store what it returns 
if __name__ == "__main__":
    data = read_CSV_file()
    print("# of rows in dataset:", len(data))
    print(data[0])
    print(data[-1])
    
    #crash = data['Collison']
    collisionTypes = {myData[6] for myData in data}
    print(collisionTypes)
    #print(type)
    
#help(csv)
#  in a variable called data