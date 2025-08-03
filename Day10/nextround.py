'''
A. Next Round
time limit per test3 seconds
memory limit per test256 megabytes
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.

Input
The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

Output
Output the number of participants who advance to the next round.
'''
# class Solution:
#     def nextround(self, n, k, scores):
n, k = map(int, input().split())
scores = list(map(int, input().split()))
qualified_count = 0
for score in scores:
    if score >= scores[k-1] and score > 0:
        qualified_count += 1

print(qualified_count) 
    
# n_test = 8
# k_test = 5
# scores_test = [10, 9, 8, 7, 7, 7, 5, 5]

# # Create an instance of the class and call the method
# solver = Solution()
# result = solver.nextround(n_test, k_test, scores_test)

# # The k-th (5th) score is 7. Scores >= 7 are [10, 9, 8, 7, 7, 7]. All are positive.
# # So, the output should be 6.
# print(f"Number of participants who advance: {result}")