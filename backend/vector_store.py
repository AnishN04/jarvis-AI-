import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from typing import List, Dict

class VectorStore:
    def __init__(self, api_key: str, index_name: str = "jarvis-knowledge"):
        """Initialize Pinecone vector store"""
        self.pc = Pinecone(api_key=api_key)
        self.index_name = index_name
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Create index if it doesn't exist
        if index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=index_name,
                dimension=384,  # all-MiniLM-L6-v2 embedding dimension
                metric='cosine',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )
        
        self.index = self.pc.Index(index_name)
    
    def add_documents(self, documents: List[str], metadata: List[Dict] = None):
        """Add documents to the vector store"""
        embeddings = self.embedding_model.encode(documents)
        
        vectors = []
        for i, (doc, emb) in enumerate(zip(documents, embeddings)):
            vector_id = f"doc_{i}"
            meta = metadata[i] if metadata and i < len(metadata) else {"text": doc}
            vectors.append({
                "id": vector_id,
                "values": emb.tolist(),
                "metadata": meta
            })
        
        self.index.upsert(vectors=vectors)
        print(f"Added {len(vectors)} documents to vector store")
    
    def search(self, query: str, top_k: int = 3) -> List[str]:
        """Search for relevant documents"""
        query_embedding = self.embedding_model.encode([query])[0]
        
        results = self.index.query(
            vector=query_embedding.tolist(),
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
