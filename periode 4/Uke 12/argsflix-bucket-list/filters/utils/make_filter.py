from typing import Callable

import streamlit as st

from backend.api.omdb_models import BaseMedium


def make_filter(
    label: str,
    options: list[str],
    filter_option: Callable[[str], Callable[[BaseMedium], bool]],
) -> tuple[str, Callable[[BaseMedium], bool]]:
    option = st.selectbox(label, options)
    return option, filter_option(option)
