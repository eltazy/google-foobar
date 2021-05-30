# PASSED

import math;

def solution(area):
    nums = []
    if area <= 0: nums = [0]
    else:
        while area > 0:
            n = int(math.sqrt(area))
            n = pow(n, 2)
            nums.append(n)
            area -= n
    print(','.join(str(i) for i in nums))
    # return nums

# solution(15324)
# solution(12)
# solution(0)
# solution(1)
# solution(1000000)
# solution()
