max_budget = 50

actions = [
    ("Action-1", 20, 0.5),
    ("Action-2", 30, 0.1),
    ("Action-3", 50, 0.15)
]

# naif
def greedy_solver(max_budget, actions):

    actions_bought = []
    budget_spent = 0

    sorted_actions = list(sorted(actions, key=lambda x: x[1], reverse=True))

    for action in sorted_actions:
        if budget_spent + action[1] > max_budget:
            return budget_spent, actions_bought
        budget_spent += action[1]
        actions_bought.append(action)


# bruteforce
def bruteforce_solver(max_budget, actions):

    actions_bought = []

    print("initial list:", actions)
    for i, action in enumerate(actions):
        print(action[1])
        if max_budget - action[1] < 0:
            return 50-max_budget, actions
        else:
            rest_actions = actions.pop(i)
            bruteforce_solver(max_budget, rest_actions)







# optimised
def dynamic_programming_solver(actions):
    pass


# print("Best combination of actions [Greedy]:")

# assert greedy_solver(max_budget, actions) == (50, [("Action-3", 50, 0.15)])

print("Best combination of actions [Bruteforce]:")

bruteforce_solver(max_budget, actions)

# print("Best combination of actions [Dynamic Programming]:")