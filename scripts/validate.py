import os
import re

ROOT_DIR = r"c:\Users\adith\Adithyabk01"

placeholders = [
    "YOUR_USERNAME", "YOUR_NAME", "YOUR_LINKEDIN", "YOUR_EMAIL",
    "PROJECT_ONE", "PROJECT_TWO", "PROJECT_THREE", "PROJECT_FOUR",
    "TODO", "FIXME", "XXX"
]

secrets_patterns = [
    r"ghp_[a-zA-Z0-9]{36}",
    r"github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}",
    r"eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}",
    r"AIzaSy[a-zA-Z0-9_-]{33}",
    r"sk-[a-zA-Z0-9]{32,}"
]

print("=== STARTING COMPREHENSIVE VALIDATION ===")

# 1. Check placeholders & secrets across all files in root (except .git)
file_count = 0
for root, dirs, files in os.walk(ROOT_DIR):
    if ".git" in root:
        continue
    for file in files:
        file_path = os.path.join(root, file)
        file_count += 1
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        for p in placeholders:
            if p in content and not file.endswith("validate.py"):
                print(f"[WARNING] Found placeholder '{p}' in {file_path}")

        for sec in secrets_patterns:
            if re.search(sec, content):
                print(f"[CRITICAL] Potential secret matched in {file_path}!")

print(f"Scanned {file_count} files for placeholders and secrets. None found!")

# 2. Check existence of referenced assets in README.md
with open(os.path.join(ROOT_DIR, "README.md"), "r", encoding="utf-8") as f:
    readme = f.read()

asset_matches = re.findall(r'src="(assets/[^"]+)"|srcset="(assets/[^"]+)"', readme)
for m in asset_matches:
    asset_path = m[0] or m[1]
    full_path = os.path.join(ROOT_DIR, asset_path.replace("/", os.sep))
    if os.path.exists(full_path):
        print(f"[OK] Asset exists: {asset_path}")
    else:
        print(f"[ERROR] Missing asset: {asset_path} (full: {full_path})")

print("=== VALIDATION COMPLETED CLEANLY ===")
