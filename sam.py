import streamlit as st

# Page Configurations
st.set_page_config(page_title="A Special Surprise!", page_icon="🎉", layout="wide")

# Background Style
def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            color: white;
        }}
        h1, h2, h3, p {{
            text-align: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }}
        .video-container {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }}
        .video-wrapper {{
            width: 60%;  /* Reduced width */
            max-width: 700px;  /* Limit max width for landscape */
            height: 300px;  /* Set a fixed height to make it look like a landscape frame */
            position: relative;
            border-radius: 10px;
            overflow: hidden;
        }}
        .video-wrapper video {{
            width: 100%;
            height: 100%;  /* Full container height to maintain the landscape look */
            object-fit: cover;  /* Ensure the video covers the full frame */
            border-radius: 10px;
        }}
        .love-letter {{
            background: rgba(255, 105, 180, 0.7);
            padding: 20px;
            border-radius: 15px;
            font-size: 20px;
            color: white;
            text-align: center;
            margin-top: 20px;
        }}
        .footer {{
            text-align: center;
            font-size: 18px;
            margin-top: 30px;
            color: white;
        }}
        .btn-surprise {{
            display: block;
            width: 50%;
            margin: auto;
            padding: 10px;
            background: #ff4081;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            cursor: pointer;
            text-align: center;
            border: none;
            font-weight: bold;
            visibility: visible;
        }}
        .btn-surprise:hover {{
            background: #ff79a6;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg()

# Title and Welcome Message
st.markdown("""
    <h1 style='color: yellow;'>🎂 Happy Birthday My Love! 🎂</h1>
    <p style='font-size: 22px;'>
        I may not be there in person, but my heart is always with you! 💖
    </p>
    """, unsafe_allow_html=True)

# Video Display Section (Landscape Rectangle)
st.markdown("### 🎥 Here’s a Special Gift for You! (view it in full screen)")
video_path = "media/sam1.mp4"  # Provide correct file path

# Display video using Streamlit's native method
st.video(video_path, start_time=0)  # `start_time=0` ensures it starts from the beginning

# Love Letter
st.markdown("### 💌 A Letter From My Heart 💌")
love_letter = """
    <div class='love-letter'>
    <p><b>My Dearest Samyu,</b></p>
    <p>Happy Birthday, my love! 🎂💖</p>
    <p>If I could make just one wish today, it would be to see your beautiful
    smile—the one that lights up my world and makes everything feel right.</p>
    <p>I know you're going through a tough time right now, and my heart aches 
    knowing that you're feeling sad. If I could, I would take all your pain away 
    and replace it with endless happiness.</p>
    <p>Being far away from you is the hardest thing, but no distance can ever 
    change how much I love you. You are in my heart every second, in my 
    thoughts every moment, and in my dreams every night.</p>
    <p>So on this special day, smile for me, my love. Smile because you are loved 
    beyond words, because you are never alone, and because our love is 
    stronger than anything life can throw at us.</p>
    <p><b>Happy Birthday, my queen. I love you endlessly.</b></p>
    <p><b>Forever yours,</b></p>
    <p><b>Cheenu ❤️</b></p>
    </div>
    """
st.markdown(love_letter, unsafe_allow_html=True)

# Final Surprise
st.markdown("### 👈Click for a Final Surprise! 🎁")
if st.button("Click for a Final Surprise! 🎁", help="Click to reveal a special surprise!"):
    st.balloons()
    st.markdown("### 🎶 Play this song and feel my presence! 💞")
    st.audio("media/blue.mp3")

# Footer
st.markdown("<p class='footer'>Made with ❤️ by your Cheenu </p>", unsafe_allow_html=True)
