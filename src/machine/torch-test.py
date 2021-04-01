# -*- encoding: utf-8 -*-

import torch

print(torch.__version__)

import torchvision.datasets as datasets
import torchvision.transforms as transforms

train = datasets.MNIST(root='~/datasets-ai', train=True, download=True, transform=transforms.ToTensor())

print(train)
