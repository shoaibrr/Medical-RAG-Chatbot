from langchain_core.prompts import ChatPromptTemplate


def get_prompt():

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert medical assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:

"I don't have enough information in the provided medical documents."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt