import streamlit as st
from streamlit_modal import Modal

from backend.api import APIWrapper
from backend.api.omdb_models import BaseMedium, DetailedMedium
from css_utils import position_modal


class DetailsModalComponent:
    """Frontend component for modal (used for "See more" or "Details")"""

    def __init__(self, medium: BaseMedium) -> None:
        # create the open button and initialize the modal
        open_modal = st.button("See more", key=medium.imdb_id + "details")
        self.medium_modal = Modal(f"{medium.title} ({medium.year})", medium.imdb_id)

        if open_modal:
            self.medium_modal.open()

        if self.medium_modal.is_open():
            # put on css and get detailed data from api
            position_modal()
            api = APIWrapper()
            self.medium_details: DetailedMedium = api.by_id(medium.imdb_id)

            # show the modal popup
            self.render()

    def render(self):
        """Renders the popup"""

        col_data = [
            f"{self.medium_details.title} ({self.medium_details.year})",
            f"Media Type: {self.medium_details.type_.title()}",
            f"Age Rating: {self.medium_details.pg_rating}",
            f"Release Date: {self.medium_details.released}",
            f"Runtime: {self.medium_details.runtime} minutes",
            f"Genre(s): {', '.join(self.medium_details.genre)}",
            f"Awards: {self.medium_details.awards}",
            f"Language(s): {', '.join(self.medium_details.language)}",
            f"Director(s): {', '.join(self.medium_details.director)}",
            f"Writer(s): {', '.join(self.medium_details.writer)}",
            f"Actor(s): {', '.join(self.medium_details.actors)}",
            f"Countries: {', '.join(self.medium_details.country)}",
            f"Metascore: {self.medium_details.metascore}",
            f"IMDb Rating: {self.medium_details.imdb_rating}",
            f"IMDb Votes: {self.medium_details.imdb_votes}",
        ]

        # write data to modal
        with self.medium_modal.container():
            for text in col_data:
                st.write(text)

            st.image(self.medium_details.poster)

            st.markdown("## Plot")
            st.write(self.medium_details.plot)
