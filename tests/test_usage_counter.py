import unittest
import os
from tablint.usage_counter import load_counter, save_counter, check_and_increment, COUNTER_PATH, FREE_LIMIT
import datetime
import json

class TestUsageCounter(unittest.TestCase):
    def setUp(self):
        if os.path.exists(COUNTER_PATH):
            os.remove(COUNTER_PATH)

    def tearDown(self):
        if os.path.exists(COUNTER_PATH):
            os.remove(COUNTER_PATH)

    def test_counter_increment_and_reset(self):
        # Should start at 0
        count, month = load_counter()
        self.assertEqual(count, 0)
        now_month = datetime.date.today().strftime('%Y-%m')
        # Increment
        check_and_increment('free')
        count, month = load_counter()
        self.assertEqual(count, 1)
        # Simulate month change
        save_counter(10, '2000-01')
        check_and_increment('free')
        count, month = load_counter()
        self.assertEqual(count, 1)
        self.assertEqual(month, now_month)

    def test_free_limit(self):
        save_counter(FREE_LIMIT, datetime.date.today().strftime('%Y-%m'))
        with self.assertRaises(Exception) as ctx:
            check_and_increment('free')
        msg = str(ctx.exception)
        self.assertIn('Free tier limit exceeded', msg)
        self.assertIn('Buy Pro', msg)

    def test_pro_unlimited(self):
        save_counter(1000, datetime.date.today().strftime('%Y-%m'))
        # Should not raise for pro
        try:
            check_and_increment('pro')
        except Exception:
            self.fail('check_and_increment raised for pro tier')

if __name__ == "__main__":
    unittest.main()
