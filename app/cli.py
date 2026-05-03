from app.rag_chain import answer_question


def main():
    print("Enterprise RAG Assistant CLI")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        question = input("Ask a question: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        if not question:
            print("Please enter a question.\n")
            continue

        try:
            result = answer_question(question)

            print("\nAnswer:")
            print(result["answer"])

            print("\nSources:")
            for source in result["sources"]:
                print(f"- {source}")

            print("\nRetrieved chunks:", result["retrieved_chunks"])
            print("-" * 60 + "\n")

        except Exception as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()