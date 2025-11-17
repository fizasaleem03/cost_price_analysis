import os
import pandas as pd

# Get the script directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to history.csv
history_file = os.path.join(base_dir, 'history.csv')
history = pd.read_csv(history_file)

