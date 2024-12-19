import pandas as pd

import numpy as np

x=np.linspace(0,1,100)

y=np.cos(x)

pd.DataFrame([x,y],index=['x','y']).T.to_csv("data/data.csv")