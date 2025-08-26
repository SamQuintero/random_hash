import hashlib
import secrets
import sys

MAX_TRIES = 1000

def random_md5_hex() -> str:
    # MD5 hex digest is always 32 hex characters
    return hashlib.md5(secrets.token_bytes(32)).hexdigest()

def main() -> None:
    for _ in range(MAX_TRIES):
        h = random_md5_hex()
        if h.startswith("00"):
            print(f"PASS: found hash {h}")
            sys.exit(0)
    print("FAIL: no matching hash found in 1000 attempts")
    sys.exit(1)

if __name__ == "__main__":
    main()