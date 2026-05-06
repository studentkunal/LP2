def chatbot():
    print("🤖 Chatbot: Hello! Welcome to our store.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        # Exit condition
        if user == "exit":
            print("🤖 Chatbot: Thank you! Visit again.")
            break

        # Greetings
        elif "hello" in user or "hi" in user:
            print("🤖 Chatbot: Hello! How can I help you?")

        # Product info
        elif "product" in user:
            print("🤖 Chatbot: We sell mobiles, laptops, and accessories.")

        # Price query
        elif "price" in user:
            print("🤖 Chatbot: Prices start from ₹10,000 depending on the product.")

        # Order tracking
        elif "order" in user or "track" in user:
            print("🤖 Chatbot: Please provide your order ID.")

        # Complaint
        elif "problem" in user or "complaint" in user:
            print("🤖 Chatbot: Sorry for the inconvenience. Please describe your issue.")

        # Default response
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run chatbot
chatbot()