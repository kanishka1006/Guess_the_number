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

# ---------------- Session State ---------------- #

if "ai_number" not in st.session_state:
    st.session_state.ai_number = random.randint(1, 100)

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "turn" not in st.session_state:
    st.session_state.turn = "ai"

if "low" not in st.session_state:
    st.session_state.low = 1

if "high" not in st.session_state:
    st.session_state.high = 100

if "ai_guess" not in st.session_state:
    st.session_state.ai_guess = None

if "last_hint" not in st.session_state:
    st.session_state.last_hint = ""

# ---------------- Start Screen ---------------- #

if not st.session_state.game_started:

    player_secret = st.number_input(
        "🎯 Choose Your Secret Number",
        min_value=1,
        max_value=100,
        step=1,
    )

    if st.button("🚀 Start Game", use_container_width=True):
        st.session_state.player_secret = player_secret
        st.session_state.game_started = True
        st.rerun()

# ---------------- Game ---------------- #

if st.session_state.game_started and not st.session_state.game_over:

    # Show previous hint
    if st.session_state.last_hint:
        st.info(st.session_state.last_hint)

    # ================= AI TURN ================= #

    if st.session_state.turn == "ai":

        st.subheader("🤖 AI's Turn")

        if st.session_state.ai_guess is None:
            st.session_state.ai_guess = (
                st.session_state.low + st.session_state.high
            ) // 2

        st.info(f"🤖 AI guesses: {st.session_state.ai_guess}")

        response = st.radio(
            "Tell the AI:",
            ["Higher", "Lower", "Correct"],
            horizontal=True,
        )

        if st.button("Submit AI Response"):

            if response == "Higher":
                st.session_state.low = st.session_state.ai_guess + 1

            elif response == "Lower":
                st.session_state.high = st.session_state.ai_guess - 1

            else:
                st.success("🤖 AI guessed your number!")
                st.balloons()
                st.session_state.game_over = True

            if not st.session_state.game_over:

                st.session_state.ai_guess = (
                    st.session_state.low + st.session_state.high
                ) // 2

                st.session_state.turn = "player"
                st.rerun()

    # ================= PLAYER TURN ================= #

    elif st.session_state.turn == "player":

        st.subheader("👤 Your Turn")

        guess = st.number_input(
            "Guess the AI's Number",
            min_value=1,
            max_value=100,
            step=1,
            key="guess"
        )

        col1, col2 = st.columns(2)

        with col1:
            submit = st.button(
                "🎮 Submit Guess",
                use_container_width=True
            )

        with col2:
            new_game = st.button(
                "🔄 New Game",
                use_container_width=True
            )

        if submit:

            if guess < st.session_state.ai_number:
                st.session_state.last_hint = "⬆️ AI says: Higher!"
                st.session_state.turn = "ai"
                st.rerun()

            elif guess > st.session_state.ai_number:
                st.session_state.last_hint = "⬇️ AI says: Lower!"
                st.session_state.turn = "ai"
                st.rerun()

            else:
                st.success("🎉 You guessed the AI's number!")
                st.balloons()
                st.session_state.game_over = True

        if new_game:

            st.session_state.ai_number = random.randint(1, 100)
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.ai_guess = None
            st.session_state.turn = "ai"
            st.session_state.game_started = False
            st.session_state.game_over = False
            st.session_state.last_hint = ""

            st.rerun()

# ---------------- Winner ---------------- #

if st.session_state.game_over:

    st.success("🎉 Game Over!")

    if st.button("Play Again"):

        st.session_state.ai_number = random.randint(1, 100)
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.ai_guess = None
        st.session_state.turn = "ai"
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.last_hint = ""

        st.rerun()