from ortools.graph import pywrapgraph
import time
import random
from copy import copy,deepcopy

def main():
	print("What kind of assignment problem are you trying to solve?\nEnter:")
	problem = int(input("1: Balanced Minimization\n2: Unbalanced Minimization\n3: Balanced Maximization\n4: Unbalanced Maximization"))
	if problem==1:
		cost = balanced_minimization()
		rows = len(cost)
		cols = len(cost[0])
	elif problem==2:
		cost = unbalanced_minimization()
		rows = len(cost)
		cols = len(cost[0])
	elif problem==3:
		cost,maxim_matrix = balanced_maximization()
		rows = len(cost)
		cols = len(cost[0])
	elif problem==4:
		cost,maxim_matrix = unbalanced_maximization()
		rows = len(cost)
		cols = len(cost[0])
	else:
		print("Invalid input")
		exit(0)

	#linear assignment solver, a specialized solver for the assignment problem
	#following code creates the solver
	assignment = pywrapgraph.LinearSumAssignment()
	#The following code adds the costs to the solver by looping over workers and 		#tasks.
	for worker in range(rows):
		for task in range(cols):
			#if cost[worker][task]:
			#creating the bipartite graph that will be used to solve the problem
			assignment.AddArcWithCost(worker, task, cost[worker][task])
	#The following code invokes the solver and displays the solution.
	solve_status = assignment.Solve()
	#checks if an optimal solution exists and displays the result accordingly
	if solve_status == assignment.OPTIMAL:
		print('Total cost = ', assignment.OptimalCost())
		print()
		maxim_sale=0
		if problem ==1 or problem==2:
			for i in range(0, assignment.NumNodes()):
				print('Worker %d assigned to task %d.  Cost = %d.  ' % (
					i+1,
					assignment.RightMate(i)+1,
					assignment.AssignmentCost(i)))
				
		
		if problem ==3 or problem==4:
			for i in range(0, assignment.NumNodes()):
				print('Worker %d assigned to task %d.  Cost = %d.  Sale is = %d' % (
					i+1,
					assignment.RightMate(i)+1,
					assignment.AssignmentCost(i),
					maxim_matrix[i][assignment.RightMate(i)]))
				
				maxim_sale += maxim_matrix[i][assignment.RightMate(i)]
		
			print("\n\nMaximum Sale is: %d" % (maxim_sale))
	
	
	#if the solution is infeasible
	elif solve_status == assignment.INFEASIBLE:
		print('No assignment is possible.')
	#if the solution has very large input costs
	elif solve_status == assignment.POSSIBLE_OVERFLOW:
		print('Some input costs are too large and may cause an integer overflow.')
		
#creating data for balanced minimization problem
def balanced_minimization():
	#input in matrix layout format
	"""
	a b c
	d e f
	g h i
	"""
	n = int(input("Enter number of rows: ")) 
	print()
	cost = []
	for i in range(n):
		cost.append([int(j) for j in input().split()])
	return cost

#creating data for unbalanced minimization problem
def unbalanced_minimization():
	rows = int(input("Enter number of rows: "))
	cols = int(input("Enter number of columns: "))
	if rows > cols:
		cost = [[random.random() for row in range(rows)] for row in range(rows)]
		for i in range(rows):
			for j in range(cols):
				cost[i][j] = int(input())
		while rows > cols:
			for i in range(rows):
				cost[i][cols]=0
			cols+=1
			
	if cols > rows:
		cost = [[random.random() for col in range(cols)] for col in range(cols)]
		for i in range(cols):
			for j in range(cols):
				if i<=rows:
					cost[i][j] = int(input())
		while cols > rows:
			for i in range(cols):
				cost[rows][i] = 0
			rows+=1
	
	return cost

#creating data for balanced maximization problem
def balanced_maximization():
	
	#input in matrix layout format
	"""
	a b c
	d e f
	g h i
	"""
	n = int(input("Enter number of rows: ")) 
	print()
	maxim_matrix = []
	for i in range(n):
		maxim_matrix.append([int(j) for j in input().split()])
		
	#converting max matrix to min matrix
	cost = deepcopy(maxim_matrix)
	maximum = max(map(max, maxim_matrix))
	for i in range(n):
		for j in range(n):
			cost[i][j]=maximum-cost[i][j]
	return cost,maxim_matrix

#creating data for unbalanced maximization problem
def unbalanced_maximization():
	rows = int(input("Enter number of rows: "))
	cols = int(input("Enter number of columns: "))
	if rows > cols:
		maxim_matrix = [[random.random() for row in range(rows)] for row in range(rows)]
		for i in range(rows):
			for j in range(cols):
				maxim_matrix[i][j] = int(input())
		while rows > cols:
			for i in range(rows):
				maxim_matrix[i][cols]=0
			cols+=1
			
	if cols > rows:
		maxim_matrix = [[random.random() for col in range(cols)] for col in range(cols)]
		for i in range(cols):
			for j in range(cols):
				if i<=rows:
					maxim_matrix[i][j] = int(input())
		while cols > rows:
			for i in range(cols):
				maxim_matrix[rows][i] = 0
			rows+=1
	
	#converting the max matrix to min matrix
	cost = deepcopy(maxim_matrix)
	maximum = max(map(max, maxim_matrix))
	for i in range(rows):
		for j in range(cols):
			cost[i][j]=maximum-cost[i][j]
	return cost,maxim_matrix		
	
#calling the main function	
if __name__ == "__main__":
	start_time = time.clock()
	main()
	print()
	print("Time =", time.clock() - start_time, "seconds")
  
