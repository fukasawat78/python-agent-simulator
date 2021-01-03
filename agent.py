import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim

device = "cuda" if torch.cuda.is_available() else "cpu"

class Agent:
    def __init__(self):
        self.action_size = 3 # stay, buy, sell
        self.prev_action = 0
        self.action = 0
        #self.policy = policy
        
        #self.gamma = 0.95
        #self.epsion = 1.0
        #self.epsilon_min = 0.01
        #self.epsilon_decay = 0.995
        #self.batch_size = 32
        
    def random_act(self):
        return random.randrange(self.action_size)

