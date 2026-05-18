import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = None
        self.text_chunks = []


    # --------------------------------
    # Convert dataframe rows → chunks
    # --------------------------------

    def create_chunks(self, df):

        chunks = []

        for _, row in df.iterrows():

            text = ""

            for col in df.columns:

                value = row[col]

                text += f"{col}: {value}\n"

            chunks.append(
                text.strip()
            )

        return chunks


    # --------------------------------
    # Build vector index
    # --------------------------------

    def build_index(self, df):

        self.text_chunks = self.create_chunks(df)

        embeddings = self.model.encode(
            self.text_chunks,
            show_progress_bar=False
        )

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings
        )


    # --------------------------------
    # Hybrid retrieval
    # --------------------------------

    def search(
        self,
        query,
        top_k=20
    ):

        if self.index is None:
            return []

        query_lower = query.lower()

        keyword_results = []

        words = query_lower.split()


        # Exact keyword retrieval
        for chunk in self.text_chunks:

            chunk_lower = chunk.lower()

            for word in words:

                if (

                    len(word) > 2

                    and

                    word in chunk_lower

                ):

                    keyword_results.append(
                        chunk
                    )

                    break


        # Return exact matches first
        if keyword_results:

            unique=[]

            seen=set()

            for item in keyword_results:

                if item not in seen:

                    unique.append(
                        item
                    )

                    seen.add(
                        item
                    )

            return unique


        # Semantic fallback
        query_embedding = self.model.encode(
            [query]
        )

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        )

        distances,indices = self.index.search(
            query_embedding,
            top_k
        )


        semantic=[]

        for idx in indices[0]:

            if idx < len(self.text_chunks):

                semantic.append(
                    self.text_chunks[idx]
                )

        return semantic


# Singleton instance
vector_store = VectorStore()