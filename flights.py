#!/usr/bin/env python3


import numpy as np
import pandas as pd

flightdelays_df = pd.read_csv(r"2007.csv")

delay = flightdelays_df[flightdelays_df["Origin"]=="SFO"].iloc[[0,1,2]].loc[:,('ArrDelay','Origin')]

delay. to_csv(r'delays.csv', index=False)

print("Soniya")
