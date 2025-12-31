import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="InfinityBank 금융 마케팅",
    page_icon="💳",
    layout="wide"
)

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# 타이틀
st.title("💳 InfinityBank 리볼빙 타겟팅 분석")
st.markdown("---")

# 프로젝트 개요
with st.expander("📌 프로젝트 개요", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **배경**
        - 무한은행 리볼빙 서비스 최적 타겟 선별
        - 리스크 최소화 + 수익성 극대화 필요
        - 고객 세그먼테이션을 통한 맞춤 전략 수립
        
        **데이터**
        - 고객 1,208명 (연소득, 총부채, 신용점수)
        - 거래 데이터 (날짜, 금액)
        """)
    
    with col2:
        st.markdown("""
        **핵심 성과**
        - ✅ **리볼빙 최적 타겟 46.5% (152명) 선별**
        - ✅ KMeans로 5개 고객군 세분화
        - ✅ 소득 대비 소비 × 신용점수 지표 개발
        - ✅ 마케팅 비용 70% 절감 전략 제안
        """)

st.markdown("---")

# 분석 프로세스
st.subheader("🔍 분석 프로세스")

process_tabs = st.tabs(["1️⃣ 데이터 전처리", "2️⃣ EDA", "3️⃣ 클러스터링", "4️⃣ 지표 개발", "5️⃣ 최종 세분화"])

with process_tabs[0]:
    st.markdown("""
    ### 📊 데이터 전처리
    
    **1. 데이터 정제**
    - '$' 문자 제거 → float 변환
    - Date 타입 변경
    - 이상치 처리: 저소득 100달러 미만 제거, 고소득자 유지
    
    **2. 파생변수 생성**
    - `total_spending`: 총 소비 금액
    - `user_grade`: 일반(90%), VIP(7%), VVIP(3%)
    - `debt_income_ratio`: 부채/소득 비율
    - `pay_ratio`: 지불 비율
    - `revolving_need_score`: 리볼빙 필요 점수 (1~4점)
    - `credit_score_grade`: 신용점수 등급 (1~5등급)
    - `sum_score`: 리볼빙 필요 점수 × 신용 점수
    """)

with process_tabs[1]:
    st.markdown("""
    ### 📈 탐색적 데이터 분석 (EDA)
    
    **주요 발견**
    - 1인 소득: 1~2만 달러 집중
    - 연소득: 2~4만 달러 집중
    - 신용점수: 중앙 집중 (670~739)
    - 총부채: 낮은 금액 집중
    
    **상관관계 분석**
    - 연소득 vs 부채: **0.49** (양의 상관)
    - 연소득 vs 신용점수: **-0.04** (무관)
    
    **인사이트**
    - 소득과 신용은 별개 → 리볼빙 승인 시 두 지표 모두 필수 확인
    """)

with process_tabs[2]:
    st.markdown("""
    ### 🎯 KMeans 클러스터링
    
    **대상**: 일반 고객 1,087명 (90%)
    
    **이유**: VVIP/VIP는 이미 프리미엄 서비스 중, 일반 고객 중 리볼빅 니즈 발굴이 수익 증대에 효과적
    
    **변수 7개**:
    1. 2015년 누적 소비 (최근 패턴)
    2. 신용점수 (상환 능력)
    3. 거래 빈도 (활성도)
    4. 거래 기간 (충성도)
    5. 연소득 (경제적 여유)
    6. 신용 등급 (리스크)
    7. 부채 비율 (재정 건전성)
    
    **결과**: 3개 군집 (K=3)
    """)
    
    # 클러스터 상세 정보
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **클러스터 0** (약 400명)
        - 2015년 소비: $31,487
        - 연소득: $36,969
        - 부채비율: 1.30
        - 거래빈도: 8,219회
        - 신용점수: 715
        
        ➡️ 안정적, 저축상품 적합
        """)
    
    with col2:
        st.markdown("""
        **클러스터 1** ⭐ (약 300명)
        - 2015년 소비: $61,884
        - 연소득: $52,687
        - 부채비율: 1.24
        - 거래빈도: 13,739회
        - 신용점수: 714
        
        ➡️ **리볼빙 최적 타겟**
        """)
    
    with col3:
        st.markdown("""
        **클러스터 2** (약 387명)
        - 2015년 소비: $39,228
        - 연소득: $47,014
        - 부채비율: 1.64
        - 거래빈도: 5,240회
        - 신용점수: 693
        
        ➡️ 부적합, 신용개선 필요
        """)

with process_tabs[3]:
    st.markdown("""
    ### 📐 리볼빙 대상 지표 개발
    
    **리볼빙 필요 점수** (소득 대비 소비)
    - ~50%: 1점
    - 51~100%: 2점
    - 101~150%: 3점
    - 151~200%: 4점
    - 200% 초과: 0.01점 (고위험)
    
    **신용 점수**
    - 800~850: 5점
    - 740~799: 4점
    - 670~739: 3점
    - 580~669: 2점
    - 300~579: 1점
    
    **추천 점수** = 리볼빙 필요 점수 × 신용 점수
    """)

with process_tabs[4]:
    st.markdown("""
    ### 🎯 최종 고객 세분화 (5개 그룹)
    
    | 그룹 | 인원 | 비율 | 특징 | 전략 |
    |------|------|------|------|------|
    | **고소비·고신용** | 152명 | 46.5% | 리볼빙 점수 3~4 × 신용 3~5 | 리볼빙 서비스 제안 ⭐ |
    | 저소비·저신용 | 50명 | 15.3% | 부채 부담 높음 | 신용 개선 프로그램 |
    | 초고소비 (고위험) | 48명 | 14.7% | 소득 대비 소비 200% 초과 | 소비 관리 컨설팅 |
    | 저소비·고신용 (안정) | 44명 | 13.5% | 재정 안정적 | 저축·투자 상품 |
    | 고소비·저신용 (위험) | 33명 | 10.1% | 연체 위험 높음 | 한도형 선불카드 |
    """)

st.markdown("---")

# 주요 성과
st.subheader("💡 주요 성과")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="리볼빙 최적 타겟",
        value="46.5%",
        delta="152명"
    )

with col2:
    st.metric(
        label="마케팅 비용 절감",
        value="70%",
        delta="정밀 타겟팅"
    )

with col3:
    st.metric(
        label="고객군 세분화",
        value="5개",
        delta="KMeans"
    )

with col4:
    st.metric(
        label="연체율 감소 예상",
        value="15%",
        delta="저신용군 배제"
    )

st.markdown("---")

# 시각화 섹션
st.subheader("📊 클러스터링 시각화")

viz_tab1, viz_tab2 = st.tabs(["클러스터 분포", "고객군 세분화"])

with viz_tab1:
    # 샘플 데이터 생성 (실제 데이터 대신)
    np.random.seed(42)
    
    # 클러스터 0: 중소비·중신용
    cluster_0 = pd.DataFrame({
        '2015년_소비': np.random.normal(31487, 5000, 400),
        '연소득': np.random.normal(36969, 4000, 400),
        '클러스터': ['클러스터 0'] * 400
    })
    
    # 클러스터 1: 고소비·고신용 (리볼빙 대상)
    cluster_1 = pd.DataFrame({
        '2015년_소비': np.random.normal(61884, 7000, 300),
        '연소득': np.random.normal(52687, 5000, 300),
        '클러스터': ['클러스터 1 (리볼빙 대상)'] * 300
    })
    
    # 클러스터 2: 저소비·저신용
    cluster_2 = pd.DataFrame({
        '2015년_소비': np.random.normal(39228, 6000, 387),
        '연소득': np.random.normal(47014, 4500, 387),
        '클러스터': ['클러스터 2'] * 387
    })
    
    df_clusters = pd.concat([cluster_0, cluster_1, cluster_2], ignore_index=True)
    
    # Plotly 산점도
    fig = px.scatter(
        df_clusters,
        x='연소득',
        y='2015년_소비',
        color='클러스터',
        title='KMeans 클러스터링 결과 (연소득 vs 2015년 소비)',
        labels={'연소득': '연소득 ($)', '2015년_소비': '2015년 누적 소비 ($)'},
        color_discrete_map={
            '클러스터 0': '#636EFA',
            '클러스터 1 (리볼빙 대상)': '#EF553B',
            '클러스터 2': '#00CC96'
        },
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

with viz_tab2:
    # 고객군 분포 파이 차트
    customer_segments = pd.DataFrame({
        '고객군': ['고소비·고신용\n(리볼빙 대상)', '저소비·저신용', '초고소비\n(고위험)', '저소비·고신용\n(안정)', '고소비·저신용\n(위험)'],
        '인원': [152, 50, 48, 44, 33],
        '비율': [46.5, 15.3, 14.7, 13.5, 10.1]
    })
    
    fig = px.pie(
        customer_segments,
        values='인원',
        names='고객군',
        title='최종 고객 세분화 (5개 그룹)',
        color_discrete_sequence=px.colors.qualitative.Set3,
        height=500
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# 비즈니스 인사이트
st.subheader("📈 비즈니스 인사이트")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.markdown("""
    ### 🔍 주요 발견
    
    **1. 소득과 신용은 별개**
    - 연소득 vs 신용점수 상관계수: -0.04
    - 고소득자라고 신용이 좋은 것은 아님
    - 리볼빙 승인 시 소득+신용 **모두 필수 확인**
    
    **2. 소비가 많다고 무조건 리볼빙 대상은 아님**
    - 소득 대비 200% 초과 소비자(48명)는 고위험
    - 소득 대비 101~200% + 신용 양호가 **최적**
    
    **3. 일반 고객 90%가 진짜 수익원**
    - VVIP/VIP는 이미 프리미엄 서비스 중
    - 일반 고객 중 46.5%가 리볼빙 잠재 고객
    - 전체의 약 **42%가 미개척 수익원**
    """)

with insight_col2:
    st.markdown("""
    ### 💼 전략적 제안
    
    **1. 마케팅 선택과 집중**
    - 전체 고객 무차별 마케팅 ❌
    - 152명(46.5%) 집중 타겟팅 ✅
    - 마케팅 예산 **70% 절감**
    
    **2. 거래 빈도 높을수록 리볼빙 전환율 ↑**
    - 클러스터 1: 거래 빈도 13,739회 (1일 3.8회)
    - 카드 의존도 높은 고객 우선 제안
    - **"이번 달 사용 금액 30% 증가" 알림 + 리볼빙 제안**
    
    **3. 장기 고객일수록 리볼빙 수용도 ↑**
    - 5년 이상 장기 고객 대상 우선 마케팅
    - "OO님, 10년간 함께해주셔서 **특별 혜택**" 메시지 활용
    """)

st.markdown("---")

# 고객군별 마케팅 전략
st.subheader("🎯 고객군별 맞춤 마케팅 전략")

strategy_tabs = st.tabs(["고소비·고신용", "초고소비", "고소비·저신용", "저소비·고신용", "저소비·저신용"])

with strategy_tabs[0]:
    st.markdown("""
    ### ⭐ 고소비·고신용 (152명, 46.5%) - 리볼빙 최적 타겟
    
    **특징**
    - 소득 대비 소비 높음 (101~200%)
    - 거래 빈도 매우 활발 (1일 3.8회)
    - 신용 양호 (714점)
    
    **전략**
    - 📱 리볼빙 서비스 알람
    - 💰 단기 현금 서비스
    - 📊 한도 상향 제안
    - 🔄 자동 납부 옵션
    
    **기대 효과**
    - 단기(3개월): 리볼빙 이용률 30% ↑
    - 중기(6개월): 교차 판매율 40% ↑
    - 장기(1년): 고객 LTV 25% ↑
    """)

with strategy_tabs[1]:
    st.markdown("""
    ### ⚠️ 초고소비 (48명, 14.7%) - 고위험군
    
    **특징**
    - 소득 대비 소비 200% 초과
    - 재정 건전성 낮음
    
    **전략**
    - 📊 분야별 금액 초과 알람
    - 💡 과소비 방지 컨설팅
    - 🚫 리볼빙 제한
    
    **기대 효과**
    - 연체율 감소
    - 장기 고객 관계 유지
    """)

with strategy_tabs[2]:
    st.markdown("""
    ### 🔴 고소비·저신용 (33명, 10.1%) - 위험군
    
    **특징**
    - 소비 높음 + 신용 낮음
    - 연체 위험 높음
    
    **전략**
    - 💳 연회비 무료
    - 🎫 한도형 선불카드
    - 📢 정부 지원금 알람
    - 📚 소비 코칭
    
    **기대 효과**
    - 신용 개선 지원
    - 이탈 방지
    """)

with strategy_tabs[3]:
    st.markdown("""
    ### 🟢 저소비·고신용 (44명, 13.5%) - 안정군
    
    **특징**
    - 재정 안정적
    - 신용 우수
    
    **전략**
    - 💰 저축 + 포인트 서비스
    - 📈 예금·투자 상품
    - ⬆️ 한도 상향
    
    **기대 효과**
    - 자산 관리 서비스 교차 판매
    """)

with strategy_tabs[4]:
    st.markdown("""
    ### 🟡 저소비·저신용 (50명, 15.3%)
    
    **특징**
    - 부채 부담 높음
    - 신용 낮음
    
    **전략**
    - 📖 신용 개선 가이드
    - 💸 소액 대출
    - 🎓 금융 교육
    
    **기대 효과**
    - 신용 회복 지원
    - 장기 우량 고객 전환
    """)

st.markdown("---")

# 기술 스택
st.subheader("🛠 기술 스택")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    **데이터 처리**
    - Python
    - Pandas
    - NumPy
    """)

with tech_col2:
    st.markdown("""
    **머신러닝**
    - Scikit-learn
    - KMeans Clustering
    - PCA
    - StandardScaler
    """)

with tech_col3:
    st.markdown("""
    **시각화**
    - Matplotlib
    - Seaborn
    - Plotly
    """)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>📧 본 프로젝트는 무한은행 리볼빙 서비스 타겟팅을 위한 분석 프로젝트입니다.</p>
    <p>데이터는 샘플 데이터로 대체되었습니다.</p>
</div>
""", unsafe_allow_html=True)
