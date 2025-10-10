import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Check if GROQ_API_KEY is set
if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY not found in .env file.")
    print("Please add your Groq API key to the .env file like this:")
    print("GROQ_API_KEY=your_api_key_here")
    exit(1)

# Initialize Groq client
try:
    print("Initializing Groq client...")
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    # List available models
    print("\nFetching available models...")
    models = client.models.list()
    print("\nAvailable models:")
    for model in models.data:
        print(f"- {model.id}")
    
    # Try with a common model name
    print("\nTrying with model: llama-3.3-70b-versatile")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Hello! How are you?",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    print("\nGroq API Response:")
    print(chat_completion.choices[0].message.content)
    
except Exception as e:
    print(f"\nError testing Groq API: {e}")
    print("\nTroubleshooting steps:")
    print("1. Make sure you have a valid Groq API key")
    print("2. Check your internet connection")
    print("3. Make sure you've added the API key to your .env file")
    print("4. Try running 'pip install --upgrade groq' to ensure you have the latest version")
    print("5. Check the Groq documentation for the latest model names: https://console.groq.com/docs/models")
    
    # If there's a way to get more detailed error info, print it
    if hasattr(e, 'response') and hasattr(e.response, 'text'):
        print("\nAdditional error details:")
        print(e.response.text)
