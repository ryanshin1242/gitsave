import pandas as pd
import numpy as np

data = {
    "이름": ["철수", "영희", "민수"],
    "나이": [20, 21, 19],
    "성별": ["남", "여", "남"]
}

df = pd.DataFrame(data)
print(df)
