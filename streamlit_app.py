import streamlit as st


st.set_page_config(
    page_title="유나라 | 자기소개",
    page_icon="✳️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Gowun+Batang:wght@400;700&display=swap');

    :root {
        --ink: #202b27;
        --muted: #66736d;
        --green: #176b52;
        --lime: #d8ed8d;
        --coral: #ef765c;
        --paper: #f5f7f2;
        --line: #dfe5dc;
    }

    .stApp {
        background: #fff;
        color: var(--ink);
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMainBlockContainer"] { max-width: 1100px; padding-top: 3.2rem; }

    .eyebrow {
        color: var(--green);
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .12em;
        text-transform: uppercase;
    }

    .hero { padding: 1rem 0 2.7rem; }

    .hero-divider { border-bottom: 1px solid var(--line); margin-bottom: 1rem; }

    .hero h1 {
        margin: .45rem 0 .55rem;
        color: var(--ink);
        font-family: 'Gowun Batang', 'Noto Serif KR', serif;
        font-size: clamp(3rem, 7vw, 5.5rem);
        font-weight: 700;
        line-height: 1.12;
    }

    .hero p { margin: 0; color: var(--muted); font-size: 1.08rem; }

    .stTabs [data-baseweb="tab-list"] {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(min(100%, 10rem), 1fr));
        gap: .5rem;
        overflow: visible;
        border-bottom: 1px solid #CBD5E1;
        background: transparent;
    }

    .stTabs [role="tab"] {
        min-height: 3.35rem;
        width: 100%;
        min-width: 0;
        box-sizing: border-box;
        padding: .55rem .45rem;
        border: 1px solid #CBD5E1 !important;
        border-radius: 4px 4px 0 0;
        background-color: #F1F5F9 !important;
        color: #334155 !important;
        font-size: .9rem;
        font-weight: 700;
        line-height: 1.35;
        text-align: center;
        white-space: normal;
        word-break: keep-all;
    }

    .stTabs [role="tab"] * { color: #334155 !important; }

    .stTabs [role="tab"][aria-selected="true"] {
        border-color: #1E3A5F !important;
        background-color: #1E3A5F !important;
        color: #FFFFFF !important;
    }

    .stTabs [role="tab"][aria-selected="true"] * { color: #FFFFFF !important; }

    .stTabs [role="tab"]:hover {
        background-color: #DBEAFE !important;
        color: #334155 !important;
    }

    .stTabs [role="tab"]:hover * { color: #334155 !important; }

    .stTabs [role="tab"][aria-selected="true"]:hover {
        background-color: #DBEAFE !important;
        color: #334155 !important;
    }

    .stTabs [data-baseweb="tab-highlight"] { background: transparent; height: 0; }
    .stTabs [data-baseweb="tab-border"] { background: transparent; }

    .section-kicker {
        margin: 2.1rem 0 .45rem;
        color: var(--coral);
        font-size: .75rem;
        font-weight: 700;
        letter-spacing: .08em;
    }

    .section-title {
        margin: 0 0 1.35rem;
        color: var(--ink);
        font-family: 'Gowun Batang', 'Noto Serif KR', serif;
        font-size: 1.8rem;
        font-weight: 700;
    }

    .section-heading { margin-bottom: 1.35rem; }
    .section-heading .section-title { margin-bottom: .4rem; }
    .section-description { margin: 0; color: var(--muted); font-size: .98rem; line-height: 1.7; }

    .intro-copy {
        max-width: 720px;
        color: #46534d;
        font-size: 1.05rem;
        line-height: 1.9;
    }

    .info-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin: 1.7rem 0 1rem;
    }

    .activity-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
        margin: 1.7rem 0 1rem;
    }

    .activity-list {
        margin: 0;
        padding-left: 1.2rem;
        color: #46534d;
        line-height: 1.8;
    }

    .activity-list li + li { margin-top: .55rem; }

    .info-item {
        min-height: 114px;
        padding: 1.15rem 1.25rem;
        border: 1px solid var(--line);
        border-radius: 5px;
        background: rgba(255, 255, 255, .62);
    }

    .info-label { margin-bottom: .6rem; color: var(--muted); font-size: .78rem; }
    .info-value { color: var(--ink); font-size: 1rem; font-weight: 700; line-height: 1.55; }

    .quote-block {
        margin: 1.4rem 0;
        padding: 1.2rem 1.4rem;
        border-left: 3px solid var(--coral);
        background: rgba(255, 255, 255, .58);
        color: var(--ink);
        font-family: 'Gowun Batang', 'Noto Serif KR', serif;
        font-size: 1.18rem;
        line-height: 1.8;
    }

    .award-line {
        padding: 1rem 1.15rem;
        border-radius: 5px;
        background: #e5eedf;
        color: #285440;
        font-size: .94rem;
        line-height: 1.7;
    }

    .st-key-award-image {
        width: 100%;
        max-width: 800px;
        margin: .85rem auto 1.8rem;
    }

    .st-key-award-image [data-testid="stImage"] { display: flex; justify-content: center; }
    .st-key-award-image img { width: 100%; height: auto; object-fit: contain; }
    .award-caption { margin: .55rem 0 0; color: var(--muted); font-size: .9rem; text-align: center; }

    .vision-panel {
        margin-top: 1.25rem;
        padding: 1.5rem;
        border-radius: 5px;
        background: var(--green);
        color: #fff;
    }

    .vision-panel .info-label { color: #c3d9ce; }
    .vision-panel .info-value { color: #fff; font-size: 1.3rem; }
    .vision-panel p { margin: .75rem 0 0; color: #e1eee7; line-height: 1.8; }

    .stCaption { color: var(--muted); }

    @media (max-width: 640px) {
        [data-testid="stMainBlockContainer"] { padding: 1.5rem 1.1rem 2rem; }
        .hero { padding: 1rem 0 1.8rem; }
        .hero p { font-size: .94rem; }
        div[data-testid="stImage"] { display: flex; justify-content: center; }
        .stTabs [data-baseweb="tab-list"] { gap: .35rem; }
        .stTabs [role="tab"] {
            min-height: 3rem;
            padding: .55rem .58rem;
            font-size: .82rem;
        }
        .info-grid { grid-template-columns: 1fr; gap: .65rem; }
        .activity-grid { grid-template-columns: 1fr; gap: .65rem; }
        .info-item { min-height: auto; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

hero_text, hero_photo = st.columns([3, 1])
with hero_text:
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">A little about me</div>
            <h1>안녕하세요,<br>유나라입니다.</h1>
            <p>배움을 꾸준히 이어가며, 받은 마음을 나누는 사람</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with hero_photo:
    st.image("IMG/080530.png.JPG", width=230)

st.markdown('<div class="hero-divider"></div>', unsafe_allow_html=True)

home, about, _projects, skills, activities, vision = st.tabs(
    [
        "👩🏻 HOME · 홈",
        "💎 ABOUT ME · 저를 소개합니다",
        "💻 PROJECTS · 프로젝트",
        "🛠️ SKILLS · 기술 역량",
        "🌱 ACTIVITIES · 활동",
        "🧭 VISION · 진로 목표",
    ]
)
subtab_labels = ["🏫 고등학교", "🎓 대학교"]

with home:
    home_high_school, _home_university = st.tabs(subtab_labels)

with home, home_high_school:
    st.markdown('<div class="section-kicker">01 / INTRODUCTION</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading"><h2 class="section-title">저를 소개합니다</h2>'
        '<p class="section-description">저의 기본 정보와 관심 분야를 소개합니다.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="intro-copy">경복비즈니스고등학교 IT과에 재학 중인 3학년 4반 유나라입니다. '
        '새로운 것을 배우고 꾸준히 실천하는 과정에서 보람을 느낍니다. '
        '좋아하는 콘텐츠를 즐기며 다양한 이야기를 만나는 시간도 소중하게 생각합니다.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="info-grid">
            <div class="info-item"><div class="info-label">SCHOOL</div><div class="info-value">경복비즈니스고등학교<br>3학년 4반 · IT과</div></div>
            <div class="info-item"><div class="info-label">NAME</div><div class="info-value">유나라</div></div>
            <div class="info-item"><div class="info-label">MY INTERESTS</div><div class="info-value">노래 감상<br>영화 · 드라마 · 예능 등 OTT 시청</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with about:
    about_high_school, _about_university = st.tabs(subtab_labels)

with about, about_high_school:
    st.markdown('<div class="section-kicker">02 / ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading"><h2 class="section-title">꾸준함으로 쌓은 책임감</h2>'
        '<p class="section-description">저의 성격과 강점, 가치관, 수상 경험을 담았습니다.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="intro-copy">아침자습 시간에 결석 없이 꾸준히 출석하며, 매일 아침 무엇을 공부할지 계획하고 '
        '실천해 왔습니다. 작은 약속과 일상의 노력을 이어온 경험은 맡은 일을 책임감 있게 해내는 힘이 되었습니다.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="award-line"><strong>꾸준한 실천과 나눔</strong><br>'
        '맡은 일에 책임감을 가지고 꾸준히 실천하며, 주변에 도움이 되는 일을 해온 점을 인정받아 '
        '한국중등교장협의회장 선행상을 받았습니다.</div>',
        unsafe_allow_html=True,
    )
    with st.container(key="award-image"):
        st.image("IMG/나라 선행상.jpg", width="stretch")
        st.markdown('<div class="award-caption">한국중등교장협의회장 선행상</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">MY VALUES</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">받은 마음을 다시 나누기</h2>', unsafe_allow_html=True)
    st.markdown(
        '<div class="quote-block">“받은 은혜를 잊지 않고, 다른 사람에게 베풀며 살아가자.”</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="intro-copy">이 가치관은 친할머니의 가르침에서 비롯되었습니다. 할머니께서는 약속을 지키는 '
        '것과 도움을 받았을 때 감사하는 태도를 늘 강조하셨습니다. 그리고 여유가 있을 때 다른 사람에게 베풀면 '
        '그 마음이 결국 자신에게 돌아온다고 말씀하셨습니다. 저도 그 가르침을 기억하며 감사와 나눔을 실천하고 싶습니다.</p>',
        unsafe_allow_html=True,
    )

with _projects:
    projects_high_school, _projects_university = st.tabs(subtab_labels)

with _projects, projects_high_school:
    st.markdown('<div class="section-kicker">03 / PROJECTS</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading"><h2 class="section-title">프로젝트</h2>'
        '<p class="section-description">전공 수업에서 진행한 프로젝트와 제작 결과물을 소개합니다.</p></div>',
        unsafe_allow_html=True,
    )

with skills:
    skills_high_school, _skills_university = st.tabs(subtab_labels)

with skills, skills_high_school:
    st.markdown('<div class="section-kicker">04 / SKILLS</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading"><h2 class="section-title">배우고 쌓아가는 IT 역량</h2>'
        '<p class="section-description">활용할 수 있는 기술과 도구, 취득한 자격증을 정리했습니다.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="section-kicker">① 💻 기술 역량</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">IT 역량</div>
                <div class="info-value">한글 문서 작성<br>프레젠테이션 제작<br>스프레드시트 활용</div>
            </div>
            <div class="info-item">
                <div class="info-label">학습 중인 기술</div>
                <div class="info-value">IT 전공 기초를 꾸준히 학습하며<br>컴퓨터 활용 역량을 키우고 있습니다.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="section-kicker">② 🏅 자격증</div>', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title">취득 완료</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">자격증</div>
                <div class="info-value">ITQ 아래한글</div>
                <div class="info-label" style="margin-top: 1rem;">등급 · 취득일</div>
                <div class="info-value">A등급 · 2024.06.27</div>
                <div class="info-label" style="margin-top: 1rem;">발급기관</div>
                <div class="info-value">한국생산성본부(KPC)</div>
            </div>
            <div class="info-item">
                <div class="info-label">자격증</div>
                <div class="info-value">ITQ 한글파워포인트</div>
                <div class="info-label" style="margin-top: 1rem;">등급 · 취득일</div>
                <div class="info-value">B등급 · 2024.08.29</div>
                <div class="info-label" style="margin-top: 1rem;">발급기관</div>
                <div class="info-value">한국생산성본부(KPC)</div>
            </div>
            <div class="info-item">
                <div class="info-label">자격증</div>
                <div class="info-value">ITQ 한글엑셀</div>
                <div class="info-label" style="margin-top: 1rem;">등급 · 취득일</div>
                <div class="info-value">A등급 · 2025.01.02</div>
                <div class="info-label" style="margin-top: 1rem;">발급기관</div>
                <div class="info-value">한국생산성본부(KPC)</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<h3 class="section-title">취득 계획</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">취득 계획</div>
                <div class="info-value">컴퓨터활용능력 2급</div>
            </div>
            <div class="info-item">
                <div class="info-label">취득 계획</div>
                <div class="info-value">ITQ 마스터</div>
                <div class="info-label" style="margin-top: 1rem;">목표</div>
                <div class="info-value">기존에 취득한 ITQ 한글파워포인트 B등급을 A등급으로 향상</div>
                <div class="info-label" style="margin-top: 1rem;">현재 등급 · 목표 등급</div>
                <div class="info-value">B등급 · A등급</div>
                <div class="info-label" style="margin-top: 1rem;">발급기관</div>
                <div class="info-value">한국생산성본부(KPC)</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with activities:
    activities_high_school, _activities_university = st.tabs(subtab_labels)

with activities, activities_high_school:
    st.markdown('<div class="section-kicker">05 / ACTIVITIES</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading"><h2 class="section-title">함께 이끌고 소통한 경험</h2>'
        '<p class="section-description">학생회와 동아리 등 학교생활 속 다양한 활동을 담았습니다.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="activity-grid">
            <div class="info-item">
                <div class="info-label">학생회 · IT과 부장</div>
                <div class="info-value">2학년부터 3학년까지</div>
                <ul class="activity-list">
                    <li>학생회 SNS 게시글을 관리했습니다.</li>
                    <li>축제에서 학생들을 인솔하고, 쓰레기를 주우며 쾌적한 환경을 만드는 데 힘썼습니다.</li>
                </ul>
            </div>
            <div class="info-item">
                <div class="info-label">금융회계사업 동아리</div>
                <div class="info-value">1학년부터 3학년까지 · 3학년 단장</div>
                <ul class="activity-list">
                    <li>서울머니쇼 박람회에 참여하고 경제 신문 스크랩 활동을 했습니다.</li>
                    <li>구독 경제를 주제로 발표했습니다.</li>
                    <li>3학년 때 단장으로서 후배와 동료들을 이끌고 원활하게 소통했습니다.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="award-line"><strong>2025년 FTA 실무인력 양성사업 모의 무역 실전대회 대상</strong><br>'
        '자료 조사 및 검토 역할을 맡아 참여했으며, 산업통상부장관상을 수상했습니다.</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="section-kicker">교과 학습 및 탐구</div>', unsafe_allow_html=True)
    st.markdown(
        '<h2 class="section-title">확률과 통계 스트레스 인지율 데이터 분석 보고서</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="activity-grid">
            <div class="info-item">
                <div class="info-label">활동 분야</div>
                <div class="info-value">통계 분석, 건강 데이터, 사회 문제 탐색이야</div>
            </div>
            <div class="info-item">
                <div class="info-label">활동 내용</div>
                <div class="info-value">확률과 통계 수업에서 고등학생 연령대를 중심으로 스트레스 인지율 데이터를 살펴보고, 집단에 따라 스트레스를 느낄 확률이 어떻게 달라지는지 분석하는 보고서를 작성함.</div>
            </div>
            <div class="info-item">
                <div class="info-label">주요 결과</div>
                <div class="info-value">청소년 및 젊은 연령대에서 스트레스를 인지하는 비율이 상대적으로 높게 나타남을 확인함.</div>
            </div>
            <div class="info-item">
                <div class="info-label">관련 역량</div>
                <div class="info-value">통계적 사고, 데이터 해석, 자료 분석, 사회 문제 탐색</div>
            </div>
        </div>
        <div class="info-item">
            <div class="info-label">배운 점 및 느낀 점</div>
            <div class="info-value">이번 탐구를 통해 스트레스와 같은 건강 관련 정보도 집단과 조건에 따라 달라지는 확률적인 데이터로 해석할 수 있다는 점을 이해했다. 특히 연령대에 따라 스트레스 인지율이 다르게 나타나는 것을 살펴보며, 건강 상태와 관련된 현상을 이해하기 위해서는 데이터를 수집하고 분석하는 과정이 중요하다는 것을 느꼈다. 또한 같은 연령대에서도 개인에 따라 스트레스를 느끼는 정도가 다를 수 있으므로, 집단별 통계뿐만 아니라 개인의 특성을 고려한 맞춤형 접근도 필요하다고 생각했다. 이를 계기로 건강 데이터 분석에 흥미를 갖게 되었으며, 앞으로 디지털 헬스케어 기기 개발 등 데이터와 IT 기술을 활용해 개인의 건강 관리를 지원하는 분야를 더 탐구하며 진로 적합성을 확인하고자 한다.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with vision:
    vision_high_school, _vision_university = st.tabs(subtab_labels)

with vision, vision_high_school:
    st.markdown('<div class="section-kicker">06 / VISION</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading"><h2 class="section-title">배움을 데이터의 가치로</h2>'
        '<p class="section-description">관심 분야와 앞으로의 진로 방향 및 목표를 소개합니다.</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="intro-copy">소프트웨어공학과에 진학해 전공 지식과 실무 역량을 차근차근 키우고, '
        'IT 분야 중에서도 데이터를 다루는 기업에 취업하는 것이 목표입니다.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="vision-panel">
            <div class="info-label">MY GOAL</div>
            <div class="info-value">소프트웨어공학과 진학 → 데이터 관련 IT 기업 취업</div>
            <p>꾸준히 배우고 책임감 있게 경험을 쌓아, 데이터를 통해 사람과 세상에 도움이 되는 일을 하고 싶습니다.</p>
        </div>
        <div class="info-grid">
            <div class="info-item"><div class="info-label">NEXT STEP</div><div class="info-value">소프트웨어공학 전공 공부</div></div>
            <div class="info-item"><div class="info-label">FIELD</div><div class="info-value">IT · 데이터</div></div>
            <div class="info-item"><div class="info-label">DIRECTION</div><div class="info-value">꾸준한 학습과 실천</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.caption("유나라 · 경복비즈니스고등학교 IT과")