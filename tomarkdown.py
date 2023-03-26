import pandas as pd
import numpy as np

df = pd.read_excel('Vocabulary.xlsx')
df = df.apply(lambda x: x.str.replace('\n', '<br>') if x.dtype == 'object' else x)
df.dropna(how='all')
md_table = df.to_markdown(index=False)
#print(md_table)
t_content=df.to_markdown()
f = open("vocabulary.md", "a")
f.write(t_content)
f.close()

