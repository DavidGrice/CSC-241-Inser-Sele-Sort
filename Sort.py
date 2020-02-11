#import libraries: time for timings, random for creating random integers
import time                 
import random               

# insertion_sort(arr)
# This function takes an array passed as the parameter (arr)
# and then sorts it.
def insertion_sort(arr):            
    for k in range(1, len(arr)):     
        current = arr[k]                
        j = k                       
        while j > 0 and arr[j-1] > current:         
            arr[j] = arr[j-1]           
            j = j - 1
            arr[j] = current   

# selection_sort(arr)
# This function takes an array passed as the parameter (arr)
# and then sorts it.
def selection_sort(arr):       
    for k in range(len(arr)):       
        current_val = k           
        next_val = k + 1          
        while (next_val < len(arr)):  
            if (arr[next_val] < arr[current_val]):  
                current_val = next_val              
            next_val  = next_val + 1                
            temp = arr[k]                                                           
            arr[k] = arr[current_val]                 
            arr[current_val] = temp                   

# Main body
if __name__ == '__main__':                           

    # Define the sizes which will be used for this project
    sizes = [1000, 2500, 5000, 7500, 10000]

    # Give the names of the array and functions types to be utilized.
    arrayTypes = ["Increasing", "Decreasing", "Random"]
    functionTypes = ["Selection", "Insertion"]

    # Create loops for iterating through the size, array, and functions
    for size in sizes:
        for arrayType in arrayTypes:

    # For every array type, initialize the proper length based upon the size
    # then take the same cells and copy them so both sorting methods have same
    # data to sort, giving the best scientific-observations as possible
    # Each function type, iterates through each of the sizes five times
    # printing out the timings per iteration for being utilized in the graphs
            if arrayType == "Increasing":
                arraySelectionIncrease = [0] * size
                arrayInsertionIncrease = [0] * size

                for cells in range (0,size):
                    arraySelectionIncrease[cells] = cells + 1
                arrayInsertionIncrease = arraySelectionIncrease

                for funcType in functionTypes:
                    if funcType == "Insertion":
                        for count in range(0,5):
                            start = time.clock()
                            insertion_sort(arrayInsertionIncrease)
                            end = time.clock()
                            print(str(size) + " Increasing Insertion: " + "{:.20f}".format(end-start))

                    elif funcType == "Selection":
                        for count in range(0,5):
                            start = time.clock()
                            selection_sort(arraySelectionIncrease)
                            end = time.clock()
                            print(str(size) + " Increasing Selection: " + "{:.20f}".format(end-start))

            elif arrayType == "Random":
                arraySelectionRandom = [0] * size
                arrayInsertionRandom = [0] * size

                for cells in range (0,size):
                    arraySelectionRandom[cells] = random.randint(0,100)
                arrayInsertionRandom = arraySelectionRandom

                for funcType in functionTypes:
                    if funcType == "Insertion":
                        for count in range(0,5):
                            start = time.clock()
                            insertion_sort(arrayInsertionRandom)
                            end = time.clock()
                            print(str(size) + " Random Insertion: " + "{:.20f}".format(end-start))

                    elif funcType == "Selection":
                        for count in range(0,5):
                            start = time.clock()
                            selection_sort(arraySelectionRandom)
                            end = time.clock()
                            print(str(size) + " Random Selection: " + "{:.20f}".format(end-start))

            elif arrayType == "Decreasing":
                arraySelectionDecreasing = [0] * size
                arrayInsertionDecreasing = [0] * size

                for cells in range(0,size):
                    arraySelectionDecreasing[cells] = size - cells
                arrayInsertionDecreasing = arraySelectionDecreasing

                for funcType in functionTypes:
                    if funcType == "Insertion":
                        for count in range(0,5):
                            start = time.clock()
                            insertion_sort(arrayInsertionDecreasing)
                            end = time.clock()
                            print(str(size) + " Decreasing Insertion: " + "{:.20f}".format(end-start))

                    elif funcType == "Selection":
                        for count in range(0,5):
                            start = time.clock()
                            selection_sort(arraySelectionDecreasing)
                            end = time.clock()
                            print(str(size) + " Decreasing Selection: " + "{:.20f}".format(end-start))