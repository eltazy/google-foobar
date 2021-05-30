# PASSED

def can_go(src, d, steps):
    if d == 'E': return 7-(src%8) >= steps
    elif d == 'W': return src%8 >= steps
    elif d == 'N': return src//8 >= steps
    else: return 7-(src//8) >= steps

def can_go_east(src, steps=1): return can_go(src, 'E', steps)
def can_go_west(src, steps=1): return can_go(src, 'W', steps)
def can_go_south(src, steps=1): return can_go(src, 'S', steps)
def can_go_north(src, steps=1): return can_go(src, 'N', steps)

def next_possible_cells(target, curr):
    all = []
    if can_go_east(curr):
        if can_go_south(curr, 2):
            tmp=curr+17
            all.append(tmp)
            if tmp==target: return all
        if can_go_north(curr, 2):
            tmp=curr-15
            all.append(tmp)
            if tmp==target: return all
    if can_go_east(curr, 2):
        if can_go_south(curr):
            tmp=curr+10
            all.append(tmp)
            if tmp==target: return all
        if can_go_north(curr):
            tmp=curr-6
            all.append(tmp)
            if tmp==target: return all
    if can_go_west(curr):
        if can_go_south(curr, 2):
            tmp=curr+15
            all.append(tmp)
            if tmp==target: return all
        if can_go_north(curr, 2):
            tmp=curr-17
            all.append(tmp)
            if tmp==target: return all
    if can_go_west(curr, 2):
        if can_go_south(curr):
            tmp=curr+6
            all.append(tmp)
            if tmp==target: return all
        if can_go_north(curr):
            tmp=curr-10
            all.append(tmp)
            if tmp==target: return all
    # print(curr, ' ------> ', all)
    return all
    
def solution(src, dest):
    depth = 0
    curr_cases = [src]
    # print('\ncurr', curr_cases)
    next_cases = []
    cont = True
    while cont:
        if (dest in curr_cases):
            cont = False
        else:
            next_cases = []
            for cell in curr_cases:
                next_cases += next_possible_cells(dest, cell)
                next_cases = next_cases
            depth += 1
        curr_cases = next_cases
        # print('next', next_cases)
    # print('\n### result: ', depth)
    return depth
    
# solution(0, 1)
# solution(19, 36)
# solution(12, 12)
# solution(34, 1)
# solution(0, 63)
