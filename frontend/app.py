
import streamlit as st
import requests
import os

st.set_page_config(page_title="Memory Resurrection AI", layout="centered")

# =========================
# TITLE
# =========================
st.markdown(
    "<h1 style='text-align:center; color:#2f5d5b;'>Memory Resurrection AI 🧠</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:18px;'>Transform your memories into elegant visual stories</p>",
    unsafe_allow_html=True
)

# =========================
# DESCRIPTION
# =========================
st.markdown(
    """
<div style='background-color:#e8ecef; padding:20px; border-radius:12px; color:#222;'>

<h4 style='color:#2f5d5b;'>✨ What this AI can do:</h4>

<ul style='color:#222; font-size:16px; line-height:1.6;'>
<li>🔍 Analyze your memories using intelligent scene understanding</li>
<li>🎭 Detect emotions and key moments automatically</li>
<li>🖼️ Reconstruct memories into realistic visual scenes</li>
<li>🎬 Generate visual storytelling outputs from simple text</li>
<li>⚡ Works in real-time with adaptive generation modes</li>
</ul>

</div>
""",
    unsafe_allow_html=True
)

st.write("")

# =========================
# INPUT
# =========================
st.subheader("✍️ Describe your memory")

text = st.text_area(
    "Memory Input",
    placeholder="Example: I was walking through a garden at sunset...",
    height=150,
    label_visibility="collapsed"
)

# =========================
# MODE
# =========================
st.subheader("⚙️ Select Generation Mode")

mode = st.selectbox(
    "Mode Selection",
    ["free", "creative", "cinematic"],
    label_visibility="collapsed"
)

# =========================
# BUTTON
# =========================
st.write("")
if st.button("🚀 Generate Memory Visualization"):

    if not text.strip():
        st.error("Please enter a memory!")
    else:
        with st.spinner("Generating..."):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/memory/parse-memory",
                    json={"text": text, "mode": mode}
                )

                # ✅ CHECK RESPONSE TYPE
                if response.status_code == 200 and "image" in response.headers.get("content-type", ""):

                    image_path = "output.jpg"

                    with open(image_path, "wb") as f:
                        f.write(response.content)

                    # ✅ VALIDATE IMAGE SIZE
                    if os.path.getsize(image_path) > 100:
                        st.success("✨ Memory Visualized Successfully!")
                        st.image(image_path, use_container_width=True)
                    else:
                        st.error("❌ Invalid image received")

                else:
                    st.error("❌ Backend did not return a valid image")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

