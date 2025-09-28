# Graph

## 207. Course schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array prerequisites where `prerequisites[i] = [a_i, b_i]` indicates that you must take course bi first if you want to take course `a_i`.

For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

**Example:**

- Input: `numCourses = 2`, `prerequisites = [[1,0]]`
- Output: `True`



### Approach 1: Cherry picking on top-down directed graph

If there are circular dependencies, it is impossible to deconstruct the graph by removing leaves iteratively, since all remaining nodes will have remaining requirements.

First we build the graph. Then as long as there are nodes in the graph:

- iterate on the graph to create the set of leaves.
- if there are no leaves, we have a circular dependency and return `False`.
- remove all leaves from the graph.
- remove all leaves from the adjacent set of all nodes. This way, all remaining nodes which dependencies are satisfied become new leaves.



![207_1](README.assets/207_1_.png)



```python
class Solution:
    def build_graph(self, prerequisites: list[list[int]]) -> dict[int, set[int]]:
        graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            graph[course].add(prerequisite)
            graph[prerequisite]

        return graph

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = self.build_graph(prerequisites)

        while graph:
            leaves = {course for course in graph if not graph[course]}
            if not leaves:
                return False
            for leaf in leaves:
                del graph[leaf]
            for course in graph:
                graph[course] -= leaves

        return True
```

Time: O(edges + vertices^2)

Space: O(edges)



### Approach 2: Using DFS on top-down directed graph

Once the graph is built, pick any node while there are still nodes in the graph and use DFS to reach the leaves.

When a leaf is found, we can remove it from the graph so that we don't search it and its dependencies more than once.

While using DFS, we keep track of the nodes in the path. If a new node we explore is already in the path, we have a circular dependency. At this point, we end picking new nodes and return the result.



![207_2](README.assets/207_2_.png)



```python
class Solution:
    def build_graph(self, prerequisites: list[list[int]]) -> dict[int, list[int]]:
        graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            graph[course].add(prerequisite)
            graph[prerequisite]

        return graph

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = self.build_graph(prerequisites)

        path = set()
        circular_dep = False

        def find_deps(course: int):
            nonlocal circular_dep

            if course not in graph:
                return

            if course in path:
                circular_dep = True
                return

            path.add(course)
            for dep in graph[course]:
                find_deps(dep)
            path.remove(course)

            del graph[course]

        while graph and not circular_dep:
            find_deps(next(iter(graph)))

        return not circular_dep
```
Time: O(edges)

Space: O(edges)



### Approach 4: DFS with array on top-down directed graph

Similar to the previous approach, but since each vertex is represented by a unique number between `[0, numCourses]`, we can represent the vertex state using an array.

This is an alternative to delete nodes from the graph to mark them as visited and using a set of the nodes in the current path.

While using DFS:

- if the node is marked as visited, do nothing &rarr; return True.
- if we are already visiting the node, we have a circular dependency &rarr; return False.
- mark the node temporarily as visiting and explore the sub-nodes. if a circular dependency is found in one of the sub-nodes, also return False.
- finally, mark the node as visited so we don't consider it again.



```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        prerequisites = prerequisites
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node: int):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            states[node] = VISITING

            for prereq in graph[node]:
                if not dfs(prereq):
                    return False

            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
```

Time: O(edges)

Space: O(edges)



### Approach 3: BFS on bottom-up directed graph

#### Approach

In contrast to the previous approaches, we build the directed graph bottom-up, which means that each prerequisite node points towards the courses needing it.

By doing so, we loose the explicit information of whether or not a node requires other nodes. We can keep track of that information using the *in-degree* value, which means how many nodes point towards it.

Nodes which don't have any requirements have no nodes pointing to them. They are source nodes.

#### Process

Once the graph is built, we iterate on the graph once to find the first source nodes.

Then, for each source node, we can iterate efficiently on impacted nodes and check whether they became a source node.

- To do that, we can decrement their in-degree value and check if zero.
- If we have a new source node, we can add it to the queue to process later.

If there is a circular dependency, we will reach a state where the queue is empty while we still didn't process all nodes.

If there is no circular dependency, we can pop all nodes from the list before finding out that the queue is empty.



![207_4](README.assets/207_4_.png)



```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for n_crs, prereq in prerequisites:
            indegree[n_crs] += 1
            adj_list[prereq].append(n_crs)

        queue = deque()
        for n_crs in range(numCourses):
            if indegree[n_crs] == 0:
                queue.append(n_crs)

        while queue:
            crs = queue.popleft()
            numCourses -= 1
            if numCourses == 0:
                return True

            for n_crs in adj_list[crs]:
                indegree[n_crs] -= 1
                if indegree[n_crs] == 0:
                    queue.append(n_crs)

        return False
```

Time: O(edges)

Space: O(edges)
