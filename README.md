
# Suffolk Backyard Ultra – Q&A App

A tiny Streamlit app that lets anyone query the Suffolk Backyard Ultra results
in plain English (thanks to `pandas-ai` + GPT).

## Quick start

```bash
git clone https://github.com/YOUR-USER/ultra-app.git
cd ultra-app

# Install deps (conda, venv or pipx—your choice)
pip install -r requirements.txt

# Put the race CSV next to app.py
cp /path/to/ANALYST\ -\ CLEAN.csv .

# Add your OpenAI key (Linux/macOS)
export OPENAI_API_KEY=sk-...

# Run!
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501).

## Deploy free on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to <https://share.streamlit.io>.
3. Select your repo & `app.py`.
4. In *Secrets* add

   ```toml
   OPENAI_API_KEY = "sk-..."
   ```
5. Click **Deploy** – share the resulting URL with your friends!

## Notes

* CSV is **.gitignored** by default so you can keep results private.
* Uses **`gpt-4o-mini`** by default (cheap & capable). Change the model
  in `app.py` if you prefer `gpt-3.5-turbo` or a local Ollama model.
