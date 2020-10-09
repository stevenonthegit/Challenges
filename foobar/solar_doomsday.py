#solar_doomsday
#Write a function answer(area) that takes as its input a single unit 
#of measure representing the total area of solar panels you have 
#(between 1 and 1000000 inclusive) and returns a list of the areas 
#of the largest squares you could make out of those panels, starting 
#with the largest squares first. 
#So, following the example above, answer(12) would return [9, 1, 1, 1].

from math import floor, sqrt

# This is an easy one, we are just going to calculate it in reverse order. We
# want to find all the squares that N contains, starting with the largest. 
# Take  √N and floor it (e.g. √12 = 3.464 = 3), and subtract the resulting square (3^2 = 9).
# Keep doing so until we reach zero. 
def answer(n):

    # check for invalid inputs
    if not isinstance(n, int) or n <= 0:
        return []

    result = []
    while(n > 0):
        square_val = floor(sqrt(n))**2 #find largest square, then subtract and continue
        n -= square_val 
        result.append(square_val)

    return result


if __name__ == '__main__':
    print(answer(12)) #expected: [9, 1, 1, 1]
    print(answer(12345)) #expected: [12321, 16, 4, 4]
    print(answer(294798)) #expected: [293764, 1024, 9, 1]
