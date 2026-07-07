import streamlit as st

from src.loader import load_text_documents
from src.chunker import split_documents
from src.embedder import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.prompt import get_prompt
from src.llm import get_llm
from src.rag_chain import create_rag_chain


@st.cache_resource
def initialize_rag():

    # Load documents
    documents = load_text_documents()

    # Split documents
    chunks = split_documents(documents)

    # Load embedding model
    embedding_model = get_embedding_model()

    # Create vector store
    vector_store = create_vector_store(chunks, embedding_model)

    # Create retriever
    retriever = get_retriever(vector_store)

    # Load prompt
    prompt = get_prompt()

    # Load LLM
    llm = get_llm()

    # Create RAG chain
    rag_chain = create_rag_chain(
        retriever,
        prompt,
        llm
    )

    return rag_chain, retriever


# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="Healthcare RAG Chatbot",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Healthcare RAG Chatbot")

# ---------------- Sidebar ----------------

with st.sidebar:

    st.header("📋 Healthcare RAG Chatbot")

    st.markdown("---")

    st.subheader("📚 Loaded Documents")

    st.write("✅ doctor_note_001.txt")
    st.write("✅ doctor_note_002.txt")
    st.write("✅ discharge_summary_001.txt")
    st.write("✅ lab_report_001.txt")
    st.write("✅ lab_report_002.txt")
    st.write("✅ prescription_001.txt")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.info(
        """
**Model:** Gemini 2.5 Flash

**Vector DB:** Chroma

**Embedding:** all-MiniLM-L6-v2

**Retriever:** Similarity Search
        """
    )

# ---------------- Initialize RAG ----------------

rag_chain, retriever = initialize_rag()

# ---------------- Chat History ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- Chat Input ----------------

question = st.chat_input("Ask a medical question...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Retrieve documents
    docs = retriever.invoke(question)

    # Generate answer
    answer = rag_chain.invoke(question)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):

        st.markdown(answer)

        with st.expander("📄 View Retrieved Documents"):

            for i, doc in enumerate(docs, start=1):

                st.markdown(f"### Document {i}")

                if "source" in doc.metadata:
                    st.write(f"**Source:** {doc.metadata['source']}")

                st.text(doc.page_content)

                st.divider()
                import os

st.sidebar.header("📂 Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload Medical Documents",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if st.sidebar.button("Process Documents"):

    upload_folder = "uploads"

    os.makedirs(upload_folder, exist_ok=True)

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            upload_folder,
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    st.sidebar.success("Documents uploaded successfully!")