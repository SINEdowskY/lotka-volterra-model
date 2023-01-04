import streamlit as st
import streamlit.components.v1 as components
import volterra


st.title("Model Lotki-Volterry")
st.sidebar.header('Variables')
initial_preys = st.sidebar.slider("Wstępna ilosc ofiar", value = 5, min_value=1, max_value=10)
initial_predators = st.sidebar.slider("Wstępna ilosc drapieżników", value=10, min_value=1, max_value=10)
a = st.sidebar.slider("a - częstość narodzin ofiar", value=1.1, min_value=0.0, max_value=5.0, step=0.1)
b = st.sidebar.slider("b - częstość umierania ofiar", value=0.4, min_value=0.0, max_value=5.0, step=0.1)
c = st.sidebar.slider("c - częstość narodzin drapieżników", value=1.1, min_value=0.0, max_value=5.0, step=0.1)
d = st.sidebar.slider("d - częstość umierania drapieżników", value=0.4, min_value=0.0, max_value=5.0, step=0.1)

model = volterra.diffrential_equations(a,b,c,d, initial_preys, initial_predators)

st.pyplot(volterra.preys_vs_predators_plot(model=model))

is_disabled = True
st.sidebar.header('Animations')
if st.sidebar.button("Generate"):
    volterra.animated_plot(model)
    volterra.animated_phase(model)
    is_disabled = False

if st.sidebar.button("Play", disabled=is_disabled):
    st.image(["./plots/plotanimation.gif","./plots/phaseanimation.gif"])

