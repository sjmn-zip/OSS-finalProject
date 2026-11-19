# [JupGo] — Lost & Found Feed

Browse recently found items in Korea as a simple feed, instead of searching for one specific item.

> **Status:** Proposal stage (Week 12). The features below are planned and not yet implemented.

---

## Purpose

Existing services such as LOST112 are built for **searching** for one specific lost item.
If you are not sure where or when you lost something, it is hard to look through
recently found items at a glance.

This project shows found items as a **feed of cards** that you can narrow down by
region, date, and item type.

## Intended Users

- People who lost something but are not sure exactly where or when
- Students and commuters who want to check recently found items near a certain area

## Features (MVP)

- [ ] **Found-item feed:** cards with item name, category, date, place found, storage place, and photo (if available)
- [ ] **Page navigation:** 20 items per page
- [ ] **Filters:** region, date range, and item type
- [ ] **Map view:** show storage places on a map *(depends on whether location data is usable; fallback: [TODO: team decision])*
- [ ] **Privacy protection:** hide photos for categories that may show personal information (ID cards, credit cards, passports)
- [ ] **Sample data mode:** run the app without an API key

### Out of Scope (v1)

- User accounts and login
- Reporting lost items
- Notifications
- Online deployment (the app runs locally)

## Tech Stack

- **Python 3.10+** (same version as our CI)
- **FastAPI** for the web server
- [TODO: template engine and other libraries once confirmed]

## Data Source

- **National Police Agency — Portal Institution Found Item Information Service**
  (Public Data Portal, data.go.kr, `LosfundInfoInqireService`)
- Format: XML (REST)
- [TODO: verify the data usage terms and add the required attribution]

## Getting Started

### 1. Get an API key

1. Sign in to [data.go.kr](https://www.data.go.kr)
2. Apply for the found item information service above
3. Copy your service key

### 2. Install and run

> **[TODO]** The commands below are the planned setup. Run them yourself and fix them before merging this README.

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

Then open `http://localhost:8000` in your browser.

### Run without an API key (sample data mode)

[TODO: command for sample data mode]

## Example Usage

[TODO: screenshot of the feed page]

## Project Structure

[TODO: add after the team confirms the folder layout]

## Team

| Role | Member | Responsibility |
| --- | --- | --- |
| Data | @uyeonee | Fetch found-item data from the API, parse and clean it |
| Map | @ogang9999 | Show storage places on a map |
| Filter | @ITM-MSJ | Filter by region, date, and item type |
| Web | @sjmn-zip | Build the feed page and connect the web pages |

## How We Work

- Every task is a GitHub issue with an owner and acceptance criteria
- Project board: Backlog → Ready → In progress → In review → Done
- Every change goes through a pull request and is reviewed by another teammate before merging
- Each member opens the pull request that connects their own part to the app
- See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## AI Use

We use AI tools to help with bounded tasks (one issue at a time).
Each pull request notes which tool was used, what it helped with, and how a human checked the result.
Every change is reviewed by a teammate.

## Current Limitations

- Shows only items registered in the police portal system; new items may appear with a delay
- Live data requires an API key (use sample data mode otherwise)
- Map view depends on whether the data provides usable location information
- Runs locally only; not deployed online

## License

This project's code is licensed under the [MIT License](LICENSE).

We chose MIT because we want our code to be openly shared and easy for others to learn from and reuse.
We have no plans to commercialize this project, so a short, permissive license with minimal conditions fits our goals.

The found-item data is **not** covered by this license. It follows the terms of its original provider.
