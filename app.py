import streamlit as st
from supabase import create_client

# O sistema busca as credenciais no "Cofre" (Secrets) que você configurou no Streamlit
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_SERVICE_KEY"]

st.set_page_config(page_title="Sistema Devasta AI", layout="wide", page_icon="🚀")

@st.cache_resource
def iniciar_conexao():
    # Conexão direta via Service Role (Bypass de rede)
    return create_client(URL, KEY)

st.title("🚀 Sistema Devasta - QG de Inteligência")

try:
    supabase = iniciar_conexao()
    # Puxa os dados do banco para validar o seu acesso
    res = supabase.table("configuracoes_payout").select("*").execute()
    
    if res.data:
        st.balloons()
        st.success(f"✅ ACESSO TOTAL LIBERADO: BEM-VINDO, {res.data[0]['titular'].upper()}!")
        
        # Painel de Controle
        col1, col2, col3 = st.columns(3)
        col1.metric("Status", "ONLINE", delta="100%")
        col2.metric("Banco de Destino", res.data[0]['banco'])
        col3.metric("Agência", res.data[0]['agencia'])
        
        st.divider()
        st.subheader("🕵️‍♂️ Missão Sniper")
        if st.button("🔥 DISPARAR AGENTE AGORA"):
            # Registra o disparo no banco de dados
            supabase.table("logs_agentes").insert({"agente": "Sniper", "acao_executada": "Ataque Total Iniciado"}).execute()
            st.snow()
            st.info("O Sniper está rastreando os produtos mais vendidos por região...")
    else:
        st.warning("Conectado, mas aguardando sincronização de dados do titular.")

except Exception as e:
    st.error("🛰️ Sintonizando sinal com o banco de dados...")
    st.info("André, se esta mensagem persistir, clique no botão de 'Reboot' no painel do Streamlit.")
    if st.button("🔄 RECONECTAR AGORA"):
        st.cache_resource.clear()
        st.rerun()
