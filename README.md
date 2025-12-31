# 📊 데이터 분석 포트폴리오

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

**데이터 기반 의사결정으로 비즈니스 임팩트를 만드는 데이터 분석가**

[📧 Email](mailto:qhal0318@gmail.com) 

</div>

---

## 🎯 프로젝트 소개

데이터 분석을 통해 비즈니스 문제를 해결하고 실질적인 성과를 창출한 프로젝트 포트폴리오입니다.

### 주요 성과

| 지표 | 성과 |
|------|------|
| 광고 사기 감소 | **98.86%** |
| 분석 시간 단축 | **96%** (8시간 → 3분) |
| 리볼빙 타겟 선별 정확도 | **46.5%** |

---

## 📂 프로젝트

### 1. 📊 IveKorea 광고 어뷰징 탐지 시스템

<img src="https://via.placeholder.com/800x400?text=IveKorea+Dashboard" width="100%">

**프로젝트 개요**
- 리워드 광고 플랫폼의 광고 사기(Ad Fraud) 탐지 시스템 구축
- 기간: 2024.08.25 ~ 2024.09.30 (5주)
- 역할: 어뷰징 탐지 전담 (4인 팀)

**핵심 성과**
- ✅ **98.86% 광고 사기 감소**
- ✅ 3.62% 유저가 전체 어뷰징의 27.52% 차지 (핵심 어뷰저 집단 식별)
- ✅ 17개 규칙 + Isolation Forest 기반 머신러닝 탐지 시스템
- ✅ 매체별 어뷰징 비율 파악 및 제재 기준 마련

**기술 스택**
- Python, Pandas, NumPy, Scikit-learn (Isolation Forest)
- Streamlit, Tableau
- 규칙 기반 스코어링 시스템

**주요 기능**
- 17개 어뷰징 탐지 규칙 (행동 패턴, 환경/통계, 머신러닝 기반)
- 3단계 민감도 설정 (엄격/평균/완화)
- 실시간 대시보드 및 리포트 다운로드

📁 [코드 보기](./pages/1_📊_IveKorea.py) 

---

### 2. 🔍 Picketing 크리에이터 분석 자동화

<img src="https://via.placeholder.com/800x400?text=Picketing+Automation" width="100%">

**프로젝트 개요**
- 설문 플랫폼 픽켓팅의 크리에이터 분석 업무 자동화
- 기간: 2024년 (1개월 인턴십)
- 역할: 데이터 인턴 (시장 조사 및 데이터 인프라 설계)

**핵심 성과**
- ✅ **분석 시간 96% 단축** (8시간 → 3분)
- ✅ Instagram 150개 계정 자동 분석
- ✅ YouTube 108개 채널 자동 분석
- ✅ 마케팅팀 리소스 절감 및 데이터 기반 의사결정 지원

**기술 스택**
- Python, Pandas, openpyxl
- Instagram Graph API, YouTube Data API v3
- API Rate Limit 관리 및 에러 핸들링

**주요 기능**
- Instagram/YouTube 크리에이터 데이터 자동 수집
- 팔로워, 구독자, 게시물 통계 자동 계산
- Excel 자동 생성 및 배치 처리

📁 [코드 보기](./pages/2_🔍_Picketing.py) 

---

### 3. 💳 InfinityBank 금융 마케팅 분석

<img src="https://via.placeholder.com/800x400?text=Banking+Analysis" width="100%">

**프로젝트 개요**
- 무한은행 리볼빙 서비스 최적 타겟 선별
- 데이터: 고객 1,208명 (연소득, 총부채, 신용점수, 거래 데이터)

**핵심 성과**
- ✅ **리볼빙 최적 타겟 46.5% (152명) 정밀 선별**
- ✅ KMeans 클러스터링으로 5개 고객군 세분화
- ✅ 소득 대비 소비 × 신용점수 지표 개발
- ✅ 마케팅 비용 70% 절감, 연체율 15% 감소 전략 제안

**기술 스택**
- Python, Pandas, NumPy
- Scikit-learn (KMeans, PCA, StandardScaler)
- Matplotlib, Seaborn, Plotly

**주요 분석**
- EDA 및 상관관계 분석 (연소득 vs 부채: 0.49, 연소득 vs 신용: -0.04)
- KMeans 클러스터링 (일반 고객 1,087명 → 3개 군집)
- 리볼빙 필요 점수 × 신용 점수 지표 개발
- 고객군별 맞춤 마케팅 전략 수립

📁 [코드 보기](./pages/3_💳_InfinityBank.py) 

---

## 🛠 기술 스택

### 언어 & 프레임워크
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

### 데이터 분석 & ML
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

### 시각화
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

### API & 기타
![Instagram](https://img.shields.io/badge/Instagram_API-E4405F?style=flat-square&logo=instagram&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube_API-FF0000?style=flat-square&logo=youtube&logoColor=white)

---

## 📊 프로젝트 구조
```
data-analysis-portfolio/
├── Home.py                              # 메인 페이지
├── pages/
│   ├── 1_📊_IveKorea.py                # 광고 어뷰징 탐지
│   ├── 2_🔍_Picketing.py               # 크리에이터 분석
│   └── 3_💳_InfinityBank.py            # 금융 마케팅
├── utils/
│   └── detector.py                      # 어뷰징 탐지 로직
├── data/                                # 데이터 파일 (비공개)
├── assets/                              # 이미지 및 아이콘
├── requirements.txt                     # 패키지 목록
└── README.md
```

---

## 🚀 로컬 실행 방법
```bash
# 1. 리포지토리 클론
git clone https://github.com/qhal0318/data-analysis-portfolio.git
cd data-analysis-portfolio

# 2. 패키지 설치
pip install -r requirements.txt

# 3. Streamlit 앱 실행
streamlit run Home.py
```

---

## 📜 자격증

- **SQLD** (SQL 개발자)
- **ADsP** (데이터분석 준전문가)

---

## 📧 Contact

- **Email**: your.email@example.com
- **LinkedIn**: [프로필 링크](#)
- **Blog**: [블로그 링크](#)
- **GitHub**: [@qhal0318](https://github.com/qhal0318)

---

<div align="center">

**© 2025 지연주. All rights reserved.**

⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!

</div>
