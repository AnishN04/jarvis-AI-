from google import genai
import os
from dotenv import load_dotenv

def test_gemini():
    print("--- Jarvis Gemini SDK V1 Diagnostic Tool ---")
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in .env file.")
        return

    print(f"API Key found (starts with: {api_key[:4]}...)")
    
    try:
        client = genai.Client(api_key=api_key)
        
        print("\nListing available models:")
        try:
            for m in client.models.list():
                print(f" - {m.name}")
        except Exception as e:
            print(f"Error listing models: {e}")

        print("\nTesting 'gemini-1.5-flash' specifically...")
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents="Hi"
            )
            print(f"Success! Response: {response.text}")
        except Exception as e:
            print(f"Failed with 'gemini-1.5-flash': {e}")

    except Exception as e:
        print(f"General Error: {e}")

if __name__ == "__main__":
    test_gemini()
