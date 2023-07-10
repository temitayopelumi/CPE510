import nltk

class Chatbot:
    def __init__(self):
        self.data = {
            "bàbá": "òbí okùnrin",
            "ìyá": "òbí obìrin",    
            "òbí": "bàbá tàbí ìyá ọmọ",
            "eniyan": "eda eniyan",
            "ọmọ": "ọmọokùnrin tàbí ọmọobìrin",
            "ana": "ìbátan nípa ìgbéyàwó",
        }
    def get_response(self, input):
        response = ""
        for key, value in self.data.items():
            if key in input:
                response = value
                break
        return response

    def get_relationship(self, input):
        tokens = nltk.word_tokenize(input)
        tagged_tokens = nltk.pos_tag(tokens)
        for tagged_token in tagged_tokens:
            if tagged_token[1] == "NOUN":
                if tagged_token[0] in self.data:
                    return self.data[tagged_token[0]]

        return None

def main():
    chatbot = Chatbot()

    while True:
        user_input = input("What do you want to ask me?")
        response = chatbot.get_response(user_input)
        if response:
            print(response)
        else:
            relationship = chatbot.get_relationship(user_input)
            if relationship:
                print(relationship)
            else:
                print("I don't understand your question. Please try again.")

if __name__ == "__main__":
    main()

