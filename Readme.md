###The Assignment Problem
- Classic Mathematic problem

The assignment problem is a fundamental combinatorial optimization problem. It consists of finding, in a weighted bipartite graph, a matching of a given size, in which the sum of weights of the edges is a minimum.


In its most general form, the problem is as follows:

The problem instance has a number of agents and a number of tasks. Any agent can be assigned to perform any task, incurring some cost that may vary depending on the agent-task assignment. It is required to perform as many tasks as possible by assigning at most one agent to each task and at most one task to each agent, in such a way that the total cost of the assignment is minimized.

####Example
Suppose that a taxi firm has three taxis (the agents) available, and three customers (the tasks) wishing to be picked up as soon as possible. The firm prides itself on speedy pickups, so for each taxi the "cost" of picking up a particular customer will depend on the time taken for the taxi to reach the pickup point. This is a balanced assignment problem. Its solution is whichever combination of taxis and customers results in the least total cost.

Now, suppose that there are four taxis available, but still only three customers. This is an unbalanced assignment problem. One way to solve it is to invent a fourth dummy task, perhaps called "sitting still doing nothing", with a cost of 0 for the taxi assigned to it. This reduces the problem to a balanced assignment problem, which can then be solved in the usual way and still give the best solution to the problem.

Similar adjustments can be done in order to allow more tasks than agents, tasks to which multiple agents must be assigned (for instance, a group of more customers than will fit in one taxi), or maximizing profit rather than minimizing cost.
