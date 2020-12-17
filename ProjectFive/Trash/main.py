'''
Genetic Algorithm for the Travelling Salesman Problem
v1.0
by
JackFrigaard
mail@jackf.net
Written for Python 3.1+
'''

import random
import copy
import os
import time
import math
import csv
from CityFile import City
from RouteFile import Route, RoutePop
from tsp_genetic_algorith import GA




try:
    from tkinter import *
    from tkinter.ttk import *
except Exception as e:
    print("[ERROR]: {0}".format(e))
    from Tkinter import *






list_of_cities =[]

#########################################
######                             ######
######    Algorithm paremeters:    ######
######                             ######
#########################################

# probability that an individual Route will mutate
k_mut_prob = 0.4

# Number of generations to run for
k_n_generations = 100
# Population size of 1 generation (RoutePop)
k_population_size = 100

# Size of the tournament selection. 
tournament_size = 7

# If elitism is True, the best from one generation will carried over to the next.
elitism = True

# Read city data from csv?
csv_cities = False

# Full path for csv file. The r prefix avoids any conflicts with backslashes.
csv_name = 'cities.csv'



class App(object):
    """
    Runs the application
    """
    def __init__(self,n_generations,pop_size, graph=False):
        '''
        Initiates an App object to run for n_generations with a population of size pop_size
        '''

        if csv_cities:
            self.read_csv()

        self.n_generations = n_generations
        self.pop_size = pop_size

        # Once all the cities are defined, calcualtes the distances for all of them.
        # for city in list_of_cities:
        #     city.calculate_distances()
        if graph:
            self.set_city_gcoords()
            
            # Initiates a window object & sets its title
            self.window = Tk()
            self.window.wm_title("Generation 0")

            # initiates two canvases, one for current and one for best
            self.canvas_current = Canvas(self.window, height=300, width=300)
            self.canvas_best = Canvas(self.window, height=300, width=300)

            # Initiates two labels
            self.canvas_current_title = Label(self.window, text="Best route of current gen:")
            self.canvas_best_title = Label(self.window, text="Overall best so far:")

            # Initiates a status bar with a string
            self.stat_tk_txt = StringVar()
            self.status_label = Label(self.window, textvariable=self.stat_tk_txt, relief=SUNKEN, anchor=W)

            # creates dots for the cities on both of the canvases
            for city in list_of_cities:
                self.canvas_current.create_oval(city.graph_x-2, city.graph_y-2, city.graph_x + 2, city.graph_y + 2, fill='blue')
                self.canvas_best.create_oval(city.graph_x-2, city.graph_y-2, city.graph_x + 2, city.graph_y + 2, fill='blue')

            # Packs all the widgets (physically creates them and places them in order)
            self.canvas_current_title.pack()
            self.canvas_current.pack()
            self.canvas_best_title.pack()
            self.canvas_best.pack()
            self.status_label.pack(side=BOTTOM, fill=X)

            # Runs the main window loop
            self.window_loop(graph)
        else:
            print("Calculating GA_loop")
            self.GA_loop(n_generations,pop_size, graph=graph)

    def set_city_gcoords(self):
        '''
        All cities have graph_x and graph_y attributes that are only referenced when showing them on the map.
        This method takes the original city.x and city.y and transforms them so that the coordinates map fully onto the 300x300 map view.
        '''

        # defines some variables (we will set them next)
        min_x = 100000
        max_x = -100000
        min_y = 100000
        max_y = -100000

        #finds the proper maximum/minimum
        for city in list_of_cities:

            if city.x < min_x:
                min_x = city.x
            if city.x > max_x:
                max_x = city.x

            if city.y < min_y:
                min_y = city.y
            if city.y > max_y:
                max_y = city.y

        # shifts the graph_x so the leftmost city starts at x=0, same for y.
        for city in list_of_cities:
            city.graph_x = (city.graph_x + (-1*min_x))
            city.graph_y = (city.graph_y + (-1*min_y))

        # resets the variables now we've made changes
        min_x = 100000
        max_x = -100000
        min_y = 100000
        max_y = -100000

        #finds the proper maximum/minimum
        for city in list_of_cities:

            if city.graph_x < min_x:
                min_x = city.graph_x
            if city.graph_x > max_x:
                max_x = city.graph_x

            if city.graph_y < min_y:
                min_y = city.graph_y
            if city.graph_y > max_y:
                max_y = city.graph_y

        # if x is the longer dimension, set the stretch factor to 300 (px) / max_x. Else do it for y. This conserves aspect ratio.
        if max_x > max_y:
            stretch = 300 / max_x
        else:
            stretch = 300 / max_y

        # stretch all the cities so that the city with the highest coordinates has both x and y < 300
        for city in list_of_cities:
            city.graph_x *= stretch
            city.graph_y = 300 - (city.graph_y * stretch)


    def update_canvas(self,the_canvas,the_route,color):
        '''
        Convenience method to update the canvases with the new routes
        '''

        # deletes all current items with tag 'path'
        the_canvas.delete('path')

        # loops through the route
        for i in range(len(the_route.route)):

            # similar to i+1 but will loop around at the end
            next_i = i-len(the_route.route)+1

            # creates the line from city to city
            the_canvas.create_line(the_route.route[i].graph_x,
                                the_route.route[i].graph_y,
                                the_route.route[next_i].graph_x,
                                the_route.route[next_i].graph_y,
                                tags=("path"),
                                fill=color)

            # Packs and updates the canvas
            the_canvas.pack()
            the_canvas.update_idletasks()

    def read_csv(self):
        with open(csv_name, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                new_city = City(row[0],float(row[1]),float(row[2]))

    def GA_loop(self,n_generations,pop_size, graph=False):
        '''
        Main logic loop for the GA. Creates and manages populations, running variables etc.
        '''

        # takes the time to measure the elapsed time
        start_time = time.time()

        # Creates the population:
        print("Creates the population:")
        the_population = RoutePop(pop_size, True)
        print ("Finished Creation of the population")

        # the_population.rt_pop[0].route = [1,8,38,31,44,18,7,28,6,37,19,27,17,43,30,36,46,33,20,47,21,32,39,48,5,42,24,10,45,35,4,26,2,29,34,41,16,22,3,23,14,25,13,11,12,15,40,9]
        # the_population.rt_pop[0].recalc_rt_len()
        # the_population.get_fittest()

        #checks to make sure there are no duplicate cities:
        if the_population.fittest.is_valid_route() == False:
            raise NameError('Multiple cities with same name. Check cities.')
            return # if there are, raise a NameError and return

        # gets the best length from the first population (no practical use, just out of interest to see improvements)
        initial_length = the_population.fittest.length

        # Creates a random route called best_route. It will store our overall best route.
        best_route = Route()

        if graph:
            # Update the two canvases with the just-created routes:
            self.update_canvas(self.canvas_current,the_population.fittest,'red')
            self.update_canvas(self.canvas_best,best_route,'green')


        # Main process loop (for number of generations)
        for x in range(1,n_generations):
            # Updates the current canvas every n generations (to avoid it lagging out, increase n)
            if x % 8 == 0 and graph:
                self.update_canvas(self.canvas_current,the_population.fittest,'red')

            # Evolves the population:
            the_population = GA().evolve_population(the_population)

            # If we have found a new shorter route, save it to best_route
            if the_population.fittest.length < best_route.length:
                # set the route (copy.deepcopy because the_population.fittest is persistent in this loop so will cause reference bugs)
                best_route = copy.deepcopy(the_population.fittest)
                if graph:
                    # Update the second canvas because we have a new best route:
                    self.update_canvas(self.canvas_best,best_route,'green')
                    # update the status bar (bottom bar)
                    self.stat_tk_txt.set('Initial length {0:.2f} Best length = {1:.2f}'.format(initial_length,best_route.length))
                    self.status_label.pack()
                    self.status_label.update_idletasks()

            # Prints info to the terminal:
            self.clear_term()
            print('Generation {0} of {1}'.format(x,n_generations))
            print(' ')
            print('Overall fittest has length {0:.2f}'.format(best_route.length))
            print('and goes via:')
            best_route.pr_cits_in_rt(True)
            print(' ')
            print('Current fittest has length {0:.2f}'.format(the_population.fittest.length))
            print('And goes via:')
            the_population.fittest.pr_cits_in_rt(True)
            print(' ')
            print('''The screen with the maps may become unresponsive if the population size is too large. It will refresh at the end.''')

            if graph:
                # sets the window title to the latest Generation:
                self.window.wm_title("Generation {0}".format(x))
        if graph:
            # sets the window title to the last generation
            self.window.wm_title("Generation {0}".format(n_generations))

            # updates the best route canvas for the last time:
            self.update_canvas(self.canvas_best,best_route,'green')
            
        # takes the end time of the run:
        end_time = time.time()

        # Prints final output to terminal:
        self.clear_term()
        print('Finished evolving {0} generations.'.format(n_generations))
        print("Elapsed time was {0:.1f} seconds.".format(end_time - start_time))
        print(' ')
        print('Initial best distance: {0:.2f}'.format(initial_length))
        print('Final best distance:   {0:.2f}'.format(best_route.length))
        print('The best route went via:')
        best_route.pr_cits_in_rt(print_route=True)

    def window_loop(self, graph):
        '''
        Wraps the GA_loop() method and initiates the window on top of the logic.
        window.mainloop() hogs the Thread, that's why the GA_loop is called as a callback
        '''
        # see http://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
        self.window.after(0,self.GA_loop(self.n_generations, self.pop_size, graph))
        self.window.mainloop()

    # Helper function for clearing terminal window
    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')







##############################
#### Declare cities here: ####
##############################

# Australian Cities:
# adelaide = City('adelaide', 138.60, -34.93)
# brisbane = City('brisbane', 153.02, -27.47)
# canberra = City('canberra', 149.13, -35.30)
# darwin = City('darwin', 130.83, -12.45)
# hobart = City('hobart', 147.32, -42.88)
# melbourne = City('melbourne', 144.97, -37.82)
# perth = City('perth', 115.85, -31.95)
# sydney = City('sydney', 151.20, -33.87)

## Random cities
# i = City('c1', 10, 2)
# j = City('c2', 1, 22)
# k = City('c3', 2, 13)

def specific_cities2():
    """function to calculate the route for files in data folder with coordinates"""
    start_time = time.time()
    f = open("data/pr2392-2.in", "r")
    f.readline()
    f.readline()
    f.readline()
    lines = int(f.readline().split()[2])
    f.readline()
    f.readline()
    for i, li in enumerate(f.readlines(), start=1):
        os.system('cls' if os.name=='nt' else 'clear')
        print("Read '{}': {}/{} lines".format(f.name, i, lines))
        c = li.split()
        if not 'EOF' in c:
            tmp = City("C" + str(c[0]), float(c[1]), float(c[2]))
    print("---Time reading file and creating Cities: %s seconds ---\n" % str(time.time() - start_time))
    
    start_time = time.time()
    print("Calculating distances...")
    for city in list_of_cities:
        city.calculate_distances()
    print("---Time Calculating distances: %s seconds ---\n" % str(time.time() - start_time))
    
    print("Searching for shortest way possible...")
    try:
        start_time = time.time()
        app = App(n_generations=k_n_generations,pop_size=k_population_size)
        print("---Route found in %s seconds ---" % str(time.time() - start_time))
    except Exception as e:
        print("\n[ERROR]: %s\n" % e)
    # try:
    # except Exception, e:
    #     print "[Exception]", e


def specific_cities():
    """function to calculate the route for files in data folder with distances"""
    try:
        start_time = time.time()
        f = open("data/3x3.in", "r")
        # f = open("data/bays29.in", "r")
        # f = open("data/d493.in", "r")
        # f = open("data/pr2392.in", "r")
        lines = int(f.readline())
        for i, li in enumerate(f.readlines(), start=1):
            os.system('cls' if os.name=='nt' else 'clear')
            print("Read '{}': {}/{} lines".format(f.name, i, lines))
            d = {}
            for j, line in enumerate(map(float, li.split()), start=1):
                d["C" + str(j)] = line
            tmp = City("C" + str(i), 10, 10, d)
        print("--- %s seconds ---" % str(time.time() - start_time))
        band = True
    except Exception as e:
        print(e)
        band = False
    if band:
        print("Searching for shortest path possible...")
        try:
            start_time = time.time()
            app = App(n_generations=k_n_generations,pop_size=k_population_size)
            print("---Route was found in %s seconds ---" % str(time.time() - start_time))
        except Exception as e:
            print("\n[ERROR]: %s\n" % e)


def random_cities():
    i = City('i', 60, 200,list_of_cities)
    j = City('j', 180, 190,list_of_cities)
    k = City('k', 100, 180,list_of_cities)
    l = City('l', 140, 180,list_of_cities)
    m = City('m', 20, 160,list_of_cities)
    n = City('n', 100, 160,list_of_cities)
    o = City('o', 140, 140,list_of_cities)
    p = City('p', 40, 120,list_of_cities)
    q = City('q', 100, 120,list_of_cities)
    r = City('r', 180, 100,list_of_cities)
    s = City('s', 60, 80,list_of_cities)
    t = City('t', 120, 80,list_of_cities)
    u = City('u', 180, 60,list_of_cities)
    v = City('v', 20, 40,list_of_cities)
    w = City('w', 100, 40,list_of_cities)
    x = City('x', 200, 40,list_of_cities)
    a = City('a', 20, 20,list_of_cities)
    b = City('b', 60, 20,list_of_cities)
    c = City('c', 160, 20,list_of_cities)
    d = City('d', 68, 130,list_of_cities)
    e = City('e', 10, 10,list_of_cities)
    f = City('f', 75, 180,list_of_cities)
    g = City('g', 190, 190,list_of_cities)
    h = City('h', 200, 10,list_of_cities)
    # a1 = City('a1', 53, 99)

    for city in list_of_cities:
        city.calculate_distances()
    ######## create and run an application instance:
    app = App(n_generations=k_n_generations,pop_size=k_population_size, graph=True)

if __name__ == '__main__':
    """Select only one function: random, specific or specific2"""
    # specific_cities2()
    #specific_cities()
    random_cities()