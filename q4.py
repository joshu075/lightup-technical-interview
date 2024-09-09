'''
Given a backpack with max capacity W and a set of items, each with two properties: weight (w) and value (v). Select the
items that give the most value without exceeding the max capacity of the backpack. Each item can only be selected
once. Return the maximum value possible.
'''

def max_item_value(W, items):
    # Base case.
    if len(items) == 0 or W == 0:
        return 0

    # Keep track of weight and value of current item.
    wt = items[0][0]
    val = items[0][1]

    # Remove current item from items list.
    remaining_items = items[1:]

    # If weight of current item exceeds remaining capacity, move on to next item.
    if wt > W:
        return max_item_value(W, remaining_items)

    else:
        # Include current item and check remaining items.
        curr_item_incl = val + max_item_value(W - wt, remaining_items)

        # Exclude current item and check remaining items.
        curr_item_excl = max_item_value(W, remaining_items)

        # Compare if including or excluding current item gives max value.
        return max(curr_item_incl, curr_item_excl)

# Change the input values here.
input1 = 10
input2 = [(5, 50), (4, 40), (6, 30)]

result = max_item_value(input1, input2)
print(result)