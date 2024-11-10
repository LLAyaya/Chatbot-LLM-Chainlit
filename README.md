# Running the Project on Google Colab and Chainlit

## Free Version on Google Colab

To run the free version of this project, simply use [Google Colab](https://colab.research.google.com/) to run the source code.

---

## Chainlit Version Setup

For the Chainlit version, follow these steps:

1. Clone the source code repository.
2. In the `Chainlit-LLM-Chatbot` folder, create a `.env` file include `OPENAI_API_KEY = "your_key"`.
3. Install the requireed dependencies:
```bash
pip install -r requirement.txt
```
4. Run the chatbot using:
```bash
chainlit init
```
```bash
chainlit run app.py
```
