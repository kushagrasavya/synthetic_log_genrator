import json
from generator.injector import inject_attacks

with open("data/raw/syslogs_original.log") as f:
    baseline_logs = f.readlines()

with open("data/raw/stratus_attack_plan.json") as f:
    attack_plan = json.load(f)

synthetic_logs = inject_attacks(baseline_logs, attack_plan)

with open("data/processed/synthetic_syslogs.log", "w") as f:
    f.writelines(synthetic_logs)

print("[+] Synthetic syslog generation complete.")
