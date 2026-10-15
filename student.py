import streamlit as st
import pandas as pd

# 1. 웹 앱 제목 설정하기
st.title("📚 공부 습관 대시보드")

# 2. 데이터 불러오기 (study.csv 파일 읽기)
df = pd.read_csv("study.csv")

# 3. 요약 지표를 한 줄에 보여주기 위해 3개의 칸(컬럼)으로 나누기
col1, col2, col3 = st.columns(3)

# 첫 번째 칸: 전체 학생 수 계산 및 표시
with col1:
    total_students = len(df)
    st.metric(label="전체 학생 수", value=f"{total_students}명")

# 두 번째 칸: 평균 점수 계산 및 표시 (소수점 1자리까지)
with col2:
    avg_score = round(df['점수'].mean(), 1)
    st.metric(label="평균 점수", value=f"{avg_score}점")

# 세 번째 칸: 평균 공부시간 계산 및 표시 (소수점 1자리까지)
with col3:
    avg_study_time = round(df['공부시간'].mean(), 1)
    st.metric(label="평균 공부시간", value=f"{avg_study_time}시간")

st.divider() # 화면에 구분선 긋기

# 4. 슬라이더를 이용해 최소 공부시간 선택받기
# 최소값, 최대값, 기본값을 데이터에 맞게 설정합니다.
min_study = st.slider(
    "최소 공부시간을 선택하세요 (시간)", 
    min_value=float(df['공부시간'].min()), 
    max_value=float(df['공부시간'].max()), 
    value=float(df['공부시간'].min())
)

# 5. 슬라이더에서 선택한 시간 이상 공부한 학생들만 걸러내기(필터링)
filtered_df = df[df['공부시간'] >= min_study]

st.subheader(f"✅ {min_study}시간 이상 공부한 학생 데이터")

# 6. 산점도 그리기 (공부시간과 점수의 관계 파악)
st.write("📌 공부시간에 따른 점수 분포 (산점도)")
st.scatter_chart(data=filtered_df, x="공부시간", y="점수")

# 7. 막대 그래프 그리기 (학생별 점수 비교)
st.write("📌 학생별 점수 (막대 그래프)")
st.bar_chart(data=filtered_df, x="학생ID", y="점수")
