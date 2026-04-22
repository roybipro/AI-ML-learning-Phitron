import streamlit as st
from api_calling import generate_note_summary
from PIL import Image

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
    
    pil_images = [Image.open(image) for image in uploaded_images]
    
    
    if pil_images:
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
    
    
    pressed = st.button("Generate Summary and Quiz", key="generate", type="primary")
    
    
    
    
#front section
if pressed:
    if not uploaded_images:
        st.error("Please upload at least one image to generate summary and quiz.")
    elif not selected_difficulty:
        st.error("Please select a difficulty level to generate summary and quiz.")
        
    if uploaded_images and selected_difficulty:
        
        #note summary
        
        with st.container(border=True):
            st.subheader("Your Note")
            
            #this portion will be replaced by API call
            genarated_notes = generate_note_summary(pil_images)
            st.markdown(genarated_notes)
            
        
        #audio summary
        
        with st.container(border=True):
            st.subheader("Audio Summary")
            
            #this portion will be replaced by API call
            
            st.text("Audio summary will be displayed here")
        
        #quiz generation
        
        with st.container(border=True):
            st.subheader(f"Quiz Questions ({selected_difficulty})")
            
            #this portion will be replaced by API call
            
            st.text("Quiz questions will be displayed here")