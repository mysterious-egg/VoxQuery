# 🎙️ VoxQuery – Talk to Your Data

> **Zero friction data analysis.** Upload a CSV. Ask questions out loud. Get insights with both visuals and a voice reading them to you.

Tired of spreadsheets? VoxQuery turns natural speech into structured intelligence using AI-powered hybrid search and real-time voice I/O. From question to answer in under 3 seconds.

**[➜ Try the Live Demo](https://voxquery.streamlit.app/)**

---

## What Makes VoxQuery Different

Unlike traditional BI tools that chain you to dashboards, VoxQuery embraces the way humans naturally communicate: **by voice**. Pair that with a hybrid search engine that actually understands both semantic intent *and* precise categorical values—and you've got something that actually works.

### ⚡ The Core Features

- **Voice-First Interface** – STT + TTS with ambient noise handling. Talk, don't type.
- **Hybrid Search (RAG+)** – Dual-stream retrieval fusing semantic embeddings + keyword matching for high-precision context.
- **Generative Analysis** – Google Gemini 1.5 Flash powers real-time analytical insights.
- **MCP Ready** – Protocol-driven backend designed for integration with AI IDEs (Cursor, Windsurf, etc.).
- **Dark Mode UI** – Minimalist Streamlit interface optimized for speed and clarity.

---

## 🏗️ Architecture

```
Voice Input
   ↓ (STT)
Query Processing
   ↓
Hybrid Search Engine
  ├─ FAISS Vector Store (semantic)
  └─ Keyword Retrieval (precision)
   ↓ (ranked fusion)
Gemini 1.5 Flash
   ↓ (analytical generation)
Text-to-Speech
   ↓
Voice Output + Dashboard Visuals
```

**Design Philosophy**: Decoupled and modular. The voice orchestration layer and data processing engine operate independently, enabling easy scaling and swapping of components.

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit + Custom CSS (Dark Aesthetic) |
| **AI Engine** | Google Gemini API 1.5 Flash |
| **Vector DB** | FAISS (Facebook AI Similarity Search) |
| **Embeddings** | Sentence-Transformers (all-MiniLM-L6-v2) |
| **Voice Ops** | SpeechRecognition (STT) + Pyttsx3 (TTS) |
| **Data Processing** | Pandas |

---

## 🚀 Get Started

### Prerequisites
- Python 3.10+
- Google Gemini API key
- Microphone (for voice input)

### Installation

```bash
# Clone the repo
git clone https://github.com/mysterious-egg/VoxQuery.git
cd VoxQuery

# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_key_here
```

### Launch

```bash
streamlit run VoiceAssistant/app.py
```

Then open your browser to `http://localhost:8501` and start talking.

---

## 📁 Project Structure

```
VoxQuery/
├── VoiceAssistant/
│   ├── app.py              # Streamlit main app
│   ├── speech_utils.py     # STT utilities
│   └── tts.py              # Text-to-speech
├── AskQuery/
│   ├── rag_engine.py       # Hybrid search + generation
│   ├── data_handler.py     # CSV processing
│   └── vector_store.py     # FAISS integration
├── requirements.txt
└── README.md
```

---

## 💡 Key Innovations

### 1. Hybrid Retrieval Pipeline
Standard RAG only uses vector embeddings. VoxQuery combines:
- **Semantic Search**: Understands user intent and nuance
- **Keyword Matching**: Catches exact IDs, names, categorical values
- **Ranked Fusion**: Merges results into a unified high-context prompt

Result? Better answers with fewer hallucinations.

### 2. Protocol-Driven Design
Built with Model Context Protocol in mind. The backend exposes analysis tools as first-class primitives, ready for integration with modern AI development environments.

### 3. Real-Time Multimodal Loop
- **Adaptive STT**: Noise cancellation, robust recognition
- **Natural TTS**: Polished audio synthesis
- **Snappy UX**: 300ms response target, dark mode for low-light analysis marathons

---

## 🎯 Use Cases

- **Instant Data Exploration** – Ask your CSV questions without writing SQL
- **Accessibility** – Voice-first for visually impaired users or hands-free scenarios
- **Meeting Insights** – Share data findings verbally in real-time
- **Quick Analysis** – Perfect for time-sensitive data moments
- **Educational Tool** – Learn data analysis through conversation

 create a branch
git checkout -b feature/your-idea

# Make your magic
# ...

# Push and open a PR
git push origin feature/your-idea
```

---

