import streamlit as st
from supabase import create_client

# CONFIGURAÇÕES DE CONEXÃO (VALIDADAS)
URL = "https://msnebpttipxfuvvvrje.supabase.co"
KEY = "sb_publishable_QDofFDpqfH2dJcGVFSoUSg_BI_ht-U-"
supabase = create_client(URL, KEY)

# INTERFACE VISUAL
st.set_page_config(page_title="Sistema Devasta AI", layout="wide")
st.title("🚀 Sistema Devasta - Dashboard de Elite")
st.sidebar.info(f"Usuário: André Nunes")

# BUSCANDO DADOS DO BANCO
try:
    payout = supabase.table("configuracoes_payout").select("*").execute()
    logs = supabase.table("logs_agentes").select("*").order("timestamp", desc=True).limit(5).execute()
    
    # LINHA 1: INFORMAÇÕES BANCÁRIAS E STATUS
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Status do Sistema", "ONLINE", delta="Pronto para Escala")
    with col2:
        st.metric("Titular do Payout", payout.data[0]['titular'])
    with col3:
        st.metric("Banco Destino", payout.data[0]['banco'])

    st.divider()

    # LINHA 2: MONITORAMENTO DOS ROBÔS
    st.subheader("🕵️‍♂️ Atividade Recente dos Agentes (Logs)")
    if logs.data:
        for log in logs.data:
            st.write(f"🕒 {log['timestamp']} | **{log['agente']}**: {log['acao_executada']}")
    else:
        st.warning("Nenhum log encontrado. Dispare o primeiro robô abaixo.")

    # BOTÃO DE COMANDO
    if st.button("🔥 DISPARAR AGENTE SNIPER AGORA"):
        supabase.table("logs_agentes").insert({
            "agente": "Sniper", 
            "acao_executada": "Varredura Global iniciada via Dashboard"
        }).execute()
        st.success("Comando enviado com sucesso para a rede de robôs!")
        st.rerun()

except Exception as e:
    st.error(f"Erro ao conectar com o Supabase: {e}")
