import numpy as np
from abc import ABCMeta, abstractmethod

class Policy(metaclass=ABCMeta):

    @abstractmethod
    def select_action(self, **kwargs):
        pass

class Imitation(Policy):
    """Determine next_strategy of all agents for the next season"""

    kappa = 0.1  # Thermal coefficient
    next_strategies = [agent.strategy for agent in agents]

    # Randomely select one neighboring agent as opponent and determine whether or not copying his strategy
    for i, focal in enumerate(agents):
        opponent_id = rnd.choice(focal.neighbors_id)
        opponent = agents[opponent_id]
        if opponent.strategy != focal.strategy and rnd.random() <= 1/(1+np.exp((focal.point-opponent.point)/kappa)):
            next_strategies[i] = opponent.strategy
        else:
            pass

    # Update strategy
    for agent, next_strategy in zip(agents, next_strategies):
        agent.strategy = next_strategy
    
    
