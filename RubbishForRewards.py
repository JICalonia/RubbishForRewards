import streamlit as st

# ––––––––––––––––
# SESSION STATE INITIALIZATION
# ––––––––––––––––

# Collection Pop-up
st.session_state.setdefault("active_dialog", None)
st.session_state.setdefault("popup_step", 1)

# Collection data
st.session_state.setdefault("selected_type", None)
st.session_state.setdefault("weight", 0.0)

# Rewards
st.session_state.setdefault("points", 0)

# Banners
st.session_state.setdefault("banner", "")
st.session_state.setdefault("banner_type", "")

# Missions
if "mission1_claimed" not in st.session_state:
    st.session_state.mission1_claimed = False

if "mission2_claimed" not in st.session_state:
    st.session_state.mission2_claimed = False

if "mission3_claimed" not in st.session_state:
    st.session_state.mission3_claimed = False

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

st.divider()

# XP AND STATUS

st.subheader("XP & Status")

XP_TO_NEXT_RANK = 250

current_xp = st.session_state.points

st.write("**Current Rank:** Beginner")

st.progress(
    min(current_xp / XP_TO_NEXT_RANK, 1.0),
    text=f"{current_xp:.0f}/{XP_TO_NEXT_RANK} XP to next rank"
)

# ––––––––––––––––
# COLLECTION
# ––––––––––––––––

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
            max_value=MAX_WEIGHT,
            step=0.01
        )

        if st.button("Next"):

                if selected_type is None:
                    st.error("Select a type first.")
                    st.stop()

                if weight <= 0:
                    st.error("Enter a valid weight.")
                    st.stop()

                if weight > MAX_WEIGHT:
                    st.error(f"Weight cannot exceed {MAX_WEIGHT:.2f} kg.")
                    st.stop()

                st.session_state.selected_type = selected_type
                st.session_state.weight = weight

                st.session_state.popup_step = 2

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

                st.session_state.active_dialog = False

                st.session_state.banner = (
                    f"Success! Reward Earned: "
                    f"{reward:.2f} points"
                )

                st.session_state.banner_type = "success"
                st.session_state.popup_step = 1
                st.rerun()
                
# COLLECT BUTTON 

if st.button("Collect Waste"):
    st.session_state.active_dialog = "collect"
    st.session_state.popup_step = 1

if st.session_state.active_dialog == "collect":
    collection_popup()

# Banner

if st.session_state.banner:

    if st.session_state.banner_type == "success":
        st.success(st.session_state.banner)

    elif st.session_state.banner_type == "warning":
        st.warning(st.session_state.banner)

st.divider()

# ––––––––––––––––
# MISSIONS
# ––––––––––––––––
         
with st.expander("Missions"):

    st.write("**50 XP per Mission reward claimed**")

    # MISSION 1
    mission1_text = "Submit 25 kg worth of Paper waste"

    if st.session_state.mission1_claimed:
        st.write(f"✅ {mission1_text}")
    else:
        st.write(mission1_text)
    
    if st.button("Claim", key="claim1"):
    
        if not st.session_state.mission1_claimed:

            st.session_state.current_xp += 50
            st.session_state.mission1_claimed = True

            st.success("Mission reward claimed!")

        else:
            st.warning("You already claimed this mission reward!")

    # MISSION 2
    mission2_text = "Submit 20 kg worth of Plastic waste"

    if st.session_state.mission2_claimed:
        st.write(f"✅ {mission2_text}")
    else:
        st.write(mission2_text)
    
    if st.button("Claim", key="claim2"):
    
        if not st.session_state.mission2_claimed:

            st.session_state.current_xp += 50
            st.session_state.mission2_claimed = True

            st.success("Mission reward claimed!")

        else:
            st.warning("You already claimed this mission reward!")

    # MISSION 3
    mission3_text = "Collect 150 Points"

    if st.session_state.mission3_claimed:
        st.write(f"✅ {mission3_text}")
    else:
        st.write(mission3_text)
    
    if st.button("Claim", key="claim3"):
    
        if not st.session_state.mission3_claimed:

            st.session_state.current_xp += 50
            st.session_state.mission3_claimed = True

            st.success("Mission reward claimed!")

        else:
            st.warning("You already claimed this mission reward!")

# Extra Stuff that isn't related to THIS college project btw.

st.divider()

st.write("[Support Me](https://ko-fi.com/datcoolpro101)")
st.write("[Check My Socials](https://datcoolpro101.carrd.co/)")
st.write("Prototype by JI Calonia - Section A224")
