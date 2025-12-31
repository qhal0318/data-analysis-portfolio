import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="Picketing 크리에이터 분석",
    page_icon="🔍",
    layout="wide"
)

# 타이틀
st.title("🔍 Picketing 크리에이터 분석 자동화")
st.markdown("---")

# 프로젝트 개요
with st.expander("📌 프로젝트 개요", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **배경**
        - 픽켓팅(설문 플랫폼) MVP 개발 인턴십
        - 마케팅팀의 크리에이터 리스트업 업무 자동화 필요
        - 수작업 분석의 시간 소요 및 비효율성 문제
        
        **기간 & 역할**
        - 기간: 2024년 (1개월)
        - 역할: 데이터 인턴 (시장 조사 및 데이터 인프라 설계)
        """)
    
    with col2:
        st.markdown("""
        **핵심 성과**
        - ✅ **분석 시간 96% 단축** (8시간 → 3분)
        - ✅ Instagram 150개 계정 자동 분석
        - ✅ YouTube 108개 채널 자동 분석
        - ✅ 마케팅팀 리소스 절감 및 데이터 기반 의사결정 지원
        """)

st.markdown("---")

# Before/After 비교
st.subheader("⏱ Before/After 비교")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📋 Before (수작업)
    
    **문제점:**
    - ❌ 크리에이터 1명당 약 3분 소요
    - ❌ 150명 분석 시 **약 8시간** 필요
    - ❌ 반복적인 단순 작업으로 인한 피로도
    - ❌ 실수 발생 가능성
    - ❌ 실시간 업데이트 어려움
    
    **프로세스:**
    1. Instagram/YouTube 직접 접속
    2. 팔로워 수, 게시물 수 수동 확인
    3. Excel에 수작업 입력
    4. 통계 계산 및 정리
    """)
    
    st.metric(
        label="분석 시간",
        value="8시간",
        delta="-96%",
        delta_color="inverse"
    )

with col2:
    st.markdown("""
    ### ⚡ After (자동화)
    
    **개선 사항:**
    - ✅ API 기반 자동 데이터 수집
    - ✅ 150명 분석 **3분 완료**
    - ✅ 정확도 향상 (API 공식 데이터)
    - ✅ 실시간 업데이트 가능
    - ✅ 확장 가능한 시스템
    
    **프로세스:**
    1. 크리에이터 리스트 입력
    2. API 자동 호출
    3. 데이터 자동 수집 및 정제
    4. Excel 자동 생성
    """)
    
    st.metric(
        label="분석 시간",
        value="3분",
        delta="+96% 효율",
        delta_color="normal"
    )

st.markdown("---")

# 크롤링 시스템 설명
st.subheader("🔧 크롤링 시스템 구조")

tab1, tab2 = st.tabs(["Instagram API", "YouTube API"])

with tab1:
    st.markdown("""
    ### 📷 Instagram Graph API
    
    **수집 데이터:**
    - 계정 이름 (username)
    - 팔로워 수 (followers_count)
    - 팔로잉 수 (follows_count)
    - 게시물 수 (media_count)
    - 프로필 이미지 URL
    - 계정 활동 상태
    
    **기술 스택:**
    - Instagram Graph API
    - Python requests
    - Pandas 데이터 처리
    - Excel 자동 생성 (openpyxl)
    
    **주요 기능:**
    - ✅ 대량 계정 일괄 조회
    - ✅ Rate Limit 자동 처리
    - ✅ 에러 핸들링 및 재시도
    - ✅ 결과 Excel 자동 저장
    """)

with tab2:
    st.markdown("""
    ### 🎥 YouTube Data API
    
    **수집 데이터:**
    - 채널 이름 (channel_title)
    - 구독자 수 (subscriber_count)
    - 총 조회수 (view_count)
    - 동영상 수 (video_count)
    - 채널 설명
    - 최근 업로드 정보
    
    **기술 스택:**
    - YouTube Data API v3
    - Python google-api-client
    - Pandas 데이터 처리
    - Excel 자동 생성 (openpyxl)
    
    **주요 기능:**
    - ✅ 채널 ID/URL 자동 변환
    - ✅ 다중 채널 병렬 처리
    - ✅ Quota 관리 및 최적화
    - ✅ 통계 자동 계산
    """)

st.markdown("---")

# 분석 결과 요약
st.subheader("📊 분석 결과 요약")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Instagram 분석",
        value="150개",
        delta="계정"
    )

with col2:
    st.metric(
        label="YouTube 분석",
        value="108개",
        delta="채널"
    )

with col3:
    st.metric(
        label="총 크리에이터",
        value="258명",
        delta="자동 분석 완료"
    )

st.markdown("---")

# 샘플 데이터 표시
st.subheader("📋 샘플 분석 결과")

# Instagram 샘플
st.markdown("**Instagram 크롤링 샘플 데이터**")
instagram_sample = pd.DataFrame({
    '계정명': ['creator_1', 'creator_2', 'creator_3', 'creator_4', 'creator_5'],
    '팔로워': [15000, 32000, 8500, 45000, 12000],
    '팔로잉': [500, 800, 350, 1200, 600],
    '게시물': [120, 340, 85, 560, 210],
    '참여율': ['3.2%', '4.5%', '2.8%', '5.1%', '3.9%']
})
st.dataframe(instagram_sample, use_container_width=True)

st.markdown("**YouTube 크롤링 샘플 데이터**")
youtube_sample = pd.DataFrame({
    '채널명': ['channel_1', 'channel_2', 'channel_3', 'channel_4', 'channel_5'],
    '구독자': [25000, 48000, 12000, 67000, 19000],
    '총 조회수': [1500000, 3200000, 850000, 4500000, 1200000],
    '동영상 수': [45, 89, 32, 125, 56],
    '평균 조회수': [33333, 35955, 26562, 36000, 21428]
})
st.dataframe(youtube_sample, use_container_width=True)

st.info("💡 **실제 데이터는 개인정보 보호를 위해 샘플 데이터로 대체되었습니다.**")

st.markdown("---")

# 비즈니스 임팩트
st.subheader("💼 비즈니스 임팩트")

impact_col1, impact_col2 = st.columns(2)

with impact_col1:
    st.markdown("""
    **정량적 성과**
    - ⏰ **작업 시간 96% 단축**: 8시간 → 3분
    - 💰 **인건비 절감**: 월 32시간 절약 (주 1회 분석 기준)
    - 📈 **확장성**: 1,000명 이상도 동일 시간 처리 가능
    - 🎯 **정확도 향상**: API 공식 데이터 사용
    """)

with impact_col2:
    st.markdown("""
    **정성적 성과**
    - 🚀 마케팅팀이 **전략 수립에 집중** 가능
    - 📊 데이터 기반 크리에이터 선정
    - 🔄 실시간 모니터링 시스템 구축 가능
    - 💡 확장 가능한 데이터 인프라 기반 마련
    """)

st.markdown("---")

# 기술 스택
st.subheader("🛠 기술 스택")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    **언어 & 라이브러리**
    - Python 3.x
    - Pandas
    - Requests
    - openpyxl
    """)

with tech_col2:
    st.markdown("""
    **API**
    - Instagram Graph API
    - YouTube Data API v3
    - OAuth 2.0 인증
    """)

with tech_col3:
    st.markdown("""
    **기타**
    - Excel 자동화
    - 에러 핸들링
    - Rate Limit 관리
    """)

st.markdown("---")

# 프로젝트 과정
st.subheader("📝 프로젝트 진행 과정")

with st.expander("1주차: 요구사항 분석 및 API 조사", expanded=False):
    st.markdown("""
    - 마케팅팀 인터뷰 및 현재 프로세스 파악
    - Instagram/YouTube API 문서 분석
    - API 키 발급 및 권한 설정
    - 샘플 코드 작성 및 테스트
    """)

with st.expander("2주차: 크롤링 시스템 개발", expanded=False):
    st.markdown("""
    - Instagram Graph API 크롤러 개발
    - YouTube Data API 크롤러 개발
    - 에러 핸들링 및 재시도 로직 구현
    - Rate Limit 관리 기능 추가
    """)

with st.expander("3주차: 데이터 처리 및 자동화", expanded=False):
    st.markdown("""
    - Pandas를 활용한 데이터 정제
    - Excel 자동 생성 기능 개발
    - 통계 계산 및 시각화
    - 배치 프로세스 자동화
    """)

with st.expander("4주차: 테스트 및 최적화", expanded=False):
    st.markdown("""
    - 150개 Instagram 계정 테스트
    - 108개 YouTube 채널 테스트
    - 성능 최적화 (병렬 처리)
    - 문서화 및 인수인계
    """)

st.markdown("---")

# 핵심 코드 스니펫
st.subheader("💻 핵심 코드 스니펫")

code_tab1, code_tab2 = st.tabs(["Instagram", "YouTube"])

with code_tab1:
    st.code("""
# Instagram Graph API 크롤링 예시
import requests
import pandas as pd

def get_instagram_data(username, access_token):
    url = f"https://graph.instagram.com/v12.0/{username}"
    params = {
        'fields': 'followers_count,follows_count,media_count',
        'access_token': access_token
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 대량 계정 처리
results = []
for username in username_list:
    data = get_instagram_data(username, access_token)
    if data:
        results.append(data)
        
df = pd.DataFrame(results)
df.to_excel('instagram_results.xlsx', index=False)
    """, language="python")

with code_tab2:
    st.code("""
# YouTube Data API 크롤링 예시
from googleapiclient.discovery import build
import pandas as pd

def get_youtube_stats(channel_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.channels().list(
        part='statistics,snippet',
        id=channel_id
    )
    response = request.execute()
    
    if response['items']:
        stats = response['items'][0]['statistics']
        return {
            'subscriber_count': stats.get('subscriberCount'),
            'view_count': stats.get('viewCount'),
            'video_count': stats.get('videoCount')
        }
    return None

# 대량 채널 처리
results = []
for channel_id in channel_id_list:
    data = get_youtube_stats(channel_id, api_key)
    if data:
        results.append(data)
        
df = pd.DataFrame(results)
df.to_excel('youtube_results.xlsx', index=False)
    """, language="python")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>📧 본 프로젝트는 픽켓팅 인턴십 기간 동안 진행되었습니다.</p>
    <p>개인정보 보호를 위해 실제 크리에이터 데이터는 포함되어 있지 않습니다.</p>
</div>
""", unsafe_allow_html=True)
