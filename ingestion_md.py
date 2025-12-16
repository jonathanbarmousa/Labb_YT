from backend.constants import DATA_PATH, VECTOR_DATABASE_PATH
from backend.data_models import TranscriptYT
import time
from pathlib import Path
import lancedb

# Setting up Vector database
def setup_db(path): 
    Path(path).mkdir(exist_ok=True) # Creates knowledge base folder if not exists
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("transcripts", schema=TranscriptYT, exist_ok=True)
    return vector_db


# Ingesting markdown files to Vector database
def md_ingestion(table):
    for file in DATA_PATH.glob("*.md"):  
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        transcript_id = file.stem
        table.delete(f"transcript_id = '{transcript_id}'") # Delete old table if exists
        table.add([
            {
                "transcript_id": transcript_id,
                "source": file.name,
                "content": content
            }
        ]) 
        
        print(f"File ingested: {file.name}")
        print(table.to_pandas()["transcript_id"])   
        time.sleep(20)
        

if __name__ == '__main__':
    vector_db = setup_db(VECTOR_DATABASE_PATH)
    md_ingestion(vector_db["transcripts"])