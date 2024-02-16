# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Laura Anderon
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    s = Stack()
    length = q_orig.size()

    # Copy data from queue into new stack
    while q_orig.is_empty() != True:
        s.push(q_orig.deq())

    # Copy data from stack into new queue
    while s.is_empty() != True:
        q_new.enq(s.pop())

    return q_new

def main():
    q = Queue(list(range(1, 5)))
    print("q")
    q.print()

    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
