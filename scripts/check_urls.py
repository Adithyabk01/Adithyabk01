import urllib.request
import re

content = open(r'c:\Users\adith\Adithyabk01\README.md', encoding='utf-8').read()
urls = set(re.findall(r'https?://[^\s\)\"\>]+', content))

print(f"Found {len(urls)} distinct URLs in README.md:\n")
for u in sorted(urls):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"[OK] {resp.status} - {u}")
    except Exception as e:
        print(f"[FAIL] {e} - {u}")
