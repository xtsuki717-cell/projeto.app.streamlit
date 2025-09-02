import streamlit as st


st.set_page_config(page_title="Painel de Estudos", page_icon="", layout="centered")

st.title("📘 Painel de Estudos")
st.write("Registre seu desempenho diário e receba dicas personalizadas para melhorar seus estudos!")


st.subheader(" Registro de Estudo")

horas = st.slider("⏱️ Quantas horas você estudou hoje?", 0, 12, 2)
pausas = st.slider("☕ Quantas pausas você fez?", 0, 20, 3)
atividade = st.selectbox("📖 Qual atividade você realizou?", ["Leitura", "Exercícios", "Revisão"])


st.subheader(" Resumo do seu estudo")
col1, col2, col3 = st.columns(3)
col1.metric("Horas Estudadas", f"{horas}h")
col2.metric("Nº de Pausas", pausas)
col3.metric("Atividade", atividade)


st.subheader("🔎 Avaliação do Estudo")
msg1, msg2, msg3 = st.columns(3)


if horas < 2:
    msg1.warning("⚠️ Poucas horas de estudo. Tente se dedicar mais.")
elif 2 <= horas <= 4:
    msg1.info("✅ Bom esforço! Continue assim.")
else:
    msg1.success("🏆 Excelente! Você estudou bastante hoje.")


if pausas == 0:
    msg2.warning("⚠️ Nenhuma pausa registrada. Pausas ajudam na concentração!")
elif 1 <= pausas <= 5:
    msg2.success("👌 Pausas equilibradas! Bom ritmo de estudo.")
else:
    msg2.info("☕ Muitas pausas podem atrapalhar o rendimento.")


if atividade == "Leitura":
    msg3.info("📖 Leitura é ótima para absorver novos conteúdos.")
elif atividade == "Exercícios":
    msg3.success("✍️ Praticar exercícios ajuda a fixar o aprendizado.")
elif atividade == "Revisão":
    msg3.success("🔁 Revisar garante melhor memorização.")


with st.expander("💡 Dicas de Estudo"):
    st.markdown("""
    - ⏳ Estude em blocos de 50 minutos com pausas de 5 a 10 minutos.  
    - 🔄 Alterne entre **Leitura, Exercícios e Revisão** para melhor aproveitamento.  
    - 😴 Tenha boas noites de sono para consolidar o aprendizado.  
    - 🗓️ Revise os conteúdos no dia seguinte para reforçar a memória.  
    """)


st.markdown("---")
st.markdown("📌 **Painel de Estudos - Criado com Streamlit**")
