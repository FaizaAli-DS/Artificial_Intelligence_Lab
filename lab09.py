import numpy as np

def trimf(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a + 1e-9), (c - x) / (c - b + 1e-9)), 0)

# ---------- Universes of discourse ----------
temp_u  = np.arange(10, 46, 0.5)     # room temperature in C
hum_u   = np.arange(0, 101, 1)       # relative humidity in %
power_u = np.arange(0, 101, 1)       # AC cooling power in %

# ---------- Fuzzy sets (linguistic terms) ----------
temp_sets  = {'cool': (10, 10, 24), 'comfortable': (20, 25, 30), 'hot': (26, 45, 45)}
hum_sets   = {'dry': (0, 0, 50), 'normal': (30, 50, 70), 'humid': (50, 100, 100)}
power_sets = {'low': (0, 0, 40), 'medium': (25, 50, 75), 'high': (60, 100, 100)}

def fuzzify(value, sets):
    return {name: float(trimf(np.array([value]), *abc)[0]) for name, abc in sets.items()}

# ---------- Rule base (IF temp AND humidity THEN power) ----------
rules = [
    ('cool',        'dry',    'low'),
    ('cool',        'normal', 'low'),
    ('cool',        'humid',  'medium'),
    ('comfortable', 'dry',    'low'),
    ('comfortable', 'normal', 'medium'),
    ('comfortable', 'humid',  'high'),
    ('hot',         'dry',    'medium'),
    ('hot',         'normal', 'high'),
    ('hot',         'humid',  'high'),
]

def ac_controller(temperature, humidity, verbose=True):
    # 1. Fuzzification
    t = fuzzify(temperature, temp_sets)
    h = fuzzify(humidity, hum_sets)
    if verbose:
        print("Fuzzified temperature:", {k: round(v, 2) for k, v in t.items()})
        print("Fuzzified humidity   :", {k: round(v, 2) for k, v in h.items()})
    # 2. Rule evaluation (AND = min) and implication (clip = min)
    aggregated = np.zeros_like(power_u, dtype=float)
    for ts, hs, ps in rules:
        strength = min(t[ts], h[hs])
        if strength > 0:
            if verbose:
                print(f"  Rule fired: IF temp is {ts} AND humidity is {hs} "
                      f"THEN power is {ps}  (strength {strength:.2f})")
            clipped = np.fmin(strength, trimf(power_u, *power_sets[ps]))
            # 3. Aggregation (OR = max)
            aggregated = np.fmax(aggregated, clipped)
    # 4. Defuzzification (centroid)
    if aggregated.sum() == 0:
        return 0.0
    return float((power_u * aggregated).sum() / aggregated.sum())

out = ac_controller(29, 65)
print(f"Crisp output -> AC cooling power = {out:.1f}%\n")

print("Temperature  Humidity  Power")
for T, H in [(18, 30), (24, 50), (32, 40), (38, 85)]:
    print(f"{T:>8} C {H:>8} % {ac_controller(T, H, verbose=False):>7.1f} %")
