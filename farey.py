import time

# Returns the rational approximation of a decimal
global recCount
recCount = 0


def re_farey(dec: float, lowerB: tuple[int] = (0, 1), upperB: tuple[int] = (1, 1)) -> tuple[int]:
    global recCount
    recCount += 1
    try:
        # naive sum the upper lower bounds to get median
        median = tuple(map(lambda i, j: i + j, lowerB, upperB))
        # Decimal expansion of median
        medianDE = median[0] / median[1]

        #print(f'Median is {median}')
        #print(f'Median Decimal Expansion is {medianDE}\n')

        # recursively hone in on the correct fraction
        if dec < medianDE:
            median = re_farey(dec, lowerB, median)
            return median
        elif dec > medianDE:
            median = re_farey(dec, median, upperB)
            return median
        else:
            #print(f'Fraction for {dec} is {median[0]}/{median[1]}' )
            return median
    except:
        #print(f'Ran out of Recursions')
        #print(f'Fraction for {dec} is close to {median[0]}/{median[1]}')
        return median


def wh_farey(dec: float, loopMax: int) -> tuple[int]:
    lowerB = (0, 1)
    upperB = (1, 1)
    median = tuple(map(lambda i, j: i + j, lowerB, upperB))
    loopCount = 0

    while (medianDE := (median[0] / median[1])) != dec:
        loopCount += 1
        #print(f'Median is {median[0]}/{median[1]}')
        #print(f'Median Decimal Expansion is {medianDE}\n')
        if dec < medianDE:
            upperB = median
            median = tuple(map(lambda i, j: i + j, lowerB, upperB))
        elif dec > medianDE:
            lowerB = median
            median = tuple(map(lambda i, j: i + j, lowerB, upperB))
        if loopCount >= loopMax:
            break
    #print(f'Fraction for {dec} is {median[0]}/{median[1]}')
    print(f'Loop count is {loopCount}')
    return median


if __name__ == '__main__':
    testDec = 0.111111111111111
    print(f'Decimal is {testDec}')
    start1 = time.perf_counter_ns()
    out1 = re_farey(testDec)
    time_elapsed_one = time.perf_counter_ns() - start1
    print(f'Recursion count is {recCount}')
    print(f'Recursive method got {out1[0]}/{out1[1]} in {time_elapsed_one}ns')

    start2 = time.perf_counter_ns()
    out2 = wh_farey(testDec, 999)
    time_elapsed_two = time.perf_counter_ns() - start2
    print(f'While method got {out2[0]}/{out2[1]} in {time_elapsed_two}ns')
