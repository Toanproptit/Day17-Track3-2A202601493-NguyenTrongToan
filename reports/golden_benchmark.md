# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **3482.8 ms**
- Average token reduction vs full source context: **1.0%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 2396.9 | 831 | 0.0% |  |
| G09 | long_term | PASS | 1523.1 | 1508 | 0.0% |  |
| G12 | semantic | PASS | 1626.4 | 878 | 0.0% |  |
| G14 | semantic | PASS | 2261.1 | 650 | 0.0% |  |
| G15 | semantic | PASS | 1377.8 | 650 | 0.0% |  |
| G19 | mixed | PASS | 6622.6 | 581 | 0.0% |  |
| G03 | long_term | PASS | 2727.3 | 1498 | 0.0% |  |
| G04 | long_term | PASS | 2134.8 | 1485 | 0.0% |  |
| G05 | long_term | PASS | 3432.6 | 1501 | 0.0% |  |
| G10 | episodic | PASS | 500.6 | 582 | 0.0% |  |
| G11 | episodic | PASS | 305.0 | 614 | 0.0% |  |
| G13 | semantic | PASS | 25287.6 | 816 | 0.0% |  |
| G16 | mixed | PASS | 3129.9 | 581 | 0.0% |  |
| G18 | mixed | PASS | 2283.0 | 500 | 11.5% |  |
| G20 | mixed | PASS | 2772.0 | 831 | 0.0% |  |
| G06 | long_term | PASS | 4784.7 | 1509 | 0.0% |  |
| G07 | long_term | PASS | 1546.9 | 1506 | 0.0% |  |
| G17 | mixed | PASS | 4944.2 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lab Assistant mentioned Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: LOTUS-88 uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lab Assistant mentioned LOTUS-88. [valid_at=2026-08-01T11:00:20Z, `

### G09 - long_term

`FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen dislikes Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen has a to-do to complete the benchmark report before Saturday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen identifies connection churn as the primary issue. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Minh Nguyen's attempt to debug async HTTP failed. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [v`

### G12 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G14 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lab Assistant mentioned Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: LOTUS-88 uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lab Assistant mentioned LOTUS-88. [valid_at=2026-08-01`

### G03 - long_term

`FACT: 'ca nhan ORCHID-27' demo avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: 'ca nhan ORCHID-27' demo prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: When explaining code, Minh Nguyen prefers to use short examples with Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen dislikes Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen has a to-do to complete the benchmark report before Saturday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguy`

### G04 - long_term

`FACT: Minh Nguyen has a to-do to complete the benchmark report before Saturday at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen often confuses Task with coroutine when learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen often confuses coroutine with Task when learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:20Z] FACT: Minh Nguyen's attempt to debug async HTTP failed. [va`

### G05 - long_term

`FACT: Minh Nguyen often confuses Task with coroutine when learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen often confuses coroutine with Task when learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: The assistant prioritizes coroutine and Task. [valid_at=2026-08-01T09:02:20Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen's attempt to debug async H`

### G10 - episodic

`EPISODE: Minh dang viet mot cai note tong ket ngan de tuan sau trinh bay cho ca nhom nghe ve cach minh phan biet giua viec ca nhan va viec o cong ty, vi may ban trong nhom hay bi lan lon. D EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Sang mai minh phai hop review tien do voi mentor nen toi nay minh muon don dep lai het may thu con dang do. Minh biet minh con vai viec chua chot xong nhung dau oc dang roi qua kho EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp Cli`

### G11 - episodic

`EPISODE: Minh dang viet mot cai note tong ket ngan de tuan sau trinh bay cho ca nhom nghe ve cach minh phan biet giua viec ca nhan va viec o cong ty, vi may ban trong nhom hay bi lan lon. D EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Sang mai minh phai hop review tien do voi mentor nen toi nay minh muon don dep lai het may thu con dang do. Minh biet minh con vai viec chua chot xong nhung dau oc dang roi qua kho EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai`

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data witho`

### G16 - mixed

`<LONG_TERM> FACT: Lab Assistant is demonstrating the 'ca nhan ORCHID-27' demo. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: 'ca nhan ORCHID-27' demo avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: 'ca nhan ORCHID-27' demo prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen's attempt to debug async HTTP failed. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00`

### G18 - mixed

`<EPISODIC> EPISODE: Minh dang viet mot cai note tong ket ngan de tuan sau trinh bay cho ca nhom nghe ve cach minh phan biet giua viec ca nhan va viec o cong ty, vi may ban trong nhom hay bi lan lon. D EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Sang mai minh phai hop review tien do voi mentor nen toi nay minh muon don dep lai het may thu con dang do. Minh biet minh con vai viec chua chot xong nhung dau oc dang roi qua kho EPISODE: Minh dang chuan bi tu on lai phan async cua Python vi tuan sau co bai kiem tra nho, ma minh thi hoc kieu de va`

### G20 - mixed

`<LONG_TERM> FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen's attempt to debug async HTTP failed. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task when learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen often confuses Task with coroutine when learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: 'ca nhan ORCHID-27' demo avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] `

### G06 - long_term

`FACT: Python is prohibited for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: 'ca nhan ORCHID-27' demo prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: The BLUEBIRD-42 project requires the use of TypeScript for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: The BLUEBIRD-42 project requires the use of NestJS for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: When explaining code, Minh Nguyen prefers to use short examples with Python. [valid_at=2026-08-01T09:00:00Z, in`

### G07 - long_term

`FACT: 'ca nhan ORCHID-27' demo avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: Lab Assistant is demonstrating the 'ca nhan ORCHID-27' demo. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=2026-08-03T10:03:20Z] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen's attempt to debug async HTTP failed. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: 'ca nhan ORCHID-27' demo prioritizes Python. [valid_at=2026`

### G17 - mixed

`<LONG_TERM> FACT: The BLUEBIRD-42 project requires the use of TypeScript for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The BLUEBIRD-42 project requires the use of NestJS for its backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: 'ca nhan ORCHID-27' demo avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: Python is prohibited for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: 'ca nhan ORCHID-27' demo prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08`
