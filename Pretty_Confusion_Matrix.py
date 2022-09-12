#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pretty-confusion-matrix


# In[1]:


import pandas as pd
import numpy as np
from pretty_confusion_matrix import pp_matrix
import matplotlib.pyplot as plt


# In[4]:


array = np.array([[341755,    340,       791,    455,         4065,          4579,    5776,      111,    370],
                  [   146,   2141,         0,      0,            0,             1,       0,        0,      0],
                  [    69,      0,       200,      0,            0,             0,       0,        0,      0],
                  [  1916,      1,         0,   2965,            0,             4,       0,        0,     16],
                  [   625,      0,         0,      3,          895,           409,     311,        0,      0],
                  [   103,      1,         0,     16,            1,         28364,      40,       18,      2],
                  [     7,      0,         0,      0,          282,           133,    4633,        0,      0],
                  [   393,      0,         0,      3,            0,             0,       0,      235,      1],
                  [   934,      1,         0,    268,            0,             8,       0,        6,     36]])

# get pandas dataframe
labels = ["pred","entity_1", "entity_2", "entity_3", "entity_4", "entity_5","entity_6", "entity_7", "entity_8"]
pred = ["true","entity_1", "entity_2", "entity_3", "entity_4", "entity_5","entity_6", "entity_7", "entity_8"]

df_cm = pd.DataFrame(array, index=labels, columns=pred)

cmap = 'gist_yarg_r'
# plt.figure(figsize=(102, 12))

pp_matrix(df_cm, cmap=cmap, figsize=(10, 10))


# In[6]:


array = np.array([[356856,        17 ,        3,         159,         182,        426,        386,        10,         203],
                  [  911  ,       1377,       0 ,        0   ,        0   ,       0   ,       0   ,       0  ,        0   ],
                  [  107   ,      0    ,      116,       0    ,       0    ,      0    ,      0    ,      0   ,       0    ],
                  [ 1924    ,     0     ,     0   ,      2866  ,      0     ,     0     ,     0     ,     3     ,     9     ],
                  [ 1289     ,    0      ,    0    ,     0      ,     654    ,    131    ,    366    ,    1      ,    0      ],
                  [ 4693      ,   3       ,   0     ,    19      ,    7       ,   23784   ,   31      ,   3       ,   5       ],
                  [ 1530       ,  0        ,  0      ,   0        ,   27       ,  59       ,  3439     ,  0        ,  0        ],
                  [  586        , 0         , 0        , 0         ,  0         , 0         , 0         , 46        , 0         ],
                  [  966         ,0          ,0         ,3           ,0          ,0          ,0          ,0          ,14         ]])

# get pandas dataframe
labels = ["pred","entity_1", "entity_2", "entity_3", "entity_4", "entity_5","entity_6", "entity_7", "entity_8"]
pred = ["true","entity_1", "entity_2", "entity_3", "entity_4", "entity_5","entity_6", "entity_7", "entity_8"]

df_cm = pd.DataFrame(array, index=labels, columns=pred)

cmap = 'gist_yarg_r'
# plt.figure(figsize=(102, 12))

pp_matrix(df_cm, cmap=cmap, figsize=(10, 10))


# In[ ]:




