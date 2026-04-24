def build_rag_prompt(query: str, context_chunks: list, chunk_texts: list) -> str:
    """
    Build a structured prompt combining retrieved context and user query.
    """
    context_text = ""
    for i, (chunk, text) in enumerate(zip(context_chunks, chunk_texts)):
        context_text += f"""
Context {i+1} (Interaction ID: {chunk['metadata']['interaction_id']}, Date: {chunk['metadata']['date']}):
{text}
---"""

    prompt = f"""
You are an AI assistant for a Life Sciences CRM system.
You help field representatives understand their past interactions with doctors (HCPs).

Use ONLY the context below to answer the question.
If the answer is not found in the context, say: "I don't have enough information to answer that."

{context_text}

Question: {query}

Answer:
""".strip()

    return prompt