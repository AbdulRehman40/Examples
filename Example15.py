import streamlit as st
import random
import time

st.title("Bano Qabil Advanced Puzzle Game")

# List of scrambled sentences and their corresponding correct answers
sentences = [
    ("What does GB stand for in computing?", "Gigabyte"),
    ("When was the first computer invented?", "Various"),
    ("What does CPU stand for?", "Central Processing Unit"),
    ("What component produces audio output on a computer?", "Speaker"),
    ("What is needed to connect to the internet?", "Device"),
    ("What does WWW stand for?", "World Wide Web"),
    ("What do the initials CD stand for?", "Compact Disc"),
    ("Who invented the first mechanical computer?", "Babbage"),
    ("What does a Printer do?", "Printing"),
    ("What does bit stand for in computing?", "Binary"),
    # Add more questions and answers below
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the largest mammal on Earth?", "Blue Whale"),
    ("Which planet is known as the Red Planet?", "Mars"),
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
        score = st.session_state.get('score', 0)
        hints_left = st.session_state.get('hints_left', 3)
        st.write(f"Score: {score}")
        st.write(f"Hints left: {hints_left}")
        st.write(f"Time Left: 5:00")  # You can implement a timer

        if st.button("Use Hint"):
            if hints_left > 0:
                hints_left -= 1
                st.session_state.hints_left = hints_left
                st.info("Hint used! Click 'Check Answer' after using a hint for the updated score.")

def about_us():
    st.title("About Us")
    st.markdown(
        """
        **Team Name**: Python Programmer  
        **Team Leader**: Syed Muhammad Shujaat Ali  
        **Members**:  
        - Hafiz M. Abdul Rehman  
        - Muhammad Anus  

        **Project Description**:  
        The final project submitted in Bano Qabil 2.0.  
        This project is a puzzle game developed using Python. Puzzle games are excellent for learning and help in developing crucial skills like problem-solving and critical thinking. This game is built online and provides an engaging platform for users to enhance their cognitive abilities.
        """
    )

def contact_us():
    st.title("Contact Us")
    st.markdown(
        """
        **Leader**: Syed Muhammad Shujaat Ali  
        **Email**: shujaatali@gmail.com  
        **Contact**: 03321031301  

        **Member: Muhammad Anus**  
        **Email**: anusmahir6@gmail.com  
        **Contact**: 03162785597  

        **Member: Hafiz M. Abdul Rehman**  
        **Email**: chappalwala00@gmail.com  
        **Contact**: 03162343374  
        """
    )

def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("Select a page", ["Home", "About Us", "Contact Us"])

    if tab == "Home":
        home()
    elif tab == "About Us":
        about_us()
    elif tab == "Contact Us":
        contact_us()

if __name__ == "__main__":
    st.session_state.hints_left = 3
    st.run(main)
