import torch
import torch.nn

class Nets(nn.Module):
	def __init__(self):
		self.layers=nn.Sequential(
				nn.Linea(10,20),
				nn.Linea(20,30).
				nn.Linear(30,10)
				)
	def forward(self,x):
		return self.layers(x)

