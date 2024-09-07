'''
This function takes two integer arrays and returns their intersection in the form of an integer array.
Order does not matter for the return.
'''

def intersection(nums1, nums2):
    ret = []
    for num in nums1:
        if num not in ret and num in nums2:
            ret.append(num)
    return ret

# Change the input values here.
result = intersection([4, 9, 5], [9, 4, 9, 8, 4])
print(result)