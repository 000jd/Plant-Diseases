import os
import time
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from utils.dataset import load_dataset
from models.model import PlantDiseasesNet
from utils.training import train, evaluate

data_path = 'data//New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)'
batch_size = 128
num_classes = 38
learning_rate = 0.001
checkpoint_path = 'PlantDiseases_checkpoint.pth'

train_loader, val_loader = load_dataset(data_path, batch_size)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = PlantDiseasesNet(num_classes)
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=0.1, patience=5)

start_epoch = 0
best_val_loss = float('inf')