from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from llm_handler import LLMHandler
from vector_store import VectorStore

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize components
llm = LLMHandler(model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
vector_store = None

# Initialize Pinecone if API key is available
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
if PINECONE_API_KEY:
    try:
        vector_store = VectorStore(api_key=PINECONE_API_KEY)
        print("✓ Pinecone vector store initialized")
    except Exception as e:
        print(f"⚠ Warning: Could not initialize Pinecone: {e}")
        print("  The assistant will work without knowledge retrieval.")
else:
    print("⚠ Warning: PINECONE_API_KEY not found in environment")
    print("  The assistant will work without knowledge retrieval.")

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    llm_status = llm.check_connection()
    pinecone_status = vector_store is not None
    
    return jsonify({
        "status": "running",
        "llm_loaded": llm_status,
        "pinecone_connected": pinecone_status
    })

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.json
        user_query = data.get('message', '')
        
        if not user_query:
            return jsonify({
                "success": False,
                "response": "Please provide a message"
            }), 400
        
        # Retrieve relevant context from vector store if available
        context = None
        if vector_store:
            try:
                context = vector_store.search(user_query, top_k=3)
            except Exception as e:
                print(f"Warning: Vector search failed: {e}")
        
        # Generate response using LLM
        result = llm.chat(user_query, context)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "response": f"Server error: {str(e)}"
        }), 500

@app.route('/add-knowledge', methods=['POST'])
def add_knowledge():
    """Endpoint to add documents to knowledge base"""
    if not vector_store:
        return jsonify({
            "success": False,
            "message": "Vector store not initialized. Please configure PINECONE_API_KEY."
        }), 400
    
    try:
        data = request.json
        documents = data.get('documents', [])
        
        if not documents:
            return jsonify({
                "success": False,
                "message": "Please provide documents to add"
            }), 400
        
        # Add documents to vector store
        metadata = [{"text": doc} for doc in documents]
        vector_store.add_documents(documents, metadata)
        
        return jsonify({
            "success": True,
            "message": f"Added {len(documents)} documents to knowledge base"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        }), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🤖 Jarvis AI Assistant Backend")
    print("="*50)
    print(f"LLM Status: {'✓ Loaded' if llm.check_connection() else '✗ Not Loaded'}")
    print(f"Pinecone Status: {'✓ Connected' if vector_store else '✗ Not Connected'}")
    print("="*50 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
