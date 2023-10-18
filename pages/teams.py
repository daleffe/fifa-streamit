import streamlit as st

st.set_page_config(
  page_title="Times",
  page_icon="⚽",
  layout="wide"
)

if not "data" in st.session_state:
  st.warning('Atualize os dados na página inicial', icon="⚠️")
else:
  df = st.session_state["data"]

  teams = df["Club"].value_counts().index
  team = st.sidebar.selectbox("Clube", teams)

  df_players = df[df["Club"] == team].set_index("Name")

  st.image(df_players.iloc[0]["Club Logo"])
  st.markdown(f"## {team}")

  columns = ["Photo","Age","Flag","Overall","Value","Wage","Joined","Height(cm.)","Weight(lbs.)","Contract Valid Until","Release Clause"]

  st.dataframe(df_players[columns],column_config={
    "Overall": st.column_config.ProgressColumn("Habilidade",help="Capacidade técnica",format="%d", min_value=0, max_value=100),
    "Value": st.column_config.NumberColumn("Valor de mercado",format="£ %.2f"),
    "Wage": st.column_config.ProgressColumn("Remuneração",help="Remuneração semanal",format="£ %.2f", min_value=0, max_value=df_players["Wage"].max()),
    "Photo": st.column_config.ImageColumn("Foto"),
    "Flag": st.column_config.ImageColumn("Nacionalidade"),
    "Height": st.column_config.NumberColumn("Altura")
  },height=512)