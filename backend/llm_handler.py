from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from typing import List

class LLMHandler:
    def __init__(self, model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        """Initialize LLM handler using Hugging Face Transformers"""
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading model: {model_name}")
        print(f"Using device: {self.device}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto" if self.device == "cuda" else None,
                low_cpu_mem_usage=True
            )
            
            if self.device == "cpu":
                self.model = self.model.to(self.device)
            
            self.pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_new_tokens=512,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
            
            self.is_loaded = True
            print("Model loaded successfully!")
            
        except Exception as e:
            print(f"Error loading model: {e}")
            self.is_loaded = False
    
    def check_connection(self) -> bool:
        """Check if model is loaded and ready"""
        return self.is_loaded
    
    def generate_response(self, query: str, context: List[str] = None) -> str:
        """Generate response using the LLM with optional context"""
        
        if not self.is_loaded:
            return "Error: Model not loaded. Please restart the server."
        
        if context and len(context) > 0:
            context_text = "\n\n".join(context)
            prompt = f"Context: {context_text}\n\nQuestion: {query}\n\nAnswer:"
        else:
            prompt = f"Question: {query}\n\nAnswer:"
        
        try:
            result = self.pipe(prompt)
            response = result[0]['generated_text']
            response = response.replace(prompt, "").strip()
            return response if response else "I'm not sure how to answer that."
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def chat(self, query: str, context: List[str] = None) -> dict:
        """Main chat function that returns structured response"""
        if not self.check_connection():
            return {
                "success": False,
                "response": "Error: Model is not loaded. Please restart the server.",
                "context_used": False
            }
        
        response = self.generate_response(query, context)
        
        return {
            "success": True,
            "response": response,
            "context_used": context is not None and len(context) > 0
        }
