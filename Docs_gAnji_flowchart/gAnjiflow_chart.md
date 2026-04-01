# gAnji Project Flowchart

```mermaid
flowchart TD

A[Forebet Predictions] --> B[Python Scraper]
C[Betting Odds Sites] --> B
D[Polymarket] --> B

B --> E[Data Cleaning & Parsing]

E --> F[(PostgreSQL Database)]

F --> G[Prediction Engine]
F --> H[Streamlit Dashboard]

G --> I[Betting Signal Generator]

I --> J[Gold Picks]
I --> K[Silver Picks]
I --> L[Bronze Picks]

J --> M[Telegram Bot]
K --> M
L --> M

H --> N[LLM Analysis Layer]

N --> M
```

## Overview
This flowchart illustrates the gAnji betting prediction system architecture, from data collection through signal distribution via Telegram.

## Components
- **Data Sources**: Aggregates predictions from Forebet, odds sites, and Polymarket
- **Processing**: Python scraper handles data extraction and cleaning
- **Storage**: PostgreSQL maintains historical and real-time data
- **Analysis**: Prediction engine generates signals; LLM layer provides insights
- **Output**: Three-tier pick system (Gold/Silver/Bronze) distributed via Telegram and dashboard
