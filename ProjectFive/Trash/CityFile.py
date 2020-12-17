


# City class
class City(object):
    """
    Stores City objects. Upon initiation, automatically appends itself to list_of_cities
    self.x: x-coord
    self.y: y-coord
    self.graph_x: x-coord for graphic representation
    self.graph_y: y-coord for graphic representation
    self.name: human readable name.
    self.distance_to: dictionary of distances to other cities (keys are city names, values are floats)
    """
    def __init__(self, name, x, y, distance_to=None, var1=[]):
        # Name and coordinates:
        self.name = name
        self.x = self.graph_x = x
        self.y = self.graph_y = y
        self.var1=var1
        # Appends itself to the global list of cities:
        self.var1.append(self)
        # Creates a dictionary of the distances to all the other cities (has to use a value so uses itself - always 0)
        self.distance_to = {self.name:0.0}
        if distance_to:
            self.distance_to = distance_to

    def calculate_distances(self): 
        '''
        self --> None
        Calculates the distances of the
        city to all other cities in the global 
        list list of cities, and places these values 
        in a dictionary called self.distance_to
        with city name keys and float values
        ''' 
        for city in self.var1:
            tmp_dist = self.point_dist(self.x, self.y, city.x, city.y)
            self.distance_to[city.name] = tmp_dist

    # Calculates the distance between two cartesian points..
    def point_dist(self, x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2)**(0.5)