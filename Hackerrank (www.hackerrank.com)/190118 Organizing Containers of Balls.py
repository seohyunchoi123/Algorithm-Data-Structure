# Question Link : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

def organizingContainers(container):
    n_nums = [0] * n
    n_balls_in_containers = [0] * n

    for i in range(n):
        n_balls_in_containers[i] = sum(container[i])
        for j in range(n):
            n_nums[j] += container[i][j]

    for i in range(n):
        if sorted(n_nums)[i] != sorted(n_balls_in_containers)[i]: # this distributions shouuld be the same
            print(n_nums, n_balls_in_containers)
            return "Impossible"

    n_min_ball = min(n_nums) # the number of balls which has the least number kind.
    idx_n_min_ball = n_nums.index(n_min_ball)
    idx_min_container = n_balls_in_containers.index(n_min_ball) #the index of container which has the least balls.

    return "Possible"

# Method To Solve: Sorting
# Time Complexity : O(n^2)
# Space Complexity : O(n^2)

# Restraint : 1 <= n <= 100


n = 3
m = [[0,2,1],
     [1,1,1],
     [2,0,0]]

print(organizingContainers(m))