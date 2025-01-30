import streamlit as st

# Placeholder for storing votes, admin credentials, and user accounts
if 'votes' not in st.session_state:
    st.session_state['votes'] = {'Rakesh': 0, 'Vikram': 0, 'Naveen': 0, 'Rohith': 0, 'Bharani': 0}

if 'admin_credentials' not in st.session_state:
    st.session_state['admin_credentials'] = {'admin': 'password123'}

if 'user_accounts' not in st.session_state:
    st.session_state['user_accounts'] = {'user1': 'pass1', 'user2': 'pass2'}

if 'voted_users' not in st.session_state:
    st.session_state['voted_users'] = set()

# Function to display admin page
def admin_page():
    st.title("Admin Dashboard")

    # Display vote count
    st.subheader("Vote Counts")
    for candidate, count in st.session_state['votes'].items():
        st.write(f"{candidate}: {count} votes")

    # Determine the leading candidate
    max_votes = max(st.session_state['votes'].values(), default=0)
    leading_candidates = [candidate for candidate, votes in st.session_state['votes'].items() if votes == max_votes]

    st.subheader("Leading Candidate")
    if max_votes == 0:
        st.write("No votes have been cast yet.")
    elif len(leading_candidates) == 1:
        st.write(f"Currently leading: **{leading_candidates[0]}** with {max_votes} votes.")
    else:
        st.write(f"Tie between: **{', '.join(leading_candidates)}** with {max_votes} votes.")

    # Option to reset votes
    if st.button("Reset Votes"):
        for candidate in st.session_state['votes']:
            st.session_state['votes'][candidate] = 0
        st.session_state['voted_users'].clear()
        st.success("Votes have been reset.")

# Function to display voting page
def voting_page():
    st.title("Voting Application")
    
    st.subheader("Class Representative Election")
    
    st.subheader("User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in st.session_state['user_accounts'] and st.session_state['user_accounts'][username] == password:
            if username in st.session_state['voted_users']:
                st.warning("You have already voted. Voting again is not allowed.")
            else:
                st.session_state['logged_in_user'] = username
                st.success("Login successful! You can now vote.")
        else:
            st.error("Invalid credentials. Please try again.")

    if 'logged_in_user' in st.session_state:
        candidates = list(st.session_state['votes'].keys())
        choice = st.radio("Choose your candidate:", candidates)
        
        if st.button("Vote"):
            if st.session_state['logged_in_user'] in st.session_state['voted_users']:
                st.warning("You have already voted.")
            else:
                st.session_state['votes'][choice] += 1
                st.session_state['voted_users'].add(st.session_state['logged_in_user'])
                st.success(f"Your vote for {choice} has been recorded. Thank you!")
                del st.session_state['logged_in_user']  # Logout user after voting

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
