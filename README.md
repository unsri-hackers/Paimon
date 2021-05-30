# Paimon
Bot that will help to manage Attack on IF group

## Getting Started

### Prerequisites

- Python 3.7
- Pip
- Pipenv -- https://pypi.org/project/pipenv/
- Get your TELEGRAM_BOT_TOKEN -- https://core.telegram.org/bots#creating-a-new-bot

### Install dependencies

```bash
pipenv install --skip-lock
```

## Run Paimon

```bash
TELEGRAM_BOT_TOKEN=<your-telegram-bot-token> pipenv run python -m src.main
```

### Using Docker

```bash
docker run -e TELEGRAM_BOT_TOKEN=<your-telegram-bot-token> ghcr.io/unsri-hackers/paimon:latest
```
## Branching
- `main` used as production only environment
- `dev` used as main source in order to start your development

## Local Development
In order to contribute to this project, we need to create PR from your local branch to `dev`

for example
```
new feature
-> git checkout -b feature/[name]

hotfix
-> git checkout -b hotfix/[name]

issue
-> git checkout -b issue/[issue_number]
```
