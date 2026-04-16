# Sample Input — Email Thread
**Use with: Email Extraction Prompt (sop_extract_email.md)**
**Demo use case: Council / Leadership IT Briefing Process**
**Complexity: Medium — contains names to scrub, political nuance, implied steps**

---

## INSTRUCTIONS FOR DEMO

1. Open your Claude Project (SOP Generator)
2. Type: `Use the email extraction approach`
3. Paste the Email Extraction Prompt from sop_extract_email.md
4. Paste the email thread below after the divider line
5. Send — review the Pass 1 and Pass 2 output
6. Point out the [IMPLIED] flags and the GAPS section to the audience
7. Ask: `Now convert this extracted content into a formal SOP`

**What to highlight for the audience:**
- The AI replaces "Director Kim" and "Steve" with role titles automatically
- The political nuance about council member preferences gets captured as [VERIFY] flags
- The 3-sentence incident rule comes through clearly as a step
- The GAPS section will flag that council member names and contact preferences are missing

---

## THE SAMPLE EMAIL THREAD

---

**From:** Robert Chen, IT Director
**To:** [New IT Director — name redacted]
**Subject:** RE: RE: RE: Council stuff — everything I know

---

Hey,

Sorry for the delayed reply, crazy week. Let me try to dump everything I know before I'm out the door.

**The basics of getting things on the Council agenda:**

Most IT stuff goes on the consent agenda — anything routine, renewals under $50K, maintenance agreements, that kind of thing. Just get it to the City Clerk's office by Wednesday noon for the following Monday meeting. City Manager's office wants a one-pager summary for every item even if it's consent — they read these the night before and hate surprises.

Anything over $50K or any new policy, new vendor relationship, or anything that changes how a department operates — that goes to action agenda and you'll need to present. Give yourself at least 3 weeks lead time to prep because the City Manager will want to preview it with you first. Don't skip that preview meeting. Seriously.

**The City Manager (Director Kim):**

Director Kim reads everything you send. She wants the executive summary to be one page maximum. She told me once she reads them standing at the printer so if it doesn't fit on one page she stops reading. Include the 3-year cost projection even if the item doesn't require it — she will ask during the meeting and you don't want to look unprepared. If there's a security angle to anything, always frame it as risk to citizens, not technical exposure. She responds to citizen impact, not cyber jargon.

**Council members (general guidance):**

There are 5 members right now. About 1-2 of them will actually ask you technical questions — the others will just vote. Never say "bandwidth" or "latency" to the full council. Use "internet speed" and "slowdowns." I made that mistake my first year. Don't say "endpoint" either — say "city computer" or "city device."

Council Member Steve in particular will ask follow-up questions — he used to work in telecom so he actually knows what he's talking about. Just be straight with him. The others mostly care about cost, timeline, and whether citizens will notice.

**When something goes wrong (incidents):**

This is the big one. If you have a P1 — something down affecting city services or public safety — you notify Director Kim within 1 hour, even at 2am. She told me she'd rather be woken up than read about it in the news. Have a plain-language status statement ready: what happened, what you are doing about it, when it will be fixed. Three sentences maximum. Do not send this in email — call first, email after it's resolved.

Never put specific technical details about the incident in writing until after it's resolved. If it becomes a public records request later, you don't want a 2am email documenting that your firewall was down for 6 hours.

**Post-meeting:**

Within 24 hours of any council meeting where IT had an item, document any commitments you made — in writing, to your own records. Council members sometimes remember agreements differently. If Council Member Steve asked a follow-up question you couldn't answer, send him a written response within 2 business days. Builds a lot of trust over time.

The IT project tracker in SharePoint gets updated with any council direction after every meeting. There's a "Council Actions" column — keep it current.

One more thing: always end your council presentation with a slide that has just your name and "Questions?" on it. Sounds obvious but I learned the hard way that ending on a content slide invites questions on the most alarming-looking chart rather than what you wanted to discuss.

Good luck. Feel free to call me after I'm out if you get stuck.

— Robert

---

**From:** [New IT Director]
**To:** Robert Chen
**Subject:** RE: RE: Council stuff — everything I know

Robert,

Thank you — this is exactly what I needed. A few follow-up questions:

1. Is there a template for the one-pager executive summary? Or did you create your own format?
2. What happens if a consent item gets pulled by a council member during the meeting?
3. Is there a specific SharePoint folder for the IT project tracker you mentioned?

---

**From:** Robert Chen
**To:** [New IT Director]
**Subject:** RE: RE: RE: Council stuff — everything I know

Good questions.

1. I created my own template — I'll attach it separately. There's no official city format. Mine has: Issue, Background, Recommended Action, Fiscal Impact, Risk if Not Approved. That order works.

2. If a consent item gets pulled — it moves to action agenda, usually later in the same meeting. You'll have to present it on the spot with no prep. Two things help: (a) always know your consent items cold, and (b) bring the vendor rep's business card to every meeting in case someone wants to call them.

3. The SharePoint folder is under IT Department > Governance > Council Actions. I'll share the exact link separately but I need to make sure IT Admin sets up your access first.

— Robert

---

*End of email thread*

---

## WHAT THE EXTRACTION SHOULD PRODUCE

After running through the Email Extraction Prompt, the Pass 2 output should include:

- **Process name:** IT Council Briefing and Communication Process
- **Steps:** Agenda routing decision (consent vs action), City Manager preview, one-pager preparation, council presentation, incident notification protocol, post-meeting documentation
- **Decision points:** IF over $50K or new policy THEN action agenda; IF P1 incident THEN call City Manager within 1 hour
- **Implied:** [IMPLIED: template format for executive summary not included in email]
- **Gaps:** Council member names and contact preferences not documented, SharePoint link not included, City Clerk submission portal not described

---

*Sample email input v1.0 | SOP Generator | TAGITM 2026*
