import torch
import torch.nn as nn
import torchvision.models as models

res50_model = models.resnet50(pretrained=True)

class ResNet50Features(nn.Module):
  def __init__(self):
    super(ResNet50Features, self).__init__()
    self.features = nn.Sequential(*list(res50_model.children())[:-2])

  def forward(self, x):
    x = self.features(x)
    return x