# eira Pilot — Budget

## Status

Working budget for an initial three-month Mumford pilot with five students and one teacher using eira for homework support. The students are assumed to use eira at the same physical location and therefore share one internet connection.

Figures below are planning estimates in SEK and should be replaced with observed Ghana/local prices and actual quotations as procurement becomes concrete.

## Pilot assumptions

- 5 students
- 1 teacher
- 3-month pilot
- 5 reasonably durable Android devices
- Protective cases and tempered-glass screen protectors for all student devices
- 1 teacher laptop
- 1 shared mobile-broadband/Wi-Fi connection
- Frontier-model inference used directly during the initial pilot, with curriculum-grounded RAG and strong prompting
- No local AI server required for the initial pilot

## Capital expenditure

| Category | Quantity | Estimated unit cost | Estimated total | Notes |
| --- | ---: | ---: | ---: | --- |
| Android devices | 5 | 1,500–2,000 SEK | 7,500–10,000 SEK | Avoid the very cheapest devices; camera, USB-C, at least 4 GB RAM and 64–128 GB storage are desirable |
| Protective cases | 5 | ~100 SEK | ~500 SEK | Durable cases for shared educational use |
| Tempered-glass screen protectors | 5 | 100–200 SEK | 500–1,000 SEK | Protect displays during repeated student use |
| Spare chargers / cables | Shared | — | ~500 SEK | Small replacement pool |
| Teacher laptop | 1 | 3,000–5,000 SEK | 3,000–5,000 SEK | A suitable used business laptop may be sufficient |
| Networking equipment | 1 | — | Included / TBD | Mobile router or hotspot if not already available |
| Power infrastructure | — | — | TBD | Add only if the pilot site demonstrates a need |
| Furniture / physical setup | — | — | TBD | Use existing facilities where possible |
| Tools / makerspace equipment | — | — | Not required initially | Outside the scope of the homework-support pilot |

**Estimated core device package:** 12,000–17,000 SEK.

## Three-month operating expenditure

| Category | Three-month estimate | Notes |
| --- | ---: | --- |
| Internet connectivity | 500–1,500 SEK | One shared connection for the pilot site rather than separate data plans for each student |
| AI / frontier-model inference | ~2,000 SEK budget | Deliberately includes headroom; actual token usage should be measured during the pilot |
| Curriculum / RAG materials and setup | 1,000–2,000 SEK | Printing, setup, accounts and other pilot materials; existing NaCCA material should be reused where possible |
| Electricity | TBD | Measure locally rather than assume |
| Maintenance | Included in reserve initially | Record actual failures and repair costs |
| Local support / administration | TBD | Determine with the local pilot partner |

## Contingency / replacement reserve

Allocate approximately **2,000 SEK** for device damage, replacement accessories, unexpected connectivity costs and other small pilot expenses.

## Working pilot envelope

Based on the estimates above, the initial three-month pilot is expected to require approximately:

**17,500–24,500 SEK**, excluding international travel and any major site or power infrastructure.

For funding applications and initial planning, use a rounded working envelope of:

**25,000 SEK**

This provides a modest contingency while keeping the pilot deliberately small.

## Cost-learning objectives

The pilot should measure rather than assume:

- AI cost per student and per homework session
- tokens and frontier-model calls per student
- mobile-data consumption
- device failure and repair rate
- teacher time required per student
- whether five simultaneous devices materially affect connectivity
- whether direct frontier-model use is economically acceptable before introducing cheaper model routing or local inference

The first pilot prioritises learning quality and reliable use over premature inference-cost optimisation. If usage demonstrates value, later versions can test routing simple questions to cheaper or open models and escalating difficult questions to frontier models.

## Budget principles

Use observed local prices whenever possible. Record the date, location, supplier and whether transport is included when collecting prices.

Separate one-time infrastructure expenditure from recurring operating expenditure so that the cost of reproducing and sustaining the pilot can be evaluated independently.

Do not add infrastructure merely because it may eventually be useful. Add local compute, additional networking, power systems or other equipment when pilot evidence demonstrates a reason for it.
