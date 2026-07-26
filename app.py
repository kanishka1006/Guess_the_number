import random
import streamlit as st

st.set_page_config(
    page_title="Guess The Number",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 Guess The Number")
st.subheader("Player vs AI")

st.markdown("---")

# Store AI number only once
if "ai_number" not in st.session_state:
    st.session_state.ai_number = random.randint(1, 100)

# Store game status
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# AI Guessing Variables
if "low" not in st.session_state:
    st.session_state.low = 1

if "high" not in st.session_state:
    st.session_state.high = 100

if "ai_guess" not in st.session_state:
    st.session_state.ai_guess = None


# Player Secret Number
player_secret = st.number_input(
    "🎯 Choose your Secret Number",
    min_value=1,
    max_value=100,
    step=1,
)

# Player Guess
guess = st.number_input(
    "🤖 Guess the AI's Number",
    min_value=1,
    max_value=100,
    step=1,
    key="guess",
)

col1, col2 = st.columns(2)

with col1:
    submit = st.button("🎮 Submit Guess", use_container_width=True)

with col2:
    reset = st.button("🔄 New Game", use_container_width=True)

if submit:

    if guess < st.session_state.ai_number:
        st.warning("⬆️ Higher!")

    elif guess > st.session_state.ai_number:
        st.warning("⬇️ Lower!")

    else:
        st.success("🎉 Correct! You guessed the AI's number.")
        st.balloons()
        st.session_state.game_over = True

if reset:
    st.session_state.ai_number = random.randint(1,100)
    st.session_state.game_over = False
    st.rerun()

st.markdown("---")
st.subheader("🤖 AI's Turn")

if st.session_state.ai_guess is None:
    st.session_state.ai_guess = (
        st.session_state.low + st.session_state.high
    ) // 2

st.info(f"🤖 AI guesses: {st.session_state.ai_guess}")

response = st.radio(
    "Tell the AI if its guess is:",
    ["Higher", "Lower", "Correct"],
    horizontal=True
)

if st.button("Submit AI Response"):

    if response == "Higher":
        st.session_state.low = st.session_state.ai_guess + 1

    elif response == "Lower":
        st.session_state.high = st.session_state.ai_guess - 1

    else:
        st.success("🤖 AI guessed your number!")
        st.balloons()

    if response != "Correct":
        st.session_state.ai_guess = (
            st.session_state.low + st.session_state.high
        ) // 2

        st.rerun()