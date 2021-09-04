#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


# In[2]:


data = pd.read_csv('Decision_Tree_ Dataset.csv')


# In[3]:


data.head()


# In[4]:


X=data.values[:,0:4]
X


# In[5]:


Y=data.values[:,5]
Y


# In[6]:


from sklearn.model_selection import train_test_split


# In[7]:


from sklearn.tree import DecisionTreeClassifier


# In[8]:


#X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)


# In[9]:


X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[10]:


from sklearn.tree import DecisionTreeClassifier


# In[11]:


clf=DecisionTreeClassifier(criterion="entropy",random_state=101)


# In[12]:


clf.fit(X_train, y_train);


# In[13]:


y_predict=clf.predict(X_test)


# In[14]:


y_predict


# In[15]:


from sklearn.metrics import classification_report


# In[16]:


print(classification_report(y_test,y_predict))


# In[17]:


from sklearn.metrics import confusion_matrix


# In[18]:


print(confusion_matrix(y_test,y_predict))


# In[19]:


from sklearn.metrics import accuracy_score


# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
cm=confusion_matrix(y_test,y_predict)
plt.figure(figsize = (6,4))
sns.heatmap(cm, annot=True, fmt=".0f")
plt.xlabel('y_test')
plt.ylabel('Truth')


# In[21]:


accuracy_score(y_test,y_predict)


# In[22]:


from sklearn.ensemble import RandomForestClassifier


# In[29]:


rfc=RandomForestClassifier(n_estimators=200);


# In[30]:


rfc.fit(X_train,y_train);


# In[31]:


predictions=rfc.predict(X_test)


# In[32]:


from sklearn.metrics import classification_report, confusion_matrix


# In[33]:


print(classification_report(y_test,predictions))


# In[28]:


print(confusion_matrix(y_test,predictions))


# # Exercise: Handwritten Digit Classification

# In[34]:


import numpy as np


# In[35]:


import pandas as pd


# In[36]:


from sklearn.datasets import load_digits


# In[39]:


import matplotlib.pyplot as plt


# In[40]:


import seaborn as sns


# In[42]:


digits=load_digits()


# In[43]:


digits


# In[44]:


digits.keys()


# In[45]:


print(digits.DESCR)


# In[46]:


digits.data.shape


# In[47]:


digits.data[0]


# In[48]:


digits.keys()


# In[49]:


digits.target.shape


# In[50]:


digits.target


# In[51]:


digits.target[0:20]


# In[52]:


digits.target_names.shape


# In[53]:


digits.target_names


# In[55]:


digits.images.shape


# In[58]:


digits.images[0]


# In[63]:


import pylab as pl
pl.gray()


# In[62]:


plt.matshow(digits.images[0]);


# In[64]:


digits.data[0]


# In[65]:


digits.target[0]


# In[66]:


for i in range(5):
    pl.matshow(digits.images[i])


# In[68]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)


# In[69]:


X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[71]:


clf=DecisionTreeClassifier(criterion='entropy', random_state=42);
clf.fit(X_train, y_train);


# In[72]:


y_pred_en=clf.predict(X_test)
y_pred_en


# In[73]:


accuracy_score(y_test,y_pred_en)


# In[76]:


from sklearn.metrics import classification_report, confusion_matrix


# In[77]:


print(classification_report(y_test,y_pred_en))


# In[78]:


print(confusion_matrix(y_test,y_pred_en))


# In[79]:


rfc=RandomForestClassifier();


# In[80]:


rfc.fit(X_train, y_train);


# In[81]:


predictions=rfc.predict(X_test)
predictions


# In[83]:


accuracy_score(y_test,predictions)


# In[84]:


print(classification_report(y_test,predictions))


# In[85]:


print(confusion_matrix(y_test,predictions))


# In[ ]:




