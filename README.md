# 🖼️ Image_Caption_Generator
More like image description than caption!

A modular, Streamlit-powered app that generates natural language captions for uploaded images using a pretrained BLIP model. Built with PyTorch and designed for clarity, scalability, and sharing.

Upload an image and get a descriptive caption in seconds.

## 📁 Project Structure

```
Image_Caption/
├── main.py                  # Entry point for Streamlit app
├── app/
│   ├── interface.py         # Streamlit UI logic
│   ├── model.py             # BLIP model loading and caption generation
│   ├── utils.py             # Image preprocessing helpers
│   ├── __pycache__/         # Python cache (ignored)
│   └── .ipynb_checkpoints/  # Jupyter backups (ignored)
├── assets/
│   └── *.png                # Sample/demo images
├── __pycache__/             # Python cache (ignored)
└── .ipynb_checkpoints/      # Jupyter backups (ignored)
```


## 🛠️ Technologies Used 

* Python 3.x
* Streamlit
* Libraries:
  
  * `PyTorch`
  * `transformers`
  * `Pillow`
  * `requests`
  * `os`
  * `io`
    
* Model:

   BLIP (Salesforce/blip-image-captioning-base) via Hugging Face

## 🧠 Model

Uses the [BLIP (Bootstrapped Language Image Pretraining)](https://github.com/salesforce/BLIP) model for zero-shot image captioning. The model is loaded via Hugging Face Transformers and optimized for inference.

## 🛠️ Setup

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies
4. Run the app:

```bash
streamlit run main.py
```

## 📦 Dependencies

- `PyTorch`
- `transformers`
- `streamlit`
- `Pillow`
- `requests`


## 🧹 Future Improvements

- Add support for multiple captions per image  
- Integrate image enhancement or resizing  
- Deploy via Hugging Face Spaces or Streamlit Cloud  
- Add drag-and-drop upload and caption history

## 📄 License

MIT License. See `LICENSE` for details.

---




