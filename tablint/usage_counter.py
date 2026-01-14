
import os
import json
import datetime
from typing import Tuple

PRO_BUILD = False  # Set to True for Pro build
COUNTER_PATH = os.path.expanduser('~/.csv_guard.usage')
FREE_LIMIT = 50  # evaluation mode (limited validations)

def load_counter(path: str = COUNTER_PATH) -> Tuple[int, str]:
    if not os.path.exists(path):
        return 0, datetime.date.today().strftime('%Y-%m')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('count', 0), data.get('month', datetime.date.today().strftime('%Y-%m'))
    except Exception:
        return 0, datetime.date.today().strftime('%Y-%m')

def save_counter(count: int, month: str, path: str = COUNTER_PATH) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'count': count, 'month': month}, f)

def check_and_increment(tier: str, path: str = COUNTER_PATH) -> None:
    count, month = load_counter(path)
    now_month = datetime.date.today().strftime('%Y-%m')
    if month != now_month:
        count = 0
        month = now_month
    if not PRO_BUILD and tier == 'free' and count >= FREE_LIMIT:
        # Do not increment or save if limit is hit
        raise Exception(f"Free tier limit exceeded: {FREE_LIMIT} validations. Buy Pro for unlimited usage.")
    count += 1
    save_counter(count, month, path)
