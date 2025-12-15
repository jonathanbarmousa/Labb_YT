from pydantic_ai import Agent
from backend.data_models import RAGYTResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb


vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)
rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        """
        You are a youtuber who specializes in Data Engineering and knows how to distinguish between different topics.
        You have a friendly, generous and practical personality. 
        When explainings concepts, you use always a clear, consistent and practical language that makes easy to understand for beginners.
        The goal is to make the channel's followers learning experience better by using the provided transcripts content. 
        Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent 
        Make sure to get to the point directly and keep the answer to a maximum of 6 sentences
        If the content you find doesn't give enough information to answer, say you need more context.
        """
    ),
    output_type=RAGYTResponse # Response from Agent
)

@rag_agent.tool_plain
def retieve_docs(query: str, top_results=3) -> str:
    results = vector_db["transcripts"].search(query=query).limit(top_results).to_list() # Retrieving top results from agent
    return f"""
    Content: {results[0]["content"]}
    """