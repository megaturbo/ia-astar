import sys
import math

__author__ = 'Alex'


class city:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        return self



# Fonctions Heuristiques
def h0(n):
    ''' h0(n) = 0 '''
    return 0


def h1(n, b):
    ''' h1(n) = distance en X entre n et b '''
    return math.fabs(n.x - b.x)


def h2(n, b):
    ''' h2(n) = distance en Y entre n et b '''
    return math.fabs(n.y - b.y)


def h3(n, b):
    ''' h3(n) = distance euclidienne '''
    return math.sqrt(h1(n, b) ** 2 + h2(n, b) ** 2)


def h4(n, b):
    ''' h4(n) = distance de Manhattan '''
    return h1(n, b) + h2(n, b)


# Algorithme
def astar(start, goal, h):
    closedSet = []
    openSet = [start]
    cameFrom = []

    g_score = []
    g_score[start] = 0

    ''' Estimation du coût total du début à la fin en Y '''
    f_score = []
    f_score[start] = h(start, goal)

    while openSet:
        current = min(openSet, g_score.get)
        if current is goal:
            return reconstruct_path(cameFrom, goal)

        openSet.remove(current)
        closedSet.append(current)
        for neighbor in current:
            if closedSet.contains(neighbor):
                continue
            tentative_g_score = g_score[current] + dist_between(current, neighbor)
            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            ''' Save the path '''
            cameFrom[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)

    return -1


def reconstruct_path(a, b):
    total_path = [b]
    while b in a.keys:
        b = a[current]
        total_path.append(current)
    return total_path


if __name__ == '__main__':
    cities = []
    connections = open('connections.txt', 'r')
    positions = open('positions', 'r')

    ''' Je ne sais guère '''
    for l.split(" ") in positions:
        cities.append(city(l[0], l[1], l[2]))
