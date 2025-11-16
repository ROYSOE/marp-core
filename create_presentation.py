#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# 색상 정의
GREEN = RGBColor(46, 204, 113)  # #2ECC71
DARK_GREEN = RGBColor(46, 125, 50)  # #2E7D32
DARK_GRAY = RGBColor(44, 62, 80)  # #2C3E50
LIGHT_GRAY = RGBColor(248, 249, 250)  # #F8F9FA
RED = RGBColor(231, 76, 60)  # #E74C3C
ORANGE = RGBColor(243, 156, 18)  # #F39C12
BLUE = RGBColor(52, 152, 219)  # #3498DB
GRAY = RGBColor(149, 165, 166)  # #95A5A6
YELLOW = RGBColor(255, 249, 196)  # #FFF9C4

# 프레젠테이션 생성
prs = Presentation()
prs.slide_width = Inches(16)
prs.slide_height = Inches(9)

def add_title(slide, title_text, color=GREEN):
    """제목 추가"""
    # 제목을 텍스트 박스로 추가
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(15), Inches(0.8))
    tf = title_box.text_frame
    tf.text = title_text
    tf.paragraphs[0].font.size = Pt(32)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = color
    tf.paragraphs[0].font.name = 'Malgun Gothic'
    return title_box

def add_text_box(slide, left, top, width, height, text, font_size=14, bold=False, color=DARK_GRAY, align=PP_ALIGN.LEFT):
    """텍스트 박스 추가"""
    textbox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = textbox.text_frame
    tf.text = text
    tf.paragraphs[0].font.size = Pt(font_size)
    tf.paragraphs[0].font.bold = bold
    tf.paragraphs[0].font.color.rgb = color
    tf.paragraphs[0].font.name = 'Malgun Gothic'
    tf.paragraphs[0].alignment = align
    tf.word_wrap = True
    return textbox

def add_box_with_border(slide, left, top, width, height, border_color=GREEN):
    """테두리 있는 박스 추가"""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    shape.fill.background()
    shape.line.color.rgb = border_color
    shape.line.width = Pt(2)
    return shape

def add_table(slide, rows, cols, left, top, width, height):
    """표 추가"""
    table_shape = slide.shapes.add_table(rows, cols, Inches(left), Inches(top), Inches(width), Inches(height))
    return table_shape.table

# ========================
# 슬라이드 1: 표지
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])  # 빈 레이아웃
# 배경색
background = slide.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = DARK_GREEN

# 제목
add_text_box(slide, 1, 2.5, 14, 1.5, "환경-복지 연결\n노인일자리 창출사업",
             font_size=40, bold=True, color=RGBColor(255,255,255), align=PP_ALIGN.CENTER)

# 부제
add_text_box(slide, 1, 4.2, 14, 0.5, "사업계획서",
             font_size=28, bold=True, color=RGBColor(255,255,255), align=PP_ALIGN.CENTER)

# 작성자 정보
info_text = "작성자: [학번] [이름]\n제출처: [학교명]\n작성일: 2025년 11월"
add_text_box(slide, 1, 6.5, 14, 1, info_text,
             font_size=16, color=RGBColor(255,255,255), align=PP_ALIGN.CENTER)

# ========================
# 슬라이드 2: 회사소개
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "회사소개")

# 비전
vision_text = '"환경과 복지의 선순환으로\n모두에게 가치를 실현한다"'
add_text_box(slide, 2, 1.5, 12, 1, vision_text,
             font_size=24, color=DARK_GRAY, align=PP_ALIGN.CENTER)

# 3개 핵심가치 박스
values = [
    ("경제적 자립성", "• 재활용 수익 창출\n• 지역 순환경제\n• 지속가능 재정"),
    ("환경적 가치", "• 재활용률 향상\n• 매립·소각 감소\n• 탄소저감"),
    ("사회적 가치", "• 고령층 일자리(60+)\n• 세대간 지식 전수\n• 취약계층 자립")
]

x_start = 1
for i, (title, content) in enumerate(values):
    x = x_start + i * 4.5
    add_box_with_border(slide, x, 3, 4, 3.5, GREEN)
    add_text_box(slide, x + 0.2, 3.2, 3.6, 0.5, title, font_size=16, bold=True, color=GREEN)
    add_text_box(slide, x + 0.2, 3.8, 3.6, 2.5, content, font_size=12, color=DARK_GRAY)

# ========================
# 슬라이드 3: 창업배경
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "창업배경 및 동기")

columns = [
    ("노인 빈곤 위기", RED, "• 노인빈곤율 39.8%\n  (출처: 통계청 2023)\n• OECD 평균의 3배\n• 기초연금 월 34.4만원 부족"),
    ("환경 위기", ORANGE, "• 연 8,032만 톤 폐기물\n  (출처: 환경부 2023)\n• 재활용률 저조\n• 노인 고용 재활용업체\n  거의 없음"),
    ("통합모델 필요", GREEN, "• 정부 노인일자리\n  109.8만개 확대\n• 환경기업 지원\n  연 325억원\n• 사회적기업 인증 확대")
]

for i, (title, color, content) in enumerate(columns):
    x = 1 + i * 4.7
    add_text_box(slide, x, 1.5, 4.2, 0.5, title, font_size=18, bold=True, color=color)
    add_text_box(slide, x, 2.2, 4.2, 3, content, font_size=13, color=DARK_GRAY)

# 하단 메시지
msg_shape = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(1), Inches(6.5), Inches(14), Inches(0.8)
)
msg_shape.fill.solid()
msg_shape.fill.fore_color.rgb = LIGHT_GRAY
msg_shape.line.color.rgb = LIGHT_GRAY
add_text_box(slide, 1.2, 6.6, 13.6, 0.6,
             "→ 환경 + 복지 통합 모델로 두 가지 사회문제를 동시 해결",
             font_size=16, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)

# ========================
# 슬라이드 4: 비즈니스 모델
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "비즈니스 모델")

# 가치사슬
add_text_box(slide, 1, 1.5, 14, 0.5, "수거 → 선별 → 재가공 → 판매",
             font_size=18, bold=True, color=DARK_GRAY, align=PP_ALIGN.CENTER)

# 4단계 프로세스
processes = [
    ("1. 수거", "가정·소상공인\n정기계약처"),
    ("2. 선별", "자동선별기\n품목별 분류\n오류율 ≤2%"),
    ("3. 재가공", "업사이클\n정제\n품질 기준화"),
    ("4. 판매", "B2B\nB2C\n기업 ESG")
]

for i, (title, content) in enumerate(processes):
    x = 1.5 + i * 3.2
    add_box_with_border(slide, x, 2.5, 2.8, 2, GREEN)
    add_text_box(slide, x + 0.2, 2.7, 2.4, 0.4, title, font_size=14, bold=True, color=GREEN)
    add_text_box(slide, x + 0.2, 3.2, 2.4, 1.5, content, font_size=11, color=DARK_GRAY)

# 주력 제품군 표
table = add_table(slide, 4, 3, 2, 5.2, 12, 1.8)
table_data = [
    ["제품", "활용 재료", "가격대"],
    ["재생 노트·메모지", "폐지", "5천~1만원"],
    ["에코 화분·수납함", "폐플라스틱", "1만~2만원"],
    ["에코백·파우치", "폐섬유", "1.5만~3만원"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(11)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:  # 헤더
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True

# ========================
# 슬라이드 5: 인력운영 계획
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "인력운영 계획")

# 인력 구성표
table = add_table(slide, 6, 5, 0.5, 1.5, 9, 2.5)
table_data = [
    ["직급", "인원", "월급여", "연봉", "주요 역할"],
    ["대표", "1명", "230만원", "2,760만원", "조직 총괄, 대외 대표"],
    ["팀장 A", "1명", "215만원", "2,580만원", "현장 운영, 프로세스 개선"],
    ["팀장 B", "1명", "215만원", "2,580만원", "예산·회계, 정부지원금"],
    ["팀원", "7명", "210만원", "17,640만원", "현장운영 (60세 이상)"],
    ["합계", "10명", "2,130만원", "25,560만원", "-"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(10)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:  # 헤더
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True
        elif i == 5:  # 합계
            cell.text_frame.paragraphs[0].font.bold = True

# 정부지원 제도
support_text = """정부지원 제도

① 고령자 고용지원금
   60세 이상, 연 840만원, 최대 2년

② 사회적기업 일자리창출
   취약계층 70%, 연 13,728만원

③ 전문인력 지원
   팀장급 2명, 1차년 연 3,840만원

④ 사업개발비
   설비·장비, 연 5천만원"""

add_text_box(slide, 10, 1.5, 5.5, 4.5, support_text, font_size=11, color=DARK_GRAY)

# 법적 준수사항
legal_text = """법적 준수사항

✓ 4대보험 가입
✓ 서면 근로계약
✓ 무기계약 전환 기준
✓ 최저임금 충족"""

add_text_box(slide, 0.5, 4.5, 9, 2, legal_text, font_size=11, color=DARK_GRAY)

# ========================
# 슬라이드 6: 온·오프라인 채널
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "온·오프라인 채널")

# 온라인 채널
online_text = """온라인 채널

• 자체 온라인몰 (1년차 하반기)
• 대형 플랫폼 입점 (2년차)
  - 쿠팡, 마켓컬리
• SNS 마케팅
  - 인스타그램, 블로그
• 글로벌 진출 (3년차+)"""

add_text_box(slide, 1, 1.5, 6.5, 3.5, online_text, font_size=13, color=DARK_GRAY)

# 오프라인 채널
offline_text = """오프라인 채널

• 정기 수거
  - 학교, 제조업체
• 박람회 참가 (연 2-3회)
  - 환경박람회
  - 사회적기업 박람회
• 체험 워크숍 (월 1회)
  - 업사이클 체험
• 기업 ESG 프로젝트"""

add_text_box(slide, 8.5, 1.5, 6.5, 3.5, offline_text, font_size=13, color=DARK_GRAY)

# 판로 구성 비중 표
table = add_table(slide, 5, 2, 4, 5.2, 8, 1.5)
table_data = [
    ["구분", "비중"],
    ["B2B (기업 대상)", "40%"],
    ["B2C (개인 소비자)", "30%"],
    ["기업협력 (ESG)", "20%"],
    ["기타", "10%"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(12)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True

# ========================
# 슬라이드 7: 연도별 인력 확대 계획
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "연도별 인력 확대 계획")

# 인력 확대 표
table = add_table(slide, 6, 7, 0.5, 1.5, 15, 2.5)
table_data = [
    ["연도", "인원", "고령층", "월인건비", "정부지원", "자부담", "월매출목표"],
    ["1년차", "10명", "7명", "2,130만원", "1,534만원", "596만원", "800만원"],
    ["2년차", "12명", "9명", "2,556만원", "1,792만원", "764만원", "1,500만원"],
    ["3년차", "15명", "10명", "3,195만원", "1,917만원", "1,278만원", "2,800만원"],
    ["4년차", "18명", "12명", "3,834만원", "1,533만원", "2,301만원", "3,500만원"],
    ["5년차", "20명", "14명", "4,260만원", "1,065만원", "3,195만원", "4,200만원"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(10)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:  # 헤더
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True
        elif i == 3:  # 3년차 - 손익분기점
            cell.fill.solid()
            cell.fill.fore_color.rgb = YELLOW

# 3단계 전략
strategies = [
    ("【1단계】 기반 구축기", "• 10명 → 12명 점진적 확대\n• 재활용 중심 안정화\n• 정부 지원 70%\n→ 운영 노하우 축적"),
    ("【2단계】 전환기", "• 15명 확대 (업사이클)\n• 고마진 제품 본격 출시\n• 정부 지원 60%\n→ 손익분기점 달성 🎯"),
    ("【3단계】 성장기", "• 18명 → 20명 (2호점)\n• 정부 지원 40% → 25%\n• 다양한 판로 확보\n→ 자립 경영 기반 확립")
]

for i, (title, content) in enumerate(strategies):
    x = 1 + i * 4.7
    add_box_with_border(slide, x, 4.5, 4.3, 2.2, GREEN)
    add_text_box(slide, x + 0.2, 4.7, 3.9, 0.4, title, font_size=12, bold=True, color=GREEN)
    add_text_box(slide, x + 0.2, 5.2, 3.9, 1.3, content, font_size=10, color=DARK_GRAY)

# ========================
# 슬라이드 8: 시장분석
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "시장분석")

# 시장 규모 표
table = add_table(slide, 4, 4, 2, 1.5, 12, 1.8)
table_data = [
    ["구분", "현황", "5년후 전망", "성장률"],
    ["글로벌 재활용시장", "79조원", "100조원", "CAGR 5.2%"],
    ["국내 재활용시장", "11조원", "14조원", "CAGR 5%"],
    ["노인 경제활동인구", "600만명", "630만명", "약 5%"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(11)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True

# 경쟁 환경
comp_text = """경쟁 환경

• 기존 재활용업체 200개+
  (노인 고용 거의 없음)

• 노인일자리 제공기관 1,000개+
  (환경사업 연계 거의 없음)"""

add_box_with_border(slide, 1, 4, 7, 2.5, ORANGE)
add_text_box(slide, 1.2, 4.2, 6.6, 2, comp_text, font_size=12, color=DARK_GRAY)

# 우리의 기회
opp_text = """우리의 기회

• 환경×복지 통합모델 시장 공백

• 정부 정책 지원 강화

• ESG 기업 협력 수요 증가"""

add_box_with_border(slide, 8.5, 4, 7, 2.5, GREEN)
add_text_box(slide, 8.7, 4.2, 6.6, 2, opp_text, font_size=12, color=DARK_GRAY)

# ========================
# 슬라이드 9: SWOT 분석
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "SWOT 분석")

swot = [
    ("Strength (강점)", GREEN,
     "• 정부 지원금 접근성 높음\n• 사회적 가치 우수\n• 통합모델로 경쟁 낮음\n\n대응전략:\n정부 지원 최대 활용", 1, 1.5),
    ("Weakness (약점)", ORANGE,
     "• 초기 투자 6,500만원 필요\n• 사업 경험 부족\n• 정부 지원 필수\n\n대응전략:\n단계적 투자 + 멘토링", 8.5, 1.5),
    ("Opportunity (기회)", BLUE,
     "• 노인일자리 정책 확대\n• 환경기업 지원 확대\n• ESG 수요 증가\n\n대응전략:\n정책 연계 강화", 1, 4.5),
    ("Threat (위협)", GRAY,
     "• 정책 변화 리스크\n• 대형업체 진입 가능\n• 가격 경쟁 심화\n\n대응전략:\n다채널 운영", 8.5, 4.5)
]

for title, color, content, x, y in swot:
    add_box_with_border(slide, x, y, 6.5, 2.5, color)
    add_text_box(slide, x + 0.2, y + 0.1, 6.1, 0.4, title, font_size=14, bold=True, color=color)
    add_text_box(slide, x + 0.2, y + 0.6, 6.1, 1.8, content, font_size=11, color=DARK_GRAY)

# ========================
# 슬라이드 10: 마케팅 전략
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "마케팅 전략")

# 타깃별 접근
targets = [
    ("[B2B 기업]", "• 폐기물 처리 비용 절감\n• ESG 경영 목표 달성 지원\n• 정기 수거 계약\n• 업사이클 제품 B2B 공급"),
    ("[B2C 소비자]", "• 친환경 제품 구매 욕구\n• 사회적 가치 소비 참여\n• 노인 일자리 기여 인식\n• 합리적 가격의 업사이클 제품"),
    ("[B2G 정부]", "• 노인 고용 확대 정책 부합\n• 환경 정책 목표 달성 기여\n• 사회적기업 육성 정책 연계\n• 지역경제 활성화")
]

for i, (title, content) in enumerate(targets):
    x = 1 + i * 4.7
    add_box_with_border(slide, x, 1.5, 4.3, 2.5, GREEN)
    add_text_box(slide, x + 0.2, 1.7, 3.9, 0.4, title, font_size=14, bold=True, color=GREEN)
    add_text_box(slide, x + 0.2, 2.2, 3.9, 1.6, content, font_size=11, color=DARK_GRAY)

# 홍보 전략
promo_text = """홍보 전략 및 예산

온라인 마케팅                     오프라인 마케팅
• SNS 운영 (주 3회)              • 전시회 참가 (연 2-3회)
• 온라인 광고                     • 체험 프로그램 (월 1회)
• 이메일 뉴스레터               • 언론 홍보 (연 4회)

연간 마케팅 예산: 1,200만원
(온라인 50% | 오프라인 33% | 콘텐츠 17%)"""

add_text_box(slide, 1, 4.5, 14, 2.2, promo_text, font_size=12, color=DARK_GRAY)

# ========================
# 슬라이드 11: 운영계획
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "운영계획")

# 시설 및 생산 능력 표
table = add_table(slide, 4, 4, 3, 1.5, 10, 1.5)
table_data = [
    ["항목", "1년차", "2-3년차", "4-5년차"],
    ["부지 규모", "300㎡", "500㎡", "800㎡+"],
    ["수거센터", "1개소", "1개소", "2개소"],
    ["선별 능력", "월 12톤", "월 24톤", "월 40톤"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(11)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True

# 운영 프로세스
add_text_box(slide, 1, 3.5, 14, 0.5, "수거 → 선별 → 포장 → 저장 → 판매 → 정산",
             font_size=16, bold=True, color=DARK_GRAY, align=PP_ALIGN.CENTER)

# 품질 관리 체계
table = add_table(slide, 5, 3, 3, 4.5, 10, 2)
table_data = [
    ["단계", "기준", "점검주기"],
    ["수거", "이물질 ≤5%", "일일"],
    ["선별", "분류 오류율 ≤2%", "일일"],
    ["보관", "화재 위험 점검", "주 1회"],
    ["목표", "ISO 14001 인증 취득", "3년차 심사, 4년차 취득"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(10)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True

# ========================
# 슬라이드 12: 조직 및 거버넌스
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "조직 및 거버넌스")

# 조직 구조
org_text = """조직 구조

대표(센터장)
 ├─ 수집팀 (팀원 3명)
 │   재활용품 수거·분류
 ├─ 선별팀 (팀원 2명)
 │   품질 관리·재가공
 └─ 판매팀 (팀원 2명)
     온·오프라인 판매, 고객관리"""

add_text_box(slide, 0.5, 1.5, 7, 3, org_text, font_size=11, color=DARK_GRAY)

# 회계 투명성
table = add_table(slide, 5, 2, 0.5, 5, 7, 1.8)
table_data = [
    ["주기", "관리 방법"],
    ["일일", "POS 시스템 자동 기록"],
    ["월 1회", "센터장 내부 검증"],
    ["분기별", "외부 모니터링"],
    ["연 1회", "전체 외부감사"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(10)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True

# ESG 거버넌스
esg_boxes = [
    ("E (환경)", "• 환경영향평가위원회\n• 분기별 재활용률 점검\n• 탄소감축 목표 모니터링"),
    ("S (사회)", "• 사회가치평가위원회\n• 고용 다양성 지표 관리\n• 지역사회 기여도 평가"),
    ("G (지배구조)", "• 이해관계자 참여 이사회\n• 재무정보 공개 (연 1회)\n• 사회적 감사 실시")
]

y_pos = 1.5
for title, content in esg_boxes:
    add_box_with_border(slide, 8, y_pos, 7.5, 1.5, GREEN)
    add_text_box(slide, 8.2, y_pos + 0.1, 7.1, 0.3, title, font_size=12, bold=True, color=GREEN)
    add_text_box(slide, 8.2, y_pos + 0.5, 7.1, 0.9, content, font_size=10, color=DARK_GRAY)
    y_pos += 1.8

# ========================
# 슬라이드 13: 5년 추진계획
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "5년 추진계획")

# 타임라인 표
table = add_table(slide, 6, 5, 0.5, 1.5, 15, 4)
table_data = [
    ["연도", "주요 과제", "월매출", "인력", "손익"],
    ["1년차", "센터 개소\n예비사회적기업 지정\n수거 네트워크 구축", "800만원", "10명", "-700만원"],
    ["2년차", "온라인몰 오픈\n파트너십 확대", "1,500만원", "12명", "-456만원"],
    ["3년차", "사회적기업 인증 ✅\n업사이클 본격화\n손익분기점 달성", "2,800만원", "15명", "+155만원"],
    ["4년차", "2호점 준비\nISO 14001 추진", "3,500만원", "18명", "+233만원"],
    ["5년차", "2호점 운영\n지역 허브 구축", "4,200만원", "20명", "+72만원"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(10)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True
        elif i == 3:  # 3년차
            cell.fill.solid()
            cell.fill.fore_color.rgb = YELLOW

# 핵심 지표
indicators = """핵심 지표 (5년 누적)

💰 경제: 누적 매출 약 39억원 | 정부 의존 72%→25%
👥 사회: 고용 10→20명 | 고령층 7→14명 | 취약계층 비율 70% 유지
🌱 환경: 누적 재활용 1,200톤 | CO₂ 감축 600톤 | 업사이클 제품 20종"""

add_text_box(slide, 0.5, 6, 15, 1, indicators, font_size=11, color=DARK_GRAY)

# ========================
# 슬라이드 14: 재무계획
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "5개년 재무계획 및 손익분기점")

# 초기 투자
table = add_table(slide, 7, 3, 0.3, 1.5, 5, 2.5)
table_data = [
    ["항목", "금액", "비고"],
    ["부동산 보증금", "2,000만원", "사무실·창고"],
    ["임차료 선납", "180만원", "3개월"],
    ["자동선별기(중고)", "1,500만원", "사업개발비"],
    ["수거차량(중고)", "2,000만원", "사업개발비"],
    ["포장재·자재", "500만원", "-"],
    ["합계", "6,500만원", "-"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(9)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True
        elif i == 6:
            cell.text_frame.paragraphs[0].font.bold = True

# 5개년 손익표
table = add_table(slide, 11, 6, 5.5, 1.5, 10.2, 4.5)
table_data = [
    ["구분(만원)", "1년차", "2년차", "3년차", "4년차", "5년차"],
    ["매출액", "9,600", "18,000", "33,600", "42,000", "50,400"],
    ["정부지원금", "18,408", "21,504", "23,004", "18,396", "12,780"],
    ["총수입", "28,008", "39,504", "56,604", "60,396", "63,180"],
    ["", "", "", "", "", ""],
    ["인건비", "25,560", "30,672", "38,340", "46,008", "51,120"],
    ["운영비", "10,848", "14,304", "16,404", "11,592", "11,196"],
    ["총지출", "36,408", "44,976", "54,744", "57,600", "62,316"],
    ["", "", "", "", "", ""],
    ["연간 손익", "-8,400", "-5,472", "+1,860", "+2,796", "+864"],
    ["누적 손익", "-8,400", "-13,872", "-12,012", "-9,216", "-8,352"]
]

for i, row_data in enumerate(table_data):
    for j, cell_text in enumerate(row_data):
        cell = table.cell(i, j)
        cell.text = cell_text
        cell.text_frame.paragraphs[0].font.size = Pt(9)
        cell.text_frame.paragraphs[0].font.name = 'Malgun Gothic'

        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
            cell.text_frame.paragraphs[0].font.bold = True
        elif i in [3, 7]:
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_GRAY
        elif i == 9 and j >= 3:  # 3년차부터 흑자
            cell.text_frame.paragraphs[0].font.color.rgb = GREEN
            cell.text_frame.paragraphs[0].font.bold = True

# 재정 전략
strategy_text = """재정 전략 및 지속가능성

【1-2년차】 기반 구축기
정부 지원 70% 의존 | 연평균 적자 7천만원

【3년차】 전환기
업사이클 본격화 | 손익분기점 달성 🎯

【4-5년차】 성장기
정부 지원 25% 감소 | 연평균 흑자 1,800만원

【6년차 이후】 완전 자립 경영"""

add_text_box(slide, 0.3, 4.5, 5, 2.2, strategy_text, font_size=10, color=DARK_GRAY)

# ========================
# 슬라이드 15: 결론 및 기대효과
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_title(slide, "결론 및 기대효과")

# 4개 효과 박스
effects = [
    ("사회적 효과", "• 5년 누적 120명·년 참여\n• 최저임금 이상 소득 보장\n• 세대통합 및 공동체 활성화", 1, 1.5),
    ("환경적 효과", "• 누적 재활용 1,200톤\n• CO₂ 감축 600톤\n• 지역 재활용률 +5%p 기여", 8.5, 1.5),
    ("경제적 효과", "• 고정직 20명 + 다수 간접 고용\n• 월 4,200만원 지역 소비\n• 지속가능한 수익 모델", 1, 4),
    ("정책 부합성", "• 노인일자리 정책 기여\n• 환경부 ESG 정책 부합\n• UN SDG 목표 부합\n  (SDG 8, SDG 12)", 8.5, 4)
]

for title, content, x, y in effects:
    add_box_with_border(slide, x, y, 6.5, 2, GREEN)
    add_text_box(slide, x + 0.2, y + 0.1, 6.1, 0.4, title, font_size=14, bold=True, color=GREEN)
    add_text_box(slide, x + 0.2, y + 0.6, 6.1, 1.3, content, font_size=11, color=DARK_GRAY)

# 최종 메시지
final_msg = '"환경과 복지를 연결하여\n지속가능한 사회적 가치를 실현합니다"'
msg_box = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(2), Inches(6.5), Inches(12), Inches(1.2)
)
msg_box.fill.solid()
msg_box.fill.fore_color.rgb = LIGHT_GRAY
msg_box.line.color.rgb = LIGHT_GRAY
add_text_box(slide, 2.2, 6.6, 11.6, 1, final_msg,
             font_size=24, bold=True, color=GREEN, align=PP_ALIGN.CENTER)

# ========================
# 저장
# ========================
prs.save('환경복지_노인일자리_창업계획서.pptx')
print("✅ PowerPoint 파일이 생성되었습니다!")
print("📁 파일명: 환경복지_노인일자리_창업계획서.pptx")
print("📊 총 슬라이드: 15개")
