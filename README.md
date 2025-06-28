# smart-pdf-insight-generator

Automated PDF insight and summary generator using a fully serverless architecture with AWS Lambda and Generative AI.

---

## 🚀 About the Project

**smart-pdf-insight-generator** is an AWS Lambda function that:
- Extracts text from PDF files,
- Summarizes the content using advanced AI models (e.g., Groq Mixtral or OpenAI GPT-4),
- Returns structured insights via a REST-like interface.

Originally built for hackathon use cases like intelligent automation and rapid report analysis.

---

## 🎯 Main Features

- ✅ **AWS Lambda** Python function ready to deploy
- 📄 **PDF text extraction** using `PyPDF2`
- 🧠 **AI summarization** logic embedded (Groq/OpenAI compatible)
- ⚡ **Minimal dependencies**, portable and fast

---

## 📁 Project Structure

```
smart-pdf-insight-generator/
│
├── app.py              # Main Lambda handler
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🧪 How to Test

You can test this function locally using the AWS Lambda console by uploading a base64-encoded PDF payload:

```json
{
  "file_bytes": "BASE64_ENCODED_PDF_CONTENT"
}
```

Or by integrating it with an API Gateway for RESTful interaction.

---

## 📦 Future Improvements

- Add file upload endpoint (via API Gateway)
- Support multilingual PDF summarization
- Improve chunking and batching for long documents
- Plug-in GROQ or OpenAI key for real summarization

---

## 🧠 AI Model Compatibility

Can be connected to:
- **OpenAI GPT-4 / GPT-4o**
- **Groq Mixtral / LLaMA-3**

A simple wrapper around your LLM of choice can be added inside `app.py`.

---

## 🛡️ License

This project is licensed under the MIT License.
