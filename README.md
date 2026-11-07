# Building with the Claude API

My course work, one folder per lesson.

## Setup
```bash
/opt/homebrew/bin/python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Put your key in `.env` (never committed):
```
ANTHROPIC_API_KEY=sk-ant-...
```
In VS Code notebooks, choose the `.venv (Python 3.13)` kernel.

## Structure
```
requirements.txt        packages for the whole project
.env                    API key (git-ignored)
lessons/
  _template_notes.md    copy this for each new lesson
  001_request/
    001_request.ipynb   lesson notebook
    request.py          same request as a plain script
    notes.md            my notes
```

## New lesson
```bash
mkdir lessons/002_topic
cp lessons/_template_notes.md lessons/002_topic/notes.md
```
New packages: `pip install <pkg>`, then add it to `requirements.txt`.

## Lessons
- [001 – Making a request](lessons/001_request/notes.md)
