# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Laura Anderson
# ASSIGNMENT:   Project 2: Stacks & Queues

from Project2.Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(braces):
    open_braces = Stack([])
    strlen = len(braces)
    str_open = "([{"
    str_closed = ")}]"

    i = 0

    while i < strlen:
        if braces[i] in str_open: #if character is an open brace
            open_braces.push(braces[i]) #put the open brace on the stack
            i += 1
        elif braces[i] in str_closed: #if character is a closed brace
            brace = str(open_braces.pop())
            match braces[i]: #match the brace and check to see if the matching open brace is at the top of the stack
                case ")":
                    if brace == "(":
                        i += 1
                    else:
                        return False
                case "]":
                    if brace == "[":
                        i += 1
                    else:
                        return False
                case "}":
                    if brace == "{":
                        i += 1
                    else:              #if there is no matching open brace on the stack return False
                        return False
        else:
            i += 1

    if open_braces.is_empty() == True: #check to make sure the stack is empty
        return True
    else:  #return false if there are any unmatched braces left on the stack
        return False


def main():
    message = ""
    print("matcher: [()] ", matcher("[()]"))
    print("matcher: {[()}} ",matcher("{[()}}"))
    print("matcher: ()",matcher("()"))
    print("matcher: (hello)",matcher("(hello)"))
    print(f"matcher: {matcher("([)]")}")




# Don't run main on import
if __name__ == "__main__":
    main()

