import json
import hashlib
import argparse
import os

# WARNING: NEVER COMMIT YOUR PRIVATE KEY TO GIT!
# This script is for offline use only. Store your private key securely and outside the repo.

PRIVATE_KEY_PATH = os.path.abspath('private_key.txt')  # Example: store as a simple secret string

# The public key and signature scheme must match the verifier in tablint (sha256 of payload)

def sign_payload(payload: str, private_key: str) -> str:
    # Simulate signing: in real use, use RSA or similar
    # Here, just hash the payload with sha256 for demo (matches verifier)
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Generate a tablint Pro license file (OFFLINE, DEMO ONLY)')
    parser.add_argument('--email', required=True, help='Licensee email (required)')
    parser.add_argument('--name', help='Licensee name (optional)')
    parser.add_argument('--output', default='csv_guard.license', help='Output license file name')
    parser.add_argument('--private-key', default=PRIVATE_KEY_PATH, help='Path to private key (text file, NOT in repo)')
    args = parser.parse_args()

    # Load private key (for demo, just a secret string)
    if not os.path.exists(args.private_key):
        print(f"ERROR: Private key not found at {args.private_key}. Never commit your private key!")
        exit(1)
    with open(args.private_key, 'r', encoding='utf-8') as f:
        private_key = f.read().strip()

    payload_obj = {
        'email': args.email,
        'name': args.name or '',
        'tier': 'pro'
    }
    payload = json.dumps(payload_obj, separators=(',', ':'))
    signature = sign_payload(payload, private_key)
    license_data = {
        'payload': payload,
        'signature': signature
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(license_data, f, indent=2)
    print(f"License file written to {args.output}\n")
    print("INSTRUCTIONS:")
    print("- Deliver this file to the user.")
    print("- User should place it as ~/.csv_guard.license or ./csv_guard.license on their machine.")
    print("- NEVER share or commit your private key!")

if __name__ == '__main__':
    main()
