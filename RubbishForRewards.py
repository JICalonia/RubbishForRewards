import streamlit as st

# Initialize session state
if "bag_type" not in st.session_state:
    st.session_state.bag_type = None

if "collected_weight" not in st.session_state:
    st.session_state.collected_weight = 0.0

MAX_WEIGHT = 15.00

reward_rates = {
    "Plastic": 5,
    "Paper": 3
}

st.title("♻️ Rubbish-For-Rewards 🪙")

st.markdown("### ---- Trash Bag ----")

# Display current bag data
current_type = st.session_state.bag_type or "None"
current_weight = st.session_state.collected_weight

st.write(f"**Type:** {current_type}")
st.write(f"**Collected Weight:** {current_weight:.2f} kg / {MAX_WEIGHT:.2f} kg")

st.divider()

# Input Controls
selected_type = st.selectbox(
    "Type",
    ["Plastic", "Paper"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=0.0,
    max_value=15.0,
    step=0.01,
    format="%.2f"
)

# Output placeholder
output_box = st.empty()

# Start Collecting Button
if st.button("Start Collecting"):

    if st.session_state.bag_type is not None:
        output_box.error(
            "Please submit the bag before collecting a new type."
        )

    elif weight <= 0 or weight > MAX_WEIGHT:
        output_box.error(
            "Invalid weight. Weight must be greater than 0 and less than or equal to 15.00 kg."
        )

    else:
        st.session_state.bag_type = selected_type
        st.session_state.collected_weight = weight

        output_box.success(
            f"Collection Recorded!\n\nType: {selected_type}\nWeight: {weight:.2f} kg"
        )

# Submit Rewards Button
if st.button("Submit for Rewards"):

    if st.session_state.bag_type is None:
        output_box.error(
            "Nothing in bag yet."
        )

    else:
        reward = (
            st.session_state.collected_weight
            * reward_rates[st.session_state.bag_type]
        )

        output_box.success(
            f"Reward Earned: {reward:.2f} points"
        )

        # Reset Bag
        st.session_state.bag_type = None
        st.session_state.collected_weight = 0.0
