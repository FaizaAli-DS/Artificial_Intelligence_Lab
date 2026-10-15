import random, math

# Maximise f(x) = x * sin(10*pi*x) + 1   on the interval [-1, 2]
def f(x):
    return x * math.sin(10 * math.pi * x) + 1

BITS, LOW, HIGH = 22, -1.0, 2.0

def decode(chrom):
    """Binary string -> real number in [LOW, HIGH]."""
    return LOW + int(chrom, 2) * (HIGH - LOW) / (2**BITS - 1)

def random_chrom():
    return ''.join(random.choice('01') for _ in range(BITS))

def tournament(pop, k=3):
    return max(random.sample(pop, k), key=lambda c: f(decode(c)))

def crossover(p1, p2, rate=0.9):
    if random.random() < rate:
        pt = random.randint(1, BITS - 1)          # single-point crossover
        return p1[:pt] + p2[pt:], p2[:pt] + p1[pt:]
    return p1, p2

def mutate(c, rate=1/BITS):
    return ''.join(b if random.random() > rate else '10'[int(b)] for b in c)

def genetic_algorithm(pop_size=50, generations=60):
    pop = [random_chrom() for _ in range(pop_size)]
    for gen in range(generations + 1):
        best = max(pop, key=lambda c: f(decode(c)))
        if gen % 10 == 0:
            print(f"Gen {gen:3d}: best x = {decode(best):.5f}, f(x) = {f(decode(best)):.5f}")
        new_pop = [best]                           # elitism
        while len(new_pop) < pop_size:
            c1, c2 = crossover(tournament(pop), tournament(pop))
            new_pop += [mutate(c1), mutate(c2)]
        pop = new_pop[:pop_size]
    return best

random.seed(42)
best = genetic_algorithm()
print(f"Best solution: x = {decode(best):.5f}, f(x) = {f(decode(best)):.5f}")
