# Spiro / GES house standards (read before any deliverable)

Every agent in `.claude/agents/` works for **Dara Cunningham**, Project Manager supporting Agency Operations and the Transformation Management Office (TMO) at Spiro (co-branded with GES – Global Experience Specialists).

## Non-negotiables
- **Draft only.** Everything an agent produces is a draft for Dara. A named human takes the last look before anything reaches a vendor, client, Briq, hmn or the wider company (the same rule the Copilot Agent Build Pack puts in every agent). Agents never send email, post, sign, approve or commit.
- **Verbatim quotes.** When quoting a speaker, copy the line exactly from the transcript, with name and timestamp. Never paraphrase a quote. If paraphrasing is needed, write it as an attributed summary and do not use quotation marks.
- **Mark inference.** Anything not read directly from a source file is marked `[inferred]`. Calculated dates are marked "calculated" and estimates "estimate".
- **Cite sources.** Every number, date, decision and owner traces to a file (and the sheet, page or section). Say "not in sources" rather than guess.
- **Confidentiality.** Reality Gap interview content stays anonymized: never attribute it to a named leader. Items marked internal (for example the D2D intake go/no-go thresholds, "don't present thresholds (e.g., $30K) at the Nov 10 meeting") never go on external or broad-audience material. Files prefixed `EXTERNAL COPY` are what the vendor saw; the others may hold internal positions.

## Writing
- **Exec-facing = brief.** Lead with the answer or the decision needed. One message per slide, and the headline is the takeaway. A one-page maximum for status updates unless asked.
- **Translate ops stats into business value.** For example, "1.1 hrs saved per project" becomes capacity freed per year at stated volume, and "~60% of projects go out with no render" becomes a win-rate and quality risk. Show the assumption.
- Plain words, active voice, no filler. Use event-industry language (shows, move-in, show kits, I&D, drayage), not generic corporate language.
- Program naming: **GES Ignite**, site **AI Ignite Hub**. Say the full name once, then "Ignite". hmn is also written "behmn"/"BeHmn" in documents; use "hmn" in GES-facing text unless matching a document title.
- At GES, "brief" also means the write-up given to a vendor so they can quote. Define the word if you use it for a Copilot prompt.

## Brand (Spiro)
- Colors: teal **#3E8B92** (primary), orange **#E8632F** (accent, sparingly). Black or dark gray text on white.
- Font: **Calibri** throughout.
- Thin rules (0.5–1 pt) to separate sections. **No heavy color blocks**, no full-bleed color fills, no gradients.
- Tables: thin teal header rule, no zebra fills or very light only.
- Primary formats: **Word, PowerPoint, Excel**. Use the docx, pptx and xlsx skills to produce real files.

## Files
- Read source documents with `python3 tools/extract_text.py "<file>"` (handles .docx, .pptx, .xlsx and .pdf). See `context/source-index.md` for what each file is.
- Save deliverables to `outputs/<workstream>/` with a dated name, for example `outputs/ignite/2026-11-18_Ignite_Status.docx`. Workstream folders: `ignite`, `otto`, `d2d`, `field-services`, `ma`, `pmo`.

## Dates
- Business days skip weekends and US holidays (the January workback lists Nov 26, Dec 25, Jan 1 and Jan 18). SOW review windows are in business days; "Day 1 is the first full business day after GES receives the plan."
- Sessions run at 8 AM Pacific.

## People (from source documents)
**GES / Spiro:** Debbie Kaplan (Executive Sponsor), Julie Holland (Executive Sponsor, People & Culture), Dallas Wright (AI CoE Lead; GES approver), Tara Phelps (Enablement Lead; Dara's backup), Dara Cunningham (Program Coordinator / PM), Michael Kaack (Platform Administrator; Mitti publisher), Santosh Lakshman (Technical Lead), Rajeev Sharma (IT and security), Graeme Lucas (Copilot usage reporting), Derek Linde (leadership welcome video), Jon Massimino (Chief Legal Officer; SOW signatory), Beth McGowean (planning-meeting deck and pre-read), Dom (D2D / Field Services lead), Terry Campanaro, Courtney Hennessey, Margot Kliebhan, Luke JeanLouis, Bhargavi, Lisa King, Jennifer (Otto and Salesforce stakeholders).
**hmn (behmn):** Alex Schwartz (Founder; delivery and relationship lead), Dr. Ernesto Lee (learning lead and Chief AI Strategist).
**Briq:** vendor of Otto, the AI sales orchestration and research platform.
Names flagged "spelled as heard" in the trackers (Yvette, Jason Needham, Mary, Maria G., Rick from Expo) need confirming before external use.
