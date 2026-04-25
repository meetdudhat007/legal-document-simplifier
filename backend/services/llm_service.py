import os
import json
import re
from pydantic import BaseModel, Field
from typing import List

# Try to use Hugging Face InferenceClient, fallback to mock for demo
USE_MOCK = False
HF_TOKEN = None

def get_hf_token():
    global HF_TOKEN
    if HF_TOKEN is None:
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if api_key and api_key != "your_huggingface_api_key_here":
            HF_TOKEN = api_key
    return HF_TOKEN

def query_huggingface(messages: list) -> str:
    """Call Hugging Face Inference API with fallback to mock"""
    token = get_hf_token()
    
    if not token:
        return generate_mock_response(messages)
    
    try:
        from huggingface_hub import InferenceClient
        client = InferenceClient(token=token)
        
        # Get the last user message
        user_message = ""
        for msg in reversed(messages):
            if msg.get("role") == "user":
                user_message = msg.get("content", "")
                break
        
        # Try text generation as fallback
        response = client.text_generation(
            user_message[:500],  # Limit input
            model="gpt2",
            max_new_tokens=200
        )
        return response
    except Exception as e:
        error_msg = str(e)
        # Always fall back to mock for any error
        return generate_mock_response(messages)

def generate_mock_response(messages: list) -> str:
    """Generate a mock response for demo when API is not available"""
    # Get the user message
    user_message = ""
    for msg in reversed(messages):
        if msg.get("role") == "user":
            user_message = msg.get("content", "")
            break
    
    # Check if this is a JSON request (document analysis)
    if "JSON" in user_message or "summary" in user_message.lower():
        return json.dumps({
            "summary": "This is a demo response. Configure your Hugging Face API key with enabled Inference API providers to get real AI responses. Go to https://huggingface.co/settings/inference to enable providers.",
            "simplified_text": "The document analysis feature requires a valid Hugging Face API token with Inference API access. Please visit your Hugging Face account settings to enable the Inference API service.",
            "key_points": [
                "Configure Hugging Face API key in backend/.env file",
                "Enable Inference API providers in Hugging Face settings",
                "Get a new API token from https://huggingface.co/settings/tokens",
                "This is a demo response - AI processing not available"
            ]
        })
    
    # For chat responses
    return "This is a demo response. The AI processing is currently unavailable because your Hugging Face API token doesn't have Inference API providers enabled. Please configure your Hugging Face account with enabled Inference API providers for full functionality."

class ProcessedDocument(BaseModel):
    summary: str = Field(description="A concise overview summary (1-2 paragraphs).")
    simplified_text: str = Field(description="A simplified, plain-English version of the main points.")
    key_points: List[str] = Field(description="Key bullet points highlighting important risks, obligations, and unusual clauses.")

def process_legal_document(text: str) -> dict:
    # Cap text to stay within limits
    capped_text = text[:300000] 
    
    messages = [
        {
            "role": "system",
            "content": "You are an expert legal assistant. Always respond in valid JSON format."
        },
        {
            "role": "user",
            "content": f"""Read the following legal document and analyze it.
Provide a concise summary, a simplified plain-English version, and key bullet points highlighting risks and obligations.

Document Text:
{capped_text}

Respond in JSON format with the following structure:
{{
    "summary": "A concise overview summary (1-2 paragraphs).",
    "simplified_text": "A simplified, plain-English version of the main points.",
    "key_points": ["Key bullet point 1", "Key bullet point 2", "Key bullet point 3"]
}}"""
        }
    ]
    
    response = query_huggingface(messages)
    
    # Extract JSON from response
    json_match = re.search(r'\{[\s\S]*\}', response)
    if json_match:
        return json.loads(json_match.group())
    return {"summary": response, "simplified_text": "", "key_points": []}

def chat_with_document(text: str, question: str, history: List[dict] = None) -> str:
    history_str = ""
    if history:
        for msg in history:
            role = "User" if msg.get("role") == "user" else "Assistant"
            history_str += f"{role}: {msg.get('content', '')}\n"
            
    capped_text = text[:300000]
    
    messages = [
        {
            "role": "system",
            "content": "You are an expert legal assistant answering questions about a document."
        },
        {
            "role": "user",
            "content": f"""Document Context:
{capped_text}

Conversation History:
{history_str}

User Question: {question}

Answer the question clearly and accurately based ONLY on the Document Context provided. If the answer is not in the document, state that you don't know based on the document."""
        }
    ]
    
    response = query_huggingface(messages)
    return response
