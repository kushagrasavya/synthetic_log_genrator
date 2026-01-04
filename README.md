Purpose of each code:


🔹data/raw/syslogs.log

Purpose:

Your original EC2 syslog

Never modified

Used as a template baseline

👉 This is the file you already uploaded.

🔹 data/processed/synthetic_syslogs.log

Purpose:

Final output file

Contains:

Real logs

Randomized attacks

Rewritten every run

🔹 generator/__init__.py

Purpose:

Marks generator/ as a Python package

Can be empty

🔹 generator/template_parser.py

Purpose:

Reads your real logs

Preserves formatting

Returns logs as a list of strings

🔹 generator/faker_profiles.py

Purpose:

Uses Faker

Generates realistic:

SSH failures

User creation logs

CPU overload logs

This is where realism lives.

🔹 generator/attack_catalog.py

Purpose:

Defines:

Attack scenarios

MITRE-style chains

Randomly selects attack per run

🔹 generator/attack_parameters.py

Purpose:

Controls randomness:

Event count

Delay

Intensity

This avoids “script-like” attacks.

🔹 generator/injector.py

Purpose:

Core brain

Injects attacks into real logs

Maintains order & timing realism
