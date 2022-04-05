# Imports libraries, packages and modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

from scipy import stats

from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import cross_val_score, train_test_split, cross_validate, cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Sets visualization style
sns.set()
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 14

# Imports data
track_features_df = pd.read_csv('../data/raw/track_features/tf_mini.csv')
session_logs_df = pd.read_csv('../data/raw/training_set/log_mini.csv')

# Checks to see dataframes available in the global space
print("Dataframes in the global name space now include:")
for name in dir():
    if name.endswith('df'):
        print(name)

