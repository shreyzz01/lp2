from collections import deque
import heapq

class Evaluation:

    def __init__(self):
        self.name = input("Enter name of employee: ")

        self.competencies = {
            "Communication": [0, 0, 0],
            "Productivity": [0, 0, 0],
            "Creativity": [0, 0, 0],
            "Integrity": [0, 0, 0],
            "Punctuality": [0, 0, 0]
        }

        self.performance = {
            "Goal1": [0, 0, 0],
            "Goal2": [0, 0, 0],
            "Goal3": [0, 0, 0],
            "Goal4": [0, 0, 0],
            "Goal5": [0, 0, 0]
        }

    def validate_weights(self, total):
        return total == 100

    def input_data(self):

        print("\nEnter rating between 1-3")

        total_weight = 0
        for key in self.competencies:
            r = int(input(f"Rating for {key}: "))
            w = int(input(f"Weightage ({100 - total_weight} remaining): "))
            total_weight += w
            self.competencies[key][0] = r
            self.competencies[key][1] = w

        if not self.validate_weights(total_weight):
            print("Invalid Competency Weight Total!")
            exit()

        total_weight = 0
        for key in self.performance:
            r = int(input(f"Rating for {key}: "))
            w = int(input(f"Weightage ({100 - total_weight} remaining): "))
            total_weight += w
            self.performance[key][0] = r
            self.performance[key][1] = w

        if not self.validate_weights(total_weight):
            print("Invalid Performance Weight Total!")
            exit()

    def calcScore(self):

        for key in self.competencies:
            r, w, _ = self.competencies[key]
            self.competencies[key][2] = (r * w) / 100

        for key in self.performance:
            r, w, _ = self.performance[key]
            self.performance[key][2] = (r * w) / 100

    def bfs_flow(self):

        graph = {
            "Start": ["Competency", "Performance"],
            "Competency": list(self.competencies.keys()),
            "Performance": list(self.performance.keys())
        }

        q = deque(["Start"])
        visited = []

        while q:
            node = q.popleft()
            visited.append(node)

            if node in graph:
                for n in graph[node]:
                    q.append(n)

        return visited

    def dfs_total(self, data, keys, index=0):

        if index == len(keys):
            return 0

        key = keys[index]
        return data[key][2] + self.dfs_total(data, keys, index + 1)

    def greedy_best_competency(self):
        best = max(self.competencies.items(), key=lambda x: x[1][2])
        return best[0]

    def dijkstra_improvement(self):

        graph = {
            "Low": {"Medium": 2, "High": 5},
            "Medium": {"High": 2},
            "High": {}
        }

        dist = {k: float('inf') for k in graph}
        dist["Low"] = 0
        pq = [(0, "Low")]

        while pq:
            d, node = heapq.heappop(pq)

            for neigh, w in graph[node].items():
                nd = d + w
                if nd < dist[neigh]:
                    dist[neigh] = nd
                    heapq.heappush(pq, (nd, neigh))

        return "Improvement path optimized."

    def printTable(self, data, title):

        print(f"\n{title}")
        print("Name\t\tRating\tWeight\tWeightedScore")

        for k, v in data.items():
            print(f"{k}\t{v[0]}\t{v[1]}\t{round(v[2], 2)}")

    def calculate(self):

        self.input_data()
        self.calcScore()
        self.bfs_flow()

        self.printTable(self.competencies, "Competency Evaluation")
        comp_total = self.dfs_total(self.competencies, list(self.competencies.keys()))

        self.printTable(self.performance, "Performance Evaluation")
        perf_total = self.dfs_total(self.performance, list(self.performance.keys()))

        total = (comp_total + perf_total) / 2

        print("\nTotal Competency Score:", round(comp_total, 2))
        print("Total Performance Score:", round(perf_total, 2))

        best = self.greedy_best_competency()
        print("Strongest Competency:", best)

        print(self.dijkstra_improvement())

        print("\nOverall Rating of", self.name, "(out of 3):", round(total, 2))

        if total >= 2.7:
            print("Employee Exceeds Expectations")
        elif total >= 1.7:
            print("Employee Meets Expectations")
        else:
            print("Employee Needs Improvement")


# Run program
obj = Evaluation()
obj.calculate()

# Enter name of employee: Akshat

# Enter rating between 1-3

# Rating for Communication: 3
# Weightage (100 remaining): 20

# Rating for Productivity: 2
# Weightage (80 remaining): 20

# Rating for Creativity: 3
# Weightage (60 remaining): 20

# Rating for Integrity: 2
# Weightage (40 remaining): 20

# Rating for Punctuality: 3
# Weightage (20 remaining): 20


# Rating for Goal1: 3
# Weightage (100 remaining): 20

# Rating for Goal2: 2
# Weightage (80 remaining): 20

# Rating for Goal3: 3
# Weightage (60 remaining): 20

# Rating for Goal4: 2
# Weightage (40 remaining): 20

# Rating for Goal5: 3
# Weightage (20 remaining): 20

# Competency Evaluation
# Name            Rating  Weight  WeightedScore
# Communication   3       20      0.6
# Productivity    2       20      0.4
# Creativity      3       20      0.6
# Integrity       2       20      0.4
# Punctuality     3       20      0.6

# Performance Evaluation
# Name            Rating  Weight  WeightedScore
# Goal1           3       20      0.6
# Goal2           2       20      0.4
# Goal3           3       20      0.6
# Goal4           2       20      0.4
# Goal5           3       20      0.6

# Total Competency Score: 2.6
# Total Performance Score: 2.6

# Strongest Competency: Communication
# Improvement path optimized.

# Overall Rating of Akshat (out of 3): 2.6
# Employee Meets Expectations