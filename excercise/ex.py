import pandas as pd

data = {
    "이름": ["지훈", "예은", "민지", "하늘", "서준", "유리"],
    "수학": [80, 92, 88, 77, 95, 85],
    "국어": [75, 90, 85, 80, 95, 89],
    "반": [1, 1, 2, 2, 1, 2]
}
df = pd.DataFrame(data)

# 반별 수학과 국어 평균, 최대값 계산
result = df.groupby("반")[["수학", "국어"]].agg(["mean", "max"])
print(result)
