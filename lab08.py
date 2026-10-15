import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------- Crisp set ----------
temperatures = [10, 18, 22, 27, 35]
hot_crisp = {t for t in temperatures if t >= 25}
print("Crisp set HOT (t >= 25):", sorted(hot_crisp))

# ---------- Discrete fuzzy sets (element: membership degree) ----------
A = {'x1': 0.2, 'x2': 0.7, 'x3': 1.0, 'x4': 0.4}
B = {'x1': 0.5, 'x2': 0.3, 'x3': 0.8, 'x4': 0.9}

union        = {x: max(A[x], B[x]) for x in A}
intersection = {x: min(A[x], B[x]) for x in A}
complement_A = {x: round(1 - A[x], 2) for x in A}

print("A           :", A)
print("B           :", B)
print("A union B   :", union)
print("A inter B   :", intersection)
print("Complement A:", complement_A)

# ---------- Continuous membership functions ----------
def trimf(x, a, b, c):
    """Triangular membership function."""
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

def trapmf(x, a, b, c, d):
    """Trapezoidal membership function."""
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a + 1e-9), 1),
                                 (d - x) / (d - c + 1e-9)), 0)

x = np.linspace(0, 40, 401)
cold = trapmf(x, -1, 0, 10, 20)
warm = trimf(x, 15, 22.5, 30)
hot  = trapmf(x, 25, 32, 40, 41)

print("\nMembership of 27 C -> cold: %.2f, warm: %.2f, hot: %.2f"
      % (cold[270], warm[270], hot[270]))

plt.figure(figsize=(7, 3.2))
NAVY = '#0E367B'                       # Iqra University blue
plt.plot(x, cold, color=NAVY, ls=':', label='Cold')
plt.plot(x, warm, color=NAVY, ls='--', label='Warm')
plt.plot(x, hot, color=NAVY, ls='-', label='Hot')
plt.fill_between(x, np.fmax(warm, hot), color=NAVY, alpha=0.12, label='Warm OR Hot')
plt.fill_between(x, np.fmin(warm, hot), color=NAVY, alpha=0.6, label='Warm AND Hot')
plt.xlabel('Temperature (C)'); plt.ylabel('Membership'); plt.legend(fontsize=8)
plt.title('Fuzzy sets for temperature')
plt.savefig('lab08_fuzzy.png', dpi=130, bbox_inches='tight')
