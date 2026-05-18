def job_scheduling(jobs):
    # Sort jobs by profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)
    # Create empty slots
    slots = [None] * max_deadline
    total_profit = 0
    # Schedule jobs
    for job in jobs:
        # Check slots backwards
        for j in range(job[1] - 1, -1, -1):
            # If slot empty
            if slots[j] is None:
                slots[j] = job[0]
                total_profit += job[2]
                break
    return slots, total_profit

# Example Jobs
jobs = [
    ('A', 4, 70),
    ('B', 1, 80),
    ('C', 1, 30),
    ('D', 2, 100),
    ('E', 3, 40),
    ('F', 2, 20)
]
Final_slots, Profit = job_scheduling(jobs)
print("Final Slots:",Final_slots)
print("Total Profit:", Profit)














'''
Job Scheduling Problem (Greedy Method)

The Job Scheduling Problem is used to schedule jobs in such a way that:

Each job has:
Job ID
Deadline
Profit
Each job takes 1 unit of time
Only one job can be done at a time
Goal → maximize total profit

Main Idea (Greedy Concept)

We use a Greedy Approach:

Pick the job with the highest profit first
Try to place it in the latest free slot before its deadline
Continue until all jobs are checked

for j in range(job[1]-1,-1,-1):
find the empty slot from left

| Step | Job | Deadline | Profit | Slot Checked | Action Taken         | Slots After Step         | Total Profit |
| ---- | --- | -------- | ------ | ------------ | -------------------- | ------------------------ | ------------ |
| 1    | D   | 2        | 100    | 2            | Placed in Slot 2     | [Empty, D, Empty, Empty] | 100          |
| 2    | B   | 1        | 80     | 1            | Placed in Slot 1     | [B, D, Empty, Empty]     | 180          |
| 3    | A   | 4        | 70     | 4            | Placed in Slot 4     | [B, D, Empty, A]         | 250          |
| 4    | E   | 3        | 40     | 3            | Placed in Slot 3     | [B, D, E, A]             | 290          |
| 5    | C   | 1        | 30     | 1            | Slot Full → Rejected | [B, D, E, A]             | 290          |
| 6    | F   | 2        | 20     | 2,1          | Both Full → Rejected | [B, D, E, A]             | 290          |

'''

