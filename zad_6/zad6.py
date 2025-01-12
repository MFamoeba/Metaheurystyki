import numpy as np
import random
import os
import csv
from collections import namedtuple

# Define structures for Problem and Solution
Customer = namedtuple("Customer", ["index", "x", "y", "demand", "ready_time", "due_date", "service_time"])

class Ant:
    def __init__(self, depot, customers, vehicle_capacity, distance_matrix, num_vehicles, alpha=1.0, beta=2.0):
        self.depot = depot
        self.customers = customers
        self.num_customers = len(customers)
        self.vehicle_capacity = vehicle_capacity
        self.distance_matrix = distance_matrix
        self.num_vehicles = num_vehicles
        self.alpha = alpha  # siła feromonu
        self.beta = beta  # siła heurystyki
        self.route = []
        self.total_distance = 0

    def construct_solution(self, pheromone_matrix):
        unvisited = set(range(1, self.num_customers + 1))
        current_vehicle = []
        current_time = 0
        current_load = 0
        self.route = []
        self.total_distance = 0

        current_node = 0  # Start at the depot
        while unvisited:
            feasible = []
            for customer in unvisited:
                cust = self.customers[customer - 1]
                travel_time = self.distance_matrix[current_node][customer]
                arrival_time = current_time + travel_time

                if (current_load + cust.demand <= self.vehicle_capacity and
                        arrival_time <= cust.due_date):
                    feasible.append(customer)

            if not feasible:
                self.route.append(current_vehicle)
                self.total_distance += self.distance_matrix[current_node][0]
                current_vehicle = []
                current_time = 0
                current_load = 0
                current_node = 0
                continue

            probabilities = []
            for customer in feasible:
                tau = pheromone_matrix[current_node][customer]  # Pheromone level
                eta = 1 / self.distance_matrix[current_node][customer]  # Heuristic
                probabilities.append((tau ** self.alpha) * (eta ** self.beta))

            probabilities = np.array(probabilities)
            probabilities /= probabilities.sum()

            next_customer = random.choices(feasible, probabilities)[0]
            unvisited.remove(next_customer)
            current_vehicle.append(next_customer)
            travel_time = self.distance_matrix[current_node][next_customer]
            current_time += travel_time
            current_node = next_customer
            current_load += self.customers[next_customer - 1].demand

        if current_vehicle:
            self.route.append(current_vehicle)
            self.total_distance += self.distance_matrix[current_node][0]

def compute_distance_matrix(depot, customers):
    points = [depot] + customers
    dist_matrix = np.zeros((len(points), len(points)))
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points):
            dist_matrix[i][j] = np.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    return dist_matrix


def optimize(depot, customers, vehicle_capacity, num_vehicles, num_ants=10, max_iterations=100, evaporation_rate=0.5):
    best_route = None
    best_distance = float('inf')
    num_customers = len(customers)
    pheromone_matrix = np.ones((num_customers + 1, num_customers + 1))
    distance_matrix = compute_distance_matrix(depot, customers)
    for iteration in range(max_iterations):
        ants = [Ant(depot, customers, vehicle_capacity, distance_matrix, num_vehicles) for _ in range(num_ants)]
        for ant in ants:
            ant.construct_solution(pheromone_matrix)
            if ant.total_distance < best_distance:
                best_distance = ant.total_distance
                best_route = ant.route
        pheromone_matrix = update_pheromones(pheromone_matrix, ants, evaporation_rate)
        #print(f"Iteration {iteration + 1}, Best Distance: {best_distance}")
    return best_route, best_distance*10

def update_pheromones(pheromone_matrix, ants, evaporation_rate):
    pheromone_matrix *= (1 - evaporation_rate)
    for ant in ants:
        for route in ant.route:
            for i in range(len(route) - 1):
                from_node = route[i]
                to_node = route[i + 1]
                pheromone_matrix[from_node][to_node] += 1 / ant.total_distance
    return pheromone_matrix


def load_customers_from_file(file_path, customers_to_load=None):
    customers = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for index, row in enumerate(reader):
            if customers_to_load is not None and index >= customers_to_load:
                break
            x, y, demand, ready_time, due_date, service_time = map(float, row)
            customers.append(Customer(index, x, y, demand, ready_time, due_date, service_time))
    depot = customers.pop(0)  # The depot is the first row
    return depot, customers



directory_path = 'data'
files = os.listdir(directory_path)
txt_files = [file for file in files if file.endswith('c105.csv')]

for file_name in txt_files:
    file_path = os.path.join(directory_path, file_name)
    customers_to_load = 100
    depot, customers = load_customers_from_file(file_path, customers_to_load)
    vehicle_capacity = 200 #25/50/75
    num_vehicles = 2

    best_route, best_distance = optimize(depot, customers, vehicle_capacity, num_vehicles)
    print("File:", file_name)
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
