import pandas as pd
import numpy as np
import sklearn
import pickle

# If the import statement doesn't produce an error, pickle is installed.
print("pickle is installed.")


# Check Pandas version
print(f'Pandas version: {pd.__version__}')

# Check NumPy version
print(f'NumPy version: {np.__version__}')

# Check scikit-learn version
print(f'scikit-learn version: {sklearn.__version__}')
