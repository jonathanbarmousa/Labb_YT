RAG Lab - YouTuber Chatbot

Detta projekt syftar till att skapa en RAG (Retrieval-Augmented Generation) chatbot som svarar på frågor om Data Engineering baserat på transkript från en YouTuber som lär ut Data Engineering. Projektet använder PydanticAI, LanceDB, FastAPI och Streamlit.

Funktioner

Datainmatning: Mata in video-transkript till en vektordatabas med LanceDB.

API Backend: Fråga kunskapsbasen via en FastAPI backend.

Chatbot-Interface: Interagera med chatboten via ett Streamlit frontend, där användare kan ställa frågor eller skicka meddelanden baserat på kunskapsbasen.

Huvudmålet är att förbättra lärandeupplevelsen genom att använda det tillhandahållna transkriptinnehållet.

1. Installation

Följ dessa steg för att initiera projektet och aktivera din virtuella miljö:

Initialisera projektet och aktivera den virtuella miljön:

uv init
source .venv/Scripts/activate


Lägg till nödvändiga paket:

uv add "package_name"


Exempel:

uv add streamlit


Generera din Gemini API-nyckel:
Logga in på Google AI Studio
 för att generera din Gemini API-nyckel.

Spara din API-nyckel:
Skapa en .env-fil i projektets rotmapp och lägg till din API-nyckel:

GOOGLE_API_KEY=<your_generated_api_key>


Viktigt: Se till att lägga till .env i din .gitignore-fil för att förhindra att dina credentials läcker på GitHub.

2. Mata in Data till LanceDB

Kör ingestion.py för att ladda in video-transkripten till LanceDB vektordatabasen:

uv run ingestion.py

3. Testa FastAPI Backend

För att starta FastAPI backend för att testa, kör:

uv run uvicorn api:app --reload


Öppna API-dokumentationen i din webbläsare:

http://127.0.0.1:8000/docs

Här kan du prova några frågor eller meddelanden, och chatboten kommer att svara baserat på kunskapsbasen.

4. Öppna Frontend i Streamlit

För att interagera med chatboten via frontend, gå till frontend-mappen och kör Streamlit-appen:

cd frontend
uv run streamlit run app.py


Detta öppnar chatbot-interfacet och låter dig börja prata med RAGtuber chatboten.

5. Distribution till Azure via VSCode (Valfritt)

Om du vill distribuera din FastAPI backend till Azure, följ dessa steg:

Installera Azure Functions i VSCode: Installera Azure Functions-tillägget i VSCode.

Skapa en Function App:

Klicka på "Create Function App in Azure".

Ange ett namn för funktionens app.

Välj lämplig plats och Python-version (t.ex., Python 3.12).

Välj "Managed Identity" för autentiseringsmetoden.

Distribuera:
När funktionens app har skapats, kan du distribuera den till Azure, och den kommer att vara tillgänglig i Azure-portalen.