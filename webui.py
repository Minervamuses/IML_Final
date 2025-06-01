# webui.py

import streamlit as st
from ultralytics import YOLO
from PIL import Image
import torch
import os

st.set_page_config(page_title="Wheat Disease Classifier", layout="centered")
st.title("🌾 Wheat Disease Classifier")
st.caption("Upload a wheat leaf image, and I will predict the disease category.")

# === 模型路徑設置 ===
DEFAULT_MODEL_PATH = "best.pt"

# 檢查模型是否存在
if not os.path.isfile(DEFAULT_MODEL_PATH):
    st.error(f"❌ Model file '{DEFAULT_MODEL_PATH}' not found. Please place your 'best.pt' in the same folder as this script.")
    st.stop()

# 載入模型
model = YOLO(DEFAULT_MODEL_PATH)
labels = ['Brown_Rust', 'Healthy', 'Yellow_Rust']

# 設定運行裝置
device = "cuda" if torch.cuda.is_available() else "cpu"
st.info(f"Using device: {device}")

# 上傳圖片
uploaded = st.file_uploader("Choose an image", type=['jpg','jpeg','png','JPG'])
if uploaded:
    img = Image.open(uploaded).convert("RGB")
    img_resized = img.resize((224, 224))
    st.image(img_resized, caption='Resized Input (224x224)', use_column_width=True)

    # 推論
    with st.spinner("Classifying..."):
        pred = model.predict(img_resized, imgsz=224, device=device, verbose=False)[0]
        cls_idx = pred.probs.top1
        cls_name = labels[cls_idx]
        conf_pct = pred.probs.top1conf * 100

    st.success(f"**Prediction:** {cls_name} ({conf_pct:.1f}%)")
    st.caption(f"Class index: {cls_idx}")

st.markdown("---")
st.caption("Developed by **Gary Chiang** | AI Wheat Disease Detection Project")
