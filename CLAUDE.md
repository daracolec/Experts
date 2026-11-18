# Experts — Dara's agent team

This repo holds Dara Cunningham's source documents (Spiro / GES Agency Operations and TMO) and a team of 12 Claude Code subagents in `.claude/agents/`. Every agent reads `context/spiro-standards.md` (house rules, brand, people) and `context/source-index.md` (what each file is). Read source files with `python3 tools/extract_text.py "<file>"`. Save deliverables to `outputs/<workstream>/`.

## Orchestration (default for every request)
The main session is the orchestrator; subagents cannot call each other. For any request Dara makes in this repo, follow `.claude/skills/ask/SKILL.md`:
1. Classify it.
2. Route to the fewest agents needed: lead delivery agent, then advisory review, then rehearsal if asked.
3. Run independent agents in parallel.
4. Verify the outputs.
5. Return one synthesized answer.

Quick factual questions can be answered directly from the sources. `/ask <request>` forces the full routing.

## Roster
| Agent | Type | Top deliverables | Build priority |
|---|---|---|---|
| `pmo-operations-lead` | Delivery | Recaps, workback calendars, RACI, status reports, plans | 1 |
| `executive-storyteller` | Delivery | Spiro-branded decks, one-pagers, talk tracks + Q&A, run-of-shows | 1 |
| `vendor-sow-manager` | Delivery | Consolidated feedback to hmn, SOW redlines, review/acceptance and installment trackers | 1 |
| `workflow-ai-automation-designer` | Delivery | Current vs new state trackers, option comparisons, Copilot agent specs, integration requirements | 1 |
| `kpi-value-analyst` | Delivery | KPI frameworks, measurement readouts, surveys, ROI/value models | 2 |
| `ma-research-analyst` | Delivery | Target one-pagers, comparison matrices, data-quality caveats | 3 |
| `cfo-board-skeptic` | Advisory | Ranked challenge list and ready/not-ready verdict on numbers | 1 |
| `learning-change-advisor` | Advisory | Learning-quality and adoption-risk reviews | 2 |
| `procurement-contracts-counsel` | Advisory | Contract/licence issues list and negotiation priorities | 2 |
| `elt-member-sim` | Simulation | Exec rehearsal and debrief | 2 |
| `vendor-counterpart-sim` | Simulation | Vendor negotiation rehearsal and debrief | 2 |
| `ignite-learner-sim` | Simulation | Learner walkthrough and debrief | 3 |

## Who leads each workstream
- **GES Ignite (hmn):** `vendor-sow-manager` leads; `learning-change-advisor` reviews; `pmo-operations-lead` runs the calendar; `kpi-value-analyst` measures.
- **Otto (Briq):** `kpi-value-analyst` leads on KPIs and attribution; `workflow-ai-automation-designer` on Salesforce integration and Disney-moment demos; `executive-storyteller` on board materials.
- **D2D and Field Services:** `workflow-ai-automation-designer` leads; `executive-storyteller` builds the planning deck.
- **M&A:** `ma-research-analyst` leads; `cfo-board-skeptic` reviews.
- **Core PM:** `pmo-operations-lead` leads.

## Typical sequences
- **Meeting to exec slide:** transcript → `pmo-operations-lead` recap → status report → `executive-storyteller` slide → `cfo-board-skeptic` (if numbers) → `elt-member-sim` rehearsal → Dara presents.
- **hmn deliverable review:** hmn draft → `learning-change-advisor` + `ignite-learner-sim` → reviewer comments merged by `vendor-sow-manager` → `procurement-contracts-counsel` if scope or cost is touched → Dara sends.
- **Process change:** workshop notes → `workflow-ai-automation-designer` tracker update → `kpi-value-analyst` value → `cfo-board-skeptic` → `executive-storyteller` deck.

## Always human-owned (never delegate to an agent)
- Sending anything outside Dara's drafts: email to hmn, Briq, clients or the company; posting to the Hub or Teams.
- Approvals, sign-off and acceptance of vendor deliverables; signing SOWs or change orders; invoices and payment deferrals.
- Pricing, scope or date commitments to any vendor or client.
- Choosing tools or vendors (Copilot vs Claude, CADLink, render tools) and setting targets presented to the ELT or board.
- People decisions: leader selection, staffing, performance judgments, mandatory-vs-voluntary policy, credential policy.
- Anything using confidential Reality Gap interview content, deal-sensitive M&A information, or individual learner data.
- The final read of any exec or board material.

## Gaps (roles the documents suggest but can't yet be defined well)
- **Pitch / new-business PM** (`Chelan Fresh x Project KO.pptx`): is client pitch support a recurring part of the job? Which deliverables (asset lists, check-in calendars, proposal decks)?
- **M&A analyst detail:** no source files. What is the thesis and screening criteria? Which data sources (PitchBook, ZoomInfo) are licensed? Who receives the work?
- **Otto / Briq specifics:** no Briq contract, board deck or talk track in the repo. What does the Briq agreement cover? Which board materials exist?
- **Brand designer:** brand rules come from Dara's brief only. Is there a Spiro master PowerPoint template or brand guide to load?
