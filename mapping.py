from curried_funcs import curried_pow

def map(f, collection):
    result_collection = []
    start = 0
    end = len(collection) - 1
    while start < end:
        result_collection.append(f(collection[start]))
        start += 1
    return result_collection
    
def map_range(f, start, end):
    result = []
    while start < end:
        result.append(f(start))
        start += 1
    return result
    
print(map_range(curried_pow(2), 0, 10))
print(map(curried_pow(2), [0,1,2,3,4,5,6,7,8,9,10]))
