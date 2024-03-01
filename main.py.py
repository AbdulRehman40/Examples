import streamlit as st
import random

st.title("Bano Qabil 2.0")

# Display the Bano Qabil logo
st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://banoqabil.pk/media/logo.png" width="200">
    </div>
""", unsafe_allow_html=True)  # Allow HTML rendering in Streamlit


# List of scrambled sentences and their corresponding correct answers
sentences = [
    ("Q1: What does GB stand for in computing?", "Gigabyte"),
    ("Q2: When was the first computer invented?", "Various"),
    ("Q3: What does CPU stand for?", "Central Processing Unit"),
    ("Q4: What component produces audio output on a computer?", "Speaker"),
    ("Q5: What is needed to connect to the internet?", "Device"),
    ("Q6: What does WWW stand for?", "World Wide Web"),
    ("Q7: What do the initials CD stand for?", "Compact Disc"),
    ("Q8: Who invented the first mechanical computer?", "Babbage"),
    ("Q9: What does a Printer do?", "Printing"),
    ("Q10: What does bit stand for in computing?", "Binary")
]

# Function to scramble the words in a sentence
def scramble_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    return " ".join(words)

# Function to check if the user's answer is correct
def check_answer(original_sentence, user_answer):
    for sent, correct_answer in sentences:
        if sent == original_sentence:
            return user_answer.lower() == correct_answer.lower()
    return False

def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("", ["Home", "About us", "Contact us"])

    if tab == "Home":
        st.title("Puzzle Game")

        if sentences:  # Check if there are sentences available
            # Select a random sentence and its corresponding correct answer from the list
            sentence, correct_answer = random.choice(sentences)
            scrambled_sentence = scramble_sentence(sentence)

            st.write("Unscramble the sentence:")
            st.write(scrambled_sentence)

            user_answer = st.text_input("Your Answer")

            if st.button("Check Answer"):
                if check_answer(sentence, user_answer):
                    st.success("Congratulations! Your answer is correct.")
                else:
                    st.error("Sorry, your answer is incorrect. Please try again.")
                    st.info(f"The correct answer is: {correct_answer}")
        else:
            st.warning("No sentences available.")

    elif tab == "About us":
        st.title("About Us")
        st.markdown(
            """
            *Team Name*: Python Programmer  
            *Team Leader*: Syed Muhammad Shujaat Ali  
            *Members*:  
            - Hafiz M. Abdul Rehman  
            - Muhammad Anus  

            *Project Description*:  
            The final project submitted in Bano Qabil 2.0.  
            This project is a puzzle game developed using Python. Puzzle games are excellent for learning and help in developing crucial skills like problem-solving and critical thinking. This game is built online and provides an engaging platform for users to enhance their cognitive abilities.
            """
        )
    elif tab == "Contact us":
        st.title("Contact Us")
        st.markdown(
            """
            *Leader*: Syed Muhammad Shujaat Ali  
            *Email*: shujaatali@gmail.com  
            *Contact*: 03321031301  

            *Member2: Muhammad Anus*  
            *Email*: anusmahir6@gmail.com  
            *Contact*: 03162785597  

            *Member3: Hafiz M. Abdul Rehman*  
            *Email*: chappalwala00@gmail.com  
            *Contact*: 03162343374  
            """
        )

if _name_ == "_main_":
    main()
