#Brute force process of testing all possible paths and backtracking upon failure is called backtracking.
#Steps:
1) Make the decision and update the current state accordingly.
2) Recursively explore all paths that branch from this updated state by calling the DFS function on this state.
3) Backtrack by undoing the decision we made and reverting the state.


def dfs(state):
    if meets_termination_condition(state):
        process_solution(state)
        return

    for decision in possible_decisions(state):
        make_decision(state, decision)
        dfs(state)
        undo_decision(state, decision)



#Timee