import torch

model_path = "../data/trained/pretrained_malconv.pth"
model = torch.load(model_path)
model.eval()