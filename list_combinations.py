# given a list of numbers and a target number k,
# Return whether or not there are two numbers in the list that add upto k
# algorithm:
    # loop through each list element
    # combine with subsequent list elements
    # if sum is equal to k, return combination

# research: permutations and combinations, enumerate

def two_sum(list, k):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == k:
                return list[i], list[j]
        
x = [4,7,1,-3,2]
print(two_sum(x, 6))
