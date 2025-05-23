import streamlit as st
import matplotlib.pyplot as plt
from data import reduced_survival_days, survival_days

# 기본 데이터 (정상 문자열로 수정)
survival_days_normal = reduced_survival_days
survival_days_wartime = survival_days

st.title("한반도 전면전 발생 시 곡물 생존 가능 일수 분석")

st.markdown(
    """
이 대시보드는 2022년 농림축산식품부 자급률 통계를 기반으로, 무역이 완전히 차단된 전면전 상황에서 
한국이 각 곡물로 며칠이나 버틸 수 있는지를 계산한 결과입니다.

- **평시 소비량 기준**: 일반적인 1인당 소비량 기준 (FAO/KOSIS)
- **전시 소비량 기준**: 소비량 30% 감축 가정
"""
)


# 그래프 표시 함수
def plot_bar(data, title):
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values(), color="skyblue")
    ax.set_ylabel("생존 가능 일수 (일)")
    ax.set_title(title)
    st.pyplot(fig)


# 두 개의 컬럼으로 시각화
col1, col2 = st.columns(2)

with col1:
    st.subheader("평시 소비량 기준")
    plot_bar(survival_days_normal, "평시 기준 생존 가능 일수")

with col2:
    st.subheader("전시 소비량 기준")
    plot_bar(survival_days_wartime, "전시 기준 생존 가능 일수")

st.markdown("---")
st.markdown("데이터 출처: 농림축산식품부 자급률 통계, KOSIS, FAO")
