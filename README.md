# AI Video Generation Pipeline

This project implements a fully automated AI video generation pipeline using Python and free-tier AI tools.

## Pipeline Flow
Input Topic → Script (Groq API) → Voice (Edge TTS) → Images (Pexels API) → Final MP4 (MoviePy)

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Add API keys in .env file

3. Run:
   python main.py

The system generates a YouTube-ready video automatically.
