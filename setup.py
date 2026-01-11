from setuptools import setup, find_packages

setup(
    name="csv-guard",
    version="0.1.0",
    description="Validate CSV files against a schema (local, offline, license-enforced)",
    author="",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'csv-guard=csv_guard.cli:main',
        ],
    },
    python_requires='>=3.7',
)
