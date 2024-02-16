# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Laura Anderson
# ASSIGNMENT:   Project 2: Stacks & Queues

from Project2.Queue import Queue
# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(queue):
    len = 0
    count = 1

    if queue.is_empty():
        return 0

    value = queue.deq() #store the first value in queue

    while not queue.is_empty():  #Loop through Queue
        if queue.front() != value:   #if the next value in queue doesn't match
            value = queue.deq()
            if count > len:         #check if the last sequence was longer than the previous longest
                len = count
            count = 1
        else:                   #If value in queue matches stored value increment counter
            count += 1
            queue.deq()

    if count <= len:        #check to see if the last sequence was longest
        pass
    else:
        len = count

    return len


def main():
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))
    print("out 0:", count_longest(Queue([])))
    print("out 1:", count_longest(Queue([l for l in "m"])))


# Don't run main on import
if __name__ == "__main__":
    main()
