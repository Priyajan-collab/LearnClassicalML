import numpy as np
import matplotlib as mt
import pandas as pd

data= pd.read_csv("../resource/archive/spotify_tracks.csv")
data=pd.DataFrame(data)
if data is not None:
    print(data.loc[[0,1]]);
else:
    print("failed to laod the data")

print("hello")