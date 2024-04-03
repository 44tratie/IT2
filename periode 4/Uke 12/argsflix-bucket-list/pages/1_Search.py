import streamlit as st

from backend.api import APIWrapper
from backend.bucket_list import BucketList
from components.details_modal import DetailsModalComponent
from css_utils import center_container

api = APIWrapper()
bucket_list = BucketList()

search_term = st.text_input("Search query:")

media = api.query_movie(search_term)

for medium in media:
    with st.container():
        cols = st.columns(2)

        with cols[0]:
            st.write(medium.title)
            st.write(medium.year)

            details_modal = DetailsModalComponent(medium)

            if medium.imdb_id in bucket_list.list:
                st.button(
                    "Remove from bucket list",
                    key=medium.imdb_id,
                    on_click=bucket_list.remove_from_list,
                    args=(medium.imdb_id,),
                )
            else:
                st.button(
                    "Add to bucket list",
                    key=medium.imdb_id,
                    on_click=bucket_list.add_to_list,
                    args=(medium,),
                )

        with cols[1]:
            st.image(medium.poster)

center_container()
