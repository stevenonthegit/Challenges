#bomb_baby
#First, the bombs self-replicate via one of two distinct processes: 
#Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
#Every Facula bomb spontaneously creates a Mach bomb.
#For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

#You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.

def answer(M, F): 
    M = int(M) 
    F = int(F)
    #handle early failure case
    if M<1 or F<1:
        return 'impossible'

    count = 0
    _max = M
    _min = F

    while _max > 1:
        # swap to keep max larger
        if _min > _max:
            _max, _min = _min, _max
        
        # We are basically iterating through this in reverse. 
        # Starting at the target M F, we are working our way backwards to 1 1. 
        # Due to the rules of replication, we know that the largest # was always the 
        # last one to be "produced", so we are starting with the max and working down.
        # 
        # We can approach this two ways: Take the difference, or use the mod remainder. 
        # E.g. M F = 100,21 is our Final round N. 
        # We can use the difference (100-21=79) and know that the N-1 round is 79,21. 
        # N-2 would be 58,21,  N-3 would be 37,21,  and N-4 is 16,21. 
        # For excessively large differences, this takes a lot of steps, so we can just
        # take the remainder (100%21=16), knowing immediately there exists a step N-K = 16,21.
        # 
        # So, by using division, we can find K (100//21=4), and apply that
        # to the total sum. In this case, it saves us a few iterations, but in the case of 
        # something extreme like 10^6, 1, we can use this technique to save 10^6 iterations. 
        mod = _max % _min
        
        if mod <= 0:
            return "impossible" # M F can never be equal (or divisible) after step 1,1
        else:
            count += _max // _min # using rules explained above
            _max  = mod

    # the loop will exit when max = 1, and min = N. e.g. 1,5 or 1,2 or 12,1.
    # it will take min-1 steps to reach that condition, so we add it to the count.
    count += _min - 1

    return count


if __name__ == '__main__':
    print(answer(3,5)) #expected: 3
    print(answer(100,21)) #expected: 12
    print(answer(9999,2)) #expected: 5000