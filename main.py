import time
import os
from algorithms.greedy_knapsack import greedy_knapsack
from algorithms.knapsack_01 import knapsack_01
from algorithms.obst import obst
from algorithms.n_queens import n_queens
from algorithms.job_sequencing import job_sequencing

def ai_select_algorithm(user_input):
    input_lower = user_input.lower()

    greedy_keywords = [
        "fraction", "continuous", "greedy", "maximize value", "partial",
        "fractional knapsack", "item split", "ratio", "value per weight", "greedy method",
        "light item", "efficient", "weight ratio", "approximate", "select greedy",
        "profit ratio", "fill bag", "greedy choice", "step by step", "immediate benefit",
        "local optimum", "highest value", "fractional item", "knapsack greedy", "greedy bag",
        "fastest choice", "non-optimal", "value density", "top ratio", "item cut",
        "partial fill", "cost-effective", "greedy solve", "highest return", "quick pick",
        "priority queue", "greedy greedy", "ratio based", "top item", "top profit",
        "not exact", "not full", "split items", "bag fill", "high efficiency",
        "item greedy", "ratio decision", "greedy ratio", "fast solve", "quick solve"
    ]

    knapsack_01_keywords = [
        "0/1", "binary", "discrete", "select items", "item yes no",
        "bag limit", "optimal value", "item pick", "knapsack 01", "dynamic knapsack",
        "non-fraction", "exact items", "full item", "choose or skip", "bag capacity",
        "dynamic table", "DP knapsack", "backtrack knapsack", "non-continuous", "fit items",
        "item inclusion", "include exclude", "DP solve", "exact fit", "bag max",
        "memory based", "recursive", "yes or no", "item chosen", "0 1 choice",
        "value compare", "limited choice", "item decision", "item exact", "selected items",
        "no split", "best combination", "capacity limit", "fixed set", "value max",
        "limited space", "no share", "dynamic program", "state table", "bounded items",
        "final value", "subset choice", "subset max", "choose fixed", "boolean choice"
    ]

    obst_keywords = [
        "tree", "search", "bst", "optimal tree", "min cost search",
        "obst", "binary tree", "key search", "frequency based", "search tree",
        "key probability", "optimal search", "binary search", "weighted tree", "lookup cost",
        "best bst", "fastest search", "tree minimize", "tree cost", "key access",
        "frequency key", "tree DP", "tree optimization", "fast tree", "tree order",
        "balanced search", "BST optimize", "node frequency", "optimal path", "obst problem",
        "sorted key", "tree algorithm", "node weight", "node cost", "least cost",
        "expected cost", "tree structure", "tree layout", "weighted BST", "tree frequency",
        "lookup weight", "query tree", "predictable search", "average cost", "low cost tree",
        "build bst", "root choice", "tree build", "tree planning", "node choose"
    ]

    n_queens_keywords = [
        "queen", "chess", "board", "n queens", "non attacking",
        "backtracking", "queen placement", "no attack", "diagonal attack", "place queens",
        "safe queen", "queen row", "recursive board", "solve n queens", "board fill",
        "row check", "column check", "diagonal check", "valid queen", "n x n",
        "conflict avoid", "row conflict", "column conflict", "diagonal conflict", "chess queen",
        "checkmate", "non threatening", "no overlap", "safety position", "chess puzzle",
        "queen config", "solution board", "queen backtrack", "recursive solve", "nqueens",
        "queens chessboard", "queen safe", "constraint satisfaction", "attack free", "recursive place",
        "no overlap queens", "arrange queens", "queen block", "board safe", "n queens problem",
        "placement logic", "board traversal", "position safety", "board backtrack", "search board"
    ]

    job_seq_keywords = [
        "job", "deadline", "schedule", "profit", "max profit",
        "task order", "time slot", "job selection", "job sequencing", "deadline profit",
        "task deadline", "max job", "job order", "priority jobs", "profit deadline",
        "max reward", "slot fill", "task scheduler", "task maximize", "job queue",
        "profit first", "early job", "timeline job", "ordered task", "greedy job",
        "earliest deadline", "best profit", "priority profit", "non overlapping", "deadline slot",
        "urgent task", "maximize task", "task planner", "schedule profit", "job placement",
        "greedy deadline", "profit sorted", "task sort", "deadline check", "job calendar",
        "profit calculation", "job benefit", "job timeline", "task fit", "best job",
        "deadline match", "job arrangement", "ordered schedule", "deadline work", "high profit"
    ]

    if any(k in input_lower for k in greedy_keywords):
        return "greedy_knapsack"
    elif any(k in input_lower for k in knapsack_01_keywords):
        return "knapsack_01"
    elif any(k in input_lower for k in obst_keywords):
        return "obst"
    elif any(k in input_lower for k in n_queens_keywords):
        return "n_queens"
    elif any(k in input_lower for k in job_seq_keywords):
        return "job_sequencing"
    else:
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\nDescribe your problem or type 'Exit', 'done', or 'thank you':")
    user_desc = input(">>> ").strip().lower()

    if user_desc in ["exit", "done", "thank you"]:
        print("Thank you!")
        break

    algo = ai_select_algorithm(user_desc)

    if algo == "greedy_knapsack":
        print("\n--- Greedy Knapsack ---")
        weights = list(map(int, input("Enter weights (space-separated): ").split()))
        values = list(map(int, input("Enter values (space-separated): ").split()))
        capacity = int(input("Enter knapsack capacity: "))
        result = greedy_knapsack(weights, values, capacity)
        print("Maximum value:", result)

    elif algo == "knapsack_01":
        print("\n--- 0/1 Knapsack ---")
        weights = list(map(int, input("Enter weights (space-separated): ").split()))
        values = list(map(int, input("Enter values (space-separated): ").split()))
        capacity = int(input("Enter knapsack capacity: "))
        result = knapsack_01(capacity, weights, values, len(weights))
        print("Maximum value:", result)

    elif algo == "obst":
        print("\n--- Optimal Binary Search Tree ---")
        keys = list(map(int, input("Enter keys (space-separated): ").split()))
        freq = list(map(int, input("Enter frequencies (space-separated): ").split()))
        result = obst(keys, freq)
        print("Minimum cost of OBST:", result)

    elif algo == "n_queens":
        print("\n--- N Queens Problem ---")
        n = int(input("Enter number of queens (N): "))
        result = n_queens(n)
        print("Total solutions:", len(result))
        if result:
            for solution in result:
                print(solution)
        else:
            print("No solution possible.")

    elif algo == "job_sequencing":
        print("\n--- Job Sequencing with Deadlines ---")
        print("Enter jobs in format: id deadline profit")
        num = int(input("Number of jobs: "))
        jobs = []
        for _ in range(num):
            job = input("Enter job: ").split()
            jobs.append((job[0], int(job[1]), int(job[2])))
        result = job_sequencing(jobs)
        print("Job order for max profit:", result)

    else:
        print("Sorry, could not understand the problem description.")

    print("\nAI Reloading.....")
    time.sleep(5)
    clear_screen()