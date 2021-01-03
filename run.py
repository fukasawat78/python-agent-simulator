import argparse
import random
import numpy as np
import pandas as pd
from envs import *
from agent import *
from visualize import *

def main():
    parser = argparse.ArgumentParser(description='Multi Agent Simulation')
    parser.add_argument('--num-agent', type=int, default=100, metavar='N',
                        help='input number of agent')
    parser.add_argument('--max-season', type=int, default=50, metavar='N',
                        help='input number of season')

    args = parser.parse_args()
    
    init_state = np.random.randint(0, args.num_agent)
    
    # 環境
    env = Environment(init_state)
    
    # エージェント
    agents = env.generate_agents(args.num_agent)
    
    hist_current_state = []
    for season in range(1, args.max_season+1):
        
        current_state = env.step(agents)
        
        hist_current_state.append(current_state)
        
    # 可視化
    ts_plot(hist_current_state)
    
    
if __name__=="__main__":
    main()
    