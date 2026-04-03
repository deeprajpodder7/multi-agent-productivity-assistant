from tools import create_event_tool

class CalendarAgent:
    def create_event(self, title: str, datetime: str):
        return create_event_tool(title, datetime)

calendar_agent = CalendarAgent()