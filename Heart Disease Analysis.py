#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Import The Libraries And Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[35]:


data = pd.read_csv('Data.csv')


# In[36]:


#Display Top 5 Rows of The Dataset
data.head ()


# In[37]:


#Display last 5 rows of the dataset
data.tail()


# In[38]:


#Number of rows and columns in the dataset
data.shape


# In[39]:


#getting some info about the data
data.info()


# Data Cleaning

# In[40]:


#checking for missing values
data.isnull().sum()


# In[41]:


#Check for duplicate data and drop them
data_dup = data.duplicated().any ()
print (data_dup)


# In[42]:


data = data.drop_duplicates() 
data.shape


# In[44]:


#Statistical measures about the data (count,mean,SD etc.)
data.describe()


# In[48]:


#Draw correlation Matrix
plt.figure(figsize=(12,5))
sns.heatmap(data.corr(),annot=True)


# In[49]:


data.columns


# Data Visualization

# In[53]:


#checking the distribution of target variable  
data['target'].value_counts()


# In[58]:


sns.countplot(x='target', data=data)
plt.show()


# In[59]:


#Find count of Male and Female in the dataset
data['sex'].value_counts()


# In[60]:


sns.countplot(x='sex', data=data)
plt.xticks ([0,1], ['Female', 'Male'])        
plt.show()


# In[61]:


#Gender distribution according to target variable
sns.countplot(x='sex', hue="target", data=data)
plt.xticks ([0,1], ['Female','Male'])
plt.legend(labels=['No-Disease','Disease'])
plt.show()


# In[63]:


#Check Age Distribution In The Dataset
sns.distplot(data['age'],bins=20)
plt.show()


# Check Chest Pain Type
# 
# • Chest pain type (4 values)
# 
# ■ Value 0: typical angina
# 
# ■ Value 1: atypical angina
# 
# ■ Value 2: non-anginal pain
# 
# ■ Value 3: asymptomatic

# In[65]:


sns.countplot(x='cp', data=data)
plt.xticks ([0,1,2,3], ["typical angina", "atypical angina", "non-anginal pain","asymptomatic"])
plt.xticks (rotation=75)
plt.show()


# In[66]:


#Chest pain distribution as per target variable
sns.countplot (x="cp", hue="target", data=data)
plt.legend (labels=["No-Disease", "Disease"])
plt.show()


# In[67]:


#Check resting blood pressure distribution
data['trestbps'].hist()


# In[68]:


#Compare Resting Blood Pressure As Per Sex Column
g=sns.FacetGrid(data, hue="sex", aspect=4)
g.map(sns.kdeplot, 'trestbps', shade=True)
plt.legend (labels=['Male', 'Female'])


# In[69]:


#Checking distribution of serum cholesterol
data['chol'].hist()


# In[70]:


#Plot continuous variables
cate_val=[]
cont_val=[]
for column in data.columns: 
    if data [column].nunique() <=10: 
        cate_val.append(column) 
    else:
        cont_val.append(column) 


# In[71]:


cate_val


# In[72]:


cont_val


# In[74]:


data.hist(cont_val,figsize=(12,5))
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




