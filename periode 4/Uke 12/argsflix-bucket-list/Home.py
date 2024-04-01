import streamlit as st
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    st.write("ArgsFlix Bucket List App")


if __name__ == "__main__":
    main()
