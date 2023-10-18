import streamlit as st

st.set_page_config(
  page_title="Jogadores",
  page_icon="⚽",
  layout="wide"
)

if not "data" in st.session_state:
  st.warning('Atualize os dados na página inicial', icon="⚠️")
else:
  df = st.session_state["data"]

  teams = df["Club"].value_counts().index
  team = st.sidebar.selectbox("Clube", teams)

  df_players = df[df["Club"] == team]

  players = df_players["Name"].value_counts().index
  player = st.sidebar.selectbox("Jogador", players)
  player_stats = df_players[df_players["Name"] == player].iloc[0]

  st.image(player_stats["Photo"])
  st.title(f"![{player_stats['Nationality']}]({player_stats['Flag']}) {player_stats['Name']} #{player_stats['Kit Number']:.0f}")
  st.markdown(f"**Clube:** {player_stats['Club']}")
  st.markdown(f"**Posição:** {player_stats['Position']}")

  col1, col2, col3 = st.columns(3)

  col1.markdown(f"**Idade:** {player_stats['Age']:.0f}")
  col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
  col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.1f}")

  st.divider()
  st.subheader(f"Habilidade: {player_stats['Overall']:.0f}")
  st.progress(int(player_stats["Overall"]),f"**Potencial**: {player_stats['Potential']:.0f}")

  col1, col2, col3 = st.columns(3)
  col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value']:.2f}")
  col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage']:.2f}")
  col3.metric(label="Cláusula de recisão", value=f"£ {player_stats['Release Clause']:.2f}")