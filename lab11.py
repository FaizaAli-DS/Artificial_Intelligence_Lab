import numpy as np

class Perceptron:
    def __init__(self, n_inputs, lr=0.1):
        self.w = np.zeros(n_inputs)
        self.b = 0.0
        self.lr = lr

    def activation(self, z):
        return 1 if z >= 0 else 0              # step function

    def predict(self, x):
        return self.activation(np.dot(self.w, x) + self.b)

    def train(self, X, y, epochs=20):
        for epoch in range(1, epochs + 1):
            errors = 0
            for xi, target in zip(X, y):
                error = target - self.predict(xi)
                if error != 0:
                    # Perceptron learning rule
                    self.w += self.lr * error * xi
                    self.b += self.lr * error
                    errors += 1
            print(f"Epoch {epoch}: misclassified = {errors}, w = {self.w}, b = {self.b:.1f}")
            if errors == 0:
                print("Converged!")
                break

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

p = Perceptron(2)
p.train(X, y_and)
print("\nAND gate predictions:")
for xi in X:
    print(f"  {xi} -> {p.predict(xi)}")

# XOR is NOT linearly separable: the perceptron never converges
print("\nTraining on XOR (10 epochs):")
q = Perceptron(2)
y_xor = np.array([0, 1, 1, 0])
for epoch in range(10):
    errs = 0
    for xi, t in zip(X, y_xor):
        e = t - q.predict(xi)
        if e: q.w += q.lr * e * xi; q.b += q.lr * e; errs += 1
print("Misclassified in last epoch:", errs, "-> XOR is not linearly separable")
