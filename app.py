
    import os
    import streamlit as st
    import pandas as pd
    from pandasai import SmartDataframe
    from pandasai.llm import OpenAI

    st.set_page_config(page_title="Suffolk Backyard Ultra – Q&A", layout="wide")

    # ---- API key ----
    openai_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
    if not openai_key:
        st.error(
            "Add your OpenAI key:
"
            "• set an environment variable OPENAI_API_KEY
"
            "  OR
"
            "• create `.streamlit/secrets.toml` with `OPENAI_API_KEY="sk-..."`"
        )
        st.stop()

    # ---- Load & tidy data ----
    @st.cache_data(show_spinner=False)
    def load_data():
        df = pd.read_csv("ANALYST - CLEAN.csv")
        df['NAME_CLEAN'] = df['NAME'].str.strip().str.casefold()
        df['LAPS_COMPLETED'] = pd.to_numeric(df['LAPS COMPLETED'], errors='coerce')
        df['IS_WINNER'] = df['POSITION'].eq('Winner')
        return df

    DF = load_data()

    # ---- LLM wrapper ----
    llm = OpenAI(model_name="gpt-4o-mini-2025-04", api_key=openai_key, temperature=0)
    sdf = SmartDataframe(DF, config={"llm": llm, "verbose": False})

    # ---- UI ----
    st.title("🏃 Suffolk Backyard Ultra – Ask Anything")

    query = st.text_input(
        "Ask a question about the results:",
        placeholder="Who won 2021 and how many laps?"
    )

    if st.button("Submit") and query:
        with st.spinner("Thinking..."):
            try:
                answer = sdf.chat(query)
                st.success(answer)
            except Exception as e:
                st.error(str(e))
