import streamlit as st

# Initialize state
defaults = {
    "show_popup": False,
    "popup_step": 1,
    "selected_type": None,
    "weight": 0.0,
    "banner": None,
    "banner_type": None
}

for key, value in defaults.items():
    st.session_state.setdefault(key, value)

# Constants

MAX_WEIGHT = 15.00

import streamlit as st

# Reward multipliers
TYPES = {
    "Plastic": 5,
    "Paper": 3,
    "Metal": 8,
    "Glass": 4
}

# TITLE
# This is where I can type this

st.title("♻️ Rubbish-For-Rewards 🪙")
st.write("BETA 1.2")
st.write(" ")
st.write("Rubbish-For-Rewards is a simulation website designed to teach people about waste management, while also keeping it fun by collecting and submitting trash and obtaining rewards in return.")

# Collection

if st.button("Collect Waste"):

    st.session_state.show_popup = True
    st.session_state.popup_step = 1

@st.dialog("Collect Waste")
def collection_popup():

    if st.session_state.show_popup:
    collection_popup()

    # STEP 1
    
    if st.session_state.popup_step == 1:

        st.subheader("Waste Information")

        selected_type = st.selectbox(
            "Type",
            options=list(TRASH_TYPES.keys()),
            index=None,
            placeholder="Select...",
            key="type_selector"
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=0.0,
            step=0.01,
            value=st.session_state.weight
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Next", key="next_btn"):

                if selected_type is None:
                    st.error("Select a type first.")
                    return

                if weight <= 0:
                    st.error("Enter a valid weight.")
                    return

                st.session_state.selected_type = selected_type
                st.session_state.weight = weight
                st.session_state.popup_step = 2

                st.rerun()

        with col2:
            if st.button("Cancel", key="cancel_btn_1"):

                st.session_state.show_popup = False
                st.session_state.popup_step = 1

                st.session_state.banner = (
                    "Collection canceled."
                )

                st.session_state.banner_type = "warning"

                st.rerun()

    # STEP 2
    
    elif st.session_state.popup_step == 2:

        st.subheader("Review Submission")

        st.write(
            f"**Type:** {st.session_state.selected_type}"
        )

        st.write(
            f"**Weight:** {st.session_state.weight:.2f} kg"
        )

        reward = (
            TRASH_TYPES[st.session_state.selected_type]
            * st.session_state.weight
        )

        st.write(
            f"**Estimated Reward:** {reward:.2f} points"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Back", key="back_btn"):

                st.session_state.popup_step = 1
                st.rerun()

        with col2:
            if st.button("Proceed", key="proceed_btn"):

                st.session_state.show_popup = False

                st.session_state.banner = (
                    f"Success! Reward Earned: "
                    f"{reward:.2f} points"
                )

                st.session_state.banner_type = "success"

                st.session_state.popup_step = 1

                st.rerun()

        with col3:
            if st.button("Cancel", key="cancel_btn_2"):

                st.session_state.show_popup = False

                st.session_state.banner = (
                    "Collection canceled."
                )

                st.session_state.banner_type = "warning"

                st.session_state.popup_step = 1

                st.rerun()
                    
# Mission

@st.dialog("Missions")
def show_popup():
    st.write("Submit 25 kg worth of Paper waste")
    st.button("Claim", key="claim1")

    st.write("Submit 25 kg worth of Paper waste")
    st.button("Claim", key="claim2")

    st.write("Submit 25 kg worth of Paper waste")
    st.button("Claim", key="claim3")

if st.button("Missions"):
    show_popup()

# Extra Stuff that isn't related to THIS college project btw.

st.write("[Support Me](https://ko-fi.com/datcoolpro101)")
st.write("[Check My Socials](https://datcoolpro101.carrd.co/)")
st.write("Prototype by JI Calonia - Section A224")
