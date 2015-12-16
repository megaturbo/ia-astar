import math

__author__ = 'thomas.roulin'


class City:
    def __init__(self, name, posx, posy):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.links = []

    def __repr__(self):
        return self.name + " " + str(self.posx) + " " + str(self.posy)

    def link_to(self, city):
        self.links.append(city)


class Link:
    def __init__(self, city1, city2, dist):
        self.city1 = city1
        self.city2 = city2
        self.dist = dist


def getCity(cities, city_name):
    return [city for city in cities if city.name == city_name]


def initCities(f_connections, f_positions):
    cities = []
    links = []

    for p in [pos.split(" ") for pos in f_positions]:
        cities.append(City(p[0], int(p[1]), int(p[2])))

    for c in [conn.split(" ") for conn in f_connections]:
        links.append(Link(getCity(cities, c[0]), getCity(cities, c[1]), int(c[2])))

    return cities, links


# HEURISTICS
def h0(a, b):
    """ h0(n) = 0 """
    return 0


def h1(a, b):
    """ h1(n) = distance en X """
    return math.fabs(a.posx - b.posx)


def h2(a, b):
    """ h2(n) = distance en Y """
    return math.fabs(a.posy - b.posy)


def h3(a, b):
    """ h3(n) = distance euclidienne """
    return math.sqrt(h1(a, b) ** 2 + h2(a, b) ** 2)


def h4(a, b):
    """ h4(n) = distance de Manhattan """
    return h1(a, b) + h2(a, b)


# ALGORITHM
def astar(start, end, heuristic):
    closed_queue = []
    open_queue = [start]
    came_from = {}

    g_score = {start: heuristic(start, end)}
    f_score = {}

    while len(open_queue) > 0:
        current = open_queue.pop(min(open_queue, key=score.get))
        if current == end:
            return  # path

        closed_queue.append(current)
        for l in current.links:
            if l in closed_queue:
                continue
            t_g_score = g_score[current] # + distance between ?
            if l not in open_queue:
                open_queue.append(l)
            elif t_g_score >= g_score[l]:
                continue

            came_from[l] = current
            g_score[l] = t_g_score
            f_score[l] = g_score[l] + heuristic(l, end)


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path


if __name__ == '__main__':
    file_links = open('connections.txt', 'r')
    file_positions = open('positions.txt', 'r')

    cities, links = initCities(file_links, file_positions)

    c0 = cities[0]
    c1 = cities[1]
    print(h1(c0, c1))
    print(h2(c0, c1))
    print(h3(c0, c1))
