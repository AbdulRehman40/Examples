import streamlit as st
import random
import time

st.title("Bano Qabil Advanced Puzzle Game")

# List of scrambled sentences and their corresponding correct answers
sentences = [
    ("What does GB stand for in computing?", "Gigabyte"),
    # ... (your other sentences)
]

# Function to scramble the words in a sentence
def scramble_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    return " ".join(words)

# Function to check if the user's answer is correct
def check_answer(original_sentence, user_answer):
    return original_sentence.lower() == user_answer.lower()

def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("", ["Home", "About us", "Contact us"])

    if tab == "Home":
        st.title("Puzzle Game")

        # Display the Bano Qabil logo
        st.image("bano_qabil_logo.png", caption='Bano Qabil Logo', use_column_width=True)

        # Select a random sentence and its corresponding correct answer from the list
        sentence, correct_answer = random.choice(sentences)
        scrambled_sentence = scramble_sentence(sentence)

        st.write("Unscramble the sentence:")
        st.write(scrambled_sentence)

        user_answer = st.text_input("Your Answer")

        if st.button("Check Answer"):
            if check_answer(correct_answer, user_answer):
                st.success("Congratulations! Your answer is correct.")
            else:
                st.error("Sorry, your answer is incorrect. Please try again.")
                st.info(f"The correct answer is: {correct_answer}")

        # Add features like scoring, hints, and timer
        st.write("Score: 0")  # You can increment the score based on correct answers
        st.write("Hints left: 3")  # Allow users to use hints
        st.write("Time Left: 5:00")  # Display a countdown timer

    # ... (rest of your code)

if __name__ == "__main__":
    main()
