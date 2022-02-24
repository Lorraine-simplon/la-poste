#%%
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("train.csv")
# %%
data.info()
# %%
img1=data.iloc[3,1:]
# %%
img1.shape
# %%
img1
# %%
img1=img1.to_numpy()
# %%
img1
# %%
img2d= np.reshape(img1,(28,28))

# %%
img2d
# %%
plt.imshow(img2d, interpolation='nearest', cmap='gray')
