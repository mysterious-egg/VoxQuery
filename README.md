# VoxQuery - Voice-Based Data Query Agent

A sophisticated voice-enabled data analysis and query system that combines speech recognition, retrieval-augmented generation (RAG), and text-to-speech capabilities. Query your CSV data using natural voice commands and receive AI-powered insights spoken back to you.

---

## 🎯 Overview

**VoxQuery** is an intelligent agent that bridges voice input with data analysis. It enables users to:
- Upload and analyze CSV files using voice queries
- Retrieve relevant data using hybrid semantic and keyword search
- Generate AI-powered insights using Google's Generative AI
- Hear responses read aloud using text-to-speech
- Interact with data through a user-friendly Streamlit web interface

---

## ✨ Key Features

### 1. **Voice Input Processing**
- Real-time microphone capture using `speech_recognition`
- Automatic ambient noise adjustment
- Configurable pause and phrase detection thresholds
- Robust error handling for audio input

### 2. **CSV Data Processing**
- Seamless CSV file upload and parsing
- Automatic data shape and dtype detection
- Missing value analysis
- Data preview and validation

### 3. **Hybrid Search (Vector + Keyword)**
- FAISS-based vector search for semantic similarity
- Keyword-based retrieval for exact matches
- Dual retrieval system combining both approaches
- Top-K result filtering

### 4. **RAG Engine (Retrieval-Augmented Generation)**
- Google Generative AI integration
- Context-aware response generation
- Dataframe analysis and insights
- Dynamic prompt generation

### 5. **Voice Output**
- Text-to-speech synthesis using `pyttsx3`
- Configurable speech rate and volume
- Automatic error handling

### 6. **Web Interface**
- Built with Streamlit for rapid deployment
- Responsive, intuitive UI
- Session state management
- Real-time feedback

---

## 📁 Project Structure

```
SimpleAgent/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
├── venv/                     # Virtual environment
│
├── AskQuery/
│   ├── __init__.py          # Package initialization
│   ├── data_handler.py      # CSV processing and data validation
│   ├── rag_engine.py        # RAG logic & AI response generation
│   ├── vector_store.py      # Vector embeddings & hybrid search
│   └── __pycache__/         # Compiled Python files
│
└── VoiceAssistant/
    ├── app.py               # Main Streamlit application
    ├── speech_utils.py      # Speech recognition utilities
    ├── tts.py               # Text-to-speech synthesis
    └── __pycache__/         # Compiled Python files
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8+**
- **Microphone** (for voice input)
- **Google Generative AI API Key**

### Step 1: Clone/Navigate to Project
```bash
cd c:\Users\maja0\OneDrive\Desktop\SimpleAgent
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```powershell
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& venv\Scripts\Activate.ps1)
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_generative_ai_api_key_here
```

**How to get a Google API Key:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Get API Key"
3. Create a new API key
4. Copy and paste into `.env` file

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest | Web interface framework |
| `pandas` | Latest | Data manipulation & analysis |
| `faiss-cpu` | Latest | Vector similarity search |
| `sentence-transformers` | Latest | Text embedding generation |
| `google-generativeai` | Latest | AI model access |
| `speech-recognition` | Latest | Audio-to-text conversion |
| `pyttsx3` | Latest | Text-to-speech synthesis |
| `python-dotenv` | Latest | Environment variable management |
| `numpy` | Latest | Numerical computations |
| `altair` | 6.1.0 | Data visualization |
| `anyio` | 4.13.0 | Async I/O support |
| `attrs` | 26.1.0 | Class utilities |

---

## 🎮 Usage

### Running the Application

**From project root:**
```bash
streamlit run VoiceAssistant/app.py
```

**Expected output:**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### Using VoxQuery

1. **Open the application** in your browser (typically `http://localhost:8501`)
2. **Upload a CSV file** using the file uploader
3. **Review data preview** to verify upload
4. **Click "Capture Voice Input"** button to record a query
5. **Speak your question** (e.g., "What are the top sales by region?")
6. **View AI-generated response** displayed on screen
7. **Hear the response** spoken aloud automatically

### Example Queries
- "What products have the highest sales?"
- "Show me customers from New York"
- "Analyze the revenue trends"
- "How many records are in this dataset?"
- "What is the average value in this column?"

---

## 🔧 Configuration & Customization

### Speech Recognition Settings
Located in `VoiceAssistant/speech_utils.py`:

```python
recognizer.pause_threshold = 1.5          # Pause duration before stop (seconds)
recognizer.phrase_threshold = 0.3         # Minimum speaking duration
recognizer.non_speaking_duration = 0.8    # Audio before speech begins
```

### Text-to-Speech Settings
Located in `VoiceAssistant/tts.py`:

```python
engine.setProperty("rate", 170)           # Speech speed (100-200 typical)
engine.setProperty("volume", 1.0)         # Volume level (0.0-1.0)
```

### Vector Store Configuration
Located in `AskQuery/vector_store.py`:

```python
model = SentenceTransformer("all-MiniLM-L6-v2")  # Embedding model
top_k = 20                                        # Number of results to retrieve
```

### Streamlit App Configuration
Located in `VoiceAssistant/app.py`:

```python
st.set_page_config(
    page_title="VoxQuery",
    page_icon="🎙️",
    layout="wide"
)
```

---

## 📚 Component Documentation

### AskQuery Module

#### **data_handler.py**
Handles CSV file processing and data validation.

```python
from AskQuery.data_handler import process_csv

result = process_csv(uploaded_file)
# Returns:
# {
#     "dataframe": pd.DataFrame,
#     "columns": list,
#     "shape": tuple,
#     "preview": pd.DataFrame,
#     "dtypes": dict,
#     "missing": dict,
#     "error": str (if failed)
# }
```

**Key Functions:**
- `process_csv(uploaded_file)` - Processes uploaded CSV and returns data dict

---

#### **vector_store.py**
Creates and manages vector embeddings for semantic search.

**Class: `VectorStore`**

```python
from AskQuery.vector_store import VectorStore

vector_store = VectorStore()
vector_store.build_index(df)
results = vector_store.search(query, top_k=20)
```

**Methods:**
- `__init__()` - Initialize with embedding model
- `create_chunks(df)` - Convert dataframe rows to text chunks
- `build_index(df)` - Create FAISS vector index from dataframe
- `search(query, top_k)` - Hybrid search combining keyword + semantic

**Hybrid Search Algorithm:**
1. **Keyword Search**: Exact word matches in chunks
2. **Vector Search**: Semantic similarity using embeddings
3. **Merge**: Combine and rank results

---

#### **rag_engine.py**
Orchestrates RAG (Retrieval-Augmented Generation) pipeline.

```python
from AskQuery import rag_engine

response = rag_engine.generate_analysis(dataframe, user_query)
```

**Key Functions:**
- `generate_analysis(df, user_query)` - Main RAG pipeline
  - Retrieves relevant data chunks
  - Constructs context-aware prompt
  - Calls Google Generative AI
  - Returns formatted response

**Process Flow:**
1. Validate API key
2. Retrieve relevant chunks via vector_store
3. Build prompt with context
4. Call Google Generative AI model
5. Return generated insights

---

### VoiceAssistant Module

#### **speech_utils.py**
Captures and converts voice to text.

```python
from VoiceAssistant.speech_utils import recognize_speech

result = recognize_speech()
# Returns:
# {
#     "success": bool,
#     "text": "recognized text",
#     "error": "error message"
# }
```

**Key Functions:**
- `recognize_speech()` - Capture microphone input and convert to text

**Features:**
- Automatic ambient noise adjustment
- Configurable pause detection
- Error handling for mic issues

---

#### **tts.py**
Converts text to spoken audio.

```python
from VoiceAssistant.tts import speak

speak("Hello, this is the response")
```

**Key Functions:**
- `speak(text)` - Convert text to speech and play audio

**Features:**
- Fresh engine initialization per call
- Configurable speech rate and volume
- Error handling for TTS failures

---

#### **app.py**
Main Streamlit application - the user interface.

**Page Configuration:**
- Title: "VoxQuery"
- Icon: 🎙️
- Layout: Wide
- Sidebar: Collapsed

**Session State Variables:**
- `query` - Current user query
- `response` - AI-generated response

**Main Workflow:**
1. Page setup and configuration
2. Load CSS styling
3. Header and navigation
4. File upload section
5. Data preview section
6. Voice input section
7. Query processing
8. Response display
9. Text-to-speech output

---

## 🔌 API Reference

### Google Generative AI Integration

**Model Used:** `gemini-pro` (default)

```python
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(prompt)
```

**Authentication:**
- Requires `GOOGLE_API_KEY` in `.env`
- API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

**Rate Limits:**
- Check Google's documentation for current limits
- Free tier: Generous for development

---

## 🐛 Troubleshooting

### Issue: Microphone Not Detected
**Solution:**
```bash
# Check if speech_recognition can find microphone
python -c "import speech_recognition as sr; sr.Microphone.list_microphone_indexes()"
```

### Issue: "GOOGLE_API_KEY missing"
**Solution:**
1. Verify `.env` file exists in project root
2. Check format: `GOOGLE_API_KEY=your_key_here` (no quotes)
3. Restart Streamlit after updating `.env`

### Issue: Vector Search Returns No Results
**Solution:**
- Ensure CSV is uploaded before querying
- Check that chunks were created: `vector_store.text_chunks`
- Verify FAISS index built: `vector_store.index`

### Issue: Speech Recognition Times Out
**Solution:**
1. Check microphone is working and unmuted
2. Speak clearly and distinctly
3. Adjust `pause_threshold` in `speech_utils.py` to lower value

### Issue: Text-to-Speech Not Working
**Solution:**
1. Windows: Install [SAPI 5](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ee431674(v=vs.85))
2. macOS: Check system speech settings
3. Test: `python -c "from pyttsx3 import init; init().say('test'); init().runAndWait()"`

### Issue: Slow Embedding Generation
**Solution:**
1. Use GPU: Install `faiss-gpu` instead of `faiss-cpu`
2. Reduce `top_k` parameter in vector search
3. Use smaller embedding model (e.g., `all-MiniLM-L6-v2`)

### Issue: Streamlit Port Already in Use
**Solution:**
```bash
# Run on different port
streamlit run VoiceAssistant/app.py --server.port 8502
```

---

## 🌐 System Requirements

### Hardware
- **Processor:** Multi-core (4+ cores recommended)
- **RAM:** 4GB minimum (8GB+ recommended)
- **Storage:** 2GB for dependencies
- **Microphone:** Any standard USB or built-in mic

### Software
- **OS:** Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python:** 3.8, 3.9, 3.10, or 3.11
- **Internet:** Required for API calls

### Network
- Stable internet connection for Google API
- Optional: Local network access (if serving to other devices)

---

## 📊 Data Processing Pipeline

```
CSV Upload
    ↓
Data Validation (process_csv)
    ↓
Data Preview & Analysis
    ↓
Text Chunks Generation
    ↓
Vector Embeddings (SentenceTransformer)
    ↓
FAISS Index Creation
    ↓
User Query (Voice Input)
    ↓
Hybrid Search (Keyword + Vector)
    ↓
Context Preparation
    ↓
Google Generative AI
    ↓
Response Generation
    ↓
Display & Text-to-Speech Output
```

---

## 🔐 Security Considerations

1. **API Keys:** Never commit `.env` file to version control
   ```bash
   # Add to .gitignore
   .env
   venv/
   __pycache__/
   ```

2. **Data Privacy:** CSV data is processed locally
   - Chunks used for search only
   - Not stored permanently
   - Consider sensitivity when uploading

3. **Rate Limiting:** Implement usage tracking for production
   - Monitor API calls
   - Set quotas per user
   - Cache repeated queries

---

## 🚦 Development & Debugging

### Enable Debug Logging
Edit `VoiceAssistant/app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Vector Store Contents
```python
print("Chunks:", vector_store.text_chunks)
print("Index size:", vector_store.index.ntotal)
print("Index dimension:", vector_store.index.d)
```

### Test RAG Pipeline Directly
```bash
python -c "
from AskQuery.rag_engine import generate_analysis
import pandas as pd

df = pd.read_csv('test.csv')
response = generate_analysis(df, 'test query')
print(response)
"
```

---

## 📈 Performance Optimization

### For Large Datasets
1. **Batch Processing:** Process chunks in batches
2. **Dimension Reduction:** Use simpler embedding model
3. **Caching:** Cache embeddings between sessions
4. **Indexing:** Use FAISS GPU version

### Code Optimization Tips
```python
# Pre-compute embeddings
embeddings_cache = {}

# Limit search scope
top_k = 10  # Reduce from 20

# Use async operations
# Consider using concurrent.futures
```

---

## 🤝 Contributing

### Code Style
- Follow PEP 8 guidelines
- Add docstrings to functions
- Use type hints where possible

### Testing
1. Test with various CSV formats
2. Test with different query types
3. Test edge cases (empty files, special characters)

### Reporting Issues
Include:
- Python version
- OS and version
- Full error message
- Steps to reproduce

---

## 📝 License

This project is provided as-is for educational and development purposes.

---

## 📞 Support & Contact

For issues or questions:
1. Check the **Troubleshooting** section
2. Review component documentation
3. Check console output and error messages
4. Verify environment setup

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | May 2026 | Initial release |
| | | Voice recognition integration |
| | | RAG engine implementation |
| | | Streamlit web interface |

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Google Generative AI](https://ai.google.dev/)
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)

---

## ✅ Checklist for First Run

- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with `GOOGLE_API_KEY`
- [ ] Microphone tested and working
- [ ] Streamlit running without errors
- [ ] CSV file uploaded successfully
- [ ] Voice input recognized correctly
- [ ] AI response generated
- [ ] Text-to-speech audio playing

---

**Happy querying! 🎙️📊**
