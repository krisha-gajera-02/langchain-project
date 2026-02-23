from langchain.chains import ConversationalRetrievalChain
from embeddings.vector_store import create_vector_store
from llm.groq_llm import get_llm


def get_solution_chain():
    vectorstore = create_vector_store()
    llm = get_llm()

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=False
    )

    return chain
