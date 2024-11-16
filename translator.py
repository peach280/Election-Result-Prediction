from deep_translator import GoogleTranslator

def translate(original: str) -> tuple:
    try:
        # Using deep-translator's GoogleTranslator API
        translated_text = GoogleTranslator(source='auto', target='en').translate(original)
        return translated_text, "auto"  # Source language is detected automatically
    except Exception as e:
        print(f"Error during translation: {e}")
        return original, "unknown"

