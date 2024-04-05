import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Display an image and set the title of the app
img1 = 'https://www.cnj.jus.br/wp-content/uploads/2020/07/fachada-tjes_787.jpg'
st.image(img1, width=600)

st.title("TJES - Núcleo de Gestão da Qualidade")
st.header("LI2 - Lab de Inovação e IA")
st.subheader("Por: Samuel Brasil")
st.write("Pontuação máxima: Governança = 680, Produtividade = 715, Transparência = 120, Dados e TI = 651")
st.divider()

def initialize_state():
    # Initialize or reset the session state variables
    if 'sections' not in st.session_state:
        st.session_state.sections = {}
    else:
        st.session_state.sections.clear()

    if 'options_values' not in st.session_state:
        st.session_state.options_values = {}
    else:
        st.session_state.options_values.clear()

    if 'uploaded_selections_set' not in st.session_state:
        st.session_state.uploaded_selections_set = set()
    else:
        st.session_state.uploaded_selections_set.clear()

def streamlit_app():
    # Initialize session state variables
    initialize_state()

    # File uploader widget for the structure
    structure_file = st.file_uploader("Por favor, carregue o arquivo 'structure.csv', com os parâmetros da pontuação", type=['csv'], key="structure_uploader")

    if structure_file is not None:
        df_structure = pd.read_csv(structure_file)

        for index, row in df_structure.iterrows():
            section = row['Category']
            option = row['Option']
            value = row['Value']

            if section not in st.session_state.sections:
                st.session_state.sections[section] = []
                st.session_state.options_values[section] = []

            st.session_state.sections[section].append(option)
            st.session_state.options_values[section].append(value)

        # File uploader widget for selections
        selections_file = st.file_uploader("Carregue o arquivo 'selections.csv', com a última versão salva - É NECESSÁRIO CARREGAR A ESTRUTURA ANTES", type=['csv'], key="selections_uploader")
        if selections_file is not None:
            df_uploaded = pd.read_csv(selections_file)
            # Create a set of selections for easy lookup
            st.session_state.uploaded_selections_set = set([f"{row['Category']}_{row['Option']}" for index, row in df_uploaded.iterrows()])

        colors = ['blue', 'green', 'orange', 'red']
        total_scores = {section: 0 for section in st.session_state.sections}
        selections = []

        # Create checkboxes for each section and option
        for section, options in st.session_state.sections.items():
            st.subheader(section)
            for option, value in zip(options, st.session_state.options_values[section]):
                checkbox_id = f'{section}_{option}'
                # Determine if the checkbox should be pre-checked
                is_checked = checkbox_id in st.session_state.uploaded_selections_set
                if st.checkbox(f'{option} - {value}', key=checkbox_id, value=is_checked):
                    total_scores[section] += value
                    selections.append([section, option, value])

        # Plotting and saving logic remains unchanged

        # Remaining plotting and saving logic remains unchanged
        # Plotting the bar chart with the scores
        fig, ax = plt.subplots()
        categories = list(total_scores.keys())
        scores = list(total_scores.values())
        ax.bar(categories, scores, color=colors)
        ax.set_xlabel('Categorias')
        ax.set_ylabel('Pontuação')
        ax.set_title('Prêmio CNJ de Qualidade')

        # Adding the scores to the bar chart
        for i, score in enumerate(scores):
            ax.text(i, score + 1, str(score), ha='center', va='bottom')

        # Display the bar chart
        st.pyplot(fig)

        # If the save button is pressed, save selections to CSV
        if st.button('Save Selections to CSV'):
            df = pd.DataFrame(selections, columns=['Category', 'Option', 'Value'])
            df.to_csv('selections.csv', index=False)
            st.success('Selections saved to CSV!')

        # Provide a download link for the CSV file
        if selections:
            df = pd.DataFrame(selections, columns=['Category', 'Option', 'Value'])
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download selections as CSV",
                data=csv,
                file_name='selections.csv',
                mime='text/csv',
            )


# Run the Streamlit app
streamlit_app()
