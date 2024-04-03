import streamlit as st

from backend.bucket_list import BucketList
from components.details_modal import DetailsModalComponent
from components.sort import SortComponent
from css_utils import center_container, invert_toggle
from filters import make_show_filter, make_type_filter
from utils import multisort

bucket_list = BucketList()

with st.container():
    filter_col, sort_col = st.columns(2)

    with filter_col:
        _, show_filter = make_show_filter()
        _, type_filter = make_type_filter()

    with sort_col:
        sort_component = SortComponent(["Title", "Year"])
        sort_component.make()


media = bucket_list.list.values()
filters = [show_filter, type_filter]
filtered_media = filter(lambda medium: all(f(medium) for f in filters), media)
sorted_media = multisort(filtered_media, sort_component.get_sort_specs())

for medium in sorted_media:
    with st.container():
        cols = st.columns(3)

        with cols[0]:
            st.toggle(
                "Seen:",
                value=medium.imdb_id in bucket_list.seen,
                key=medium.imdb_id,
                on_change=bucket_list.update_seen,
                args=(medium.imdb_id,),
            )
            details_modal = DetailsModalComponent(medium)
            st.button(
                "Remove from bucket list",
                key=medium.imdb_id + "-remove",
                on_click=bucket_list.remove_from_list,
                args=(medium.imdb_id,),
            )

        with cols[1]:
            st.write(medium.title)
            st.write(medium.year)

        with cols[2]:
            st.image(medium.poster)


center_container()
invert_toggle()
