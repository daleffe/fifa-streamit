import webbrowser
import streamlit as st
import pandas as pd

from datetime import datetime

pages = st.source_util.get_pages('home.py')

new_page_names = {
   'home': 'Início',
   'players': 'Jogadores',
   'teams': 'Times',
}

for key, page in pages.items():
   if page['page_name'] in new_page_names:
      page['page_name'] = new_page_names[page['page_name']]

st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>""", unsafe_allow_html=True)

if "data" not in st.session_state:
  ds = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col = 0)

  ds = ds[ds["Contract Valid Until"] >= datetime.today().year]
  ds = ds[ds["Value"] > 0]
  ds = ds.sort_values(by="Overall", ascending=False)

  st.session_state["data"] = ds

st.write("# FIFA 2023")
st.sidebar.write("Vigisoft")

btn = st.button("Acesse os dados de exemplo")

if btn:
    webbrowser.open_newtab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/")
    st.button(btn)

st.markdown("O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contratos e afiliações de clubes. Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados ​​em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.")
