# 📊 공부 습관 대시보드 (Study Habits Dashboard)

안녕하세요! 이 프로젝트는 파이썬(Python)과 웹 프레임워크를 처음 다뤄보는 분들을 위해 만들어진 **간단한 데이터 분석 대시보드**입니다.
`streamlit`과 `pandas` 라이브러리를 사용하여 학생들의 공부 습관 데이터(`study.csv`)를 분석하고 웹 화면에 예쁘게 시각화합니다.

## 🚀 주요 기능
* **핵심 지표 요약**: 전체 학생 수, 평균 점수, 평균 공부시간을 상단에 한눈에 보여줍니다.
* **데이터 필터링**: 슬라이더를 움직여 원하는 '최소 공부시간' 이상의 학생 데이터만 걸러서 볼 수 있습니다.
* **시각화 (그래프)**: 
    * 공부시간과 점수의 관계를 보여주는 **산점도**
    * 필터링된 학생별 점수를 비교하는 **막대 그래프**

## 🛠️ 준비물 (설치 방법)
이 앱을 실행하려면 파이썬이 설치되어 있어야 하며, 외부 라이브러리 두 가지가 필요합니다.
터미널(Windows의 경우 명령 프롬프트나 PowerShell, Mac은 터미널)을 열고 아래 명령어를 입력해 주세요.

```bash
pip install streamlit pandas
```

## 📂 프로젝트 구조
프로젝트 폴더 안에는 다음 두 파일이 같은 위치에 있어야 합니다:
* `app.py` : 대시보드를 실행하는 파이썬 코드 파일 (이름은 자유롭게 지어도 됩니다)
* `study.csv` : 학생 데이터가 들어있는 데이터 파일 (열: 학생ID, 공부시간, 스마트폰, 점수)

## ▶️ 실행 방법
터미널에서 `app.py`가 있는 폴더로 이동한 후, 다음 명령어를 입력하세요:

```bash
streamlit run app.py
```
명령어를 입력하면 인터넷 브라우저 창이 새로 열리면서 대시보드 웹 앱이 나타납니다! 🎉

## 📝 전체 코드 (`app.py`)
```python
import streamlit as st
import pandas as pd

# 1. 앱의 제목을 설정합니다.
st.title('공부 습관 대시보드')

# 2. pandas를 이용해 study.csv 파일을 읽어옵니다.
df = pd.read_csv('study.csv')

# 3. 전체 학생 수, 평균 점수, 평균 공부시간을 계산합니다.
total_students = len(df)
avg_score = df['점수'].mean()
avg_study_time = df['공부시간'].mean()

# 4. 화면을 3개의 열(칸)로 나누어 핵심 지표를 한 줄에 보여줍니다.
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="전체 학생 수", value=f"{total_students}명")
with col2:
    st.metric(label="평균 점수", value=f"{avg_score:.1f}점")
with col3:
    st.metric(label="평균 공부시간", value=f"{avg_study_time:.1f}시간")

st.divider()

# 5. 슬라이더를 만들어 사용자로부터 '최소 공부시간'을 입력받습니다.
max_study_time = float(df['공부시간'].max())
min_study_time = st.slider('최소 공부시간을 선택하세요:', min_value=0.0, max_value=max_study_time, value=0.0)

# 6. 선택한 최소 공부시간 이상인 학생들만 남도록 데이터를 필터링(조건 검색)합니다.
filtered_df = df[df['공부시간'] >= min_study_time]

# 7. 필터링된 데이터를 바탕으로 공부시간과 점수의 관계를 보여주는 산점도를 그립니다.
st.subheader('공부시간과 점수의 관계')
st.scatter_chart(data=filtered_df, x='공부시간', y='점수')

# 8. 필터링된 데이터를 바탕으로 학생별 점수를 보여주는 막대 그래프를 그립니다.
st.subheader('학생별 점수')
st.bar_chart(data=filtered_df, x='학생ID', y='점수')
```