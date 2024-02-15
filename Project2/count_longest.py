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
    # FIXME
    count = 1
    value = queue.deq()

    print("queue is empty ", queue.is_empty())
    print("queue contains ", queue)

    if queue.is_empty():
        return 0
    if queue.size() == 1:
        return 1

    while not queue.is_empty():
        if queue.front() != value:
            value = queue.deq()
            if count > len:
                len = count
            count = 1
        else:
            count += 1
            queue.deq()
    if count <= len:
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
