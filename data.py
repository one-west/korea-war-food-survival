import pandas as pd

file_path = "./농림축산식품부_양곡자급률_20231231.csv"

df = pd.read_csv(file_path, encoding="cp949")

# 가장 최신 연도 데이터 확인 (최근 연도 기준)
latest_year_data = df.sort_values(by="연도", ascending=False).iloc[0]

# 필요한 품목별 자급률 추출
latest_year = latest_year_data["연도"]
self_sufficiency_rates = {
    "쌀": latest_year_data["쌀"],
    "밀": latest_year_data["밀"],
    "콩": latest_year_data["콩"],
    "옥수수": latest_year_data["옥수수"],
}

# 출처: 통계청 KOSIS 25.05.22 기준

## 인구 수
population = 51684564

## 1인당 하루 소비량 (kg)
daily_consumption_per_person = {"쌀": 0.2, "밀": 0.15, "콩": 0.05, "옥수수": 0.3}

## 연간 총 소비량 (만 톤 기준, FAO 등 참조)
annual_consumption = {"쌀": 370, "밀": 444, "콩": 130, "옥수수": 1000}

# 정부 비축량 (만 톤 기준, 보도자료 등 기반 추정)
stockpile = {"쌀": 45, "밀": 10, "콩": 5, "옥수수": 10}

# 생존 가능 일수 계산
survival_days = {}

for grain in daily_consumption_per_person:
    daily_total_need_ton = (
        population * daily_consumption_per_person[grain] / 1000
    )  # 톤 단위
    available_ton = (
        annual_consumption[grain] * (self_sufficiency_rates[grain] / 100)
    ) + stockpile[grain]
    survival_days[grain] = int(
        (available_ton * 10000) / daily_total_need_ton
    )  # 만 톤 → 톤

# 전시 상황에서는 식량 절감을 고려하여 소비량 30% 감축
reduced_consumption = {k: v * 0.7 for k, v in daily_consumption_per_person.items()}

# 생존 가능 일수 재계산
reduced_survival_days = {}

for grain in reduced_consumption:
    daily_total_need_ton = population * reduced_consumption[grain] / 1000  # 톤 단위
    available_ton = (
        annual_consumption[grain] * (self_sufficiency_rates[grain] / 100)
    ) + stockpile[grain]
    reduced_survival_days[grain] = int(
        (available_ton * 10000) / daily_total_need_ton
    )  # 만 톤 → 톤
