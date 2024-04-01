import streamlit as st


def center_container() -> None:
    st.write(
        """<style>
        [data-testid="stHorizontalBlock"] {
            align-items: center;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def invert_toggle() -> None:
    st.write(
        """<style>
        [data-testid="stCheckbox"]>label {
            flex-direction: row-reverse;
            justify-content: center;
            gap: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
