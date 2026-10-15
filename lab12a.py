import numpy as np

np.random.seed(1)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])               # XOR

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Network: 2 inputs -> 4 hidden neurons -> 1 output
W1 = np.random.randn(2, 4); b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1); b2 = np.zeros((1, 1))
lr = 0.5

for epoch in range(1, 10001):
    # ----- Forward pass -----
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    loss = np.mean((y - out) ** 2)
    # ----- Backward pass (chain rule) -----
    d_out = (out - y) * out * (1 - out)          # dL/dz2
    d_h = (d_out @ W2.T) * h * (1 - h)           # dL/dz1
    # ----- Gradient descent update -----
    W2 -= lr * h.T @ d_out;  b2 -= lr * d_out.sum(axis=0, keepdims=True)
    W1 -= lr * X.T @ d_h;    b1 -= lr * d_h.sum(axis=0, keepdims=True)
    if epoch % 2000 == 0:
        print(f"Epoch {epoch:5d}  MSE loss = {loss:.5f}")

print("\nXOR predictions after training:")
for xi, o in zip(X, out):
    print(f"  {xi} -> {o[0]:.3f} -> class {int(o[0] > 0.5)}")
