#!/usr/bin/env python
# coding: utf-8
# %%
import pandas as pd
import pathlib
from jinja2 import Template
import sys

df = pd.read_csv('batteries.csv')
print(df)
print(df['Name'])
print(df['ID'])
print(df['DOB'])
data = df
obs = len(df.index)


# %%
# vars: {{ID}}, {{Name}}, {{DOB}}
def genfsh(file, obs):
    for row in df.itertuples():
        Name = str(row.Name)
        ID = str(row.ID)
        DOB = str(row.DOB)
        suffix = 'bulk-' + str(row.ID)
        print(suffix, Name, ID, DOB)

        # put through jinja2
        path = pathlib.Path(file)
        text = path.read_text()
        t = Template(text)
        msg = t.render(
            ID=ID,
            Name=Name,
            DOB=DOB,
        )
        path_out = pathlib.Path(f"output/{suffix}.fsh")
        path_out.write_text(msg)

genfsh('template.fsh', obs)

# %%
