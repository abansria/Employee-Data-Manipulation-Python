#Amit Bansria
#Employee-Data-Manipulation-Python
#May 19, 2024

def main():
    

    # Answer #1 
    # List of 10 employees 'firstname lastname'
    fullList = ['Amit Bansria', 'Nargis Fakhri', 'Dakota Johnson', 'Priyanka Chopra', 
                'Nora Fatehi', 'Scarlett Johansson', 'Rachel Weisz', 'Rachel McAdams', 
                                    'Kaya Scodelario', 'Brie Larson']

    # splittling this list in half
    # first let us determine the total length of this list (Downey, 2015, p. 91)
    length = len(fullList)

    # now lets divide this length to get 5 (assume the list is of length 10)
    half = length // 2 # note we use // division to get an integer

    # storing the data in two lists, using Slices (Downey, 2015, pp. 91-92)
    newList1 = fullList[:half]
    newList2 = fullList[half:]

    
    # Displaying the results of each of these lists
    print('\n', 'The first half of this list: ', newList1)
    print('\n', 'The second half of this list: ', newList2)

    # Answer #2
    # Adding a new employee "Kriti Brown" to newList2
    # To add to the new list we can use the built-in List method
    # listname.append() (Downey, 2015, p. 92)
    newList2.append('Kriti Brown')

    # Displaying the results of this addition to newList2
    print('\n','The new second list: ',newList2)

    # Answer #3
    # Deleting the second employee name from newList1
    # here we are using the del operator to delete the second name
    # (Downey, 2015, p. 94)
    del newList1[1]

    # Displaying the results of this deletion to newList1
    print('\n','The modified first list: ', newList1)    

    # Answer #4
    # Merging these two lists newList1 and newList2 to form updatedList
    # Here we use the List operator + to combine the two lists
    # (Downey, 2015, p. 91)
    updatedList = newList1 + newList2

    # Displaying the results of this new updatedList
    print('\n', 'The updated new list: ', updatedList)

    # Answer #5
    # The salay list stores the salaries of 10 employees
    salaryList = [40000, 90000, 110000, 120000, 80000, 60000, 70000, 50000, 100000]
    # We will Traverse this list using for loop to give a 4% raise to each member
    # (Downey, 2015, p.91)
    for i in range(len(salaryList)):
        salaryList[i] = salaryList[i] + (salaryList[i]*0.04)

    # Displaying the results of this new updated salary list
    print('\n', 'The new revised salary list is: ', salaryList)

    # Answer #6
    # Sorting the salary List (Downey, 2015, p.92)
    salaryList.sort()

    # Displaying the top three salaries
    print('\n', 'The top three salaries are: ', salaryList[6:], '\n')    

main()