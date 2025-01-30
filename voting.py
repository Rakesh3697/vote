import streamlit as st
import pandas as pd

# Placeholder for storing votes and admin credentials
if 'votes' not in st.session_state:
    st.session_state['votes'] = {'Candidate A': 0, 'Candidate B': 0, 'Candidate C': 0}

if 'admin_credentials' not in st.session_state:
    st.session_state['admin_credentials'] = {'admin': 'password123'}

# Function to display admin page
def admin_page():
    st.title("Admin Dashboard")

    # Display vote count
    st.subheader("Vote Counts")
    for candidate, count in st.session_state['votes'].items():
        st.write(f"{candidate}: {count} votes")

    # Option to reset votes
    if st.button("Reset Votes"):
        for candidate in st.session_state['votes']:
            st.session_state['votes'][candidate] = 0
        st.success("Votes have been reset.")

# Function to display voting page
def voting_page():
    st.title("Voting Application")

    # List candidates
    candidates = list(st.session_state['votes'].keys())
    choice = st.radio("Choose your candidate:", candidates)

    if st.button("Vote"):
        st.session_state['votes'][choice] += 1
        st.success(f"Your vote for {choice} has been recorded. Thank you!")

# Main app
def main():
    st.sidebar.title("Navigation")
    menu = ["Vote", "Admin"]
    choice = st.sidebar.radio("Go to:", menu)

    if choice == "Admin":
        st.sidebar.subheader("Admin Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if (username in st.session_state['admin_credentials'] and 
                st.session_state['admin_credentials'][username] == password):
                st.success("Login successful!")
                admin_page()
            else:
                st.error("Invalid credentials. Please try again.")
    else:
        voting_page()

if __name__ == "__main__":
    main()
