# Module 07 — Build Your Own OSINT Tools

Once you understand the techniques, automate them. Three starter projects:

## 1. Subdomain watcher (your own domain)
```python
import requests, json

DOMAIN = "yourdomain.com"          # yours only
r = requests.get(f"https://crt.sh/?q=%.{DOMAIN}&output=json", timeout=30)
names = {e["name_value"] for e in r.json()}
print("\n".join(sorted(names)))
```
Run daily via cron, diff against yesterday's list, alert on new subdomains.

## 2. Metadata scrubber
CLI tool: walk a folder, use ExifTool to strip GPS/author fields in place,
report what was removed. Useful for every photo you share publicly.

## 3. Cert monitor
Query crt.sh weekly for new certificates on your domains — new certs are
an early warning of spoofing or takeover.

## Level up
- Package one of these as a proper Python project (setup.py, tests, README)
- Publish it on your GitHub with the same structure as this repo
