import streamlit as st
import pandas as pd
import numpy as np
import json
import joblib
import os

# detector 모듈 임포트 (utils 폴더에서)
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from utils.detector import prepare_data, calculate_abuse_scores, get_blocklist
except ImportError:
    st.error("❌ detector 모듈을 찾을 수 없습니다. utils/detector.py 파일을 확인하세요.")
    st.stop()

# 페이지 설정
st.set_page_config(
    page_title="IveKorea 광고 어뷰징 탐지",
    page_icon="📊",
    layout="wide"
)

# 타이틀
st.title("📊 IveKorea 광고 어뷰징 탐지 시스템")
st.markdown("---")

# 프로젝트 개요
with st.expander("📌 프로젝트 개요", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **배경**
        - 리워드 광고 플랫폼의 광고 사기(Ad Fraud) 탐지
        - 자동화된 봇과 어뷰징 전문 유저 식별
        
        **기간 & 인원**
        - 기간: 2024.08.25 ~ 2024.09.30 (5주)
        - 인원: 4명 (본인 역할: 어뷰징 탐지 전담)
        """)
    
    with col2:
        st.markdown("""
        **핵심 성과**
        - ✅ **98.86% 광고 사기 감소**
        - ✅ 3.62% 유저가 27.52% 어뷰징 차지 (핵심 어뷰저 집단 식별)
        - ✅ 17개 규칙 + 머신러닝 기반 탐지 시스템
        - ✅ 매체별 어뷰징 비율 파악 및 제재 기준 마련
        """)

st.markdown("---")

# 데이터 정보
st.info("📌 **데모 모드**: 실제 프로젝트에서 사용한 데이터로 분석 결과를 확인할 수 있습니다.")

# 어뷰징 탐지 규칙 설명
st.subheader("🔍 어뷰징 탐지 규칙 (17개)")

tab1, tab2, tab3 = st.tabs(["행동 패턴 기반", "환경/통계 기반", "머신러닝 기반"])

with tab1:
    st.markdown("""
    | 규칙 | 설명 | 점수 |
    |------|------|:----:|
    | `Short_CTIT` | 전환 시간 5초 미만 (물리적으로 불가능) | 15점 |
    | `Fraud_Long_CTIT` | 전환 시간 1시간 초과 (유령 클릭) | 35점 |
    | `Consistent_CTIT` | 기계적으로 일정한 전환 시간 | 40점 |
    | `Rapid_Click` | 클릭 간격 1초 미만 | 10점 |
    | `Burst_Attack` | 5분 내 15회 이상 클릭 폭주 | 15점 |
    | `Heavy_Click_Spam` | 50회 이상 과도한 클릭 (미전환) | 20점 |
    | `Suspicious_Early_Hour` | 심야 시간대 의심 활동 | 10점 |
    | `Suspicious_Single_Conversion` | 단일 클릭 + 심야 활동 | 30점 |
    """)

with tab2:
    st.markdown("""
    | 규칙 | 설명 | 점수 |
    |------|------|:----:|
    | `Many_Devices_Per_IP` | 단일 IP에서 6개 이상 디바이스 | 25점 |
    | `Many_IPs_Per_Device` | 단일 디바이스에서 15개 이상 IP | 25점 |
    | `AWS_IP_Used` | 서버 IP (AWS 등) 사용 | 25점 |
    | `Abnormal_CVR` | 전환율 90% 초과 매체 | 45점 |
    | `Media_Concentration` | 소수 매체 집중 공략 | 20점 |
    | `Combo_Stealth_Bot` | AWS IP + 심야 활동 | 30점 |
    | `Combo_Focused_Fraud` | 매체 집중 + 다수 IP 사용 | 35점 |
    """)

with tab3:
    st.markdown("""
    | 규칙 | 설명 | 점수 |
    |------|------|:----:|
    | `Anomaly_Model_Flag` | Isolation Forest 기반 클릭 간격 이상 탐지 | 45점 |
    | `CTIT_Anomaly_Model` | Isolation Forest 기반 CTIT 패턴 이상 탐지 | 35점 |
    
    **Isolation Forest**
    - 비지도 학습 기반 이상치 탐지 알고리즘
    - 정상 패턴에서 벗어난 행동을 자동으로 식별
    """)

st.markdown("---")

# 주요 성과
st.subheader("💡 주요 성과 및 인사이트")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="어뷰징 감소율",
        value="98.86%",
        delta="광고 사기 차단"
    )

with col2:
    st.metric(
        label="핵심 어뷰저 비율",
        value="3.62%",
        delta="전체 어뷰징의 27.52% 차지"
    )

with col3:
    st.metric(
        label="탐지 규칙",
        value="17개",
        delta="규칙 + ML 기반"
    )

st.markdown("---")

# 비즈니스 인사이트
st.subheader("📈 비즈니스 인사이트")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.markdown("""
    **핵심 발견**
    - 전체 유저의 **3.62%가 전체 어뷰징의 27.52%**를 차지
    - 소수의 핵심 어뷰저 집단이 대부분의 사기 발생
    - 특정 매체에서 어뷰징이 집중적으로 발생
    """)

with insight_col2:
    st.markdown("""
    **전략적 제안**
    - 완전 제거보다 **어뷰징 다발 매체의 리워드 금액 조정**이 효과적
    - 매체별 어뷰징 비율 파악으로 리워드 정책 차별화
    - 실시간 모니터링으로 신규 어뷰징 패턴 조기 발견
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
    - Isolation Forest
    - 규칙 기반 스코어링
    """)

with tech_col3:
    st.markdown("""
    **시각화**
    - Streamlit
    - Tableau
    - Matplotlib
    """)

st.markdown("---")

# 프로젝트 결과물
st.subheader("📊 결과물")

result_tab1, result_tab2 = st.tabs(["Streamlit 대시보드", "Tableau 대시보드"])

with result_tab1:
    st.markdown("""
    **Streamlit 대시보드 기능**
    - ✅ 핵심 컬럼 선택 및 어뷰징 분석 실행
    - ✅ 3단계 민감도 설정 (엄격/평균/완화)
    - ✅ 어뷰징 유저가 가장 많이 이용한 매체 Top 10
    - ✅ 디바이스별 어뷰징 점수 및 사유 리포트
    - ✅ CSV 다운로드 기능
    """)
    
    st.info("💡 실제 대시보드는 별도로 배포되어 있습니다. (데이터 보안상 비공개)")

with result_tab2:
    st.markdown("""
    **Tableau 대시보드 구성**
    - **Overview**: 총 매출, 전환율, 매체별 성과 현황
    - **Revenue**: 시간별 리워드 지급액, 매체별 성과 분석
    - **Abuse**: 어뷰징 기기 수, 의심 클릭 비율, 시간대별 어뷰징 점수
    """)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>📧 본 프로젝트는 실제 기업 데이터를 활용하여 진행되었습니다.</p>
    <p>데이터 보안을 위해 실제 데이터 파일은 포함되어 있지 않습니다.</p>
</div>
""", unsafe_allow_html=True)
