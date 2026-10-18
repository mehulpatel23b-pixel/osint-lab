# Module 01 — Foundations

## Concepts
- What OSINT is (and isn't): collecting publicly available data to answer questions
- The intelligence cycle: collect → process → analyze → report
- OPSEC: your own footprint is your first case study
- Documentation: every finding needs a source, timestamp, and screenshot

## Set up your lab
```bash
# Kali / Termux / Ubuntu
sudo apt update && sudo apt install whois dnsutils exiftool python3-pip
pip install requests dnspython
mkdir ~/osint-journal
```

## Exercise: investigate yourself
1. Google your own name + city. Screenshot everything you find.
2. Check [haveibeenpwned.com](https://haveibeenpwned.com) for your email.
3. Write a 1-page "threat profile" of yourself based only on public data.
4. Fix one thing you did not like (privacy setting, old account, leaked data).

**Done when:** you have a journal folder and your own threat profile written.
