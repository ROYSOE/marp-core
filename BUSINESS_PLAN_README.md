# 환경-복지 연결 노인일자리 창출사업 프레젠테이션

## 📋 개요

이 프레젠테이션은 환경과 복지를 연결하는 노인일자리 창출사업의 사업계획서입니다.
Marp를 사용하여 Markdown 형식으로 작성되었습니다.

## 📁 파일 구성

- `business-plan-presentation.md` - 메인 프레젠테이션 파일 (15개 슬라이드)
- `business-plan-theme.css` - 커스텀 CSS 테마 파일
- `BUSINESS_PLAN_README.md` - 이 파일

## 🎯 슬라이드 구성 (총 15개)

1. **표지** - 제목 및 기본 정보
2. **회사소개** - 비전 및 핵심가치
3. **창업배경 및 동기** - 노인빈곤, 환경위기, 통합모델 필요성
4. **비즈니스 모델** - 가치사슬 및 제품군
5. **인력운영 계획** - 조직구성 및 임금체계
6. **온·오프라인 채널** - 판매채널 전략
7. **연도별 인력 확대 계획** - 5개년 인력 로드맵
8. **시장분석** - 시장규모 및 경쟁환경
9. **SWOT 분석** - 강점, 약점, 기회, 위협
10. **마케팅 전략** - B2B/B2C/B2G 전략
11. **운영계획** - 시설, 프로세스, 품질지표
12. **조직 및 거버넌스** - 조직구조, 회계, ESG, 리스크
13. **5년 추진계획** - 연차별 목표 및 성과지표
14. **5개년 재무계획 및 손익분기점** - 초기투자, 손익계획
15. **결론 및 기대효과** - 사회적/환경적/경제적 효과

## 🚀 사용 방법

### 1. Marp CLI로 변환

```bash
# HTML로 변환
npx @marp-team/marp-cli business-plan-presentation.md -o output.html

# PDF로 변환
npx @marp-team/marp-cli business-plan-presentation.md -o output.pdf

# PowerPoint로 변환
npx @marp-team/marp-cli business-plan-presentation.md -o output.pptx
```

### 2. VS Code에서 미리보기

1. VS Code에 [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) 확장 설치
2. `business-plan-presentation.md` 파일 열기
3. `Ctrl+Shift+V` (또는 `Cmd+Shift+V`)로 미리보기 실행

### 3. 온라인 에디터 사용

[Marp Web](https://web.marp.app/)에서 파일 내용을 복사하여 사용 가능

## ✏️ 커스터마이징

### 개인정보 수정

파일에서 다음 항목을 수정하세요:

```markdown
**작성자:** [학번] [이름]      ← 여기에 학번과 이름 입력
**제출처:** [학교명]            ← 여기에 학교명 입력
```

### 이미지 추가

프레젠테이션의 이미지 플레이스홀더 위치에 실제 이미지를 추가할 수 있습니다:

```markdown
<!-- 이미지 플레이스홀더: img_company_sustainable.jpg -->
![회사 지속가능성](./images/company_sustainable.jpg)
```

권장 이미지:
- 회사 앰블럼: 5cm×5cm (표지)
- 지속가능성 이미지: 8cm×6cm (슬라이드 2)
- 재활용 배경: 투명도 20% (슬라이드 3)
- 업사이클 제품: 제품 이미지 (슬라이드 4)
- 재활용 시설: 시설 사진 (슬라이드 8)

### 색상 변경

`business-plan-theme.css` 파일에서 색상 변수를 수정:

```css
:root {
  --primary-green: #2E7D32;   /* 주요 녹색 */
  --light-green: #E8F5E9;     /* 연한 녹색 */
  --accent-green: #2ECC71;    /* 강조 녹색 */
  /* ... */
}
```

## 📊 주요 특징

- ✅ 반응형 레이아웃
- ✅ 표와 차트가 포함된 데이터 시각화
- ✅ 색상 구분을 통한 정보 구조화
- ✅ 3컬럼/4컬럼 그리드 레이아웃
- ✅ SWOT, 재무계획 등 전문적인 비즈니스 내용
- ✅ 한글 폰트 최적화 (맑은 고딕)

## 💡 팁

1. **프레젠테이션 모드**: 브라우저에서 `F11`을 눌러 전체화면으로 발표
2. **인쇄**: PDF로 변환 후 인쇄하면 깔끔한 문서 출력 가능
3. **수정**: Markdown 형식이므로 텍스트 에디터로 쉽게 수정 가능
4. **버전 관리**: Git으로 버전 관리가 용이함

## 📝 라이선스

이 프레젠테이션 템플릿은 교육 및 비즈니스 목적으로 자유롭게 사용 가능합니다.

## 🔗 참고 자료

- [Marp 공식 문서](https://marp.app/)
- [Marp CLI 사용법](https://github.com/marp-team/marp-cli)
- [Markdown 문법 가이드](https://www.markdownguide.org/)
