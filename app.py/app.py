from transformers import pipeline

# 1. Load the model
print("Loading AI model... please wait.")
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# 2. Parvin E'tesami Context
context_text = """
Parvin E'tesami was a prominent Iranian poet known for her didactic and social poetry. 
She was born in 1907 in Tabriz and grew up in a literary family. 
Her poems often focused on themes of social justice, poverty, and the role of women in society. 
She is considered one of the most influential female poets of Iran.
"""

def run_qa_bot():
    print("\n" + "="*40)
    print("AI BOT READY: Ask about Parvin E'tesami")
    print("Type 'quit' to stop.")
    print("="*40)
    
    while True:
        user_question = input("Your Question: ").strip()

        if user_question.lower() in ["quit", "exit", "stop"]:
            print("Shutting down. Goodbye!")
            break

        if not user_question:
            continue

        # Process the answer
        result = qa_model(question=user_question, context=context_text)
        print(f"Answer: {result['answer']}")
        print(f"Confidence: {result['score']:.2%}")
        print("-" * 30)

# 3. Start the bot directly
run_qa_bot()