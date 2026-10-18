# Module 06 — Infrastructure Mapping

Practice target: your own home IP, router, and servers.

## Concepts
- Shodan / Censys index every internet-facing service in the world
- Ports, banners, and what they reveal about a host
- Certificate logs tie infrastructure to organizations

## Steps
1. Find your public IP (`curl ifconfig.me`).
2. Look it up on Shodan and Censys. What services face the internet from your network?
3. Check your router admin panel — is it exposed? Close it.
4. If you own a VPS: scan **it** with nmap from your own machine:
```bash
nmap -sV -p- your-vps-ip        # your own server only
```
5. Check crt.sh for your domains — every cert maps infrastructure you control.

**Done when:** you can draw a map of your own internet-facing infrastructure, and nothing unexpected is open.
