import tkinter as tk
from tkinter import messagebox
from algorithms.greedy_knapsack import greedy_knapsack
from algorithms.knapsack_01 import knapsack_01
from algorithms.obst import obst
from algorithms.n_queens import n_queens
from algorithms.job_sequencing import job_sequencing

def run_algorithm():
    algo = algorithm_var.get()
    if algo == "Greedy Knapsack":
        weights = list(map(int, weights_entry.get().split()))
        values = list(map(int, values_entry.get().split()))
        capacity = int(capacity_entry.get())
        result = greedy_knapsack(weights, values, capacity)
        messagebox.showinfo("Result", f"Maximum value: {result}")
    elif algo == "0/1 Knapsack":
        weights = list(map(int, weights_entry.get().split()))
        values = list(map(int, values_entry.get().split()))
        capacity = int(capacity_entry.get())
        result = knapsack_01(capacity, weights, values, len(weights))
        messagebox.showinfo("Result", f"Maximum value: {result}")
    elif algo == "Optimal Binary Search Tree":
        keys = list(map(int, keys_entry.get().split()))
        freq = list(map(int, freq_entry.get().split()))
        result = obst(keys, freq)
        messagebox.showinfo("Result", f"Minimum cost of OBST: {result}")
    elif algo == "N Queens":
        n = int(n_entry.get())
        result = n_queens(n)
        messagebox.showinfo("Result", f"Total solutions: {len(result)}")
    elif algo == "Job Sequencing":
        jobs = []
        job_entries = job_entry.get("1.0", tk.END).strip().splitlines()
        for job in job_entries:
            id, deadline, profit = job.split()
            jobs.append((id, int(deadline), int(profit)))
        result = job_sequencing(jobs)
        messagebox.showinfo("Result", f"Job order for max profit: {result}")

# Create the main window
root = tk.Tk()
root.title("Algorithm Selector")

# Dropdown for algorithm selection
algorithm_var = tk.StringVar(value="Greedy Knapsack")
algorithms = ["Greedy Knapsack", "0/1 Knapsack", "Optimal Binary Search Tree", "N Queens", "Job Sequencing"]
algorithm_menu = tk.OptionMenu(root, algorithm_var, *algorithms)
algorithm_menu.pack()

# Input fields for weights, values, capacity, etc.
weights_entry = tk.Entry(root)
weights_entry.pack()
weights_entry.insert(0, "Enter weights (space-separated)")

values_entry = tk.Entry(root)
values_entry.pack()
values_entry.insert(0, "Enter values (space-separated)")

capacity_entry = tk.Entry(root)
capacity_entry.pack()
capacity_entry.insert(0, "Enter knapsack capacity")

keys_entry = tk.Entry(root)
keys_entry.pack()
keys_entry.insert(0, "Enter keys (space-separated)")

freq_entry = tk.Entry(root)
freq_entry.pack()
freq_entry.insert(0, "Enter frequencies (space-separated)")

n_entry = tk.Entry(root)
n_entry.pack()
n_entry.insert(0, "Enter number of queens (N)")

job_entry = tk.Text(root, height=5, width=30)
job_entry.pack()
job_entry.insert(tk.END, "Enter jobs in format: id deadline profit\n")

# Button to run the selected algorithm
run_button = tk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.pack()

# Start the GUI event loop
root.mainloop()
