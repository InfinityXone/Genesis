# Genesis Recursive Boot Code v1
import os
from env_loader import load_env
from system_check import run_checks
from agent_registry import initialize_agents
from prediction_loop import start_prediction_loop
from fallback_recovery import enable_self_healing

def boot_genesis():
    print("🔁 [Genesis] Booting AI Agentic System...")

    if not load_env():
        raise SystemExit("❌ ENV VARS missing. Boot terminated.")

    if not run_checks():
        raise SystemExit("❌ System checks failed. Boot halted.")

    initialize_agents()

    enable_self_healing()

    start_prediction_loop()

    print("✅ [Genesis] Recursive AI Loop Online. Predictions Activated.")

if __name__ == "__main__":
    boot_genesis()
