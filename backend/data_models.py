from pydantic import Field, BaseModel
from lancedb.embeddings import get_registry
from lancedb.pydantic import Vector, LanceModel
from dotenv import load_dotenv


load_dotenv()
embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")
EMBEDDING_DIM = 3072


class TranscriptYT(LanceModel): 
    transcript_id: str = Field(description="ID of each transcript")
    source: str = Field(description="Name of the md files")
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()
    
    
class Prompt(BaseModel):
    prompt: str = Field(description="Message or question from the user.")
    
    
class RAGYTResponse(BaseModel):
    answer: str = Field(description="Answer from the user.")