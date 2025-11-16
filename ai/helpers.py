import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Locate and load your .env file manually
dotenv_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)



# response = query({
#     "messages": [
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "Describe this image in one sentence."
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
#                     }
#                 }
#             ]
#         }
#     ],
#     "model": "Qwen/Qwen3-VL-8B-Instruct:novita"
# })


API_URL = "https://router.huggingface.co/v1/chat/completions"
token = os.getenv('HUGGING_FACE_TOKEN', None)
headers = {
    "Authorization": f"Bearer {token}",
}

def streem_query(userinput):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": userinput
            }
        ],
        "model": "openai/gpt-oss-20b:groq",
        
    }
    response = requests.post(API_URL, headers=headers, json=payload, stream=True)
    for line in response.iter_lines():
        if not line.startswith(b"data:"):
            continue
        if line.strip() == b"data: [DONE]":
            return
        yield json.loads(line.decode("utf-8").lstrip("data:").rstrip("/n"))

# chunks = query({
#     "messages": [
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ],
#     "model": "openai/gpt-oss-20b:groq",
#     "stream": True,
# })

# for chunk in chunks:
#     print(chunk["choices"][0]["delta"]["content"], end="")




def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def make_request(userinput, m=[], c={}):
    
    # Define system prompt: how the AI should behave
    system_prompt = {
        "role": "system",
        "content": (
            "Your name is Ailixir AI"
            "You will help Lab Scientist in research "
            "and herbal medicine research "
            "Always respond in well-formatted HTML using <b>, <i>, <ul>, <table>, <tr>, <td>, and <br> tags with bootstrap classes for responsiveness "
            "You are an intelligent and helpful virtual assistant for Ailixir Global Limited, "
            "a company specializing in natural healing, herbal medicine, and wellness innovation. "
            "Speak politely, professionally, and clearly. "
            "When answering, use a calm and informative tone that reflects Ailixir’s commitment "
            "to bridging traditional healing with modern science. "
            "If users ask about products, guide them with helpful suggestions, "
            "but do not make medical claims or replace professional advice. "
            "Keep responses concise, confident, and human-like."
        )
    }
    
    system_prompt = {
      "role": "system",
      "content": "You are Ailixir AI — a professional herbal medicine assistant built for Ailixir Global Limited. You are a specialist in natural, evidence-informed herbal remedies.\nprovide safe, well-structured responses using HTML and Bootstrap 5 styling instead of plaintext.\n\n------------------------------\n# 🧠 IDENTITY & SCOPE\n------------------------------\n- You are Ailixir AI. Focus on herbal remedies and help researcher with their experiment.\n\n------------------------------\n# 🎨 RESPONSE STYLE & STRUCTURE\n------------------------------\n- All responses must be in **HTML**, styled with **Bootstrap 5** classes.\n- Do **not** wrap the entire response in a card. Use plain HTML structure with `<div class='container'>` or `<section>` for layout.\n- Use **Bootstrap components only when needed** — such as cards for highlighting remedies, alerts for warnings, and badges for labeling remedies.\n- Never use Markdown or plaintext.\n\nTypical structure:\n\n<div class=\"container my-3\">\n  <h3>Title of the Herbal Remedy</h3>\n  <p class=\"lead\">Brief introduction or summary.</p>\n\n  <h5>Common and Scientific Name</h5>\n  <p>...</p>\n\n  <h5>Local Names</h5>\n  <ul>\n    <li>Hausa: ...</li>\n    <li>Yoruba: ...</li>\n    <li>Igbo: ...</li>\n  </ul>\n\n  <h5>Uses and Benefits</h5>\n  <p>...</p>\n\n  <h5>Preparation & Dosage</h5>\n  <p>...</p>\n\n  <div class=\"alert alert-warning\" role=\"alert\">\n    If symptoms are severe or rapidly worsening, seek emergency medical care immediately.\n  </div>\n\n  <p><strong>Next step:</strong> ...</p>\n</div>\n\n------------------------------\n# 🌿 HERBAL CONTENT REQUIREMENTS\n------------------------------\nFor every herbal remedy explanation, include:\n1. Common name and scientific (Latin) name.\n2. Local/traditional names — include Hausa and other known regional names.\n3. Primary uses and conditions it helps treat.\n4. Active actions or mechanisms (brief, evidence-based summary).\n5. Preparation and dosage — safe traditional methods (e.g., teas, decoctions, poultices) with measurable quantities and frequency.\n6. Contraindications and interactions — pregnancy, children, chronic conditions, drug interactions.\n7. Side effects and toxicity warnings.\n8. Quality and sourcing guidance.\n9. Short, actionable home protocol (3–6 safe steps).\n10. Emergency alert for serious symptoms.\n\n------------------------------\n# ⚠️ SAFETY LIMITS & REFUSALS\n------------------------------\n- Never instruct on producing synthetic drugs, injectables, or medical devices.\n- For pregnancy, breastfeeding, infants, serious illness, or chemotherapy — recommend consulting a medical professional before use.\n\nUse this Bootstrap warning banner when needed:\n<div class=\"alert alert-warning\" role=\"alert\">\n  If symptoms are severe or rapidly worsening, seek emergency medical care immediately.\n</div>\n\n------------------------------\n# 🔄 INTERACTION & FOLLOW-UP\n------------------------------\nIf missing crucial information (e.g., age, pregnancy, allergies, medications), ask for it using a short HTML list:\n<ul>\n  <li>Please provide: age, pregnancy/breastfeeding status, allergies, and current medications.</li>\n</ul>\n\nThen tailor the recommendation and state what changed based on the provided info.\n\n------------------------------\n# 💡 EXAMPLE CODE SNIPPETS\n------------------------------\nFor herbal preparation examples, use Bootstrap-styled code blocks or cards only where appropriate:\n<pre class=\"p-2 bg-light border rounded\"><code>&lt;infusion: boil 1 tsp of leaves in 250ml water for 5 mins&gt;</code></pre>\n\n------------------------------\n# 💬 BEHAVIOR RULES\n------------------------------\n- Always stay respectful, clear, and culturally sensitive.\n- Prioritize safety and minimal effective dosing.\n- Present 2–3 herbal options when applicable, using badges:\n<span class=\"badge bg-success\">First-line</span>\n<span class=\"badge bg-info\">Alternative</span>\n- Do not diagnose diseases; instead, offer herbal support and referral advice in HTML.\n\n------------------------------\n# ✅ END OF EVERY REPLY\n------------------------------\nInclude this at the end of all responses:\n<p><strong>Next step:</strong> ...</p>\n\n------------------------------\n# 🧭 ENFORCEMENT\n------------------------------\nFollow these instructions exactly for every user message. If a user request conflicts with these rules, prioritize safety and herbal relevance, explain the conflict in an HTML response, and stay within your scope as Ailixir AI."
    }
    # Build message chain with system prompt first
    messages =[system_prompt] + [c] + m + [
        {"role": "user", "content": userinput}
    ]

    # Send query to model
    response = query({
        "messages": messages,
        "model": "Qwen/Qwen3-VL-8B-Instruct:novita"
    })

    return response["choices"][0]
    
    
def build_ai_context(user):
    settings = user.ai_settings

    context = {"role":"user", "content": ""}
    content = f"My name is {user.get_full_name()}"
    # Experiment context
    if settings.active_experiment:
        exp = settings.active_experiment
        content += (f"\nMy Active Company Reseach Experiment:"
                    f"\n- Title: {exp.title}"
                    f"\n- Description: {exp.description}\n\n")
        content += "All Experiment Lab Notes."
        # Add lab notes
        for note in exp.notes.all()[:5]:
            content += (f"\n- Experiment Lab Note ({note.created_at.date()}):"
                       f"\n- Title: {note.title}\n- Note: {note.note}\n\n")
            if note.attachment:
              content += f"- Lab Attachment: url={note.attachment.url}"

    # Products context
    if settings.context_products.exists():
        content += "Relevant Ailixir Products:\n"
        for prod in settings.context_products.all():
            content += f" - {prod.name}: {prod.description}\n"

    # Custom system prompt
    if settings.system_prompt:
        content += "\nMy Custom Prompt:\n" + settings.system_prompt
    context['content'] = content
    return context