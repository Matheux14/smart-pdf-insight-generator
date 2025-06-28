
# smart-pdf-insight-generator

Automated PDF insight and summary generator leveraging a fully serverless architecture with AWS Lambda and state-of-the-art Generative AI.

---

## 🚀 About the Project

**smart-pdf-insight-generator** is a serverless backend function designed for rapid PDF document analysis. It:
- Extracts text from PDF files using Python and `PyPDF2`
- Summarizes the extracted content with a large language model (Groq Llama 3, Mixtral, or OpenAI GPT-4)
- Returns a structured, executive-ready summary through a simple REST API

Originally built for hackathons and business automation, it's ready for production and demo purposes.

---

## 🏗️ How it Works (AWS Lambda Architecture)

This application is built entirely around AWS Lambda:
- **Lambda** is used as the central backend, triggered by API Gateway when a user uploads a PDF.
- On each request, the Lambda function:
    1. Receives and decodes a base64-encoded PDF file.
    2. Extracts the text content from the PDF in-memory.
    3. Invokes a connected AI model (Groq/OpenAI) to generate a concise summary using a business-oriented prompt.
    4. Returns a JSON response with the summary and extracted content.

No servers to manage—everything runs and scales automatically within AWS Lambda.

---

## 🎯 Main Features

- ✅ **AWS Lambda** Python function—simple, portable, and cloud-native
- 📄 **PDF text extraction** with PyPDF2 (no temp files, works in-memory)
- 🤖 **LLM Summarization** with Groq (Llama 3, Mixtral) or OpenAI GPT models
- ⚡ **Minimal dependencies**—fast cold starts, works out-of-the-box
- 🛡️ **CORS-ready** for front-end integration

---

## 📁 Project Structure

```
smart-pdf-insight-generator/
│
├── app.py              # Main Lambda handler and business logic
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
```

---

## 🧪 How to Deploy & Test

### 1. Live Demo

- **Test the app here:**  
  [https://smart-pdf-i-gen.vercel.app/](https://smart-pdf-i-gen.vercel.app/)

- **Or call the API directly:**  
  [[https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/](https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/Prod/analyze-pdf/)]([[https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/](https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/Prod/analyze-pdf/)](https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/Prod/analyze-pdf/))

### 2. Deploy on AWS Lambda

- Upload `app.py` as your Lambda function code.
- Ensure dependencies in `requirements.txt` are included (use Lambda layers or a deployment package).
- Set environment variables for your Groq or OpenAI API keys as needed.

### 3. API Gateway (optional)

- Integrate with API Gateway to allow POST requests from your app or tools like Postman.
- Make sure to send the PDF file as a base64-encoded string in the body.

#### Example event payload for Lambda:

```json
{
  "body": "BASE64_ENCODED_PDF_CONTENT",
  "isBase64Encoded": true,
  "httpMethod": "POST"
}
```

---

## 🧠 AI Model Compatibility

Supported out-of-the-box:
- **Groq** (Llama 3, Mixtral)
- **OpenAI** (GPT-4, GPT-4o, GPT-3.5)
- Easily extend to Claude (Anthropic) or other LLMs

Plug your API key and model name in `app.py` as shown in the code comments.

---

## 🚦 Usage & Endpoints

- **POST** `/analyze-pdf`  
  Upload a base64-encoded PDF to receive its summary.
- **OPTIONS** preflight supported (CORS-ready)
- Returns JSON with original text and AI-generated summary.

---

## 💡 Future Directions

- Drag-and-drop file upload front-end
- Batch PDF processing and chunked analysis
- Storage of summaries in AWS S3 or DynamoDB
- Multi-language and OCR support

---

## 🛠️ AWS Tools Used

- **AWS Lambda** (main compute runtime)
- **API Gateway** (REST interface)
- **IAM** (permissions)
- **S3** (optional for storage of results)

---

## 🏷️ License

This project is licensed under the MIT License.

---

## 🔗 Live Demo & API

- Web App: [https://smart-pdf-i-gen.vercel.app/](https://smart-pdf-i-gen.vercel.app/)
- API: [[https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/](https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/Prod/analyze-pdf/)]([[https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/](https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/Prod/analyze-pdf/)](https://yyqocvqwpk.execute-api.us-east-1.amazonaws.com/Prod/analyze-pdf/))
