from src.loader import load_text_documents
from src.chunker import split_documents
from src.embedder import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.llm import get_llm
from src.prompt import get_prompt
from src.rag_chain import create_rag_chain


def main():

    # Load documents
    documents = load_text_documents()
    print(f"Loaded {len(documents)} documents")

    # Split documents
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    # Embedding model
    embedding_model = get_embedding_model()

    # Vector store
    vector_store = create_vector_store(chunks, embedding_model)

    # Retriever
    retriever = get_retriever(vector_store)

    # Prompt
    prompt = get_prompt()

    # LLM
    llm = get_llm()

    # Create RAG Chain
    rag_chain = create_rag_chain(
        retriever,
        prompt,
        llm
    )

    while True:

        question = input("\nAsk a medical question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = rag_chain.invoke(question)

        print("\nAnswer:\n")
        print(answer)
        print("-" * 70)


if __name__ == "__main__":
    main()