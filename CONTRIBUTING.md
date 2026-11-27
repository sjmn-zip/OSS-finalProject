# Contributing

Thank you for helping with the Lost & Found Feed project! This guide explains how we work together. (Lost & Found Feed 프로젝트에 기여해 주셔서 고맙습니다. 이 문서는 우리 팀이 함께 일하는 방법을 설명합니다.)

Everyone who takes part in this project must follow our [Code of Conduct](CODE_OF_CONDUCT.md). (이 프로젝트에 참여하는 모든 사람은 [행동 강령](CODE_OF_CONDUCT.md)을 따라야 합니다.)

---

## 1. Pick an issue (이슈 고르기)

* Every task is a GitHub issue with an owner and acceptance criteria. (모든 작업은 담당자와 완료 조건이 있는 GitHub 이슈로 관리합니다.)
* Before you start, comment on the issue or assign yourself. (작업을 시작하기 전에 이슈에 댓글을 남기거나 자신을 담당자로 지정합니다.)
* Do not take an issue that someone else has already claimed. (다른 사람이 이미 맡은 이슈는 가져가지 않습니다.)
* Work on only one or two issues at a time. (한 번에 한두 개의 이슈만 작업합니다.)
* Move the issue on the project board as you go: Backlog → Ready → In progress → In review → Done. (작업 진행에 따라 프로젝트 보드에서 이슈를 옮깁니다.)

If you find a bug or have an idea that has no issue yet, open a new issue first. (이슈가 없는 버그나 아이디어가 있으면 먼저 새 이슈를 만듭니다.)

## 2. Set up your environment (개발 환경 설정)

You need **Python 3.10 or newer**, the same version as our CI. (CI와 같은 **Python 3.10 이상**이 필요합니다.)

```bash
# create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# set the API key (never commit your key)
export LOST_FOUND_API_KEY="your-key"   # Windows PowerShell: $env:LOST_FOUND_API_KEY="your-key"

# start the server
uvicorn app.main:app --reload
```

See the [README](README.md#1-get-an-api-key) for how to get an API key from data.go.kr. If you do not have a key, use sample data mode. (API 키 발급 방법은 [README](README.md#1-get-an-api-key)를 보세요. 키가 없으면 샘플 데이터 모드를 사용합니다.)

## 3. Create a branch (브랜치 만들기)

Never commit directly to `main`. Create a branch for each issue. (`main`에 직접 커밋하지 않습니다. 이슈마다 브랜치를 만듭니다.)

```bash
git switch main
git pull
git switch -c feature/12-region-filter
```

Branch names: `<type>/<issue-number>-<short-description>` (브랜치 이름 규칙)

| Type | Use for |
|---|---|
| `feature` | New features (새 기능) |
| `fix` | Bug fixes (버그 수정) |
| `docs` | Documentation only (문서만 수정) |
| `refactor` | Code changes that do not change behavior (동작이 바뀌지 않는 코드 정리) |

## 4. Write code (코드 작성)

* Follow PEP 8: 4-space indentation and `snake_case` names. (PEP 8을 따릅니다: 4칸 들여쓰기, `snake_case` 이름.)
* Add docstrings to public functions and classes. (공개 함수와 클래스에는 docstring을 씁니다.)
* Use meaningful variable and function names. (의미 있는 변수명과 함수명을 씁니다.)
* Handle errors and edge cases, such as empty results, a missing API key or a failed API request. (빈 결과, API 키 없음, API 요청 실패 같은 오류와 예외 상황을 처리합니다.)
* Keep personal information hidden. Do not show photos of ID cards, credit cards or passports. (개인정보를 보호합니다. 신분증, 신용카드, 여권 사진은 보여주지 않습니다.)
* If you add or remove a package, update `requirements.txt`. (패키지를 추가하거나 제거하면 `requirements.txt`를 업데이트합니다.)

## 5. Test your change (테스트)

Run the tests before you open a pull request. (풀 리퀘스트를 열기 전에 테스트를 실행합니다.)

```bash
python -m pytest
```

* Add tests for new or changed behavior. (새로 추가하거나 바뀐 동작에는 테스트를 추가합니다.)
* Use sample data in tests, not live API calls. (테스트에서는 실제 API 호출 대신 샘플 데이터를 사용합니다.)
* If you changed the UI, open the page in your browser and check it. (UI를 바꿨다면 브라우저에서 직접 확인합니다.)

## 6. Commit (커밋)

Write short commit messages in the imperative mood. (커밋 메시지는 짧게, 명령형으로 씁니다.)

```
Add region filter to the feed page
Fix crash when the API returns no items
```

**Never commit** (절대 커밋하지 않을 것):

* API keys or `.env` files (API 키, `.env` 파일)
* The `.venv` folder (`.venv` 폴더)
* Scratch or debug scripts (임시 스크립트, 디버그용 파일)

If you committed a key by mistake, tell the team right away and issue a new key on data.go.kr. (실수로 키를 커밋했다면 바로 팀에 알리고 data.go.kr에서 키를 재발급받습니다.)

## 7. Open a pull request (풀 리퀘스트 열기)

* Push your branch and open a pull request to `main`. (브랜치를 푸시하고 `main`으로 풀 리퀘스트를 엽니다.)
* Fill in every section of the pull request template. (풀 리퀘스트 템플릿의 모든 항목을 채웁니다.)
* Link the issue with a closing keyword, such as `Closes #12`. (`Closes #12`처럼 닫는 키워드로 이슈를 연결합니다.)
* Keep each pull request focused on one change. (풀 리퀘스트 하나에는 변경 하나만 담습니다.)
* Each member opens the pull request that connects their own part to the app. (각자 맡은 부분을 앱에 연결하는 풀 리퀘스트는 본인이 엽니다.)

## 8. Review (리뷰)

* Every pull request must be reviewed and approved by another teammate before merging. (모든 풀 리퀘스트는 머지 전에 다른 팀원의 리뷰와 승인을 받아야 합니다.)
* Do not merge your own pull request without a review. (리뷰 없이 자신의 풀 리퀘스트를 머지하지 않습니다.)
* As a reviewer, check that the code works, matches the issue's acceptance criteria and follows this guide. (리뷰어는 코드가 동작하는지, 이슈의 완료 조건을 만족하는지, 이 가이드를 따르는지 확인합니다.)
* Keep review comments kind and specific. Explain *why* you suggest a change. (리뷰 댓글은 친절하고 구체적으로 씁니다. 수정을 제안할 때는 이유를 설명합니다.)

## 9. Using AI tools (AI 도구 사용)

* Use AI for bounded tasks, one issue at a time. (AI는 이슈 하나 단위의 범위가 정해진 작업에 사용합니다.)
* Do not submit code you do not understand, even if AI wrote it. (AI가 작성했더라도 본인이 이해하지 못한 코드는 올리지 않습니다.)
* Be ready to explain every line you submit. (제출한 모든 줄을 직접 설명할 수 있어야 합니다.)
* Fill in the **AI usage** section of the pull request: the tool, what it helped with and how you checked the result. Write "None" if you did not use AI. (풀 리퀘스트의 **AI usage** 항목에 사용한 도구, 도움받은 부분, 결과를 확인한 방법을 적습니다. AI를 쓰지 않았다면 "None"이라고 씁니다.)

## 10. Data (데이터)

* The found-item data comes from the National Police Agency through data.go.kr and follows the provider's terms, not our MIT License. (습득물 데이터는 data.go.kr을 통해 경찰청에서 제공하며, 우리 MIT 라이선스가 아니라 제공처의 이용 조건을 따릅니다.)
* Do not commit large raw API responses. Keep sample data small. (큰 API 응답 원본은 커밋하지 않습니다. 샘플 데이터는 작게 유지합니다.)

## Questions (질문)

If you are stuck or unsure, ask in the issue or contact a maintainer: @uyeonee, @ogang9999, @ITM-MSJ, @sjmn-zip. (막히거나 헷갈리면 이슈에 질문하거나 메인테이너에게 연락하세요.)



#PR template

<!--
PR title: a short summary of the change
-->

## Related issue
<!-- Use a closing keyword so the issue closes automatically when this PR is merged. -->
Closes #

## What does this change and why?
<!-- What problem does this PR solve, and how did you solve it? -->


## Files changed
<!-- List the main files and what each one does. -->
- 

## How was this tested?
<!-- e.g. test results, URLs you opened in the browser, edge cases you tried -->
- [ ] `python -m pytest` passes locally
- 

## Screenshots
<!-- Only if the UI changed. Delete this section otherwise. -->


## AI usage
<!-- Required by our README. Write "None" if you did not use AI. -->
- Tool:
- What it helped with:
- How a human checked the result:

## Author checklist
- [ ] I understand every line of code in this PR
- [ ] Code follows PEP 8 (4-space indentation, snake_case names, docstrings)
- [ ] Variable and function names are meaningful
- [ ] Errors and edge cases are handled (e.g. empty results, missing API key)
- [ ] No API keys, `.env`, `.venv`, or test-only files are committed
- [ ] `requirements.txt` is updated if I added a package
- [ ] README or other docs are updated if needed


