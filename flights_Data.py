#!/usr/bin/env python3

import pandas as pd
import numpy as np

flights_df = pd.read_csv(r"2007.csv", delimiter = ',')

delay = flights_df.groupby('Dest').count().reset_index().loc[:,('Dest','Year')].head(3)

delay. to_csv (r'data.csv', index=False)


