# Wheat Disease Classifier 🌾

A project for classifying wheat leaf diseases using YOLOv8 image classification.

## 📂 Files

- `wheat_training.ipynb` - Model training notebook (Colab)
- `webui.py` - Streamlit Web UI for inference
- `wheat.yaml` - Dataset configuration file
- `requirements.txt` - Python dependencies
- `README.md` - This file

## 🗂 Dataset

This project uses the **Five Crop Diseases Dataset** from Kaggle:
- 📦 [Kaggle Dataset](https://www.kaggle.com/datasets/shubham2703/five-crop-diseases-dataset)

⚠️ Note: The original dataset contains multiple crops. If you want to run this project with balanced class samples, it is recommended to use only the **Wheat** data, as it has more balanced class distributions.

## 🚀 How to Use

### 1️⃣ Download the Dataset

1. Go to the [Kaggle dataset page](https://www.kaggle.com/datasets/shubham2703/five-crop-diseases-dataset) and download the dataset.
2. Extract the files and select the **Wheat** images only:
   - Wheat___Brown_Rust
   - Wheat___Healthy
   - Wheat___Yellow_Rust
3. Place these three folders in your `/training` directory.

### 2️⃣ Train the Model

1. Open `wheat_training.ipynb` in **Google Colab**.
2. Mount Google Drive in the notebook.
3. Run all cells to:
   - Split the dataset into train/val/test (80/10/10).
   - Train the YOLOv8 classification model.
4. After training, the best model will be saved as `best.pt`.

### 3️⃣ Run the Web UI

1. Download `best.pt` from Colab and place it in the **same folder** as `webui.py`.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
