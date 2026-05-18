# # AskQuery/rag_engine.py

# import os
# from pathlib import Path
# from dotenv import load_dotenv
# import google.generativeai as genai

# from AskQuery.vector_store import (
#     vector_store
# )


# # -------------------------------------
# # Load env
# # -------------------------------------

# ROOT = Path(__file__).resolve().parent.parent

# load_dotenv(
#     ROOT / ".env"
# )


# # -------------------------------------
# # Generate response
# # -------------------------------------

# def generate_analysis(
#     df,
#     user_query
# ):

#     try:

#         API_KEY = os.getenv(
#             "GOOGLE_API_KEY"
#         )

#         if not API_KEY:

#             return (
#                 "GOOGLE_API_KEY missing"
#             )


#         genai.configure(
#             api_key=API_KEY
#         )

#         model = genai.GenerativeModel(
#             "gemini-2.5-flash"
#         )


#         # Build vector store
#         vector_store.build_index(
#             df
#         )


#         # Retrieve relevant rows
#         retrieved = vector_store.search(
#             user_query,
#             top_k=5
#         )


#         if len(retrieved) == 0:

#             return (
#                 "No relevant data found."
#             )


#         retrieved_context = "\n\n".join(
#             retrieved
#         )


#         prompt = f"""
# You are VoxQuery.

# Retrieved Dataset Context:

# {retrieved_context}

# User Question:

# {user_query}

# Rules:

# 1. Answer only from retrieved context
# 2. Never invent information
# 3. If unavailable say:

# "This information cannot be determined."

# 4. Explain naturally
# """


#         response = model.generate_content(
#             prompt
#         )


#         return response.text


#     except Exception as e:

#         return (
#             f"RAG Error: {str(e)}"
#         )
import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd

# -----------------------------
# Load Environment Variables
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(
    dotenv_path=ENV_PATH,
    override=True
)

API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)

if not API_KEY:
    raise ValueError(
        f"GOOGLE_API_KEY missing.\nChecked: {ENV_PATH}"
    )

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# -----------------------------
# Context Builder
# -----------------------------

def build_context(df):

    sample_size = min(
        20,
        len(df)
    )

    sample_data = df.sample(
        sample_size,
        random_state=42
    )

    context = f"""
Dataset Summary

Total Rows:
{df.shape[0]}

Total Columns:
{df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

Missing Values:
{df.isnull().sum().to_string()}

Sample Records:
{sample_data.to_string()}
"""

    return context


# -----------------------------
# Analysis Function
# -----------------------------

from AskQuery.vector_store import vector_store

def generate_analysis(df, user_query):

    try:

        # Build index only once
        if vector_store.index is None:

            vector_store.build_index(df)

        # Retrieve relevant rows
        retrieved_chunks = vector_store.search(
            user_query,
            top_k=8
        )

        if not retrieved_chunks:

            return "No relevant information found."

        retrieved_context = "\n\n".join(
            retrieved_chunks
        )

        prompt = f"""
You are VoxQuery AI.

STRICT RULES:

1. Answer ONLY from retrieved data
2. Never invent values
3. If unavailable say:
"This cannot be determined from available data."

RETRIEVED DATA:

{retrieved_context}

QUESTION:

{user_query}

ANSWER:
"""

        response = model.generate_content(
            prompt
        )

        return response.text.strip()

    except Exception as e:

        return f"Analysis Error: {str(e)}"