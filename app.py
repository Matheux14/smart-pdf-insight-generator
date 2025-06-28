import json
import base64
import io
import sys
import os
from datetime import datetime

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

def extract_text_from_pdf(file_bytes):
    if PdfReader is None:
        return "PyPDF2 non disponible."
    try:
        reader = PdfReader(io.BytesIO(file_bytes))
        text = ''
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text() or ''
            text += page_text + '\n'
        return text
    except Exception as e:
        print(f"[Erreur lecture PDF] {e}", file=sys.stderr)
        return f"[Erreur lecture PDF] {e}"

def simple_summarizer(text, max_sentences=3):
    import re
    sentences = re.split(r'(?<=[.!?]) +', text)
    summary = ' '.join(sentences[:max_sentences])
    return summary

def smart_groq_summary(text):
    import openai

    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        return "[Erreur Groq] Aucune clé API définie"
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    prompt = (
        "Summarize this PDF document as if you were explaining it to a C-level executive. "
        "Extract ONLY the key information, main findings, recommended actions, and any important insights that could support business decision-making. "
        "Your summary must be clear, concise, and actionable, avoiding unnecessary technical or background details. "
        "Whenever possible, use bullet points or numbered lists for clarity.\n\n"
        "Structure your output as follows:\n"
        "1. Executive Summary (2-3 sentences)\n"
        "2. Key Points or Findings (bulleted list)\n"
        "3. Recommended Actions (bulleted or numbered list)\n"
        "4. Additional Insights (optional)\n\n"
        f"PDF content:\n{text[:6000]}"
    )

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "Tu es un assistant expert en résumé de documents professionnels, peu importe la langue."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[Erreur Groq] {e}", file=sys.stderr)
        return f"[Erreur Groq] {e}"

# === HEADERS CORS À INCLURE PARTOUT (compatible React) ===
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
    "Access-Control-Allow-Methods": "POST,OPTIONS"
}

def lambda_handler(event, context):
    print("Lambda handler called", file=sys.stderr)
    method = (
        event.get("httpMethod")
        or event.get("requestContext", {}).get("http", {}).get("method", "")
    )

    # GESTION DES REQUÊTES OPTIONS (CORS preflight)
    if method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": ""
        }

    if method == "POST":
        try:
            print(f"Event keys: {list(event.keys())}", file=sys.stderr)
            file_bytes = None
            if event.get("isBase64Encoded"):
                print("Décodage base64 (isBase64Encoded true)", file=sys.stderr)
                file_bytes = base64.b64decode(event["body"])
            else:
                print("Décodage base64 (raw body)", file=sys.stderr)
                file_bytes = base64.b64decode(event["body"])

            if not file_bytes:
                return {
                    "statusCode": 400,
                    "headers": CORS_HEADERS,
                    "body": json.dumps({"error": "Aucun fichier PDF fourni."})
                }

            text = extract_text_from_pdf(file_bytes)
            summary = simple_summarizer(text)

            try:
                ai_summary = smart_groq_summary(text)
            except Exception as e:
                ai_summary = f"[Erreur Groq] {e}"

            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "message": "PDF processed successfully!",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "extracted_text": text[:1000] + ("..." if len(text) > 1000 else ""),
                    "summary": summary,
                    "ai_summary": ai_summary
                })
            }
        except Exception as e:
            print(f"Exception Lambda: {e}", file=sys.stderr)
            return {
                "statusCode": 500,
                "headers": CORS_HEADERS,
                "body": json.dumps({"error": f"Erreur interne: {e}"})
            }

    # Par défaut : GET ou autre
    return {
        "statusCode": 200,
        "headers": CORS_HEADERS,
        "body": json.dumps({
            "message": "🚀 Endpoint /analyze-pdf prêt. POSTez un PDF (body = base64 PDF) pour recevoir son résumé.",
            "Owner": "Konan Othniel",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "format": "POST body = chaîne base64 du PDF. Headers: Content-Type: text/plain"
        })
    }
