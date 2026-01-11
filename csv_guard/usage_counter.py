import os
import json
import datetime
from typing import Tuple

COUNTER_PATH = os.path.expanduser('~/.csv_guard.usage')
FREE_LIMIT = 50

def load_counter() -> Tuple[int, str]:
    if not os.path.exists(COUNTER_PATH):
        return 0, datetime.date.today().strftime('%Y-%m')
    try:
        with open(COUNTER_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('count', 0), data.get('month', datetime.date.today().strftime('%Y-%m'))
    except Exception:
        return 0, datetime.date.today().strftime('%Y-%m')

def save_counter(count: int, month: str):
    with open(COUNTER_PATH, 'w', encoding='utf-8') as f:
        json.dump({'count': count, 'month': month}, f)

def check_and_increment(tier: str) -> None:
    count, month = load_counter()
    now_month = datetime.date.today().strftime('%Y-%m')
    if month != now_month:
        count = 0
        month = now_month
    if tier == 'free' and count >= FREE_LIMIT:
        raise Exception(f"Free tier limit exceeded: {FREE_LIMIT} validations per month. Please upgrade to Pro.")
    count += 1
    save_counter(count, month)
