'''
This function takes two integer arrays and returns their intersection in the form of an integer array.
Order does not matter for the return.
'''

def intersection(nums1, nums2):
    ret = []

    for num in nums1:
        # Check if unique value is in second array.
        if num not in ret and num in nums2:
            ret.append(num)
    return ret

# Change the input values here.
input1 = [4, 9, 5]
input2 = [9, 4, 9, 8, 4]

result = intersection(input1, input2)
print(result)