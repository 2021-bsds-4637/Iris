#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
# read_csv() # use to load or import csv file 
file=pd.read_csv("file:///C:\\Users\\Hp\\Downloads\Iris.csv")
print(file) 
import matplotlib.pyplot as plt


# In[9]:


file["Species"].value_counts()


# In[15]:


# Create a scatter plot of sepal length versus sepal width
file.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm')
plt.show()


# In[16]:


# Create a histogram of petal length
file['PetalLengthCm'].plot(kind='hist', bins=20)
plt.show()


# In[26]:


# Group the file by species
grouped = file.groupby('Species')

# Plot the different features for each species using subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

for i, feature in enumerate(['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']):
    row = i // 2
    col = i % 2
    ax = axes[row, col]
    for species, group in grouped:
        ax.scatter(group.index, group[feature], label=species)
    ax.set_xlabel('Sample Index')
    ax.set_ylabel(feature)
    ax.legend()

# Display the plots
plt.tight_layout()
plt.show()


# In[21]:


# Create a bar chart of the number of flowers in each species
species_count = file["Species"].value_counts()
plt.bar(species_count.index, species_count.values)
plt.xlabel("Species")
plt.ylabel("Number of Flowers")
plt.title("Number of Flowers per Species")

# Display the plot
plt.show()


# In[23]:


# Create a line plot of petal width over time (assuming the data is sorted by time)
plt.plot(file["PetalWidthCm"])
plt.xlabel("Time")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Width over Time")

# Display the plot
plt.show()


# In[ ]:




