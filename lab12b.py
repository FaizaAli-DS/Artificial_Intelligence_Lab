import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.1307,), (0.3081,))])
train_set = datasets.MNIST('data', train=True, download=True, transform=transform)
test_set  = datasets.MNIST('data', train=False, download=True, transform=transform)
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
test_loader  = DataLoader(test_set, batch_size=1000)

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),                 # 28x28 image -> 784 vector
            nn.Linear(784, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 10))           # 10 digit classes
    def forward(self, x):
        return self.net(x)

model = MLP()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(1, 6):
    model.train(); total = 0
    for images, labels in train_loader:
        optimizer.zero_grad()
        loss = loss_fn(model(images), labels)   # forward pass
        loss.backward()                         # backpropagation
        optimizer.step()                        # update weights
        total += loss.item()
    model.eval(); correct = 0
    with torch.no_grad():
        for images, labels in test_loader:
            correct += (model(images).argmax(1) == labels).sum().item()
    print(f"Epoch {epoch}: train loss = {total/len(train_loader):.4f}, "
          f"test accuracy = {100*correct/len(test_set):.2f}%")
