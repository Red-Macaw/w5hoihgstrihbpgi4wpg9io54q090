import streamlit as st
from PIL import Image

img = Image.open("NeuraSwiftchromeicon.png")
st.set_page_config(
    
    page_title="NeuraSwift",
    page_icon=img,
)


st.title("Welcome to NeuraSwift")
st.write("Empowering Minds, Shaping Futures")

# Section: What We Do
st.header("What We Do")
st.write("""
At **NeuraSwift**, we believe that **AI is for everyone**. Our mission is to harness the potential of artificial intelligence to make education accessible, engaging, and effective for all—**completely free of charge**.

We create a suite of interactive educational bots designed to support learners across subjects and skill levels. Each bot in NeuraSwift provides specialized assistance, whether it's solving complex math problems, helping you understand challenging concepts, or guiding you through documents quickly and intuitively. NeuraSwift is here to bridge gaps in learning, making high-quality education more achievable.

**Why choose NeuraSwift?**  
- **Free for All**: All our educational bots are free to use, ensuring accessible education for everyone, anywhere.
- **Personalized Learning**: Our bots adapt to each user, providing support and feedback tailored to your unique needs.
- **Future-Focused**: We continuously work on expanding our bot family, adding new subjects and capabilities to meet the evolving needs of learners around the world.
""")

# Section: Meet Our Bots
st.header("Our Bots")
st.write("""
NeuraSwift offers a growing range of AI-powered bots designed to make learning more interactive and engaging:

- **Numerix** – A dedicated math tutor bot that’s always available to explain concepts, help solve problems, and guide you through equations with ease.
- **DocuBot** – Our PDF assistant bot that enables you to upload any document and get fast, clear answers or summaries. Perfect for studying notes, textbooks, or research documents.
- *(More bots coming soon!)*

Each bot is crafted to enhance your learning experience, making it easier to dive into subjects, ask questions, and get instant assistance whenever you need it.
""")

# Section: Get Started
st.header("Get Started")
st.write("""
Ready to begin your learning journey with NeuraSwift?  
Explore our bots, ask questions, and start discovering a whole new way to learn with AI. Simply select a bot to begin, and let NeuraSwift guide you through your lessons and study materials—all at your own pace.
""")