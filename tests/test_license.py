import unittest
import os
import json
from tablint.license import get_license_tier, LicenseError

class TestLicense(unittest.TestCase):
    def setUp(self):
        self.license_path = os.path.expanduser('~/.csv_guard.license')
        self.valid_payload = json.dumps({"tier": "free"})
        self.valid_license = {
            "payload": self.valid_payload,
            "signature": __import__('hashlib').sha256(self.valid_payload.encode('utf-8')).hexdigest()
        }
        with open(self.license_path, 'w', encoding='utf-8') as f:
            json.dump(self.valid_license, f)

    def tearDown(self):
        if os.path.exists(self.license_path):
            os.remove(self.license_path)


    def test_valid_license(self):
        tier = get_license_tier()
        self.assertEqual(tier, 'free')


    def test_invalid_signature(self):
        with open(self.license_path, 'w', encoding='utf-8') as f:
            lic = dict(self.valid_license)
            lic['signature'] = 'bad'
            json.dump(lic, f)
        with self.assertRaises(LicenseError):
            get_license_tier()


    def test_missing_license_defaults_to_free(self):
        os.remove(self.license_path)
        tier = get_license_tier()
        self.assertEqual(tier, 'free')

    def test_pro_license(self):
        valid_payload = json.dumps({"tier": "pro"})
        valid_license = {
            "payload": valid_payload,
            "signature": __import__('hashlib').sha256(valid_payload.encode('utf-8')).hexdigest()
        }
        with open(self.license_path, 'w', encoding='utf-8') as f:
            json.dump(valid_license, f)
        tier = get_license_tier()
        self.assertEqual(tier, 'pro')

if __name__ == "__main__":
    unittest.main()
