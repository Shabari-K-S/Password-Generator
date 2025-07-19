# 🔐 Strong Password Generator API

A fast and secure API built with FastAPI to generate cryptographically strong passwords. Perfect for tokens, login credentials, salts, or any scenario requiring secure random strings.

---

## 🚀 Features

- 🔒 Cryptographically secure using Python’s `secrets` module
- ⚙️ Fully customizable options:
  - Password length
  - Include uppercase letters
  - Include lowercase letters
  - Include numbers
  - Include special characters
- ⚡ FastAPI-powered and production-ready
- 🌍 CORS enabled for frontend integration

---

## 📦 Technologies Used

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn (for ASGI server)

---

## 📥 API Endpoint

**POST** `/generate`

### 🔧 Request Body (JSON)
```json
{
  "length": 24,
  "include_uppercase": true,
  "include_lowercase": true,
  "include_numbers": true,
  "include_special_chars": true
}
````

### ✅ Response Example

```json
{
  "generated_string": "aZ$9LrX@83k1Q%uE6VgTzYpn",
  "length": 24
}
```

---

## 💡 Use Cases

* 🔐 Password generator for sign-up/login flows
* 🎟️ Secure tokens or invite codes
* 🧂 Salt generation for cryptographic hashing
* 🛡️ Temporary access codes or session IDs

---

## 🛠️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Shabari-K-S/Password-Generator.git
cd Password-Generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn main:app --reload
```

Now visit: [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

---

## 🌐 Deployment Ready

* Dockerfile (coming soon!)
* RapidAPI integration
* Easily deployable to Render, Railway, or Vercel

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or issue anytime.

---

## ✨ Author

**Shabari K S**
📧 [shabaricse2003@gmail.com](mailto:shabaricse2003@gmail.com)


