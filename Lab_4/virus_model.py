from mesa import Agent, Model
from mesa.space import ContinuousSpace
from mesa.time import SimultaneousActivation  # Fixed import
from mesa.datacollection import DataCollector
import random, math

# Agent representing a computer in a network
class ComputerAgent(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.status = "vulnerable"
        self.recovery_timer = 0
        self.pos = pos  # Position tracking for movement

    def step(self):
        if self.status == "infected":
            self.infect_others()
            self.recovery_timer -= 1
            if self.recovery_timer <= 0:
                self.status = "protected"
        
        if self.status == "to_infect":
            self.status, self.recovery_timer = "infected", self.model.recovery_time
        
        self.move()

    def infect_others(self):
        for other in self.model.schedule.agents:
            if other.status == "vulnerable" and self.distance(other) < self.model.infection_radius:
                if random.random() < self.model.infection_chance:
                    other.status = "to_infect"

    def distance(self, other):
        x1, y1 = self.pos
        x2, y2 = other.pos
        return math.hypot(x1 - x2, y1 - y2)

    def move(self):
        dx, dy = random.uniform(-1, 1), random.uniform(-1, 1)
        x, y = self.pos
        new_x, new_y = min(max(x + dx, 0), self.model.width), min(max(y + dy, 0), self.model.height)
        self.pos = (new_x, new_y)
        self.model.space.move_agent(self, (new_x, new_y))  # Fix for position update

# Model representing a virus spread simulation
class VirusModel(Model):
    def __init__(self, population=100, initial_infected=5, infection_radius=2, infection_chance=0.5, recovery_time=30, width=20, height=20):
        self.population, self.infection_radius, self.infection_chance, self.recovery_time = population, infection_radius, infection_chance, recovery_time
        self.width, self.height = width, height
        self.schedule, self.space = SimultaneousActivation(self), ContinuousSpace(width, height, torus=True)

        self.datacollector = DataCollector(model_reporters={
            "Infected": lambda m: self.count_status("infected"),
            "Protected": lambda m: self.count_status("protected"),
            "Time": lambda m: m.schedule.time
        })

        self.create_agents(initial_infected)
        self.running = True

    def create_agents(self, initial_infected):
        agents = [ComputerAgent(i, self, (random.uniform(0, self.width), random.uniform(0, self.height))) for i in range(self.population)]
        for agent in agents:
            self.space.place_agent(agent, agent.pos)
            self.schedule.add(agent)

        for agent in random.sample(agents, initial_infected):
            agent.status, agent.recovery_timer = "infected", self.recovery_time

    def count_status(self, status):
        return sum(1 for a in self.schedule.agents if a.status == status)

    def step(self):
        self.datacollector.collect(self)
        if all(agent.status != "infected" for agent in self.schedule.agents):
            self.running = False
        self.schedule.step()
