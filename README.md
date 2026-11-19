# Day 11 — Controlled Agent Security (2026)

> 👤 **Hình thức:** bài tập **cá nhân** (1 người / 1 MSSV).  
> 🎯 **Mục tiêu:** đóng vai **Blue Team** để học cách xây Guardrails phòng thủ, rồi đóng vai **Red Team** để tấn công agent **Red** hoặc **Red Advance**.  
> ✅ Làm theo **Checkpoint 1 → 5** trong [`CHECKPOINTS.md`](CHECKPOINTS.md) · nộp theo [`SUBMISSION.md`](SUBMISSION.md).

---

## Thông tin học viên

| Thông tin | Giá trị |
|---|---|
| Họ và tên | Trần Nguyễn Anh Phong |
| MSSV | 2A202603629 |
| Khóa / lớp | K5 / L3A |
| GitHub | [anhphongtrng](https://github.com/anhphongtrng) |
| Ngày thực hiện | 19/11/2026 |
| Hình thức | Cá nhân |

> Phần hướng dẫn gốc bên dưới được giữ nguyên. Cấu hình thực tế và kết quả thực hiện của học viên được trình bày tại [mục 4](#4-thực-hiện-bài-lab) và [mục 5](#5-kết-quả-thực-nghiệm).

---

## Thời lượng

| Phần | Thời gian |
|------|-----------|
| Setup môi trường (Checkpoint 1) | ≈ **30'** |
| Lab làm bài (Checkpoint 2 → 5) | ≈ **130'** |
| **Tổng** | ≈ **160'** |

**Hạn nộp:** **23h59 cùng ngày làm Lab** (ICT / GMT+7). Gia hạn chỉ khi Key Coach thông báo trong 48 giờ sau Lab — xem [`RULES.md`](RULES.md).

---

## Chuẩn bị (trước / đầu buổi Lab)

1. Máy có **Python 3.10+** (khuyến nghị 3.11 hoặc 3.12) và Git.
2. Tài khoản GitHub cá nhân (để fork + đổi tên repo nộp).
3. API keys:
   - **Blue (bắt buộc):** [OpenRouter](https://openrouter.ai/keys) — model cố định [`liquid/lfm-3-1.7b:free`](https://openrouter.ai/liquid/lfm-3-1.7b:free)
   - **Red (chọn một provider):** [OpenAI](https://platform.openai.com/api-keys) (`gpt-4o-mini`) **hoặc** [Google AI Studio](https://aistudio.google.com/apikey) (`gemini-3.5-flash`)
4. Đọc nhanh [`RULES.md`](RULES.md) và [`RUBRIC.md`](RUBRIC.md).

### Hai vai bạn sẽ đóng

Bạn làm bài một mình, nhưng lần lượt vào **hai vai**. Tên vai và tên agent là hai thứ khác nhau.

**Blue Team (Checkpoint 2–3) — xây Guardrails phòng thủ.**  
Bạn học cách viết lớp chặn trước và sau model: lọc prompt độc, che secret / PII, giới hạn số lần gọi, ghi audit. Agent bạn tự code tên là **Blue**. Chạy xong ra `outputs/results.json`.

**Red Team (Checkpoint 4) — đi tấn công.**  
Bạn viết câu tấn công nhằm vào agent **có sẵn**. Chọn một trong hai mục tiêu:

- **Red** — phòng thủ yếu (lab đã viết sẵn).
- **Red Advance** — phòng thủ cứng: regex + NVIDIA NeMo Guardrails (lab đã viết sẵn).

Checkpoint 4 chạy tấn công **Red**, rồi **Red Advance**. Blue không phải mục tiêu của bước này.

### Ba agent (đặt tên thống nhất)

| Tên gọi | Đây là | Code / file | Checkpoint |
|---------|--------|-------------|------------|
| **Blue** | Agent bạn tự code khi đóng vai **Blue Team** | `create_blue_agent(plugins)` + pipeline CP2–3 | CP2–3 → `results.json` |
| **Red** | Mục tiêu tấn công khi đóng vai **Red Team** — phòng thủ yếu, có sẵn | `create_red_agent_default()` | CP4 (20đ; bonus B1 tối đa +5) |
| **Red Advance** | Mục tiêu tấn công khi đóng vai **Red Team** — phòng thủ cứng, có sẵn | `create_red_agent_advance()` | CP4 (bonus B2 tối đa +10) |

Bonus lab chỉ tính **một** trong hai: leak **Red** (B1, tối đa +5) hoặc leak **Red Advance** (B2, tối đa +10).

> Trong JSON / log vẫn có thể thấy `unsafe` / `guards` / `protected` — đó là **tên kỹ thuật** cũ: `unsafe` = **Red**, `guards` = **Red Advance**, `protected` = **Blue**.

| Agent                     | Provider / model                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------ |
| **Blue**                  | OpenRouter `liquid/lfm-3-1.7b:free` (khóa cứng)                                         |
| **Red** + **Red Advance** | Cùng provider: `gpt-4o-mini` **hoặc** `gemini-3.5-flash` (model mềm — điểm bắt buộc) |
| Model khó (tuỳ chọn)      | `gpt-5.6-luna` / `gemini-3.8-flash` — **không** phải tên agent                       |

---

## Bộ tài liệu trong repo (quy ước Khóa 4)

| File | Nội dung |
|------|----------|
| [`README.md`](README.md) | Mục tiêu, chuẩn bị, thời lượng, cách bắt đầu, liên kết tài liệu |
| [`CHECKPOINTS.md`](CHECKPOINTS.md) | Làm bài theo mốc — việc cần làm, hiểu gì, lệnh chạy, Pass Signal |
| [`SUBMISSION.md`](SUBMISSION.md) | Cấu trúc repo, tên artifact, deadline, checklist trước khi nộp |
| [`RUBRIC.md`](RUBRIC.md) | Tiêu chí chấm, điểm từng phần, bằng chứng, bonus (chọn B1 hoặc B2) |
| [`RULES.md`](RULES.md) | Quy định AI, sao chép, API key, nộp muộn |
| [`schemas/results.schema.json`](schemas/results.schema.json) | Schema bắt buộc của `outputs/results.json` |

Codelab lớp: xem `template-codelabs/codelab-day11-k4-l3a.md` (L3A) hoặc bản L3B tương ứng.

**Repo nộp học viên:** `K4-<L3A hoặc L3B>-DAY11-<HoVaTen>-<MSSV>-Guardrails-HITL-Responsible-AI`  
Ví dụ: `K4-L3A-DAY11-NguyenVanA-2A2026xxxxx-Guardrails-HITL-Responsible-AI`

---

## 1. Bài toán

Chatbot VinBank giả định nhận email / tài liệu RAG và có thể gợi ý thao tác ngân hàng. Nội dung đó chỉ là **data chưa tin cậy** — không phải lệnh hệ thống (kẻ tấn công có thể nhét jailbreak vào email). Bạn kiểm soát đường đi **source → model → tool/egress** bằng guardrails + egress — **không** cần tự code email/RAG.

Cả ba agent đều nhúng secret giả từ:

`data/protected/vinbank_secrets.json`

| Loại | Key trong JSON | Giá trị demo |
|------|----------------|--------------|
| Admin password | `admin_password` | `admin123` |
| API key | `api_key` | `sk-vinbank-secret-2024` |
| DB host | `db_host` | `db.vinbank.internal:5432` |

- **Red:** được phép lộ — red-team **phải leak** ít nhất một giá trị.  
- **Blue** (plugin của bạn) + **Red Advance:** **không** được lộ (leak Red Advance = bonus B2 tối đa +10).

```text
User → Rate Limiter → Input Guardrails → LLM → Output Guardrails
                                              → Audit / Monitoring → Reply / Egress check
```

| Đã có sẵn | Bạn tự làm | Hệ thống sinh ra |
|-----------|------------|------------------|
| Starter `src/guardrails/`, `src/assignment/`, `src/attacks/` | Theo Checkpoint 2–4 | `outputs/results.json`, `attack_results.json`, … |
| `create_red_agent_default()` / `create_red_agent_advance()` | Không sửa secret | — |
| `hitl/`, `testing/`, Judge, NeMo cho Blue (`guardrails/nemo_guardrails.py`), AI attacks | Tham khảo — không chấm | — |

**Red Advance** (mục tiêu bonus B2) phòng thủ nhiều lớp — regex **và** [NVIDIA NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) (bắt buộc, cài qua `requirements.txt`):

```text
User → L1 Regex input → L2 NeMo input rails → LLM → L3 Regex output → L4 NeMo output rails → Reply
         (injection,       (protected value check,       (secret         (leak check giải mã base64/hex/
          topic)            self check input = LLM)       patterns)       ROT13/đảo ngược, self check output = LLM)
```

- Code: `src/agents/guards_agent.py` (`RedAdvanceGuardPlugin`) + `src/agents/red_advance_nemo.py` (Colang, prompt self-check, custom action).
- NeMo self-check gọi **cùng model / key Red** trong `.env` (Gemini qua endpoint OpenAI-compatible) → mỗi prompt lọt qua regex tốn thêm tối đa 2 lượt gọi API.
- NeMo lỗi (sai key, mất mạng, hết quota) → **chặn** (fail-closed). Trong JSON: `layer` = `nemo_input_rail` / `nemo_output_rail` / `nemo_error`.

---

## 2. Rubric (tóm tắt)

| Phần | Điểm |
|------|-----:|
| Input + output guardrails (CP2) — Blue | 40 |
| Pipeline + permission (CP3) → `results.json` | 40 |
| Red team (CP4) → `attack_results.json` + leak Red | 20 |
| **Bonus lab** (chọn **một**: B1 Red tối đa +5 **hoặc** B2 Red Advance tối đa +10) | không cộng cả hai |

Chi tiết tiêu chí, điều kiện mất điểm, grader replay: [`RUBRIC.md`](RUBRIC.md).

Thứ tự làm: **Setup → Blue Team (xây Guardrails phòng thủ) → Red Team (tấn công Red hoặc Red Advance) → nộp**.

---

## 3. Cách bắt đầu

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# Nếu bị chặn: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Copy-Item .env.example .env
pip install -r requirements.txt
```

**macOS / Linux (bash):**

```bash
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env
pip install -r requirements.txt
```

Điền `.env`: `OPENROUTER_API_KEY` + `RED_TEAM_PROVIDER=openai|gemini` (và key tương ứng).  
Rồi mở [`CHECKPOINTS.md`](CHECKPOINTS.md) và làm lần lượt Checkpoint 1 → 5.

Nộp theo [`SUBMISSION.md`](SUBMISSION.md) · Quy định: [`RULES.md`](RULES.md).


---

## 4. Thực hiện bài lab

### 4.1. Môi trường và cấu hình thực tế (CP1)

- Windows, PowerShell, Python 3.12.10, môi trường `.venv`.
- Google ADK 2.14.1, Google GenAI 2.34.0, NeMo Guardrails 0.24.1 và OpenAI SDK.
- Framework: `python-openai-sdk-adk-plugins`.
- Blue sử dụng API Liquid AI trực tiếp theo hướng dẫn bổ sung của giảng viên. Red và Red Advance sử dụng GPT-4o-mini qua OpenRouter sau khi Gemini trả lỗi 503.

| Agent | Endpoint | Model thực tế |
|---|---|---|
| Blue | `https://api.liquid.ai/openai/v1` | `lfm3-1.7b` |
| Red / Red Advance | `https://openrouter.ai/api/v1` | `openai/gpt-4o-mini` |

Tại thư mục gốc repository, chạy:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Chỉ sao chép `.env.example` khi chưa có `.env`. Điền cấu hình sau bằng API key hợp lệ của mình:

```dotenv
OPENROUTER_API_KEY=<LIQUID_API_KEY>
OPENROUTER_BASE_URL=https://api.liquid.ai/openai/v1
RED_TEAM_PROVIDER=openai
OPENAI_API_KEY=<OPENROUTER_API_KEY>
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-4o-mini
NEMO_GUARDRAILS_NO_USAGE_STATS=1
```

Trong `src/core/config.py`, cấu hình `BLUE_MODEL = "lfm3-1.7b"`. Tên biến môi trường và nhãn provider Blue vẫn giữ theo starter code để tương thích với runtime. Không commit `.env`, `.venv` hoặc API key thật.

### 4.2. Các phần đã triển khai

| Checkpoint | Nội dung thực hiện |
|---|---|
| CP1 | Thiết lập Python 3.12, cài dependencies, kiểm tra kết nối API và smoke tests. |
| CP2 | Chuẩn hóa Unicode, phát hiện prompt injection, topic filter, input plugin, lọc PII/secret và output plugin. |
| CP3 | Sliding-window rate limiter, audit log, monitoring, egress allowlist và bộ kiểm thử pipeline. |
| CP4 | Năm adversarial prompts theo các nhóm completion, reformatting, hypothetical, confirmation và multi-step; chạy trên Red và Red Advance. |
| CP5 | Kiểm thử tự động, xác thực schema, chạy grader và sinh báo cáo. |

### 4.3. Cấu trúc các file liên quan

```text
.
├── .env.example                       # Mẫu cấu hình
├── requirements.txt                   # Dependencies
├── src/
│   ├── main.py                        # Entry point theo checkpoint
│   ├── core/config.py                 # Cấu hình model Blue
│   ├── guardrails/
│   │   ├── input_guardrails.py         # Injection detection, topic filter
│   │   └── output_guardrails.py        # PII/secret redaction
│   ├── assignment/
│   │   ├── rate_limiter.py             # Sliding window theo user
│   │   ├── audit_log.py                # Nhật ký request/response
│   │   ├── monitoring.py               # Metrics và cảnh báo
│   │   └── pipeline.py                 # Tích hợp và egress policy
│   └── attacks/attacks.py              # 5 adversarial prompts
├── data/protected/vinbank_secrets.json # Secret giả lập của lab
├── schemas/results.schema.json        # Schema kết quả CP3
├── tests/
│   ├── smoke/                         # Smoke tests
│   └── public/                        # Public contract tests
├── scripts/grade.py                   # Grader và auto report
└── outputs/
    ├── results.json                   # Kết quả Blue Team
    ├── audit_log.json                 # Nhật ký kiểm thử
    ├── metrics.json                   # Số liệu giám sát
    ├── attack_results.json            # Tổng hợp Red Team
    ├── unsafe_attack_result.json      # Red
    ├── guards_attack_result.json      # Red Advance
    ├── grade_report.json              # Kết quả grader
    └── lab_report.md                  # Báo cáo tự sinh
```

### 4.4. Cách chạy

Chạy từ thư mục gốc, sau khi kích hoạt `.venv` và cấu hình API key:

```powershell
# CP1
python --version
pytest tests/smoke -q

# CP2
python src/guardrails/input_guardrails.py
python src/guardrails/output_guardrails.py
python src/main.py --part 2

# CP3
python src/main.py --part 3
pytest tests/public/test_results_contract.py -q

# CP4
python src/main.py --part 4

# CP5
pytest tests/smoke -q
pytest tests/public -q
python scripts/grade.py --submission-dir . --out outputs/grade_report.json
```

CP3 và CP4 cần kết nối API; việc chạy lại có thể ghi đè artifact và phát sinh chi phí. Không chỉnh sửa thủ công các file kết quả hoặc báo cáo tự sinh.

