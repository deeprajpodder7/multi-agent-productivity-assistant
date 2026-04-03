# Multi-Agent Productivity Assistant

A multi-agent AI system that manages tasks, schedules, and notes using natural language.

## Features
- Multi-agent architecture (Coordinator + sub-agents)
- Multi-step workflow execution
- Tool-based design (MCP-style)
- Real-time database interaction
- Cloud Run deployment

## Architecture
User → FastAPI → Coordinator → Sub-Agents → Tools → Database

## API Endpoints
- POST /run
- GET /tasks
- GET /events
- GET /notes

## Tech Stack
- Google Gemini
- FastAPI
- SQLAlchemy
- Cloud Run
