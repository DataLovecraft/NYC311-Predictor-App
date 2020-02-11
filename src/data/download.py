#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", None)

results = client.get("erm2-nwe9", limit=2000)

results_df = pd.DataFrame.from_records(results)
