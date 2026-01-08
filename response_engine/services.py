from .utils import choose_random

def generate_response(room_type, recent_interactions, semantic_context):
    """
    Core Response Engine logic
    No rule traceability
    Safe to no-op
    """

    # 1️⃣ Base response pool
    base_responses = [
        "Understood.",
        "Noted.",
        "Okay.",
        "I see.",
    ]

    # 2️⃣ Context-aware enrichment
    if semantic_context:
        base_responses.extend([
            f"This seems related to {semantic_context[0]}",
            f"Earlier context suggests {semantic_context[0]}",
        ])

    # 3️⃣ Room-specific tuning
    if room_type == "PRIVATE_DIALOGUE":
        base_responses.extend([
            "Tell me more.",
            "I'm listening.",
        ])

    if room_type == "PUBLIC_CHAT":
        base_responses.extend([
            "Let's keep it moving.",
            "Continuing the discussion.",
        ])

    # 4️⃣ Non-deterministic pick
    text_response = choose_random(base_responses)

    # 5️⃣ Optional audio tokens (ONLY if audio room)
    audio_tokens = None
    if room_type == "AUDIO_BROADCAST":
        audio_tokens = ["<pause>", text_response, "<end>"]

    # 6️⃣ Graceful degradation
    return {
        "text": text_response,
        "audio_tokens": audio_tokens
    }
