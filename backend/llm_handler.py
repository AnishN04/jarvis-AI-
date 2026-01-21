from google import genai
import os
from typing import List

class LLMHandler:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        """
        Initialize LLM handler using the new Google GenAI SDK
        """
        self.model_name = model_name
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.client = None
        self.is_loaded = False
        
        if self.api_key:
            try:
                self.client = genai.Client(api_key=self.api_key)
                self.is_loaded = True
                print(f"✓ Gemini model '{model_name}' initialized via new SDK")
            except Exception as e:
                print(f"✗ Error initializing Gemini SDK: {e}")
        else:
            print("⚠ Warning: GEMINI_API_KEY not found in environment")
    
    def check_connection(self) -> bool:
        """Check if Gemini API is configured and ready"""
        return self.is_loaded
    
    def generate_response(self, query: str, context: List[str] = None) -> str:
        """Generate response using Gemini with optional context"""
        
        if not self.is_loaded:
            return "Error: Gemini API not configured. Please add GEMINI_API_KEY to your .env file."
        
        # Build prompt with context if available
        if context and len(context) > 0:
            context_text = "\n\n".join(context)
            prompt = f"""
You are Jarvis, a helpful AI assistant. Use the following context to answer the user's question.
If the context doesn't contain the answer, use your general knowledge but mention it's not in the context.

Context:
{context_text}

User Question: {query}
Jarvis:"""
        else:
            prompt = f"User Question: {query}\nJarvis:"
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def chat(self, query: str, context: List[str] = None) -> dict:
        """Main chat function that returns structured response"""
        if not self.check_connection():
            return {
                "success": False,
                "response": "Error: Gemini API not configured. Please check your .env file.",
                "context_used": False
            }
        
        response = self.generate_response(query, context)
        
        return {
            "success": True,
            "response": response,
            "context_used": context is not None and len(context) > 0
        }
