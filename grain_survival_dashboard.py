import streamlit as st
import matplotlib.pyplot as plt
from data import reduced_survival_days, survival_days

# 기본 데이터
survival_days_normal = survival_days  # 평시
survival_days_wartime = reduced_survival_days  # 전시 (30% 절감)

# 한글 폰트 설정
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 타이틀 및 소개
st.title("🇰🇷 한반도 전면전 발생 시 곡물 생존 가능 일수 분석")

st.markdown("""
### 📘 프로젝트 개요
이 분석은 한반도에서 전면전이 발생했을 경우, 주요 곡물 자급률과 정부 비축량만으로 **국민이 얼마나 생존할 수 있는지를 시뮬레이션**합니다.

- 📅 기준 연도: **2022년**
- 📊 출처: 농림축산식품부, KOSIS, FAO
- 🎯 분석 대상: 쌀, 밀, 콩, 옥수수
""")

st.markdown("---")

# 수평 이중 막대 그래프
def plot_combined_bar(normal, wartime):
    labels = list(normal.keys())
    x = range(len(labels))

    normal_values = list(normal.values())
    wartime_values = list(wartime.values())

    bar_height = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh([i + bar_height for i in x], normal_values, height=bar_height, label="평시", color="skyblue")
    ax.barh(x, wartime_values, height=bar_height, label="전시", color="salmon")

    ax.set_xlabel("생존 가능 일수 (일)")
    ax.set_yticks([i + bar_height / 2 for i in x])
    ax.set_yticklabels(labels)
    ax.set_title("✅ 곡물별 생존 가능 일수 비교")
    ax.legend()
    ax.grid(True, axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)

# 원형 그래프 비교
def plot_pie_comparison(normal, wartime):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].pie(normal.values(), labels=normal.keys(), autopct="%1.1f%%", startangle=140)
    axes[0].set_title("🌾 평시 기준 비중")

    axes[1].pie(wartime.values(), labels=wartime.keys(), autopct="%1.1f%%", startangle=140)
    axes[1].set_title("⚠️ 전시 기준 비중")

    plt.suptitle("📊 곡물별 비중 비교 (Pie Chart)")
    plt.tight_layout()
    st.pyplot(fig)

# ------------------------
# 시각화 영역
# ------------------------

st.subheader("📊 곡물 생존 가능 일수 비교 (막대 그래프)")
plot_combined_bar(survival_days_normal, survival_days_wartime)

st.subheader("🥧 곡물별 비중 비교 (원형 그래프)")
plot_pie_comparison(survival_days_normal, survival_days_wartime)

st.markdown("---")
st.markdown("""
### 📌 분석 요약
- ✅ **쌀은 1년 이상 생존 가능** (자급률 100% 이상 + 비축량)
- ⚠️ **옥수수, 밀은 수입 의존 심각** → 1달 내 고갈
- 🔄 전시 상황에서는 **소비량 절감 시 최대 생존일 증가**

### 📂 데이터 출처
- 농림축산식품부 자급률 통계 (2022)
- 통계청 KOSIS
- FAO Food Balance Sheet
""")
