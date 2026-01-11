import unittest
import json
import os
from tablint.license import verify_signature

class TestLicenseVerifier(unittest.TestCase):
    def setUp(self):
        # Use a test payload and signature (matches the demo generator)
        self.payload = json.dumps({"email": "test@example.com", "name": "Test User", "tier": "pro"}, separators=(',', ':'))
        self.signature = __import__('hashlib').sha256(self.payload.encode('utf-8')).hexdigest()
        self.license_data = {
            'payload': self.payload,
            'signature': self.signature
        }

    def test_valid_signature(self):
        self.assertTrue(verify_signature(self.license_data))

    def test_invalid_signature(self):
        bad_license = dict(self.license_data)
        bad_license['signature'] = 'bad'
        self.assertFalse(verify_signature(bad_license))

    def test_missing_fields(self):
        self.assertFalse(verify_signature({'payload': self.payload}))
        self.assertFalse(verify_signature({'signature': self.signature}))
        self.assertFalse(verify_signature({}))

if __name__ == "__main__":
    unittest.main()
