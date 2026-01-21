import os
from google import genai
from pinecone import Pinecone, ServerlessSpec
from typing import List, Dict

class VectorStore:
    def __init__(self, api_key: str, index_name: str = "jarvis-gemini-v2"):
        """
        Initialize Pinecone vector store using Gemini embeddings (New SDK)
        """
        self.pc = Pinecone(api_key=api_key)
        self.index_name = index_name
        
        # Configure Gemini for embeddings
        self.gemini_api_key = os.getenv('GEMINI_API_KEY')
        if self.gemini_api_key:
            self.client = genai.Client(api_key=self.gemini_api_key)
        
        # Create index if it doesn't exist
        # text-embedding-004 has 768 dimensions
        if index_name not in self.pc.list_indexes().names():
            print(f"Creating new Pinecone index '{index_name}'...")
            self.pc.create_index(
                name=index_name,
                dimension=768,
                metric='cosine',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )
        
        self.index = self.pc.Index(index_name)
    
    def get_embedding(self, text: str) -> List[float]:
        """Get embedding for a single text using Gemini New SDK"""
        result = self.client.models.embed_content(
            model="text-embedding-004",
            contents=text,
            config={
                'task_type': 'retrieval_document'
            }
        )
        return result.embeddings[0].values
    
    def add_documents(self, documents: List[str], metadata: List[Dict] = None):
        """Add documents to the vector store"""
        vectors = []
        for i, doc in enumerate(documents):
            emb = self.get_embedding(doc)
            vector_id = f"doc_{i}_{os.urandom(4).hex()}" # Unique ID
            meta = metadata[i] if metadata and i < len(metadata) else {"text": doc}
            vectors.append({
                "id": vector_id,
                "values": emb,
                "metadata": meta
            })
        
        self.index.upsert(vectors=vectors)
        print(f"Added {len(vectors)} documents to vector store")
    
    def search(self, query: str, top_k: int = 3) -> List[str]:
        """Search for relevant documents using New SDK"""
        result = self.client.models.embed_content(
            model="text-embedding-004",
            contents=query,
            config={
                'task_type': 'retrieval_query'
            }
        )
        query_embedding = result.embeddings[0].values
        
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        contexts = []
        for match in results['matches']:
            if 'text' in match['metadata']:
                contexts.append(match['metadata']['text'])
        
        return contexts
    
    def clear_index(self):
        """Clear all vectors from the index"""
        self.index.delete(delete_all=True)
        print("Cleared vector store")
