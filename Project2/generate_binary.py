# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Laura Anderson 2/15/2023
# ASSIGNMENT:   Project 2: Stacks & Queues

from Project2.Queue import Queue
from Project2.Stack import Stack

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):

    s = Stack([])  # used to store digits of individual binary numbers
    numbers = Queue([])  # Stores list of binary numbers to return
    num = 0
    bin_num = ""

    if N >= 1:  # If N is less than 1 return the empty Queue()
        numbers.enq("1")  # add 1 (binary #1) to every binary number

        for i in range(N-1):
            num = i + 2 #Start at 2

            while num > 0:   #Calculates binary number in reverse and adds to stack
                s.push(num % 2)
                num //= 2

            while not s.is_empty():  #moves binary number in correct order to string
                bin_num += str(s.pop())

            numbers.enq(bin_num)    #add to queue
            bin_num = ""
            i += 1

    return numbers

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()
    generate_binary_numbers(0).print()



# Don't run main on import
if __name__ == "__main__":
    main()

