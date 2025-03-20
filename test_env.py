import os
from dotenv import load_dotenv

# Force reload environment variables
load_dotenv(override=True)

# Print environment variables for debugging
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY", "MISSING"))
print("SUPABASE_URL:", os.getenv("SUPABASE_URL", "MISSING"))
print("YOUTUBE_API_KEY:", os.getenv("YOUTUBE_API_KEY", "MISSING"))
print("ELEVENLABS_API_KEY:", os.getenv("ELEVENLABS_API_KEY", "MISSING"))
print("STRIPE_SECRET_KEY:", os.getenv("STRIPE_SECRET_KEY", "MISSING"))
print("STRIPE_PUBLIC_KEY:", os.getenv("STRIPE_PUBLIC_KEY", "MISSING"))

