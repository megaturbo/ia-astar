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
    return 0


def h1(a, b):
    return math.fabs(a.posx - b.posx)


def h2(a, b):
    return math.fabs(a.posy - b.posy)


if __name__ == '__main__':
    file_links = open('connections.txt', 'r')
    file_positions = open('positions.txt', 'r')

    cities, links = initCities(file_links, file_positions)
