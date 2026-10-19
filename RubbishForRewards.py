import streamlit as st

# ––––––––––––––––
# SESSION STATE INITIALIZATION
# ––––––––––––––––

# Collection Pop-up
st.session_state.setdefault("active_dialog", None) # Collect Waste
st.session_state.setdefault("popup_step", 1)

# Collection data
st.session_state.setdefault("selected_type", None) # Selected Type
st.session_state.setdefault("weight", 0.0) #Weight

# XP Rewards
st.session_state.setdefault("points", 0) # Rank XP
st.session_state.setdefault("xpbonus", 0) # Bonus XP

# Point Rewards
if "reward_total" not in st.session_state:
    st.session_state.reward_total = 0

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

# Mission Status
if "mission1_status" not in st.session_state:
    st.session_state.mission1_status = 0

if "mission2_status" not in st.session_state:
    st.session_state.mission2_status = 0

if "mission3_status" not in st.session_state:
    st.session_state.mission3_status = 0

# Current XP
if "current_xp" not in st.session_state:
    st.session_state.current_xp = 0

# Constants

MAX_WEIGHT = 15.00

# Reward multipliers

TYPES = {
    "Plastic": 5,
    "Paper": 3,
    "Cans": 7,
    "Compost": 2,
    "Glass": 8
}

# TITLE
# This is where I can type this

st.title("♻️ Rubbish-For-Rewards 🪙")
st.write("BETA 1.3")
st.write(" ")
st.write("Rubbish-For-Rewards is a simulation website designed to teach people about waste management, while also keeping it fun by collecting and submitting trash and obtaining rewards in return.")

st.divider()

# ––––––––––––––––
# XP AND STATUS
# ––––––––––––––––

st.subheader("Your Rank")

# XP Rank
XP_TO_RANK_TWO = 250 # Det. the current rank 

current_xp = st.session_state.points

st.write("**Current Rank:** Beginner")

st.progress(
    min(current_xp / XP_TO_RANK_TWO, 1.0),
    text=f"{current_xp:.0f}/{XP_TO_RANK_TWO} XP to next rank"
)

# Session XP Bonus
SESSION_BONUS = 100

bonus_xp = min(
    st.session_state.xpbonus,
    SESSION_BONUS
)

st.progress(
    bonus_xp / SESSION_BONUS,
    text=f"Session Bonus: {bonus_xp}/{SESSION_BONUS} XP"
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

        # Reward = Type * Weight
        reward = TYPES[st.session_state.selected_type] * st.session_state.weight
        st.session_state.reward_total += reward

        # VOID
        
        st.write(
            f"**Reward:** {reward:.2f} points"
        )

        col1, col2 = st.columns(2)

        # Back Button
        with col1:

            if st.button("Back"):

                st.session_state.popup_step = 1
                st.rerun()

        # Proceed Button
        with col2:

            if st.button("Proceed"):

                if st.session_state.selected_type == "Paper":
                    st.session_state.mission1_status += st.session_state.weight

                elif st.session_state.selected_type == "Plastic":
                    st.session_state.mission2_status += st.session_state.weight

                st.session_state.mission3_status = reward
                
                st.session_state.active_dialog = None

                bonus_earned = reward // 5    # Divides the Reward Earned to 5 and leaving the quotient
                
                remaining_bonus = max(
                    0,
                    SESSION_BONUS - st.session_state.xpbonus
                )

                bonus_to_add = min(
                    bonus_earned,
                    remaining_bonus
                )

                st.session_state.xpbonus += bonus_to_add # Adds XP to Bonus Bar
                st.session_state.points += bonus_to_add # Adds XP to Rank Bar

                st.session_state.banner = (
                    f"Success! Reward Earned: {reward:.2f} points"
                    f" (+{bonus_to_add} Bonus XP)"
                )

                st.session_state.banner_type = "success"
                st.session_state.popup_step = 1
                st.rerun()
                
# ----------------
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

    # ----------------
    # MISSION 1 - Submit 25 kg worth of Paper waste
  
    if "mission1_claimed" not in st.session_state:
        st.session_state.mission1_claimed = False

    mission1_status = st.session_state.mission1_status # Analyzes the Mission Status
    M1_REQ = 25
    mission1_text = "Submit 25 kg worth of Paper waste"

    if st.session_state.mission1_claimed:
        st.write(f"✅ {mission1_text}")
        st.success("Mission reward claimed!")
    else:
        st.write(mission1_text)

    st.progress(
        min(st.session_state.mission1_status / 25, 1.0),
        text=f"{mission1_status:.0f}/{M1_REQ}"
    )
    
    if st.button("Claim", key="claim1"):

        if st.session_state.mission1_claimed:
            st.warning("You already claimed this mission reward!")

        elif st.session_state.mission1_status >= M1_REQ:
            st.success("Mission reward claimed!")
            st.session_state.points += 50
            st.session_state.mission1_claimed = True
            st.rerun()

        else:
            st.error("Mission still incomplete to claim reward.")

    # ----------------
    # MISSION 2 - Submit 20 kg worth of Plastic waste
 
    if "mission2_claimed" not in st.session_state:
        st.session_state.mission2_claimed = False

    mission2_status = st.session_state.mission2_status # Analyzes the Mission Status
    M2_REQ = 20
    mission2_text = "Submit 20 kg worth of Plastic waste"
    
    if st.session_state.mission2_claimed:
        st.write(f"✅ {mission2_text}")
        st.success("Mission reward claimed!")
    else:
        st.write(mission2_text)

    st.progress(
        min(st.session_state.mission2_status / 20, 1.0),
        text=f"{mission2_status:.0f}/{M2_REQ}"
    )
    
    if st.button("Claim", key="claim2"):
    
        if st.session_state.mission2_claimed:
            st.warning("You already claimed this mission reward!")
    
        elif st.session_state.mission2_status >= M2_REQ:
            st.success("Mission reward claimed!")
            st.session_state.points += 50
            st.session_state.mission2_claimed = True
            st.rerun()
    
        else:
            st.error("Mission still incomplete to claim reward.")

    # ----------------
    # MISSION 3 - Collect 150 Points
    
    if "mission3_claimed" not in st.session_state:
        st.session_state.mission3_claimed = False

    mission3_status = st.session_state.mission3_status # Analyzes the Mission Status
    M3_REQ = 200
    mission3_text = "Collect 200 Points"
    
    if st.session_state.mission3_claimed:
        st.write(f"✅ {mission3_text}")
        st.success("Mission reward claimed!")
    else:
        st.write(mission3_text)

    st.progress(
        min(st.session_state.mission3_status / 200, 1.0),
        text=f"{mission3_status:.0f}/{M3_REQ}"
    )
    
    if st.button("Claim", key="claim3"):
    
        if st.session_state.mission3_claimed:
            st.warning("You already claimed this mission reward!")
    
        elif st.session_state.mission3_status >= M3_REQ:
            st.success("Mission reward claimed!")
            st.session_state.points += 50
            st.session_state.mission3_claimed = True
            st.rerun()
    
        else:
            st.error("Mission still incomplete to claim reward.")
            
# ––––––––––––––––
# Extra Stuff that isn't related to THIS college project btw.
# ––––––––––––––––

st.divider()

st.write("[Support Me](https://ko-fi.com/datcoolpro101)")
st.write("[Check My Socials](https://datcoolpro101.carrd.co/)")
st.write("Prototype by JI Calonia - Section A224")
