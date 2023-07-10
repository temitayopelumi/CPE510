import nltk

class Chatbot:

    def __init__(self):
        self.data = {
            "person": "a human being",
            "father": "male parent of a child",
            "mother": "female parent of a child",
            "parent": "a person's father or mother",
            "child": "a son or daughter",
            "inlaw": "a relative by marriage"  
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
        user_input = input("What do you want to ask me? ")
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
