import time
import torch
import torch.nn as nn
import torch.optim as optim
import tqdm

def train(model, train_loader, val_loader, criterion, optimizer, scheduler, device, num_epochs, checkpoint_path):
    # Training loop implementation
    best_val_loss = float('inf')

    for epoch in range(num_epochs):
        start_time = time.time()
        train_loss = 0.0
        val_loss = 0.0

        # Training
        model.train()
        for images, labels in tqdm.tqdm(train_loader, desc=f"Epoch {epoch + 1}/{num_epochs} - Training"):
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            train_loss += loss.item() * images.size(0)

        # Validation
        model.eval()
        with torch.no_grad():
            for images, labels in tqdm.tqdm(val_loader, desc=f"Epoch {epoch + 1}/{num_epochs} - Validation"):
                images = images.to(device)
                labels = labels.to(device)

                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item() * images.size(0)

        # Calculate average losses
        train_loss /= len(train_loader.dataset)
        val_loss /= len(val_loader.dataset)

        # Print epoch statistics
        elapsed_time = time.time() - start_time
        print(f"Epoch {epoch + 1}/{num_epochs} - Training Loss: {train_loss:.4f} - Validation Loss: {val_loss:.4f} - Time: {elapsed_time:.2f}s")

        # Save the best model
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), checkpoint_path)

        # Adjust the learning rate
        scheduler.step(val_loss)

def evaluate(model, data_loader, criterion, device):
    # Evaluation function implementation
    model.eval()
    total_loss = 0.0
    correct_predictions = 0

    with torch.no_grad():
        for images, labels in tqdm.tqdm(data_loader, desc="Evaluation"):
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)
            total_loss += loss.item() * images.size(0)

            _, predicted = torch.max(outputs, 1)
            correct_predictions += (predicted == labels).sum().item()

    # Calculate average loss and accuracy
    average_loss = total_loss / len(data_loader.dataset)
    accuracy = correct_predictions / len(data_loader.dataset)

    print(f"Evaluation - Loss: {average_loss:.4f} - Accuracy: {accuracy * 100:.2f}%")

    return average_loss, accuracy
