# LLM Security Testing Framework

An automated framework that attacks LLM-powered applications, measures how often the attacks succeed, applies defenses, and proves the improvement with numbers.

> Status: planning phase. Work in progress.

## Problem

Teams ship chatbots and AI agents that can be tricked with a single clever message: leaking the system prompt, bypassing restrictions, or exposing sensitive data. Most teams have no systematic way to measure how secure their LLM application actually is.

## Idea

Attack a target LLM app automatically, measure the **Attack Success Rate (ASR)**, add defenses, then re-run the same attacks and compare before and after.

## How it works

1. **Attack library**: categorized attacks (direct and indirect prompt injection, jailbreaks, system prompt extraction, multi-turn attacks), mapped to the OWASP Top 10 for LLM Applications.
2. **Automated generation**: an "attacker" model creates new variations of each attack instead of relying on fixed payloads.
3. **Evaluation**: a "judge" model (LLM-as-judge) decides whether each attack succeeded.
4. **Defense and reporting**: input/output filtering and guardrails, then a report with ASR before vs. after.

## Target goal

Show a measurable result, for example: ASR reduced from X% to Y% after applying defenses, across multiple models.

## Tech stack (planned)

- Python (async, OOP), pytest
- Ollama (local open-source models)
- FastAPI (the vulnerable demo app used as the target)
- Docker and GitHub Actions (later)

## Standards

- OWASP Top 10 for LLM Applications
- MITRE ATLAS

## Roadmap

- [ ] Set up Ollama and run a local model
- [ ] Build the target chatbot with a secret system prompt
- [ ] Attack runner: send attacks, store responses
- [ ] Attack library v1 (categorized)
- [ ] LLM-as-judge evaluation
- [ ] Attacker model for automatic attack generation
- [ ] Defenses: input/output filters
- [ ] Before/after comparison and report
- [ ] Docker and CI


## Ethics

All testing is done only on models and applications I own or that are meant for testing. Nothing here targets third-party systems.

## License

MIT
