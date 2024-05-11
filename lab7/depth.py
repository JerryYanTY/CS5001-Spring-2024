def depth(my_dict: dict, c_depth=0):
    if not isinstance(my_dict, dict):  # if the current value is not a dictionary, return curr depth
        return c_depth
    elif my_dict == {}:  # if the current value is an empty dictionary, add 1 to curr depth
        return c_depth + 1
    return max(depth(my_dict[key], c_depth + 1) for key in my_dict)  # recursively call the function to traverse the
    # dict, and return the highest value
