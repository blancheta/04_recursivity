def recursive_function(budget, elements, depth=0):

    for element in elements:
        # New
        bud = budget

        elements_left = elements.copy()
        elements_left.remove(element)

        # 1
        # bud -= element

        # 2 - New
        # if bud - element > 0 or depth == 0:
        #     bud -= element
        # else:
        #     print("Reach limit or end")
        #     break

        # This block is just to help us to visualise what is happening
        if depth == 0:
            print("", str(element), elements_left, "<= To explore")
        else:
            if elements_left:
                print(depth * " | - >", str(element), elements_left, "<= To explore", bud)
            else:
                print(depth * " | - >", str(element), elements_left, "<= No more to explore", bud)
        if elements_left:
            # ------New------->*
            recursive_function(bud, elements_left, depth + 1)
        else:
            break

recursive_function(1, [1, 2, 3])

# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
