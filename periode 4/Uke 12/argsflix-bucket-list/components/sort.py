import streamlit as st


class SortComponent:
    """Frontend component for sorting"""

    def __init__(self, options: list[str]) -> None:
        # options are options to sort by
        self.options = options

    def make(self) -> None:
        """Renders the component"""

        self.choices = [""]  # placeholder for -1 indexing
        self.reverses = []  # whether the sorting should be reversed or not

        # generates boxes in order to multisort
        for i in range(len(self.options)):
            # 80% 20% space
            sort_by_col, reverse_sort_col = st.columns((0.8, 0.2))

            with sort_by_col:
                # add a box with options that has not already been selected
                selected = set(filter(lambda choice: choice is not None, self.choices))
                self.choices.append(
                    st.selectbox(
                        f"Sort by ({i + 1}):",
                        [option for option in self.options if option not in selected],
                        index=None,
                        disabled=self.choices[-1] is None,
                    )
                )

            with reverse_sort_col:
                # add a box that marks the sort_i as reverse
                st.markdown("Reverse")
                self.reverses.append(
                    st.checkbox(f"Reverse {i + 1}", label_visibility="collapsed")
                )

    def get_sort_specs(self) -> list[tuple[str, bool]]:
        """Gets sort specs from the sort component that is compliant with multisort"""

        try:
            return list(
                map(
                    lambda sort_spec: (sort_spec[0].lower(), sort_spec[1]),
                    filter(
                        lambda sort_spec: sort_spec[0] is not None,
                        zip(self.choices[1:], self.reverses),
                    ),
                )
            )
        except:
            return []
