from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE


def get_llm():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME,
        temperature=TEMPERATURE,
    )
