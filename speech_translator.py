#-----------------------------------------This code can convert any language into the given target language---------------------------------------#


import azure.cognitiveservices.speech as speechsdk

def translate_speech_from_hindi(subscription_key, region):
    # Mapping of language codes to their full names
    language_names = {
        "fr": "French",
        "en": "English",
        "ta": "Tamil",
        "or": "oriya",
        "mr": "Marathi",
        "bn": "Bengali",
        "gu": "Gujarati",
        "hi-IN": "Hindi"
    }
    
    # Create a speech translation configuration
    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=subscription_key, region=region)
    
    # Set the language for speech recognition to Hindi (India)
    translation_config.speech_recognition_language = "en-US"
    
    # Add target languages for translation
    target_languages = ["fr", "en", "ta", "or", "mr", "bn", "gu", "hi-IN" ]  # French, English, Tamil, Telugu, Marathi, Bengali, Gujarati
    for language in target_languages:
        translation_config.add_target_language(language)
    
    # Create a translation recognizer with the given settings
    recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)
    
    print("Say something in english...")
    
    # Start speech recognition and translation
    result = recognizer.recognize_once()
    
    # Check the result
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print(f"Recognized: {result.text}")
        print("Translations:")
        for language, translation in result.translations.items():
            language_full_name = language_names.get(language, language)
            print(f"{language_full_name} ({language}): {translation}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

# Replace with your Azure subscription key and service region
subscription_key = "f08d5e67aa82417abb102789759b0c87"
region = "eastus"

# Call the function to recognize and translate speech from Hindi
translate_speech_from_hindi(subscription_key, region)