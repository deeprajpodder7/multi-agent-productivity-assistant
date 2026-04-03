from google import genai
import os
from dotenv import load_dotenv
from agent_task import task_agent
from agent_calendar import calendar_agent
from agent_notes import notes_agent

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class CoordinatorAgent:
    def run(self, user_input: str):

        prompt = f"""
        You are an AI assistant that extracts multiple actions from user input.

        Break the input into a list of actions.

        Return ONLY valid JSON (no explanation, no markdown):

        [
            {{
                "type": "task/calendar/note",
                "title": "...",
                "datetime": "...",
                "content": "..."
            }}
        ]

        Rules:
        - If it's a task → fill "title"
        - If it's a calendar event → fill "title" and "datetime"
        - If it's a note → fill "content"
        - Return a list even if only one item

        Input: {user_input}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        import json

        try:
            text = response.text.strip()

            # 🔥 Clean Gemini output
            text = text.replace("```json", "").replace("```", "").strip()

            print("DEBUG Gemini Output:", text)

            data_list = json.loads(text)

        except Exception as e:
            return f"Error parsing AI response: {str(e)}"

        results = []

        for data in data_list:

            action_type = data.get("type", "")

            if action_type == "task":
                results.append(
                    task_agent.create_task(
                        data.get("title", "Untitled Task")
                    )
                )

            elif action_type == "calendar":
                results.append(
                    calendar_agent.create_event(
                        data.get("title", "Event"),
                        data.get("datetime", "unknown time")
                    )
                )

            elif action_type == "note":
                results.append(
                    notes_agent.save_note(
                        data.get("content", "")
                    )
                )

        return results


agent = CoordinatorAgent()