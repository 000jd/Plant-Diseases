import torch
from torchvision import transforms
from model import QuantizablePlantDiseasesNet
from utils import classes

def predict_diseases(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])

    image = transform(image).unsqueeze(0)

    model = QuantizablePlantDiseasesNet(num_classes=38)
    model.load_state_dict(torch.load('PlantDiseases_quantized_checkpoint.pth', map_location=torch.device('cpu')))
    model.eval()

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)

    plant_name = classes.class_names[predicted.item()]
    return plant_name