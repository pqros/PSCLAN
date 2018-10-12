import pandas as pd
import numpy as np
import warnings
import re

target_type = np.float64
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter("always")
    my_data = pd.read_csv("Wednesday-workingHours.pcap_ISCX.csv")
    for w in ws:
        s = str(w.message)
        print("Warning message:", s)
        match = re.search(r"Columns \(([0-9,]+)\) have mixed types\.", s)
        if match:
            columns = match.group(1).split(',')
            columns = [int(c) for c in columns]
            print("Applying %s dtype to columns:" % target_type, columns)
            my_data.iloc[:, columns] = my_data.iloc[:, columns].astype(target_type)
    my_data.iloc[0:99, 0:4].to_csv("data_sample.csv", sep='\t', encoding='utf-8')
    my_data.dtypes.to_json("dtypes.json")
    print("Finished.")
