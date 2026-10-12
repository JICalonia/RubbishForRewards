import streamlit as st

# Session State Initialization

if "bag_type" not in st.session_state:
    st.session_state.bag_type = None

if "collected_weight" not in st.session_state:
    st.session_state.collected_weight = 0.0

if "message" not in st.session_state:
    st.session_state.message = ""

if "message_type" not in st.session_state:
    st.session_state.message_type = ""

if "step" not in st.session_state:
    st.session_state.step = 1

if "reward_message" not in st.session_state:
    st.session_state.reward_message = None

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

# Trash Bag Information

display_type = (
    st.session_state.bag_type
    if st.session_state.bag_type is not None
    else "None"
)

st.write(f"**Type:** {display_type}")

if st.session_state.collected_weight == 0.0:
    st.error("Nothing in bag yet.")
else:
    st.write(
        f"**Collected Weight:** "
        f"{st.session_state.collected_weight:.2f} kg / {MAX_WEIGHT:.2f} kg"
    )

st.divider()

# Collection

if st.button("Collect Waste"):
    st.session_state.step = 1
    collection_popup()

    @st.dialog("Collect Waste")
    def collection_popup():

        # STEP 1
        if st.session_state.step == 1:

            waste_type = st.selectbox(
                "Type",
                options=list(TYPES.keys()),
                index=None,
                placeholder="Select..."
            )

            weight = st.number_input(
                "Weight (kg)",
                min_value=0.0,
                step=0.1
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Next"):

                    if waste_type is None:
                        st.error("Select a type first.")
                        return

                    if weight <= 0:
                        st.error("Enter a valid weight.")
                        return

                    st.session_state.type = waste_type
                    st.session_state.weight = weight
                    st.session_state.step = 2

                    st.rerun()

            with col2:
                if st.button("Cancel"):
                    st.session_state.reward_message = (
                        "Collection canceled."
                    )
                    st.rerun()

        # STEP 2
        elif st.session_state.step == 2:

            st.subheader("Review Submission")

            st.write(
                f"Type: {st.session_state.type}"
            )

            st.write(
                f"Weight: {st.session_state.weight} kg"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Proceed"):

                    reward = (
                        TYPES[st.session_state.type]
                        * st.session_state.weight
                    )

                    st.session_state.reward_message = (
                        f"✅ Success! Reward Earned: "
                        f"{reward:.2f} points"
                    )

                    st.session_state.step = 1

                    st.rerun()

            with col2:
                if st.button("Cancel"):

                    st.session_state.reward_message = (
                        "Collection canceled."
                    )

                    st.session_state.step = 1

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

# Status

st.markdown("### Status")

if st.session_state.message:

    if st.session_state.message_type == "success":
        st.success(st.session_state.message)

    elif st.session_state.message_type == "error":
        st.error(st.session_state.message)

# Extra Stuff that isn't related to THIS college project btw.

st.write("[Support Me](https://ko-fi.com/datcoolpro101)")
st.write("[Check My Socials](https://datcoolpro101.carrd.co/)")
st.write("Prototype by JI Calonia - Section A224")
