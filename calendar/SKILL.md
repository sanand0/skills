---
name: calendar
description: Manage my calendar and scheduled TODOs. Use for meeting invites, travel itineraries, calendar sync, and follow-up actions. Use meeting-prep for meeting preparation.
---

My calendar is my schedule, TODO list and a way to protect time.

## Sources and sync

- `s.anand@straive.com` is my primary and work calendar. Invite `root.node@gmail.com` (personal calendar) and set `guestsCanModify: true` (and vice versa).
  Use `anand-laptops` skill for how to use `gws` to access calendars.
- Keep calendars in sync. `~/code/scripts/accept-invites"` accept invites in both directions and trash acceptances.
- Prefer time zones local to where I'll be.
- Avoid Meet link on blocks, reminders or travel.

## Make changes safely

- Show the intended changes for large/risky updates: matched existing IDs, create vs update vs cancel, account, invitees, time zone, recurrence scope and side effects
  Straightforward requests need no extra approval.
- After writes, re-read organizer events and the personal/calendar attendee copies. Verify all fields. Check partial failures before retrying.
- Report what changed, what was left untouched, and what needs attention. List each travel leg or bulk change with dates. Mention what wasn't verified.

## Scheduling

- Slots: `uv run ~/code/scripts/freeslots.py --tz IST --days 7` shows both zones. Check colleagues with `gws calendar freebusy query`. Quote times in their zone and mine.
- Title: `Priya / Anand` for a 1:1 (add the org or topic if it helps: `Priya / Anand - TA role`). Use topic as title for group meetings.
- Location: For in-person, add venue, map link, my phone. Add `Travel` either side and stretch the block for networking. Say so in the description.
- Google Meet: Not for blocks, only meetings with others. Create via `gws` on Calendar with open access, guests can modify, and turn on moderation, auto recording/transcript/smart-notes generation.
- Description: write similar to my better invites:
  "This is a working session ... Before the call, please ... try ...";
  or "Could you share your screen and show what you've used it for? I'm curious what worked and what didn't."
  Keep uncertainty or optional attendance explicit.
  Include links where relevant.
  Common sections:
  - **Context**: e.g. "X suggested 'talk to Priya about…'.
  - **Agenda**: e.g. "Let's discuss how you're using AI agents…"
  - **Prep.** Small and concrete: "install ChatGPT desktop and try these 3 questions", "mail me the draft before the session", "prepare one real example".
  - **PS.** Common examples:
    - Sorry - best I could do across time zones.
    - Slot was free on your calendar; happy to move.
    - Sam - purely for you to read the meeting notes.
    - Entirely optional. Please forward as required.
- Create blocks if required:
    - 30-60 min of "Meeting prep" before talks, workshops, or important meetings if free.
    - 15-30 min of "Spillover" for talks, workshops, important / social events that could run over.
    - 15 min of "Wrap-up" after interviews, etc. to write up notes.
- Protect history in recurring event edits. End the old series and start a new one with the same body, guests, edit rights and Meet settings. Past instances keep their recordings.

## Travel

1. Save tickets in `~/Dropbox/Travel/YYYY-MM Place/` (the month the trip starts; the main country, or `India`). Name them like the newest files there:
   - `2026-03-14 Flight 6E-1004 SIN-MAA ABC123.pdf`. One file per ticket; a connection lists every flight: `Flight SIN-LHR EK-353 EK-001 ABC123`.
   - `2026-03-17 Train 20608 MAS-SBC 4123456789.pdf`, `2026-03-17 Hotel Lemon Tree Bangalore.pdf`, `2026-03-21 Boarding Pass BLR-SIN 6E-1006.pdf`.
   - Save visas, insurance, invitation letters and event tickets go there too. Dates are local departure or check-in dates.
2. One event per leg, titled `Flight 6E 1004 SIN-MAA ABC123` or `Train 20608 MAS-SBC 4123456789`.
   Exact ticket times, each end in its own time zone - then check the flight's length looks right.
   Description: airline, route, PNR, seat or coach, baggage, ticket path, checklist for visa, invitation letter, insurance.
   No PNR yet? Add the leg anyway, say "PNR pending", and update when available.
3. Wrap each leg in blocks:
   `Travel to airport` → `At airport` → flight → `Transit at DXB` → flight → `Immigration` → `Travel home` (or `Travel to hotel`, `Travel from airport`). `Travel to station` before a train.
   Keep titles this short; add where and why in location and description.
   Size the blocks from closest past trips. Else, estimate based on airport/traffic/other delays with plenty of buffer.
4. Block time for entry forms during "At airport" depending on the form, e.g. 5 min for SGAC.
5. First visit, or first in years (check `travel.csv`)? Research entry rules, airport→hotel by public transport, payments, roaming, weather, vegetarian food, what's worth a walk. Save it as `<place>.md` in the trip folder.
6. After the trip, offer to add the trip to `travel.csv` + `immigration.tsv` and to move the folder to `Archive/`.

## Commands

`gws` defaults to work. For personal, prefix `GOOGLE_WORKSPACE_CLI_CONFIG_DIR="$HOME/.config/gws-root.node@gmail.com"`. `--dry-run` previews a write: use it on the first of each kind.

```bash
# What's already there? (q searches titles and descriptions)
gws calendar events list --params '{"calendarId":"primary","timeMin":"2026-03-14T00:00:00+08:00","timeMax":"2026-03-22T00:00:00+08:00","singleEvents":true,"orderBy":"startTime","q":"Flight"}'

# A leg: each end in its own zone. sendUpdates=all makes the personal copy appear.
gws calendar events insert --params '{"calendarId":"primary","sendUpdates":"all"}' --json '{"summary":"Flight 6E 1458 SIN-BLR ABC123","description":"IndiGo 6E 1458. SIN → BLR. PNR ABC123. Seat 7C. 30 kg. Ticket: ~/Dropbox/Travel/2026-12 India/2026-12-24 Flight 6E-1458 SIN-BLR ABC123.pdf","start":{"dateTime":"2026-12-24T19:30:00","timeZone":"Asia/Singapore"},"end":{"dateTime":"2026-12-24T21:40:00","timeZone":"Asia/Kolkata"},"attendees":[{"email":"root.node@gmail.com"}],"guestsCanModify":true}'

# A meeting: add "conferenceDataVersion":1 to --params, and to --json:
#   "conferenceData":{"createRequest":{"requestId":"<unique>","conferenceSolutionKey":{"type":"hangoutsMeet"}}}
# Meet space: GET by meeting code, PATCH by the returned name (spaces/<id>). The code won't patch.
gws meet spaces get --params '{"name":"spaces/abc-defg-hij"}'
gws meet spaces patch --params '{"name":"spaces/NAME","updateMask":"config.accessType,config.moderation,config.artifactConfig"}' --json '{"config":{"accessType":"OPEN","moderation":"ON","artifactConfig":{"recordingConfig":{"autoRecordingGeneration":"ON"},"transcriptionConfig":{"autoTranscriptionGeneration":"ON"},"smartNotesConfig":{"autoSmartNotesGeneration":"ON"}}}}'

# Change: send only the fields that change. "attendees" replaces the whole list: send everyone, with their responseStatus.
# sendUpdates "none" for a fix guests needn't hear about; "all" when the time, place or agenda changes.
gws calendar events patch --params '{"calendarId":"primary","eventId":"ID","sendUpdates":"none"}' --json '{"guestsCanModify":true}'
```
