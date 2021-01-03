import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ts_plot(data):
    
    df_data = pd.Series(data)
    df_data.columns = ["Market Demand Results"]
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(df_data)
    
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.hist(df_data)

    plt.tight_layout()
    plt.show()