from mean_var_std import calculate

# Test the function
print("Result for [0..8]:")
print(calculate([0,1,2,3,4,5,6,7,8]))

# Test error handling
try:
    calculate([1,2,3])
except ValueError as e:
    print("Error handled correctly:", e)
