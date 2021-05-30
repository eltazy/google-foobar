# FAILED


# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and
# freeing Commander Lambda's bunny workers, but once they're free of the work
# duties the bunnies are going to need to escape Lambda's space station via the
# escape pods as quickly as possible. Unfortunately, the halls of the space
# station are a maze of corridors and dead ends that will be a deathtrap for the 
# escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling
# project that will give you the opportunity to make things a little easier for the bunnies.
# Unfortunately (again), you can't just remove all obstacles between the bunnies and the
# escape pods - at most you can remove one wall per escape pod path, both to maintain
# structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a
# work area exit and ending at the door to an escape pod. The map
# is represented as a matrix of 0s and 1s, where 0s are passable space
# and 1s are impassable walls. The door out of the station is at the top left (0,0)
# and the door into an escape pod is at the bottom right (w-1,h-1). 

# Write a function solution(map) that generates the length of the shortest path
# from the station door to the escape pod, where you are allowed to remove
# one wall as part of your remodeling plans. The path length is the total
# number of nodes you pass through, counting both the entrance and exit nodes
#. The starting and ending positions are always passable (0). The map will always be 
# solvable, though you may or may not need to remove a wall. The height and width of
# the map can be from 2 to 20. Moves can only be made in cardinal directions;
# no diagonal moves are allowed.

class Path:
    def __init__(self, seq, tail, broke_wall=False):
        self.seq = seq
        self.tail = tail
        self.broke_wall = broke_wall

    def __repr__(self):
        return self.seq
    
    def add2seq(self, c):
        self.seq += c

    def break_wall(self, val=True):
        self.broke_wall = val

class Cell:
    def __init__(self, x, y, walled=0, dead=0, traversed=False):
        self.x = x
        self.y = y
        self.walled = walled
        self.dead = dead
        self.traversed = traversed
        
    def __repr__(self):
        return 'T' if self.traversed else '-'
        # return '({}, {})'.format(self.x, self.y)
        # return '[ x:{}, y:{}, walled:{}, dead:{} ]'.format(self.x, self.y, self.walled, self.dead)

    def is_on_edge(self, size):
        return self.x==0 or self.y==0 or self.x==size-1 or self.y==size-1


def voisins(cell, h, l):
    poss = [
        voisinE(cell, l),
        voisinS(cell, h),
        voisinN(cell),
        voisinW(cell)
    ]
    return [v for v in poss if v]

def voisin(cell, dir, h, l):
    if dir=='N': return voisinN(cell)
    if dir=='S': return voisinS(cell, h)
    if dir=='E': return voisinE(cell, l)
    if dir=='W': return voisinW(cell)

def voisinN(cell):
    if cell.y==0: return False
    return cell.x, cell.y-1, 'N'

def voisinS(cell, h):
    if cell.y==h-1: return False
    return cell.x, cell.y+1, 'S'

def voisinW(cell):
    if cell.x==0: return False
    return cell.x-1, cell.y, 'W'

def voisinE(cell, l):
    if cell.x==l-1: return False
    return cell.x+1, cell.y, 'E'

def solution(map):
    H, L = len(map), len(map[0])
    for i, line in enumerate(map):
        for j, case in enumerate(line):
            map[i][j] = Cell(j, i, case)
    
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            neighbours = voisins(cell, H, L)
            n_walls_around = len([v for v in neighbours if map[v[1]][v[0]].walled])
            if cell.walled:
                if cell.is_on_edge(H):
                    if n_walls_around>1:
                        map[i][j].dead = 1
                elif n_walls_around>2:
                        map[i][j].dead = 1
            elif n_walls_around>3:
                map[i][j].dead = 1

            # print('### edge cell. at ({}, {})'.format(cell.x, cell.y))
    board = map
    # print('############# BOARD:', board)
    pos = Cell(0, 0)
    paths = [Path('0', pos)]
    map[0][0].traversed = True
    traverse = 0
    print('### paths:', paths)
    while traverse<1000:
        for i, path in enumerate(paths):
            tail = (0, 0, 'T')
            for dir in path.seq[1:]:
                if dir in 'NSEW':
                    tail = voisin(Cell(tail[0], tail[1]), dir, H, L)
                map[tail[1]][tail[0]].traversed=True

            # found_none=False
            if path.seq[-1] in 'DA': continue
            tmp=[]
            neighbours = voisins(path.tail, H, L)
            # print('all neig', neighbours, 'of', path.tail)
            for line in map:
                print(line)
            # print('\n')
            open_neig = [v for v in neighbours if not map[v[1]][v[0]].traversed]
            for v in open_neig:
                # print('open neig', open_neig, 'of', path.tail)
                if not map[v[1]][v[0]].traversed:
                    if v[0]==L-1 and v[1]==H-1:
                        tmp.append(Path(path.seq+'A', None, path.broke_wall))
                    elif map[v[1]][v[0]].dead:
                        continue
                        # tmp.append(Path(path.seq+'D', None, path.broke_wall))
                    elif map[v[1]][v[0]].walled:
                        if path.broke_wall: continue
                            # tmp.append(Path(path.seq+'D', None, path.broke_wall))
                        else:
                            path.broke_wall = True
                            tmp.append(Path(path.seq+v[2], map[v[1]][v[0]], True))
                    else: tmp.append(Path(path.seq+v[2], map[v[1]][v[0]], path.broke_wall))
                # map[v[1]][v[0]].traversed = True
                # else:
                
            # print('@@@ board', board)
            for line in map:
                # print(line)
                for cell in line:
                    cell.traversed=False
            # print('@@@ map', map)
            # map = board
            map[0][0].traversed = True
            # print('### paths bef:', paths)
            if tmp:
                print('next', tmp, 'for', path)
                # print('searched', tmp[0].seq[:-1])
                index = [j for j, p in enumerate(paths) if p.seq == tmp[0].seq[:-1]]
                # print('found at', index)
                if index:
                    index = index[0]
                    paths = paths[:index] + tmp + paths[index+1:]
            else:
                path.seq+='D'
                print('next', tmp, 'for', path)
            # paths = paths[:i-1] + tmp + paths[i+1:]
            # print('### paths:', paths)
        traverse+=1
    rep = min([len(p.seq) for p in paths if p.seq[-1]=='A'])
    print('### rep:', rep)
    return rep

# solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])

# solution([ [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

solution([
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
    ])
