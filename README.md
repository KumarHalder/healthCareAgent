# HealthBot - Advanced Patient Education System

## Overview

HealthBot is an intelligent patient education system designed to provide reliable, comprehensible health information to patients. The system uses a structured 7-phase workflow to ensure effective learning and comprehension assessment.

## Features

- **Interactive Health Education**: Provides patient-friendly explanations of medical topics
- **Real-time Information Retrieval**: Searches current medical databases for up-to-date information
- **Comprehension Assessment**: Tests patient understanding with relevant quiz questions
- **Multi-source Verification**: Aggregates information from multiple reliable medical sources
- **Session Management**: Allows patients to learn about multiple topics in one session

## System Architecture

The HealthBot system implements a 7-phase workflow:

1. **Topic Inquiry** - Collects patient's health topic of interest
2. **Information Gathering** - Searches medical databases for current information
3. **Information Processing** - Analyzes and structures the retrieved content
4. **Information Presentation** - Delivers patient-friendly explanations
5. **Comprehension Assessment** - Tests understanding with quiz questions
6. **Response Evaluation** - Provides detailed feedback on patient responses
7. **Session Management** - Manages session continuation or completion

## Technical Stack

- **Python 3.8+**
- **LangChain Framework** - For workflow orchestration
- **LangGraph** - State machine implementation
- **OpenAI API** - Natural language processing
- **Tavily Search API** - Medical information retrieval
- **Jupyter Notebook** - Interactive development environment

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd healthCareAgent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp config.env.example config.env
   # Edit config.env with your API keys
   ```

## Configuration

Create a `config.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://openai.vocareum.com/v1  # If using Vocareum
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the HealthBot notebook**
   ```
   healthbot_prototype.ipynb
   ```

3. **Run all cells** to initialize the system

4. **Execute the final cell** to start an interactive session

## Project Structure

```
healthCareAgent/
├── healthbot_prototype.ipynb    # Main implementation notebook
├── requirements.txt             # Python dependencies
├── config.env                  # Environment configuration
├── PROJECT_REQUIREMENTS.md     # Project specifications
├── README.md                   # This file
└── .venv/                      # Virtual environment (created after setup)
```

## API Requirements

### OpenAI API
- **Purpose**: Natural language processing and content generation
- **Configuration**: Supports standard OpenAI endpoints and Vocareum integration
- **Usage**: Content summarization, quiz generation, response evaluation

### Tavily Search API
- **Purpose**: Real-time medical information retrieval
- **Configuration**: Medical-focused search parameters
- **Usage**: Gathering current, reliable health information from trusted sources

## Workflow Details

### Phase 1: Topic Inquiry
Collects the patient's health topic of interest through an interactive interface.

### Phase 2: Information Gathering
Searches multiple medical databases and trusted health sources for current information on the specified topic.

### Phase 3: Information Processing
Analyzes retrieved content, removes duplicates, and structures information for patient consumption.

### Phase 4: Information Presentation
Converts medical information into patient-friendly language while maintaining accuracy and completeness.

### Phase 5: Comprehension Assessment
Generates relevant quiz questions to test patient understanding of the presented material.

### Phase 6: Response Evaluation
Evaluates patient responses and provides detailed feedback with additional explanations when needed.

### Phase 7: Session Management
Manages session flow, allowing patients to learn about additional topics or conclude their session.

## Safety and Compliance

- **Educational Purpose**: All information provided is for educational purposes only
- **Medical Disclaimer**: Users are advised to consult healthcare professionals for medical advice
- **Source Attribution**: All information includes citations to original medical sources
- **Privacy**: No personal health information is stored or transmitted

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Quality
The project follows Python best practices:
- Type hints for better code documentation
- Error handling and graceful degradation
- Modular design with clear separation of concerns
- Comprehensive logging and status reporting

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For technical support or questions about the HealthBot system:

- **Documentation**: Refer to `PROJECT_REQUIREMENTS.md` for detailed specifications
- **Issues**: Report bugs or request features through the issue tracker
- **Contact**: Reach out to the development team for additional support

## Acknowledgments

- Medical content sourced from trusted healthcare organizations
- Built with LangChain and LangGraph frameworks
- Powered by OpenAI and Tavily APIs for reliable information processing

---

**Disclaimer**: This system is designed for educational purposes only. Always consult qualified healthcare professionals for medical advice, diagnosis, or treatment decisions.
