from src.vectorstore.chroma_store import (
    get_chroma_client,
    get_or_create_collection,
    search_collection,
)

from src.embeddings.ollama_embeddings import (
    get_embedding_model,
)

from src.retrieval.retriever import (
    format_retrieval_results,
)

from src.retrieval.retriever import (
    is_relevant,
)

from src.generation.prompt_builder import (
    build_rag_prompt,
)

from src.generation.llm import (
    get_llm,
)

from src.generation.citations import (
    format_sources,
)


def main():

    # ==========================================
    # INITIALIZE COMPONENTS ONCE
    # ==========================================

    client = get_chroma_client()

    collection = get_or_create_collection(
        client
    )

    embedding_model = get_embedding_model()

    llm = get_llm()


    # ==========================================
    # APPLICATION HEADER
    # ==========================================

    print("\n" + "=" * 60)
    print("ENTERPRISE RAG ASSISTANT")
    print("Type 'exit' to quit")
    print("=" * 60)


    # ==========================================
    # CONTINUOUS QUESTION LOOP
    # ==========================================

    while True:

        # --------------------------------------
        # GET USER QUESTION
        # --------------------------------------

        query = input(
            "\nAsk a question: "
        ).strip()


        # --------------------------------------
        # EXIT APPLICATION
        # --------------------------------------

        if query.lower() in [
            "exit",
            "quit",
            "q"
        ]:

            print("\nGoodbye!")

            break


        # --------------------------------------
        # EMPTY QUESTION VALIDATION
        # --------------------------------------

        if not query:

            print(
                "\nPlease enter a valid question."
            )

            continue


        # ======================================
        # QUERY EMBEDDING
        # ======================================

        query_embedding = (
            embedding_model.embed_query(
                query
            )
        )


        # ======================================
        # VECTOR DATABASE SEARCH
        # ======================================

        results = search_collection(
            collection=collection,
            query_embedding=query_embedding,
            top_k=3
        )


        # ======================================
        # FORMAT RETRIEVAL RESULTS
        # ======================================

        retrieved_chunks = (
            format_retrieval_results(
                results
            )
        )


        # ======================================
        # RELEVANCE GUARDRAIL
        # ======================================

        relevant = is_relevant(
            retrieved_chunks
        )


        # ======================================
        # NO RELEVANT DOCUMENT FOUND
        # ======================================

        if not relevant:

            print(
                "\nFINAL ANSWER:\n"
            )

            print(
                "I don't know based on the "
                "provided documents."
            )

            continue


        # ======================================
        # BUILD RAG PROMPT
        # ======================================

        prompt = build_rag_prompt(
            query=query,
            retrieved_chunks=retrieved_chunks
        )


        # ======================================
        # CALL LOCAL LLM
        # ======================================

        response = llm.invoke(
            prompt
        )


        # ======================================
        # PRINT FINAL ANSWER
        # ======================================

        print(
            "\nFINAL ANSWER:\n"
        )

        print(
            response.content
        )


        # ======================================
        # SOURCE CITATIONS
        # ======================================

        sources = format_sources(
            retrieved_chunks
        )


        print(
            "\nSOURCES:"
        )

        print(
            sources
        )


if __name__ == "__main__":

    main()
