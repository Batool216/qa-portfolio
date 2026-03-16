# QA Portfolio — Azrieli College Student Portal

## About This Project
End-to-end manual and automated testing of the Azrieli College of 
Engineering student portal (yedion.jce.ac.il) — a live production 
system used daily by all students and faculty at Jerusalem College 
of Engineering.

## My Responsibilities
- Sole owner of the **login flow** test suite (TC_01–TC_09)
- Wrote and executed 82 test cases across 4 modules
- Produced all three formal QA documents (STP, STD, STR)
- Identified a **critical bug**: valid credentials triggered 
  unexpected logout (TC_01 — Failed)
- Automated login flow tests using Selenium and Python (PyCharm)

## Modules Tested
| Module | Description |
|--------|-------------|
| Login Flow | Authentication, MFA, session handling, edge cases |
| Messages (הודעות ופניות) | Inbox, send, delete, attachments |
| Course Sites (אתרי קורסים) | Navigation, filters, downloads |
| Schedule System (מערכת שעות) | Timetable, filters, export |

## Test Results Summary
| Type | Total | Passed | Failed |
|------|-------|--------|--------|
| Positive | 61 | 59 | 2 |
| Negative | 8 | 5 | 3 |
| Edge/Boundary | 13 | 13 | 0 |
| **Total** | **82** | **77** | **5** |

**Pass rate: 93.9%**

## Documents
- `STP_Test_Plan.docx` — Test strategy, scope, risks, team responsibilities
- `STD_Login_and_Features.docx` — All 82 test cases with steps, 
   expected vs actual results
- `STR_Test_Report.docx` — Final test report with metrics and findings

## Automation
- `test_login_fixed.py` — Selenium/Python automated tests for the 
  login module
- Covers valid login, invalid credentials, empty fields, MFA edge 
  cases, forgot password flow
- Uses pytest fixtures for reusable login logic
- Credentials managed via environment variables (not hardcoded)

## Tools Used
Python · Selenium · PyCharm · pytest · Chrome DevTools · 
Manual Testing · Formal QA Documentation
