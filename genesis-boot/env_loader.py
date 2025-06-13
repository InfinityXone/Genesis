import os
from dotenv import load_dotenv

def load_env():
    print("🔐 Loading ENV...")
    load_dotenv()

    keys = ["OPENAI_KEY", "SUPABASE_URL", "SUPABASE_KEY", "GROQ_KEY"]
    missing = [k for k in keys if not os.getenv(k)]

    if missing:
        print(f"❌ Missing keys: {missing}")
        return False

    print("✅ ENV Loaded")
    return True
