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

# Constants

MAX_WEIGHT = 15.00

TRASH_TYPES = {
    "Plastic": 5,
    "Paper": 3,
    "Cans":, 7,
    "Compost":, 2
}

# Title

st.title("♻️ Rubbish-For-Rewards 🪙")

# Trash Bag Information

st.markdown("### ---- Trash Bag ----")

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

# Input Controls

selected_type = st.selectbox(
    "Type",
    ["Plastic", "Paper"]
)

entered_weight = st.number_input(
    "Weight (kg)",
    min_value=0.00,
    max_value=15.00,
    value=0.00,
    step=0.01,
    format="%.2f"
)

# Start Collecting

if st.button("Start Collecting"):

    if st.session_state.bag_type is not None:
        st.session_state.message = (
            "Please submit the bag before collecting a new type."
        )
        st.session_state.message_type = "error"

    elif entered_weight <= 0:
        st.session_state.message = (
            "Invalid weight. Weight must be greater than 0 and "
            "less than or equal to 15.00 kg."
        )
        st.session_state.message_type = "error"

    else:
        st.session_state.bag_type = selected_type
        st.session_state.collected_weight = entered_weight

        st.session_state.message = (
            f"Collection Recorded!\n\n"
            f"Type: {selected_type}\n"
            f"Weight: {entered_weight:.2f} kg"
        )
        st.session_state.message_type = "success"

        st.rerun()

# Submit For Rewards

if st.button("Submit for Rewards"):

    if st.session_state.collected_weight == 0.0:

        st.session_state.message = (
            "Nothing in bag yet."
        )
        st.session_state.message_type = "error"

    else:

        reward = (
            st.session_state.collected_weight *
            TRASH_TYPES[st.session_state.bag_type]
        )

        st.session_state.message = (
            f"Reward Earned: {reward:.2f} points"
        )
        st.session_state.message_type = "success"

        # Reset immediately
        st.session_state.bag_type = None
        st.session_state.collected_weight = 0.0

        st.rerun()

st.markdown("### Status")

if st.session_state.message:

    if st.session_state.message_type == "success":
        st.success(st.session_state.message)

    elif st.session_state.message_type == "error":
        st.error(st.session_state.message)

st.write("[Support Me](https://ko-fi.com/datcoolpro101)")
st.write("[Check My Socials](https://datcoolpro101.carrd.co/)")
st.write("Prototype by JI Calonia - Section A224")
