import streamlit as st
from main import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

st.image("./images/banner.png", width=500)
st.title(":zap: Password Generator")


option = st.radio(
    "Select a password generator",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == 'Pin Code':
    
    length = st.slider("Select the lenght of the Pin Code.", 4, 32)

    generator = PinGenerator(length)

elif option == 'Random Password':
    length = st.slider("Select the lenght of the Password.", 8, 100)
    include_number = st.toggle("Include Numbers")
    include_symbol = st.toggle("Include Symbols")

    generator = RandomPasswordGenerator(length, include_number, include_symbol )

elif option == 'Memorable Password':
    num_of_words = st.slider("Select the number of words:", 2, 10)
    separator = st.text_input("Seperator", value='-')
    capitalize = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(num_of_words, separator, capitalize)


     
    
password = generator.generate()
st.write(fr"Your password is: `{password}`")
