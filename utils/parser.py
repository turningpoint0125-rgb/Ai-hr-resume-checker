import json
import re

def parse_output(text):

    if not text or not text.strip():
        raise ValueError(
            "The model returned an empty response. This usually means the "
            "API key is missing/invalid, or the request was blocked by a "
            "safety filter. Check your GOOGLE_API_KEY in .env."
        )

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError(
            "Could not find any JSON in the model's response. "
            f"Raw response was:\n\n{text[:1500]}"
        )

    try:
        return json.loads(match.group())
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Model response looked like JSON but failed to parse ({e}). "
            f"Raw response was:\n\n{text[:1500]}"
        )