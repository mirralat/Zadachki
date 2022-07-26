import math
number = float(input())
def float_to_ratio(flt):
    if int(flt) == flt: # to prevent 3.0 -> 30/10
        return int(flt), 1
    flt_str = str(flt)
    flt_split = flt_str.split('.')
    numerator = int(''.join(flt_split))
    denominator = 10 ** len(flt_split[1])
    x = math.gcd(numerator, denominator)
    s = (int(numerator/x),'/', int(denominator/x))
    print(s)
    stre = ''
    for item in s:
        ex = str(item)
        stre +=  ex
    print(stre)
    
float_to_ratio(number)
