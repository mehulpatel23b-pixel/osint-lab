# Module 09 — Network & Infrastructure Deep Dive (Advanced)

Beyond Shodan: passive DNS, ASN-level mapping, IP history.
Scope: your own domains, your VPS, and public datasets.

## Concepts
- Passive DNS — historical DNS records without touching the target
- ASNs and BGP: who announces your IP space (bgp.he.net)
- IP history: hosting changes over time (SecurityTrails, ViewDNS)
- Wayback + DNS diffing to map an infrastructure's history

## Tools & queries
```bash
# your own domain — full record history
curl -s "https://dns.google/resolve?name=yourdomain.com&type=A" | jq
# ASN / routing
# https://bgp.he.net/dns/yourdomain.com
# https://viewdns.info/iphistory/?domain=yourdomain.com
```

## Exercise
1. Pull the IP history of your own domain. Map every hosting change you ever made.
2. Find your ISP/host's ASN on bgp.he.net. What else do they announce?
3. Diff your domain's DNS today vs its Wayback-era records.
4. Build a one-page infrastructure timeline of your own web presence since you bought the domain.

**Done when:** your infra timeline is complete and you can explain each transition.
