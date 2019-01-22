# Question Link : https://www.hackerrank.com/challenges/queens-attack-2/problem

def queensAttack(n, k, r_q, c_q, obstacles):
    possible = 2 * (n - 1) # horizontally, vertically
    possible += (n - max(r_q, c_q)) + (min(r_q, c_q) - 1) # in direction of y = x
    tmp = r_q + c_q - 1 # in direction of y = -x
    if tmp > n:
        tmp = 2 * n - tmp
    possible += tmp - 1
    obs_cand = [0]*8 # considering only the closest obstacle to queen for each way of 8 ways.
    for obstacle in obstacles:
        r, c = obstacle
        if r == r_q: # in case of the same row
            if c > c_q:
                obs_cand[0] =  max(obs_cand[0], (n - c + 1))
            else:
                obs_cand[1] = max(obs_cand[1], c)
        elif c == c_q: # in case of the same column
            if r > r_q:
                obs_cand[2] = max(obs_cand[2], (n - r + 1))
            else:
                obs_cand[3] = max(obs_cand[3], r)
        elif (r - r_q) == (c - c_q): # in case that they are on y = x line together
            if c > c_q:
                obs_cand[4] = max(obs_cand[4], (n - max(r, c) + 1))
            else:
                obs_cand[5] = max(obs_cand[5], min(r, c))
        elif (r - r_q) == -(c - c_q): # in case that they are on y = -x line together
            if r + c <= n:
                if c > c_q:
                    obs_cand[6] = max(obs_cand[6],r)
                else:
                    obs_cand[7] = max(obs_cand[7], c)
            else:
                if c > c_q:
                    obs_cand[6] = max(obs_cand[6], (n - c + 1))
                else:
                    obs_cand[7] = max(obs_cand[7], (n - r + 1))
    return possible - sum(obs_cand)

print(queensAttack(8, 1, 4, 4 ,[(3,5), (2,6)]))

# Method to Solve : If conditions. No specific data structure or algorithmic methods
# Time Complexity : O(n)
# Space Complexity : O(1)