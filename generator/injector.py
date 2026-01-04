from random import choice
from .attack_models import ssh_bruteforce, create_user, cryptomining
from .time_controller import generate_kernel_time

ATTACK_MAP = {
    "SSH Brute Force": ssh_bruteforce,
    "Create Local User": create_user,
    "Cryptomining": cryptomining
}

def inject_attacks(baseline_logs, attack_plan):
    synthetic = baseline_logs.copy()

    for phase in attack_plan["attack_chain"]:
        generator = ATTACK_MAP[phase["type"]]
        for _ in range(phase["duration_minutes"]):
            synthetic.append(
                f"{generate_kernel_time()} {generator()}\n"
            )

    return synthetic
