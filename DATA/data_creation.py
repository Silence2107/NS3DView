import pandas as pd

import numpy as np

M=np.linspace(1,2,100)
R=np.linspace(10,14,100)

pd.DataFrame([M,R],index=['M','R']).T.to_csv("./data.csv")