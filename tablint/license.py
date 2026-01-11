import os
import json
import base64
import hashlib
import sys
from typing import Optional

# Embedded public key (example, replace with real key for production)
PUBLIC_KEY = {
    'e': 65537,
    'n': 2357  # Example modulus, replace with a real one
}

LICENSE_PATHS = [
    os.path.expanduser('~/.csv_guard.license'),
    os.path.join(os.getcwd(), 'csv_guard.license')
]

class LicenseError(Exception):
    pass

def load_license_file() -> Optional[dict]:
    for path in LICENSE_PATHS:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except Exception:
                    continue
    return None

def verify_signature(license_data: dict) -> bool:
    # Simulate RSA signature verification (real implementation should use a proper RSA verify)
    # Here, we just check a dummy signature for demonstration
    payload = license_data.get('payload')
    signature = license_data.get('signature')
    if not payload or not signature:
        return False
    # In a real implementation, verify the signature using the embedded public key
    # For now, just check that signature == sha256(payload)
    expected_sig = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    return signature == expected_sig


def get_license_tier() -> str:
    """
    Returns 'pro' if a valid license file is found, otherwise 'free'.
    Only errors if a license file is present but invalid.
    """
    license_data = load_license_file()
    if not license_data:
        return 'free'
    if not verify_signature(license_data):
        raise LicenseError('License signature verification failed. Please ensure your license file is valid.')
    # Parse payload
    try:
        payload = json.loads(license_data['payload'])
    except Exception:
        raise LicenseError('License payload is invalid.')
    # Check required fields
    if 'tier' not in payload or payload['tier'] not in ('free', 'pro'):
        raise LicenseError('License tier is missing or invalid.')
    return payload['tier']
