def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance
    
def improve(update, stop, guess=1, max_updates=100):
    k = 0
    while not stop(guess) and k < max_updates:
        print(guess)
        guess = update(guess)
        k += 1
    return guess
