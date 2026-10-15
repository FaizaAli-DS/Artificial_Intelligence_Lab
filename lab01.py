import random

class VacuumEnvironment:
    """Two-square world: locations 'A' and 'B', each Clean (0) or Dirty (1)."""
    def __init__(self):
        self.status = {'A': random.randint(0, 1), 'B': random.randint(0, 1)}
        self.agent_location = random.choice(['A', 'B'])

    def percept(self):
        return (self.agent_location, self.status[self.agent_location])

    def execute(self, action):
        if action == 'Suck':
            self.status[self.agent_location] = 0
        elif action == 'Right':
            self.agent_location = 'B'
        elif action == 'Left':
            self.agent_location = 'A'

def reflex_vacuum_agent(percept):
    """Condition-action rules: decide using ONLY the current percept."""
    location, dirty = percept
    if dirty:
        return 'Suck'
    elif location == 'A':
        return 'Right'
    else:
        return 'Left'

random.seed(7)
env = VacuumEnvironment()
env.status = {'A': 1, 'B': 1}; env.agent_location = 'B'
print("Initial state :", env.status, "| Agent at", env.agent_location)
score = 0
for step in range(1, 5):
    p = env.percept()
    action = reflex_vacuum_agent(p)
    env.execute(action)
    if action == 'Suck':
        score += 10      # reward for cleaning
    else:
        score -= 1       # cost of moving
    print(f"Step {step}: percept={p} -> action={action:5s} | world={env.status}")
print("Final state   :", env.status)
print("Performance score:", score)
