import numpy as np
import os
import sys

sys.path.append('../')

from agent import Agent

class Environment:
    
    def __init__(self, init_state):
        self.old_state = init_state
        self.current_state = 0
        
    def generate_agents(self, num_agent):
        agents = [Agent() for agent_id in range(num_agent)]
    
        return agents
        
    def step(self, agents):
        
        n_stay = 0
        n_buy = 0
        n_sell = 0
        total_demand = 0
        for i, agent in enumerate(agents):
            
            action = agent.random_act()
            
            if action == 0:
                n_stay += 1
            elif action == 1:
                n_buy += 1
            else:
                n_sell += 1
            
        current_state = n_buy - n_sell

        return current_state
            
                
            
            
            
    