import pandas as pd
import streamlit as st

def show_ranking(results):

    if len(results) == 0:
        return

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="Score",
        ascending=False
    )

    st.subheader("🏆 Candidate Ranking")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="candidate_ranking.csv",
        mime="text/csv"
    )