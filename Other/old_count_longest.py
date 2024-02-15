point1 = 0
    point2 = 1
    value = queue.deq()
    curr_len = 0

    while not queue.is_empty():
        if queue.front() != value:
            curr_len = point2 - point1
            if curr_len > len:
                len = curr_len
            point1 = point2
            point2 += 1
            value = queue.deq()
        else:
            point2 += 1
            queue.deq()

    #checks to see how long the last substring was and if it was longer than previous
    curr_len = point2 - point1
    if curr_len <= len:
        pass
    else:
        len = curr_len