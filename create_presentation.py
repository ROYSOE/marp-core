#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
환경-복지 연결 노인일자리 창출사업 프레젠테이션 생성기
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from PIL import Image, ImageDraw, ImageFont
import io

# 색상 정의
PRIMARY_GREEN = RGBColor(46, 125, 50)      # #2E7D32
LIGHT_GREEN = RGBColor(232, 245, 233)      # #E8F5E9
ACCENT_GREEN = RGBColor(46, 204, 113)      # #2ECC71
TEXT_DARK = RGBColor(44, 62, 80)           # #2C3E50
ORANGE = RGBColor(245, 124, 0)             # #F57C00
BLUE = RGBColor(25, 118, 210)              # #1976D2
PURPLE = RGBColor(123, 31, 162)            # #7B1FA2
YELLOW = RGBColor(255, 235, 59)            # #FFEB3B
RED = RGBColor(229, 57, 53)                # #E53935

def create_logo():
    """회사 앰블럼 생성 (환경 + 복지)"""
    # 5cm = 약 189 픽셀 (96 DPI 기준)
    size = 400
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 배경 원
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin],
                 fill=(46, 125, 50, 255), outline=(46, 204, 113, 255), width=8)

    # 재활용 심볼 (삼각형 화살표 3개)
    center = size // 2
    radius = 120

    # 녹색 계열로 재활용 화살표 표현
    import math
    for i in range(3):
        angle = math.radians(i * 120 - 90)
        x = center + radius * math.cos(angle)
        y = center + radius * math.sin(angle)

        # 화살표
        points = [
            (x - 15, y - 30),
            (x + 15, y - 30),
            (x, y)
        ]
        draw.polygon(points, fill=(232, 245, 233, 255))

    # 중앙에 사람 아이콘 (원 + 반원으로 단순화)
    # 머리
    head_r = 30
    draw.ellipse([center-head_r, center-80, center+head_r, center-20],
                 fill=(255, 255, 255, 255))
    # 몸통
    body_points = [
        (center-40, center-10),
        (center+40, center-10),
        (center+50, center+50),
        (center-50, center+50)
    ]
    draw.polygon(body_points, fill=(255, 255, 255, 255))

    # 저장
    logo_path = '/home/user/marp-core/logo_emblem.png'
    img.save(logo_path)
    return logo_path

def add_title_slide(prs):
    """슬라이드 1: 표지"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 빈 슬라이드

    # 배경색
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = PRIMARY_GREEN

    # 로고
    logo_path = create_logo()
    left = Inches(4.5)
    top = Inches(1.0)
    slide.shapes.add_picture(logo_path, left, top, height=Inches(2))

    # 제목
    title_box = slide.shapes.add_textbox(Inches(1), Inches(3.5), Inches(8), Inches(1))
    title_frame = title_box.text_frame
    title_frame.text = "환경-복지 연결 노인일자리 창출사업"
    p = title_frame.paragraphs[0]
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER

    # 부제
    subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(4.6), Inches(8), Inches(0.5))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "사업계획서"
    p = subtitle_frame.paragraphs[0]
    p.font.size = Pt(28)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER

    # 작성 정보
    info_box = slide.shapes.add_textbox(Inches(2), Inches(6.2), Inches(6), Inches(1))
    info_frame = info_box.text_frame
    info_text = "작성자: [학번] [이름]\n제출처: [학교명]\n작성일: 2025년 11월"
    info_frame.text = info_text
    for p in info_frame.paragraphs:
        p.font.size = Pt(18)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

def add_company_intro_slide(prs):
    """슬라이드 2: 회사소개"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # 제목만

    # 제목
    title = slide.shapes.title
    title.text = "회사소개"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 비전
    vision_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(0.8))
    vision_frame = vision_box.text_frame
    vision_frame.text = '💡 비전: "환경과 복지의 선순환으로 모두에게 가치를 실현한다"'
    p = vision_frame.paragraphs[0]
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.alignment = PP_ALIGN.CENTER

    # 3개 박스 (경제, 환경, 사회)
    box_width = 2.8
    box_height = 2.2
    y_pos = 2.5

    boxes = [
        {
            'title': '경제적 자립성',
            'items': ['• 재활용 수익 창출', '• 지역 순환경제', '• 지속가능 재정'],
            'x': 0.8
        },
        {
            'title': '환경적 가치',
            'items': ['• 재활용률 향상', '• 매립·소각 감소', '• 탄소저감'],
            'x': 3.8
        },
        {
            'title': '사회적 가치',
            'items': ['• 고령층 일자리(60+)', '• 세대간 지식 전수', '• 취약계층 자립'],
            'x': 6.8
        }
    ]

    for box in boxes:
        # 박스 틀
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(box['x']), Inches(y_pos),
            Inches(box_width), Inches(box_height)
        )
        shape.line.color.rgb = ACCENT_GREEN
        shape.line.width = Pt(3)
        shape.fill.background()

        # 텍스트
        text_frame = shape.text_frame
        text_frame.margin_top = Inches(0.1)
        text_frame.margin_left = Inches(0.1)
        text_frame.word_wrap = True

        # 제목
        p = text_frame.paragraphs[0]
        p.text = box['title']
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.alignment = PP_ALIGN.CENTER

        # 항목들
        for item in box['items']:
            p = text_frame.add_paragraph()
            p.text = item
            p.font.size = Pt(14)
            p.font.color.rgb = TEXT_DARK
            p.space_before = Pt(6)

def add_background_slide(prs):
    """슬라이드 3: 창업배경 및 동기"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "창업배경 및 동기"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 3컬럼
    col_width = 2.8
    col_height = 3.0
    y_pos = 1.8

    columns = [
        {
            'icon': '🚨',
            'title': '노인 빈곤 위기',
            'stat': '노인빈곤율 39.8%',
            'desc': 'OECD 최고 수준\n일자리 창출 시급',
            'color': RED,
            'x': 0.8
        },
        {
            'icon': '🌍',
            'title': '환경 위기',
            'stat': '연 8,032만 톤',
            'desc': '폐기물 증가\n재활용 인프라 부족',
            'color': ORANGE,
            'x': 3.8
        },
        {
            'icon': '✅',
            'title': '통합모델 필요',
            'stat': '정책적 지원 확대',
            'desc': '노인일자리 + 환경기업\n사회적기업 육성',
            'color': PRIMARY_GREEN,
            'x': 6.8
        }
    ]

    for col in columns:
        # 박스
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(col['x']), Inches(y_pos),
            Inches(col_width), Inches(col_height)
        )
        shape.line.color.rgb = col['color']
        shape.line.width = Pt(4)
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(255, 255, 255)

        text_frame = shape.text_frame
        text_frame.margin_top = Inches(0.2)

        # 아이콘 + 제목
        p = text_frame.paragraphs[0]
        p.text = f"{col['icon']} {col['title']}"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = col['color']
        p.alignment = PP_ALIGN.CENTER

        # 통계
        p = text_frame.add_paragraph()
        p.text = col['stat']
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_DARK
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(12)

        # 설명
        p = text_frame.add_paragraph()
        p.text = col['desc']
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_DARK
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(8)

    # 하단 메시지
    msg_box = slide.shapes.add_textbox(Inches(1.5), Inches(5.2), Inches(7), Inches(0.6))
    msg_frame = msg_box.text_frame
    msg_frame.text = "💡 환경 + 복지 통합 모델로 두 문제 동시 해결"
    p = msg_frame.paragraphs[0]
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.alignment = PP_ALIGN.CENTER

    # 출처
    source_box = slide.shapes.add_textbox(Inches(6), Inches(6.8), Inches(3.5), Inches(0.3))
    source_frame = source_box.text_frame
    source_frame.text = "출처: 통계청 2023, 환경부 2023"
    p = source_frame.paragraphs[0]
    p.font.size = Pt(10)
    p.font.color.rgb = RGBColor(102, 102, 102)
    p.alignment = PP_ALIGN.RIGHT

def add_business_model_slide(prs):
    """슬라이드 4: 비즈니스 모델"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "비즈니스 모델"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 가치사슬 프로세스 (화살표)
    process_y = 1.8
    steps = ['수거', '선별', '재가공', '판매']

    for i, step in enumerate(steps):
        x = 1.2 + i * 2.0

        # 박스
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(process_y),
            Inches(1.6), Inches(0.6)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = ACCENT_GREEN
        shape.line.color.rgb = PRIMARY_GREEN

        text_frame = shape.text_frame
        p = text_frame.paragraphs[0]
        p.text = step
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        # 화살표 (마지막 제외)
        if i < len(steps) - 1:
            arrow = slide.shapes.add_shape(
                MSO_SHAPE.RIGHT_ARROW,
                Inches(x + 1.7), Inches(process_y + 0.15),
                Inches(0.25), Inches(0.3)
            )
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = PRIMARY_GREEN
            arrow.line.fill.background()

    # 주력 제품 표
    left = Inches(1)
    top = Inches(3.0)
    width = Inches(8)
    height = Inches(2.5)

    table = slide.shapes.add_table(4, 3, left, top, width, height).table

    # 헤더
    headers = ['재생 문구류', '에코 생활용품', '패션 소품']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 내용
    products = [
        ['재생 노트·메모지', '에코 화분·수납함', '에코백·파우치'],
        ['5,000~15,000원', '10,000~30,000원', '8,000~20,000원'],
        ['B2C 30%', 'B2B 40%', 'B2C/협력 30%']
    ]

    for row_idx, row_data in enumerate(products, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(14)
            p.alignment = PP_ALIGN.CENTER
            cell.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

def add_hr_plan_slide(prs):
    """슬라이드 5: 인력운영 계획"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "인력운영 계획"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 인력 구성 표
    left = Inches(0.8)
    top = Inches(1.8)
    width = Inches(8.4)
    height = Inches(2.5)

    table = slide.shapes.add_table(6, 5, left, top, width, height).table

    # 헤더
    headers = ['직급', '인원', '월급(만원)', '연봉(만원)', '주요 역할']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['대표', '1', '230', '2,760', '총괄 경영'],
        ['팀장A', '1', '215', '2,580', '운영·안전관리'],
        ['팀장B', '1', '215', '2,580', '재무·인사'],
        ['팀원', '7', '210', '2,520', '수거·선별·판매'],
        ['합계', '10', '2,130', '25,560', '취약계층 70%']
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.alignment = PP_ALIGN.CENTER

            # 합계 행 강조
            if row_idx == 5:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GREEN
                p.font.bold = True

    # 법적 준수사항
    compliance_box = slide.shapes.add_textbox(Inches(1), Inches(4.5), Inches(8), Inches(0.5))
    compliance_frame = compliance_box.text_frame
    compliance_frame.text = "⚖️ 법적 준수: 4대보험 가입 | 서면 근로계약 | 무기계약 전환 | 최저임금 충족"
    p = compliance_frame.paragraphs[0]
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_DARK
    p.alignment = PP_ALIGN.CENTER

    # 정부지원
    support_box = slide.shapes.add_textbox(Inches(1), Inches(5.2), Inches(8), Inches(1.2))
    support_frame = support_box.text_frame
    support_frame.text = "💰 정부지원 제도"
    p = support_frame.paragraphs[0]
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN

    support_items = ['고령자 고용지원', '사회적기업 일자리창출', '전문인력 지원', '사업개발비']
    for item in support_items:
        p = support_frame.add_paragraph()
        p.text = f"• {item}"
        p.font.size = Pt(12)
        p.level = 1

def add_channel_slide(prs):
    """슬라이드 6: 온·오프라인 채널 + 원형 차트"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "온·오프라인 채널"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 좌측: 온라인
    online_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(4), Inches(2.5))
    online_frame = online_box.text_frame

    p = online_frame.paragraphs[0]
    p.text = "🌐 온라인"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BLUE

    online_items = [
        '• 자체몰: 1년차 하반기',
        '• 플랫폼: 쿠팡·마켓컬리 (2년차)',
        '• SNS: 인스타그램·블로그',
        '• 글로벌: 3년차 이후'
    ]
    for item in online_items:
        p = online_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.space_before = Pt(6)

    # 우측: 오프라인
    offline_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.8), Inches(4), Inches(2.5))
    offline_frame = offline_box.text_frame

    p = offline_frame.paragraphs[0]
    p.text = "🏪 오프라인"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ORANGE

    offline_items = [
        '• 정기 수거: 학교·제조업체',
        '• 박람회: 연 2-3회',
        '• 체험 워크숍: 월 1회',
        '• 기업 ESG: 프로젝트 협력'
    ]
    for item in offline_items:
        p = offline_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.space_before = Pt(6)

    # 원형 차트 - 판로 비중
    chart_data = CategoryChartData()
    chart_data.categories = ['B2B', 'B2C', '기업협력', '기타']
    chart_data.add_series('비중', (40, 30, 20, 10))

    x, y, cx, cy = Inches(2.5), Inches(4.5), Inches(5), Inches(2.5)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.PIE, x, y, cx, cy, chart_data
    ).chart

    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.legend.include_in_layout = False

    # 데이터 레이블 표시
    chart.plots[0].has_data_labels = True
    data_labels = chart.plots[0].data_labels
    data_labels.show_percentage = True
    data_labels.show_category_name = True

def add_hr_expansion_slide(prs):
    """슬라이드 7: 연도별 인력 확대 계획 + 막대그래프"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "연도별 인력 확대 계획"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 표
    left = Inches(0.5)
    top = Inches(1.8)
    width = Inches(9)
    height = Inches(2.2)

    table = slide.shapes.add_table(6, 7, left, top, width, height).table

    # 헤더
    headers = ['연도', '인원', '고령층', '월인건비\n(만원)', '정부지원\n(만원)', '자부담\n(만원)', '월매출목표\n(만원)']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['1년차', '10', '7', '2,130', '1,534', '596', '800'],
        ['2년차', '12', '9', '2,556', '1,792', '764', '1,500'],
        ['3년차', '15', '10', '3,195', '1,917', '1,278', '2,800'],
        ['4년차', '18', '12', '3,834', '1,533', '2,301', '3,500'],
        ['5년차', '20', '14', '4,260', '1,065', '3,195', '4,200']
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.alignment = PP_ALIGN.CENTER

            # 3년차 강조 (손익분기점)
            if row_idx == 3:
                cell.fill.solid()
                cell.fill.fore_color.rgb = YELLOW
                p.font.bold = True

    # 막대그래프 - 고령층 인원 증가
    chart_data = CategoryChartData()
    chart_data.categories = ['1년차', '2년차', '3년차', '4년차', '5년차']
    chart_data.add_series('고령층 인원', (7, 9, 10, 12, 14))

    x, y, cx, cy = Inches(1), Inches(4.3), Inches(8), Inches(2.5)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
    ).chart

    chart.has_legend = False
    chart.has_title = True
    chart.chart_title.text_frame.text = "고령층 인원 증가 추이"

    # 값 레이블 표시
    chart.plots[0].has_data_labels = True
    data_labels = chart.plots[0].data_labels
    data_labels.show_value = True

def add_market_analysis_slide(prs):
    """슬라이드 8: 시장분석"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "시장분석"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 시장 규모 표
    left = Inches(1)
    top = Inches(1.8)
    width = Inches(8)
    height = Inches(1.5)

    table = slide.shapes.add_table(4, 4, left, top, width, height).table

    # 헤더
    headers = ['구분', '현재', '5년 후', 'CAGR']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['글로벌 재활용 시장', '79조원', '100조원', '5.2%'],
        ['국내 재활용 시장', '11조원', '14조원', '5.0%'],
        ['고령층 경제활동인구', '600만명', '630만명', '-']
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.alignment = PP_ALIGN.CENTER

    # 경쟁환경 박스
    comp_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.8), Inches(3.8),
        Inches(4), Inches(2)
    )
    comp_box.fill.solid()
    comp_box.fill.fore_color.rgb = RGBColor(255, 235, 238)
    comp_box.line.color.rgb = RED
    comp_box.line.width = Pt(2)

    text_frame = comp_box.text_frame
    p = text_frame.paragraphs[0]
    p.text = "경쟁 현황"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RED

    comp_items = ['• 재활용업체 다수 존재', '• 노인 고용 비율 낮음', '• 노인일자리기관 연계 부족']
    for item in comp_items:
        p = text_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.space_before = Pt(8)

    # 기회 박스
    opp_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(5.2), Inches(3.8),
        Inches(4), Inches(2)
    )
    opp_box.fill.solid()
    opp_box.fill.fore_color.rgb = LIGHT_GREEN
    opp_box.line.color.rgb = PRIMARY_GREEN
    opp_box.line.width = Pt(2)

    text_frame = opp_box.text_frame
    p = text_frame.paragraphs[0]
    p.text = "시장 기회"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN

    opp_items = ['• 환경×복지 통합 공백', '• 정책 지원 확대', '• ESG 수요 급증']
    for item in opp_items:
        p = text_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.space_before = Pt(8)

    # 출처
    source_box = slide.shapes.add_textbox(Inches(5), Inches(6.5), Inches(4), Inches(0.3))
    source_frame = source_box.text_frame
    source_frame.text = "출처: 통계청, 환경부, 산업리포트 2023"
    p = source_frame.paragraphs[0]
    p.font.size = Pt(10)
    p.font.color.rgb = RGBColor(102, 102, 102)
    p.alignment = PP_ALIGN.RIGHT

def add_swot_slide(prs):
    """슬라이드 9: SWOT 분석 (4사분면)"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "SWOT 분석"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 4개 박스
    box_width = 4.2
    box_height = 2.3

    swot_data = [
        {
            'title': 'Strength (강점)',
            'items': ['✓ 정부지원 접근성 우수', '✓ 높은 사회적 가치', '✓ 경쟁 강도 낮음'],
            'strategy': '정부 사업 활용, 브랜딩 강화',
            'color': LIGHT_GREEN,
            'title_color': PRIMARY_GREEN,
            'x': 0.8, 'y': 1.8
        },
        {
            'title': 'Weakness (약점)',
            'items': ['⚠ 초기투자 부담', '⚠ 사업 경험 부족', '⚠ 정책 의존도 높음'],
            'strategy': '단계적 확장, 멘토링, 수익 다각화',
            'color': RGBColor(255, 243, 224),
            'title_color': ORANGE,
            'x': 5.2, 'y': 1.8
        },
        {
            'title': 'Opportunity (기회)',
            'items': ['📈 노인일자리 정책 확대', '📈 환경기업 지원 증가', '📈 ESG 경영 확산'],
            'strategy': '정책 모니터링, B2B 강화',
            'color': RGBColor(227, 242, 253),
            'title_color': BLUE,
            'x': 0.8, 'y': 4.3
        },
        {
            'title': 'Threat (위협)',
            'items': ['⚡ 정책 변화 리스크', '⚡ 대형업체 진입', '⚡ 가격 경쟁 심화'],
            'strategy': '차별화, 품질 경쟁력 확보',
            'color': RGBColor(236, 239, 241),
            'title_color': RGBColor(149, 165, 166),
            'x': 5.2, 'y': 4.3
        }
    ]

    for swot in swot_data:
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(swot['x']), Inches(swot['y']),
            Inches(box_width), Inches(box_height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = swot['color']
        shape.line.color.rgb = swot['title_color']
        shape.line.width = Pt(2)

        text_frame = shape.text_frame
        text_frame.margin_top = Inches(0.15)
        text_frame.margin_left = Inches(0.15)

        # 제목
        p = text_frame.paragraphs[0]
        p.text = swot['title']
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = swot['title_color']

        # 항목들
        for item in swot['items']:
            p = text_frame.add_paragraph()
            p.text = item
            p.font.size = Pt(12)
            p.space_before = Pt(4)

        # 대응전략
        p = text_frame.add_paragraph()
        p.text = f"\n대응전략: {swot['strategy']}"
        p.font.size = Pt(11)
        p.font.italic = True
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

def add_marketing_slide(prs):
    """슬라이드 10: 마케팅 전략"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "마케팅 전략"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 3개 타깃 박스
    box_width = 2.8
    box_height = 2.5
    y_pos = 1.8

    targets = [
        {
            'title': 'B2B',
            'items': ['• 정기수거 계약', '• ESG 납품 제안', '• 비용절감 사례'],
            'budget': '연 400만원',
            'color': RGBColor(227, 242, 253),
            'x': 0.8
        },
        {
            'title': 'B2C',
            'items': ['• 업사이클 스토리텔링', '• 사회적 가치 마케팅', '• 제품 품질 강조'],
            'budget': '연 500만원',
            'color': RGBColor(252, 228, 236),
            'x': 3.8
        },
        {
            'title': 'B2G',
            'items': ['• 정책 연계 보고', '• 일자리 성과 지표', '• 환경 개선 효과'],
            'budget': '연 300만원',
            'color': RGBColor(243, 229, 245),
            'x': 6.8
        }
    ]

    for target in targets:
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(target['x']), Inches(y_pos),
            Inches(box_width), Inches(box_height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = target['color']
        shape.line.color.rgb = PRIMARY_GREEN
        shape.line.width = Pt(2)

        text_frame = shape.text_frame
        text_frame.margin_top = Inches(0.1)

        p = text_frame.paragraphs[0]
        p.text = f"🎯 {target['title']}"
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_GREEN
        p.alignment = PP_ALIGN.CENTER

        for item in target['items']:
            p = text_frame.add_paragraph()
            p.text = item
            p.font.size = Pt(12)
            p.space_before = Pt(4)

        p = text_frame.add_paragraph()
        p.text = f"\n💰 {target['budget']}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ORANGE
        p.alignment = PP_ALIGN.CENTER

    # 홍보 실행 표
    left = Inches(1)
    top = Inches(4.5)
    width = Inches(8)
    height = Inches(2)

    table = slide.shapes.add_table(4, 3, left, top, width, height).table

    # 헤더
    headers = ['구분', '온라인', '오프라인']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['활동', 'SNS 콘텐츠 월 8회\n블로그 포스팅', '박람회 연 2-3회\n체험 워크숍 월 1회\n언론 보도 연 4회'],
        ['연간 예산', '700만원', '500만원'],
        ['총 예산', '연간 1,200만원', '']
    ]

    for row_idx, row_data in enumerate(data, 1):
        if row_idx == 3:  # 총 예산 행
            merged_cell = table.cell(row_idx, 1)
            merged_cell.merge(table.cell(row_idx, 2))
            merged_cell.text = row_data[1]
            p = merged_cell.text_frame.paragraphs[0]
            p.font.size = Pt(14)
            p.font.bold = True
            p.alignment = PP_ALIGN.CENTER
            merged_cell.fill.solid()
            merged_cell.fill.fore_color.rgb = YELLOW
        else:
            for col_idx, text in enumerate(row_data):
                if col_idx == 0 or (row_idx < 3 and col_idx > 0):
                    cell = table.cell(row_idx, col_idx)
                    cell.text = text
                    p = cell.text_frame.paragraphs[0]
                    p.font.size = Pt(12)
                    if col_idx == 0:
                        cell.fill.solid()
                        cell.fill.fore_color.rgb = LIGHT_GREEN
                        p.font.bold = True
                        p.alignment = PP_ALIGN.CENTER

def add_operation_slide(prs):
    """슬라이드 11: 운영계획"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "운영계획"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 시설 및 생산능력 표
    left = Inches(0.8)
    top = Inches(1.8)
    width = Inches(8.4)
    height = Inches(1.3)

    table = slide.shapes.add_table(4, 4, left, top, width, height).table

    # 헤더
    headers = ['구분', '1년차', '2-3년차', '4-5년차']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['시설 면적', '300㎡', '500㎡', '800㎡+'],
        ['센터 수', '1개소', '1개소', '2개소'],
        ['선별능력', '월 12톤', '월 24톤', '월 40톤']
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.alignment = PP_ALIGN.CENTER

    # 운영 프로세스 (6단계)
    process_y = 3.3
    steps = ['수거', '선별', '포장', '저장', '판매', '정산']

    for i, step in enumerate(steps):
        x = 0.8 + i * 1.45

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(x), Inches(process_y),
            Inches(1.2), Inches(0.5)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = ACCENT_GREEN
        shape.line.color.rgb = PRIMARY_GREEN

        text_frame = shape.text_frame
        p = text_frame.paragraphs[0]
        p.text = step
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER
        text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

        # 화살표 (마지막 제외)
        if i < len(steps) - 1:
            arrow = slide.shapes.add_shape(
                MSO_SHAPE.RIGHT_ARROW,
                Inches(x + 1.25), Inches(process_y + 0.1),
                Inches(0.15), Inches(0.3)
            )
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = PRIMARY_GREEN
            arrow.line.fill.background()

    # 품질지표
    quality_box = slide.shapes.add_textbox(Inches(0.8), Inches(4.0), Inches(4), Inches(1.5))
    quality_frame = quality_box.text_frame

    p = quality_frame.paragraphs[0]
    p.text = "✅ 품질지표"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN

    quality_items = ['• 이물질 비율: ≤5%', '• 선별 오류율: ≤2%', '• 화재 안전점검: 주 1회', '• ISO 14001: 4년차 취득']
    for item in quality_items:
        p = quality_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(12)
        p.space_before = Pt(4)

    # 생산능력→매출 연결 표
    left = Inches(5), Inches(4.0)
    width = Inches(4)
    height = Inches(1.5)

    table2 = slide.shapes.add_table(4, 3, Inches(5), Inches(4.0), Inches(4), Inches(1.5)).table

    # 헤더
    headers2 = ['처리량', '제품믹스', '월매출']
    for i, header in enumerate(headers2):
        cell = table2.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data2 = [
        ['12톤/월', '30%', '800만원'],
        ['24톤/월', '40%', '1,500만원'],
        ['40톤/월', '50%', '2,800만원']
    ]

    for row_idx, row_data in enumerate(data2, 1):
        for col_idx, text in enumerate(row_data):
            cell = table2.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            p.alignment = PP_ALIGN.CENTER

def add_governance_slide(prs):
    """슬라이드 12: 조직 및 거버넌스"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "조직 및 거버넌스"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 조직구조
    org_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(4), Inches(2))
    org_frame = org_box.text_frame

    p = org_frame.paragraphs[0]
    p.text = "🏢 조직구조"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN

    org_items = [
        '대표(센터장)',
        '  ├─ 수집팀 (수거·운송)',
        '  ├─ 선별팀 (분류·가공)',
        '  └─ 판매팀 (마케팅·영업)'
    ]
    for item in org_items:
        p = org_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(12)
        p.font.name = 'Consolas'
        p.space_before = Pt(4)

    # 회계 투명성 표
    left = Inches(5.2)
    top = Inches(1.8)
    width = Inches(4)
    height = Inches(1.8)

    table = slide.shapes.add_table(5, 2, left, top, width, height).table

    # 헤더
    cell = table.cell(0, 0)
    cell.text = "💼 회계 투명성"
    cell.merge(table.cell(0, 1))
    cell.fill.solid()
    cell.fill.fore_color.rgb = BLUE
    p = cell.text_frame.paragraphs[0]
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['일일', 'POS 자동기록'],
        ['월간', '내부 검증'],
        ['분기', '외부 모니터링'],
        ['연간', '외부감사']
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            if col_idx == 0:
                p.font.bold = True
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GREEN

    # ESG 지표
    esg_y = 3.9
    esg_items = [
        {'title': 'E (환경)', 'items': ['재활용률', 'CO₂ 감축량'], 'x': 0.8},
        {'title': 'S (사회)', 'items': ['취약계층 고용', '평균 임금'], 'x': 3.5},
        {'title': 'G (지배구조)', 'items': ['이사회 운영', '재무 공개'], 'x': 6.2}
    ]

    for esg in esg_items:
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(esg['x']), Inches(esg_y),
            Inches(2.5), Inches(1.2)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = LIGHT_GREEN
        shape.line.color.rgb = PRIMARY_GREEN

        text_frame = shape.text_frame
        p = text_frame.paragraphs[0]
        p.text = esg['title']
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_GREEN

        for item in esg['items']:
            p = text_frame.add_paragraph()
            p.text = f"• {item}"
            p.font.size = Pt(11)
            p.space_before = Pt(2)

    # 리스크 관리
    risk_box = slide.shapes.add_textbox(Inches(0.8), Inches(5.3), Inches(8.4), Inches(1.5))
    risk_frame = risk_box.text_frame

    p = risk_frame.paragraphs[0]
    p.text = "⚠️ 리스크 관리: 정책변동(수익 다각화) | 원재료(다수 공급처) | 품질(공정 개선) | 인력(처우 개선)"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_DARK

def add_roadmap_slide(prs):
    """슬라이드 13: 5년 추진계획"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "5년 추진계획"
    title.text_frame.paragraphs[0].font.size = Pt(40)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 연차별 표
    left = Inches(0.5)
    top = Inches(1.8)
    width = Inches(9)
    height = Inches(3.5)

    table = slide.shapes.add_table(6, 5, left, top, width, height).table

    # 헤더
    headers = ['연차', '핵심 과제', '월매출', '인원', '손익']
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    data = [
        ['1년차', '센터 개소, 예비사회적기업\n수거 네트워크 구축', '800만', '10명', '-700만'],
        ['2년차', '온라인몰 오픈, 파트너십\n채널 다각화', '1,500만', '12명', '-456만'],
        ['3년차', '사회적기업 인증\n손익분기 달성 ⭐', '2,800만', '15명', '+155만'],
        ['4년차', '2호점 준비, ISO 추진\n제조·판매 분리', '3,500만', '18명', '+233만'],
        ['5년차', '2호점 운영, 지역 허브\n브랜드 확립', '4,200만', '20명', '+72만']
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            if col_idx == 0:
                p.font.bold = True
                p.alignment = PP_ALIGN.CENTER

            # 3년차 강조
            if row_idx == 3:
                cell.fill.solid()
                cell.fill.fore_color.rgb = YELLOW
                p.font.bold = True

    # 핵심 지표
    kpi_box = slide.shapes.add_textbox(Inches(0.8), Inches(5.5), Inches(8.4), Inches(1.3))
    kpi_frame = kpi_box.text_frame

    p = kpi_frame.paragraphs[0]
    p.text = "📊 5년 핵심 지표"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN

    kpi_items = [
        '• 누적 매출: 약 39억원  • 정부 의존도: 72%→25%  • 고령층 고용: 7명→14명  • 재활용 1,200톤, CO₂ 600톤 감축'
    ]
    for item in kpi_items:
        p = kpi_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(13)
        p.space_before = Pt(6)

def add_financial_slide(prs):
    """슬라이드 14: 5개년 재무계획 + 꺾은선 그래프"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])

    title = slide.shapes.title
    title.text = "5개년 재무계획 및 손익분기점"
    title.text_frame.paragraphs[0].font.size = Pt(36)
    title.text_frame.paragraphs[0].font.color.rgb = PRIMARY_GREEN

    # 초기투자 표 (좌상단)
    left = Inches(0.5)
    top = Inches(1.6)
    width = Inches(3)
    height = Inches(2.2)

    table1 = slide.shapes.add_table(7, 2, left, top, width, height).table

    # 헤더
    cell = table1.cell(0, 0)
    cell.text = "💰 초기투자"
    cell.merge(table1.cell(0, 1))
    cell.fill.solid()
    cell.fill.fore_color.rgb = ORANGE
    p = cell.text_frame.paragraphs[0]
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER

    # 데이터
    invest_data = [
        ['보증금', '2,000'],
        ['임차료 선납', '180'],
        ['자동선별기', '1,500'],
        ['수거차량', '2,000'],
        ['포장·자재', '500'],
        ['운영자금', '320']
    ]

    for row_idx, row_data in enumerate(invest_data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table1.cell(row_idx, col_idx)
            if col_idx == 1:
                cell.text = f"{text}만원"
            else:
                cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            if col_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GREEN

    # 5개년 손익 표
    left = Inches(3.8)
    top = Inches(1.6)
    width = Inches(5.7)
    height = Inches(2.2)

    table2 = slide.shapes.add_table(8, 6, left, top, width, height).table

    # 헤더
    headers2 = ['구분', '1년차', '2년차', '3년차', '4년차', '5년차']
    for i, header in enumerate(headers2):
        cell = table2.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    # 데이터
    finance_data = [
        ['매출', '9,600', '18,000', '33,600', '42,000', '50,400'],
        ['정부지원', '18,408', '21,504', '23,004', '18,396', '12,780'],
        ['총수입', '28,008', '39,504', '56,604', '60,396', '63,180'],
        ['인건비', '25,560', '30,672', '38,340', '46,008', '51,120'],
        ['운영비', '10,848', '14,304', '16,404', '11,592', '11,196'],
        ['총지출', '36,408', '44,976', '54,744', '57,600', '62,316'],
        ['연간손익', '-8,400', '-5,472', '+1,860', '+2,796', '+864']
    ]

    for row_idx, row_data in enumerate(finance_data, 1):
        for col_idx, text in enumerate(row_data):
            cell = table2.cell(row_idx, col_idx)
            cell.text = text if col_idx == 0 else f"{text}"
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9)
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

            if col_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GREEN
                p.font.bold = True

            # 연간손익 행 강조
            if row_idx == 7:
                p.font.bold = True
                if '+' in text:
                    p.font.color.rgb = PRIMARY_GREEN
                elif '-' in text:
                    p.font.color.rgb = RED

    # 꺾은선 그래프 - 손익 추이
    chart_data = CategoryChartData()
    chart_data.categories = ['1년차', '2년차', '3년차', '4년차', '5년차']
    chart_data.add_series('연간손익 (만원)', (-8400, -5472, 1860, 2796, 864))

    x, y, cx, cy = Inches(0.8), Inches(4.0), Inches(8), Inches(2.8)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.LINE_MARKERS, x, y, cx, cy, chart_data
    ).chart

    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.has_title = True
    chart.chart_title.text_frame.text = "손익분기점 분석 (3년차 달성)"

    # 값 레이블 표시
    chart.plots[0].has_data_labels = True
    data_labels = chart.plots[0].data_labels
    data_labels.show_value = True

def add_conclusion_slide(prs):
    """슬라이드 15: 결론 및 기대효과"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 빈 슬라이드

    # 배경색
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(248, 249, 250)

    # 제목
    title_box = slide.shapes.add_textbox(Inches(1), Inches(0.5), Inches(8), Inches(0.7))
    title_frame = title_box.text_frame
    title_frame.text = "결론 및 기대효과"
    p = title_frame.paragraphs[0]
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.alignment = PP_ALIGN.CENTER

    # 4개 효과 박스
    box_width = 4.2
    box_height = 2

    effects = [
        {
            'icon': '👥',
            'title': '사회적 효과',
            'items': ['• 5년 누적 120명·년 참여', '• 최저임금 이상 소득 보장', '• 지역 공동체 활성화'],
            'color': LIGHT_GREEN,
            'border': PRIMARY_GREEN,
            'x': 0.8, 'y': 1.5
        },
        {
            'icon': '🌍',
            'title': '환경적 효과',
            'items': ['• 누적 재활용 1,200톤', '• CO₂ 600톤 감축', '• 지역 재활용률 +5%p'],
            'color': RGBColor(227, 242, 253),
            'border': BLUE,
            'x': 5.2, 'y': 1.5
        },
        {
            'icon': '💰',
            'title': '경제적 효과',
            'items': ['• 고정직 20명 창출', '• 월 4,200만원 지역 소비', '• 지속가능 수익 모델'],
            'color': RGBColor(255, 243, 224),
            'border': ORANGE,
            'x': 0.8, 'y': 3.8
        },
        {
            'icon': '🎯',
            'title': '정책 부합',
            'items': ['• SDG 8: 양질의 일자리', '• SDG 12: 책임있는 소비', '• ESG 경영 확산 기여'],
            'color': RGBColor(243, 229, 245),
            'border': PURPLE,
            'x': 5.2, 'y': 3.8
        }
    ]

    for effect in effects:
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(effect['x']), Inches(effect['y']),
            Inches(box_width), Inches(box_height)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = effect['color']
        shape.line.color.rgb = effect['border']
        shape.line.width = Pt(3)

        text_frame = shape.text_frame
        text_frame.margin_top = Inches(0.15)

        p = text_frame.paragraphs[0]
        p.text = f"{effect['icon']} {effect['title']}"
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = effect['border']
        p.alignment = PP_ALIGN.CENTER

        for item in effect['items']:
            p = text_frame.add_paragraph()
            p.text = item
            p.font.size = Pt(13)
            p.space_before = Pt(6)

    # 최종 메시지
    msg_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(1.5), Inches(6.0),
        Inches(7), Inches(0.9)
    )
    msg_box.fill.solid()
    msg_box.fill.fore_color.rgb = LIGHT_GREEN
    msg_box.line.color.rgb = PRIMARY_GREEN
    msg_box.line.width = Pt(3)

    text_frame = msg_box.text_frame
    text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = text_frame.paragraphs[0]
    p.text = "환경과 복지를 연결하여\n지속가능한 사회적 가치를 실현합니다"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.alignment = PP_ALIGN.CENTER
    p.line_spacing = 1.3

def main():
    """메인 함수"""
    print("📊 환경-복지 연결 노인일자리 창출사업 프레젠테이션 생성 중...")

    # 프레젠테이션 생성
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    print("1/15 표지 슬라이드 생성 중...")
    add_title_slide(prs)

    print("2/15 회사소개 슬라이드 생성 중...")
    add_company_intro_slide(prs)

    print("3/15 창업배경 슬라이드 생성 중...")
    add_background_slide(prs)

    print("4/15 비즈니스 모델 슬라이드 생성 중...")
    add_business_model_slide(prs)

    print("5/15 인력운영 계획 슬라이드 생성 중...")
    add_hr_plan_slide(prs)

    print("6/15 온·오프라인 채널 슬라이드 생성 중...")
    add_channel_slide(prs)

    print("7/15 연도별 인력 확대 슬라이드 생성 중...")
    add_hr_expansion_slide(prs)

    print("8/15 시장분석 슬라이드 생성 중...")
    add_market_analysis_slide(prs)

    print("9/15 SWOT 분석 슬라이드 생성 중...")
    add_swot_slide(prs)

    print("10/15 마케팅 전략 슬라이드 생성 중...")
    add_marketing_slide(prs)

    print("11/15 운영계획 슬라이드 생성 중...")
    add_operation_slide(prs)

    print("12/15 조직 및 거버넌스 슬라이드 생성 중...")
    add_governance_slide(prs)

    print("13/15 5년 추진계획 슬라이드 생성 중...")
    add_roadmap_slide(prs)

    print("14/15 재무계획 슬라이드 생성 중...")
    add_financial_slide(prs)

    print("15/15 결론 슬라이드 생성 중...")
    add_conclusion_slide(prs)

    # 저장
    output_file = '/home/user/marp-core/환경복지_노인일자리_사업계획서.pptx'
    prs.save(output_file)
    print(f"\n✅ 프레젠테이션 생성 완료!")
    print(f"📁 파일 위치: {output_file}")
    print(f"📊 총 슬라이드 수: {len(prs.slides)}개")

if __name__ == '__main__':
    main()
