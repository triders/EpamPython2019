"""Компания выполняет процесс доставки путем пошаговой итерации. 
Компания имеет в распоряжении заданное изначально количество 
траков и кораблей. 
Компания выполняет "процесс доставки" заставляет "работать"
каждые транспортное средство пока каждый из списка контейнеров не будет 
иметь статус "доставлен". "процесс доставки выполняется пошагово с визуальным 
отображением местонахождения каждого из контейнеров на текущем шаге."


"""
from collections import deque


class DeliveryCompany:
	def __init__(self, containers, num_trucks, num_ships, truck_start, ship_start):
		self.time_spent = 0
		self.containers = containers
		self.truck_start = truck_start
		self.ship_start = ship_start 
		self.trucks = [Truck(truck_start) for i in range(num_trucks)]
		self.ships = [Ship(ship_start) for i in range(num_ships)]

	def process_delivery(self):
		"""deliver goes by step (1 step = 1 distance = 1 time)"""
		while not all(container.delivered for container in self.containers):
			self.time_spent += 1
			print(f'   STEP #{self.time_spent}')
			for ship in self.ships:
				ship.work(self.containers)
			for truck in self.trucks:
				truck.work(self.containers)
			print(self)
	
	def __str__(self):
		res = ''
		for container in containers:
			resi = ' ' + (container.destination.truck_dist)*'—' + \
			(container.destination.ship_dist)*'~' + '\n'
			resi = resi[:container.location] + '▌' + resi[container.location+1:]
			res += resi
		return res


class Warehouse:
	def __init__(self, name, truck_dist, ship_dist):
		self.name = name
		self.truck_dist = truck_dist
		self.ship_dist = ship_dist


class Container:
	def __init__ (self, destination: Warehouse):
		self.destination = destination
		self.location = 0
		self.delivered = False
	
	def __str__(self):
		return f"Container {self.destination.name}"


class Transport:
	_number = 0
	def __init__(self, start_location):
		self.start_position = True
		self.start_location = start_location
		self.location = start_location
		self.load = None 
		self.number = Transport._number
		Transport._number += 1


	def start_delivery(self, load: Container):
		self.start_position = False
		self.load = load


	def step_travel(self):
		if not self.start_position:
			self.location += 1
			self.load.location = self.location

	def step_travel_back(self):
		if not self.start_position:
			self.location -= 1
			if self.location == self.start_location:
				self.start_position = True


class Truck(Transport):

	def work(self, containers):
		if self.start_position:

			# start delivery
			for container in containers:
				if not container.delivered and container.location == 0:
					self.start_delivery(container)
					print(f'>truck #{self.number} picked {container} for delivery')
					self.step_travel()
					print(self)
					break
			else:
				return

		if not self.start_position:
			
			if self.load and self.load.location < self.load.destination.truck_dist:
				self.step_travel()
				print(self)
				return

			if self.load and self.load.location == self.load.destination.truck_dist:
				# final location for truck
				if not self.load.destination.ship_dist:
					self.load.delivered = True
				self.load = None
				print(f'truck #{self.number} is now empty')
				return
				
			if not self.load and self.start_position < self.location:
				# step return back
				super().step_travel_back()
				print(self)
				return

	def __str__(self):
		return f"truck #{self.number} with load {str(self.load)} \
		now on location {str(self.location)}"


class Ship(Transport):

	def work(self,containers):
		if self.start_position:
			# start delivery if route to warehouse includes ship
			for container in containers:
				
				if not container.delivered \
				and container.destination.ship_dist !=0 \
				and container.location == self.start_position:
					self.start_delivery(container)
					print(f'>ship #{self.number} picked {container} for delivery')
					self.step_travel()
					break

		if not self.start_position:

			if self.load \
			and self.load.destination.truck_dist <= \
			self.load.location < \
			self.load.destination.truck_dist + self.load.destination.ship_dist:
				self.step_travel()
				print(self)
				return

			if self.load \
			and self.load.location == \
			self.load.destination.truck_dist + self.load.destination.ship_dist:
				self.load.delivered = True
				self.load = None
				print(f'ship #{self.number} is now empty')
				return
				
			if not self.load and self.start_position < self.location:
				# step return back
				super().step_travel_back()
				print(self)
				return

	def __str__(self):
		return f"ship #{self.number} with load {str(self.load)}\
		 now on location {str(self.location)}"



warehouses = {'A': Warehouse('A', 1, 4), 'B': Warehouse('B', 5, 0)}

# containers_seq = input('Enter containers sequence: ')
containers_seq = 'AABABBAB'
# containers_seq = 'BBBB'


containers = [Container(warehouses[i]) for i in containers_seq]

delivery_company = DeliveryCompany(containers, num_trucks=2, num_ships=1, truck_start=0, ship_start=1)

delivery_company.process_delivery()

print('Total time spent:', delivery_company.time_spent)

