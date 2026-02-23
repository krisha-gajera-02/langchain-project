🚀 Features

💬 Chat-based UI 

🧠 Conversational Memory (remembers previous messages)

🔍 Semantic Search (RAG) using FAISS vector store

⚡ Groq LLM Integration 

📁 Service-based Knowledge Ingestion from text files

🖥️ Streamlit Web App (no frontend framework needed)



🧠 How It Works 

User enters a business problem

Text is embedded using Sentence Transformers

Relevant knowledge is retrieved from FAISS

Groq LLM generates a response

Conversation history is maintained

Response is displayed in chat UI


⚙️ Tech Stack
Component	   Technology

UI	           Streamlit
LLM	           Groq (via LangChain)
Embeddings	   Sentence Transformers
Vector DB	   FAISS
Framework	   LangChain
Language	   Python


1️⃣ Clone Repository

git clone https://github.com/krisha-gajera-02/langchain-project

cd ai_solution_consultant

2️⃣ Create Virtual Environment

python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

▶️ Run the Application

streamlit run app.py


🧪 Known Limitations

Theme preference resets on page refresh

Local vector store (not persistent across restarts)

Requires internet access for Groq API


👨‍💻 Author

Krisha Gajera
AI Solution Consultant Project
