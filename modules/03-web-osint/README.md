# Module 03 — Web OSINT

Practice target: your own website.

## Concepts
- Google dorks: `site:`, `inurl:`, `filetype:`, `intitle:`, `-` exclusions
- robots.txt and sitemap.xml — what sites tell you on purpose
- The Wayback Machine — sites' deleted history
- Technology fingerprinting

## Dorks to practice (on your own site)
```
site:yourdomain.com
site:yourdomain.com filetype:pdf
inurl:admin site:yourdomain.com
intitle:"index of" site:yourdomain.com
```

## Exercise
1. Run the [Google Hacking Database](https://exploit-db.com/google-hacking-database) top queries against your own site.
2. Pull an old version of your homepage from the Wayback Machine and diff it.
3. Read your own robots.txt — is anything listed that should not be public?
4. Install Wappalyzer and fingerprint your stack, then check what it missed.

**Done when:** you have a list of unintended exposures on your own site — and fixed them.
