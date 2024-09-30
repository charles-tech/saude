import streamlit as st

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_tmb(sexo, peso, altura, idade):
    if sexo == 'Masculino':
        return 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * idade)
    else:
        return 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * idade)

def calcular_macros(tmb_ajustada):
    # Proporções de macronutrientes
    proporcoes = {
        "carboidratos": 0.55,  # 55% das calorias
        "proteinas": 0.20,     # 20% das calorias
        "gorduras": 0.25       # 25% das calorias
    }

    # Calorias de cada macronutriente
    calorias_carboidratos = tmb_ajustada * proporcoes["carboidratos"]
    calorias_proteinas = tmb_ajustada * proporcoes["proteinas"]
    calorias_gorduras = tmb_ajustada * proporcoes["gorduras"]

    # Convertendo calorias em gramas
    gramas_carboidratos = calorias_carboidratos / 4
    gramas_proteinas = calorias_proteinas / 4
    gramas_gorduras = calorias_gorduras / 9

    return gramas_carboidratos, gramas_proteinas, gramas_gorduras

def main():
    st.title("Calculadora de IMC, TMB e Macronutrientes")

    st.header("Dados Pessoais")
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
    peso = st.number_input("Peso (kg)", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (m)", min_value=0.0, format="%.2f")
    idade = st.number_input("Idade", min_value=0)

    st.header("Nível de Atividade Física")
    atividade = st.selectbox("Frequência de Exercícios", [
        "Sedentário (pouco ou nenhum exercício)",
        "Levemente ativo (exercício leve 1-3 dias/semana)",
        "Moderadamente ativo (exercício moderado 3-5 dias/semana)",
        "Altamente ativo (exercício pesado 6-7 dias/semana)",
        "Extremamente ativo (exercício muito pesado/trabalho físico)"
    ])

    fatores_atividade = {
        "Sedentário (pouco ou nenhum exercício)": 1.2,
        "Levemente ativo (exercício leve 1-3 dias/semana)": 1.375,
        "Moderadamente ativo (exercício moderado 3-5 dias/semana)": 1.55,
        "Altamente ativo (exercício pesado 6-7 dias/semana)": 1.725,
        "Extremamente ativo (exercício muito pesado/trabalho físico)": 1.9
    }

    if st.button("Calcular"):
        imc = calcular_imc(peso, altura)
        tmb = calcular_tmb(sexo, peso, altura, idade)
        tmb_ajustada = tmb * fatores_atividade[atividade]

        gramas_carboidratos, gramas_proteinas, gramas_gorduras = calcular_macros(tmb_ajustada)

        st.success(f"Seu IMC é: {imc:.2f}")
        st.success(f"Sua TMB é: {tmb:.2f} calorias/dia")
        st.success(f"Sua TMB ajustada para o nível de atividade é: {tmb_ajustada:.2f} calorias/dia")
        
        st.header("Sugestão de Consumo de Macronutrientes")
        st.info(f"Carboidratos: {gramas_carboidratos:.2f} g")
        st.info(f"Proteínas: {gramas_proteinas:.2f} g")
        st.info(f"Gorduras: {gramas_gorduras:.2f} g")

if __name__ == "__main__":
    main()