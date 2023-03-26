import pandas as pd
import numpy as np

open("vocabulary.md", mode='w').close()

df = pd.read_excel('Vocabulary.xlsx')
df = df.apply(lambda x: x.str.replace('\n', '<br>') if x.dtype == 'object' else x)
df = df.dropna(how='all')
df = df.reset_index(drop=True)
md_table = df.to_markdown(index=False)
#print(md_table)

f = open("vocabulary.md", "a")
f.write(md_table)
f.close()

