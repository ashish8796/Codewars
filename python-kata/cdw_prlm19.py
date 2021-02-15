'''Write a method highestRank(arr) (or highest-rank in clojure) which 
returns the number which is most frequent in the given input array (or ISeq). 
If there is a tie for most frequent number, return the largest number of which is most frequent.
'''


arr = [12, 10, 8, 12, 7, 6, 4, 10, 10]

def highest_rank(arr):
    return sorted([(arr.count(i),i) for i in set(arr)])[-1][-1]
    

print(highest_rank(arr))