# Notary - AI transcription and note generation 

## Project Proposal

---

### 1. Project Description

#### Problem Statement

In academic, corporate, and creative environments, individuals regularly rely on audio content—meetings, lectures, brainstorming sessions, interviews—but often lack efficient means to convert spoken information into organized written notes. Manual transcription is tedious, and standard voice-to-text software does not structure content or highlight key takeaways.

#### Objective

This project proposes the development of an **AI-powered assistant** capable of capturing audio input, transcribing speech, and intelligently summarizing it into structured, human-readable notes. The assistant will combine open-source speech recognition and language models to deliver a flexible, lightweight, and accurate note-generation pipeline.

#### Key Features

- **Audio Input Interface**: Users can record audio in real-time or upload pre-recorded files.
- **Speech-to-Text Transcription**: Integration with OpenAI's open-source Whisper model for high-quality transcription.
- **Intelligent Summarization**: Notes are generated using summarization models such as GPT-3.5/4 or open-source equivalents (e.g., Mistral).
- **User Interface**: Command-line interface or web-based UI (e.g., Streamlit or Gradio) for ease of use.
- **Export Options**: Notes can be saved or exported a text file format.

#### Innovation and Practical Impact

This tool stands out by bridging the gap between transcription and actionable note-taking using both open and proprietary language models. It offers:

- A modular, privacy-friendly alternative to cloud-based transcription apps.
- Support for local and offline execution using open-source LLMs.
- Practical utility for students, educators, researchers, and professionals.

---

### 2. Resources to Use

#### Open-Source Repositories

- **Whisper by OpenAI**: [https://github.com/openai/whisper](https://github.com/openai/whisper)
- **ChatGPT 4o by OpenAI** [https://chatgpt.com/](https://chatgpt.com/)
- **Gradio (Web Interface)**: [https://github.com/gradio-app/gradio](https://github.com/gradio-app/gradio)

#### Data Sources

- Custom-collected audio files (e.g., classroom recordings, meeting simulations)

#### Relevant Coursework and Lab Materials

- Advanced utilization of GPT models.
- Labs covering RESTful API integrations and CLI tool development.
- ChatGPT API integration.

---

### 3. Deliverables and Timeline

#### Final Deliverables

- **Functional Prototype**:
  - Audio input module
  - Whisper-based transcription engine
  - Summarization pipeline
- **Demonstration**:
  - Live walkthrough using a CLI or web-based app
- **Documentation**:
  - User wiki with setup instructions
- **Evaluation Metrics**:
  - Transcription quality assessment (manual or automated)
  - Summarization quality metrics (e.g., ROUGE or human evaluation)
  - Resource usage (e.g., inference time, memory footprint)

#### Project Timeline

| Week       | Milestone                                                     |
|------------|---------------------------------------------------------------|
| Week 1     | Initial project setup and Whisper integration                 |
| Week 2     | Summarization logic and integration with GPT or open-source LLM |
| Week 3     | UI development (CLI or web-based) and file export features    |
| Week 4     | Performance testing and user feedback collection              |
| Final Week | Final polishing, presentation preparation, and code documentation |

