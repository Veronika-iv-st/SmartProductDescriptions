# 🧠 SmartProductDescriptions

An AI-powered product description enhancer built with LangChain and GPT-3.5.

This project transforms simple product descriptions into persuasive, emotional, and sales-optimized texts — ideal for ecommerce.

---

## 🚀 What does it do?

- Takes a basic product description from the user.
- Generates a refined version using commercial and emotional language.
- Uses LangChain + OpenAI to generate content dynamically.

---

## 🛠️ Technologies used

- **Python 3.10+**
- **LangChain**
- **LangChain Community**
- **LangChain OpenAI** ✅
- **OpenAI Python SDK**
- **python-dotenv** (for environment variable management)
- **virtualenv** (recommended)

---

## ⚙️ Installation

### 1. Clone the repository

Create and activate a virtual environment
bash
Copiar
Editar
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
3. Install the required dependencies
bash
Copiar
Editar
pip install langchain langchain-community langchain-openai openai python-dotenv
🔐 Set up your API key
Create a .env file in the root of the project.

Add your OpenAI key inside:

env
Copiar
Editar
OPENAI_API_KEY=sk-your_key_here

▶️ How to use
Run the main script:

bash
Copiar
Editar
python mejorador_producto.py