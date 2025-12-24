from transformers import pipeline

# 1. Loading the high-speed English model
print("Loading AI model... Please wait.")
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# 2. Updated context with death and age information
context_text = """
Parvin E'tesami was a prominent Iranian poet known for her didactic and social poetry. 
She was born in 1907 in Tabriz.
Her poems often focused on themes of social justice and the lives of the underprivileged.
"""

def run_qa_bot():
    print("\n" + "="*40)
    print("  Parvin E'tesami QA Bot is Ready!")
    print("  (Type 'quit' or 'exit' to stop)")
    print("="*40)

    while True:
        user_question = input("\nAsk a question about Parvin: ").strip()
        
        if user_question.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        if not user_question:
            continue

        # Get the answer from the model
        result = qa_model(question=user_question, context=context_text)
        
        print(f"\nAnswer: {result['answer']}")
        print(f"Confidence Score: {result['score']:.2%}")
        print("-" * 30)

# 3. Entry point to run the bot
if name == "__main__":
    run_qa_bot9()
