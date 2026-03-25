import hashlib
import requests
import os
import sys
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
API_URL = "https://www.virustotal.com/api/v3/files/"

if not API_KEY:
    print("[!] Error: VIRUSTOTAL_API_KEY not found in .env file")
    sys.exit(1)

def generate_hashes(filepath):
    """
    Generates MD5, SHA1, and SHA256 hashes for a given file.
    Returns a dictionary of hashes or None if file cannot be read.
    """
    if not isinstance(filepath, str) or not filepath.strip():
        return None

    if not os.path.isfile(filepath):
        print(f"[!] Error: file not found — {filepath}")
        return None

    try:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)

        return {
            "filepath": filepath,
            "md5": md5.hexdigest(),
            "sha1": sha1.hexdigest(),
            "sha256": sha256.hexdigest()
        }

    except (IOError, OSError) as e:
        print(f"[!] Error reading file {filepath}: {e}")
        return None

def check_hash(hash_value):
    """
    Submits a hash to VirusTotal and returns detection results.
    """
    if not isinstance(hash_value, str) or not hash_value.strip():
        return None

    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(API_URL + hash_value, headers=headers)

        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]
            name = data["data"]["attributes"].get("meaningful_name", "Unknown")

            return {
                "hash": hash_value,
                "malicious": stats["malicious"],
                "suspicious": stats["suspicious"],
                "undetected": stats["undetected"],
                "harmless": stats["harmless"],
                "name": name,
                "total_engines": sum(stats.values())
            }

        elif response.status_code == 404:
            return {
                "hash": hash_value,
                "malicious": 0,
                "suspicious": 0,
                "undetected": 0,
                "harmless": 0,
                "name": "Not found in VirusTotal database",
                "total_engines": 0
            }

        elif response.status_code == 429:
            print("[!] Rate limit hit — too many requests")
            return None

        else:
            print(f"[!] API error — status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"[!] Connection error: {e}")
        return None