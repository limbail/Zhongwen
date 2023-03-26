import pandas as pd
import numpy as np

open("vocabulary.md", mode='w').close()

style="""
<style>
table th:first-of-type {
    width: 5%;
}
table th:nth-of-type(2) {
    width: 5%;
}
table th:nth-of-type(3) {
    width: 5%;
}
table th:nth-of-type(4) {
    width: 5%;
}
table th:nth-of-type(5) {
    width: 30%;
}
table th:nth-of-type(6) {
    width: 20%;
}
table th:nth-of-type(7) {
    width: 30%;
}
</style>
"""

df = pd.read_excel('Vocabulary.xlsx')
df = df.apply(lambda x: x.str.replace('\n', '<br>') if x.dtype == 'object' else x)
df.dropna(how='all')
md_table = df.to_markdown(index=False)
#print(md_table)
t_content=df.to_markdown()
f = open("vocabulary.md", "a")
f.write(style)
f.write(t_content)
f.close()

