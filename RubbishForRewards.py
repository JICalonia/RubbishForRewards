import streamlit as st

# SESSION STATE

st.session_state.setdefault("show_popup", False)
st.session_state.setdefault("popup_step", 1)

# Collection data
st.session_state.setdefault("selected_type", None)
st.session_state.setdefault("weight", 0.0)

# Rewards
st.session_state.setdefault("points", 0)

# Banners
st.session_state.setdefault("banner", "")
st.session_state.setdefault("banner_type", "")

# Constants

MAX_WEIGHT = 15.00

# Reward multipliers

TYPES = {
    "Plastic": 5,
    "Paper": 3,
    "Cans": 7,
    "Compost": 2
}

# TITLE
# This is where I can type this

st.title("♻️ Rubbish-For-Rewards 🪙")
st.write("BETA 1.2")
st.write(" ")
st.write("Rubbish-For-Rewards is a simulation website designed to teach people about waste management, while also keeping it fun by collecting and submitting trash and obtaining rewards in return.")

# Collection

@st.dialog("Collect Waste")
def collection_popup():

    # STEP 1
    if st.session_state.popup_step == 1:

        st.write("Enter collection details.")

        selected_type = st.selectbox(
            "Type",
            options=list(TYPES.keys()),
            index=None,
            placeholder="Select..."
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=0.0,
            step=0.01
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Next"):

                if selected_type is None:
                    st.error("Select a type first.")
                    st.stop()

                if weight <= 0:
                    st.error("Enter a valid weight.")
                    st.stop()

                st.session_state.selected_type = selected_type
                st.session_state.weight = weight

                st.session_state.popup_step = 2

                st.rerun()

        with col2:

            if st.button("Cancel"):

                st.session_state.show_popup = False

                st.session_state.banner = "Collection canceled."
                st.session_state.banner_type = "warning"

                st.session_state.popup_step = 1

                st.rerun()

    # STEP 2
    elif st.session_state.popup_step == 2:

        st.subheader("Review")

        st.write(
            f"**Type:** {st.session_state.selected_type}"
        )

        st.write(
            f"**Weight:** {st.session_state.weight:.2f} kg"
        )

        reward = (
            TYPES[
                st.session_state.selected_type
            ]
            * st.session_state.weight
        )

        st.write(
            f"**Reward:** {reward:.2f} points"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Back"):

                st.session_state.popup_step = 1
                st.rerun()

        with col2:

            if st.button("Proceed"):

                st.session_state.show_popup = False

                st.session_state.banner = (
                    f"Success! Reward Earned: "
                    f"{reward:.2f} points"
                )

                st.session_state.banner_type = "success"

                st.session_state.popup_step = 1

                st.rerun()
                
# BUTTON

if st.button("Collect Waste"):

    st.session_state.show_popup = True
    st.session_state.popup_step = 1

# Show dialog
if st.session_state.show_popup:
    collection_popup()

# Banner

if st.session_state.banner:

    if st.session_state.banner_type == "success":
        st.success(st.session_state.banner)

    elif st.session_state.banner_type == "warning":
        st.warning(st.session_state.banner)
                    
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
