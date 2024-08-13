# main.py
# Initialize connection.
def init_connection() -> Session:
    return Session.builder.configs(st.secrets["snowpark"]).create()

if __name__ == "__main__":
    # Initialize the filters
    session = init_connection()
