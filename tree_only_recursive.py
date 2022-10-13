def recursive_function(elements, depth=0):

    elements_left = elements.copy()
    element = elements_left.pop()

    # This block is just to help us to visualise what is happening
    if depth == 0:
        print("", str(element), elements_left, "<= To explore")
    else:
        if elements_left:
            print(depth * " | - >", str(element), elements_left, "<= To explore")
        else:
            print(depth * " | - >", str(element), elements_left, "<= No more to explore")

    if elements_left:
        recursive_function(elements_left, depth + 1)


recursive_function([1, 2, 3])

# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
