# Rephrasing Tool: AI-Powered Text Paraphraser

Effortlessly rephrase and paraphrase text with this AI-driven tool. Designed for writers, students, and professionals, it ensures your text is clear, concise, and tailored to your desired tone or style. Whether you're creating content, improving clarity, or avoiding plagiarism, this tool has you covered.

---

## Features

- **AI-Powered Paraphrasing**: Uses advanced natural language processing (NLP) models to rephrase sentences while preserving their original meaning.
- **Customizable Output**: Allows users to adjust the tone (e.g., formal, casual) or style of the paraphrased text for different contexts.
- **Interactive Interface**: User-friendly web application for entering and processing text with real-time results.
- **Multi-Language Support**: Supports paraphrasing in multiple languages for global usability.
- **Deployment Ready**: Configured for easy deployment on cloud platforms like Heroku, enabling accessibility from anywhere.

---

## Tools and Libraries

This project is built with:
- **Python**: Core programming language.
- **Hugging Face Transformers**: For leveraging pre-trained NLP models like GPT and T5.
- **Flask**: To develop a lightweight, interactive web application.
- **Pandas & NumPy**: For handling text preprocessing and optimization.
- **Streamlit**: Optional interactive interface for quick deployment.
- **Heroku**: For scalable cloud deployment.

---

## Dataset

The tool can work with any textual dataset provided by the user. For training and fine-tuning (if required), public datasets such as Quora Question Pairs and ParaNMT can be utilized.

### Dataset Example:
Original Sentence:  
*"AI is revolutionizing industries across the globe."*  
Paraphrased Sentence:  
*"Artificial intelligence is transforming businesses worldwide."*

---

## Challenges Addressed

- **Text Clarity**: Enhances readability by simplifying complex sentences.
- **Avoiding Redundancy**: Rephrases redundant text into concise formats.
- **Contextual Accuracy**: Preserves the meaning of sentences during rephrasing, ensuring contextual relevance.
- **Customization Needs**: Provides tailored outputs for academic, professional, or casual contexts.

---

## Results

- **Enhanced Readability**: Simplified sentences without losing meaning.
- **Tone Adaptability**: Successfully adjusts tone and style based on user preference.
- **Multilingual Capability**: Supports rephrasing in multiple languages (depending on the pre-trained model).

---

## Installation

Follow these steps to set up and run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/teckyonAI/AI_PDF_Analyzer.git

   
2. Navigate to the project directory:
   ```bash
   cd AI_PDF_Analyzer

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up your OpenAI API key:
   - Create a `.env` file in the root directory.
   - Add the following line to the `.env` file:
    ```bash
    OPENAI_API_KEY=your_openai_api_key

6. Run the application:
    ```bash
    python app.py

---

## Usage

1. Upload a PDF document through the application interface.
2. Select the desired operation (e.g., summarization, extraction, or insights).
3. View the results directly in the app or download them for further use.

---

## Deployment

This project is configured for deployment on platforms like Heroku. 

---

## Contribution

Contributions are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of the changes.

