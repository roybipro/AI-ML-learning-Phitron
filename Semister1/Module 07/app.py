import streamlit as st


st.title("Note summary and Quiz Generator")
st.markdown("upload upto 3 images to generate note summary and quiz questions")

st.divider()


#sidebar

with st.sidebar:
    st.header("Upload your notes")
    uploaded_images = st.file_uploader("Choose images",
                                      accept_multiple_files=True,
                                      type=["jpg", "jpeg", "png"]
                                      )
    if uploaded_images:
        if len(uploaded_images) > 3:
            st.error("Please upload a maximum of 3 images.")
        else:
            column = st.columns(len(uploaded_images))
            
            for i , image in enumerate(uploaded_images):
                with column[i]:
                    st.image(image, caption=image.name, width="stretch")
                    
            st.success(f"{len(uploaded_images)} file(s) uploaded successfully!")
            

    #difficulty
    selected_difficulty = st.selectbox(
                "Select difficulty level",
                 ["Easy", "Medium", "Hard"], key="difficulty",
                 index=None
                 )
    
    if selected_difficulty:
        st.success(f"Selected difficulty: {selected_difficulty}")
        
    else:
        st.error("Please select a difficulty level.")
    
    st.button("Generate Summary and Quiz", key="generate", type="primary")