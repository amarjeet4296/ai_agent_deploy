import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()

def generate_content(topic):
    """Generate content using Groq API with a single agent approach."""
    try:
        # Initialize Groq client
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
            # Explicitly set proxies to None to avoid any issues
            proxies=None
        )
        
        # System prompt that defines the agent's role and behavior
        system_prompt = """You are an expert content creator with deep knowledge across many subjects. 
        Your task is to create a well-researched, engaging, and informative article on the given topic.
        
        Follow these steps:
        1. Research the topic thoroughly
        2. Create an outline with key sections
        3. Write the article with proper formatting
        4. Include relevant examples, data, and sources
        5. Ensure the content is well-structured with an introduction, body, and conclusion
        6. Use markdown formatting for better readability
        7. Include section headers (##), bullet points, and bold/italic text where appropriate
        
        The article should be comprehensive yet easy to understand, suitable for a general audience.
        """
        
        # User prompt with the topic
        user_prompt = f"""Write a comprehensive, well-researched article about: {topic}
        
        Please include:
        - An engaging introduction
        - Main content with subsections
        - Relevant examples and data
        - A conclusion that summarizes key points
        - Sources or references if possible
        
        Format the response in markdown.
        """
        
        # Make the API call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        # Return the generated content
        return response.choices[0].message.content
        
    except Exception as e:
        return f"An error occurred while generating content: {str(e)}"



def main():
    st.set_page_config(page_title="AI Content Writer", page_icon="✍️")
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-title {
        font-size: 2.5em;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 2em;
    }
    .content-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 5px solid #4B8BBE;
    }
    .stButton>button {
        background-color: #4B8BBE;
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px 0;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #306998;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header section
    st.markdown("<h1 class='main-title'>AI Content Writer</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Generate high-quality, well-researched content with AI</p>", unsafe_allow_html=True)
    
    # Try to load logo, but don't fail if it doesn't exist
    try:
        st.image("logo4.jpg", width=300, use_column_width=True)
    except:
        pass
    
    # Topic input
    topic = st.text_input(
        "**What would you like to write about?**", 
        "", 
        placeholder="e.g., The Future of Renewable Energy, Benefits of Meditation, etc.",
        help="Enter a topic for your article"
    )
    
    # Generate button
    if st.button("Generate Content"):
        if not topic.strip():
            st.warning("Please enter a topic first!")
        else:
            with st.spinner('🧠 Generating your content... This may take a minute or two.'):
                try:
                    # Generate content
                    content = generate_content(topic)
                    
                    # Display the generated content in a nice container
                    st.markdown("---")
                    st.markdown("## ✨ Your Generated Content")
                    st.markdown("<div class='content-box'>" + content + "</div>", unsafe_allow_html=True)
                    
                    # Add a download button
                    st.download_button(
                        label="📥 Download as Markdown",
                        data=content,
                        file_name=f"{topic[:30].replace(' ', '_').lower()}_article.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.info("Please make sure your Groq API key is properly set in the .env file.")
    

if __name__=='__main__':
    main()