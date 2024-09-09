'''
This function takes an integer target and an integer array and finds the shortest continuous subarray where
the sum of the subarray is >= the target. Returns the length of the subarray.
If the subarray does not exist, return 0.
'''

def shortest_subarray(target, nums):
    # Base case.
    if max(nums) >= target:
        return 1
    
    # Pointers for sliding window technique.
    head, tail = 0, 0
    curr_sum = 0

    # Any possible answer is less than or equal to length of array.
    curr_shortest_len = len(nums) + 1

    # Move tail pointer to end of array.
    while tail < len(nums):
        curr_sum += nums[tail]

        # Whenever sum becomes greater than or equal to target, move head pointer towards the tail.
        while curr_sum >= target:
            # Check if current length is the shortest length.
            curr_shortest_len = min(curr_shortest_len, tail - head + 1)
            curr_sum -= nums[head]
            head += 1
        tail += 1

    # No matching subarray.
    if curr_shortest_len == len(nums) + 1:
        return 0

    return curr_shortest_len

# Change the input values here.
input1 = 7
input2 = [2,3,1,2,4,3]

result = shortest_subarray(input1, input2)
print(result)