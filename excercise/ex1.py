import pandas as pd

data = {
    "이름": ["지훈", "예은", "민지", "하늘", "서준", "유리"],
    "수학": [80, 92, 88, 77, 95, 85],
    "국어": [75, 90, 85, 80, 95, 89]
}
df = pd.DataFrame(data)

filtered = df[df["국어"] >=85 ]
sorted_df = filtered.sort_values(["국어","수학"],ascending=[False,True])
print(sorted_df)


df.to_csv("학생점수.csv", index=False, encoding="utf-8-sig")

df2 = pd.read_csv("학생점수.csv")
print(df2)