# Module 02 — Domain Reconnaissance

Practice domain: **one you own.** (A cheap .in/.xyz domain counts.)

## Concepts
- WHOIS records: registrar, dates, nameservers, registrant
- DNS record types: A, AAAA, MX, TXT, NS, CNAME
- Certificate transparency: crt.sh exposes every TLS cert ever issued for a domain
- Passive vs active enumeration

## Commands
```bash
whois example.com
dig example.com ANY +noall +answer
dig mx example.com
dig txt example.com
curl -s "https://crt.sh/?q=example.com&output=json" | jq '.[].name_value' -r | sort -u
```

## Tools
- subfinder (passive subdomain discovery)
- [SecurityTrails](https://securitytrails.com) free tier

## Exercise
1. Map your domain fully: every record, every subdomain.
2. Find one subdomain you forgot existed.
3. Look up your domain on crt.sh — did any cert surprise you?
4. Bonus: point your domain's DNS to a service, then confirm with dig.

**Done when:** you can explain every record in your zone file.
