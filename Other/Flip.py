#Practice Problem 1
#Laura Anderson
#Flip - take numbers from stack and reverse them
import Queue
import Stack


#Practice Problem #3
# function takes Postfix arithmatic problem and converts to infix problem
def in2pf(queue):
    s = Stack.Stack()
    operators = "+-/*"
    num1 = 0
    num2 = 0
    infixstr = ""
    infixQ = Queue.Queue()
    infixQ.enq(queue.deq())

    while queue.is_empty() != True:

        if str(queue.front()) in operators: #if operator add to queue and add # on top of stack to queue after operator
            infixQ.enq(queue.deq())
            infixQ.enq(s.pop())
        else:   #if not an operator add number to stack
            s.push(queue.deq())
    # print("Infix queue = ", infixQ)

    while infixQ.is_empty() != True: #Convert queue to string for better display formatting
        infixstr = infixstr + str(infixQ.deq())
    return(infixstr)


#Practice Problem #1
#Take a list and return list in reverse order
 flip(list):
    s = Stack()
    length = len(list)
    i = 0

    while i < length:
        s = list.pop()
        i += 1
        print(s)


# print(flip(Stack([1, 2, 3, 4])))

#Function that takes a queue of sorted numbers and returns the # of unique numbers in queue
#Practice Problem #2
def count_unique(queue):
    totUniq = 1
    last_num = queue.deq()
    cur_num = 0

    while queue.is_empty() != True: #Loop through queue until empty
        cur_num = queue.deq()
        if cur_num != last_num: #If the current num is different than previous num, increment total - we have a transition to new num
            totUniq += 1
            last_num = cur_num
        else:
            last_num = cur_num

    return(totUniq)


    print("total unique numbers = ", totUniq)

# queuelist = Queue()
numqueue = Queue.Queue()
test_queue = Queue.Queue()

for i in range(1,5):
    test_queue.enq(i)
    test_queue.enq(i)
    test_queue.enq(i)

in2pf(test_queue)

new_queue = Queue.Queue()

new_queue.enq(5)
new_queue.enq(4)
new_queue.enq("*")
new_queue.enq(7)
new_queue.enq("+")

print("PostFix Equation is", new_queue)
print("Infix Equation is ", in2pf(new_queue))




print(test_queue)
print("test_queue = ", end="")
print(count_unique(test_queue))









