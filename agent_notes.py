from tools import save_note_tool

class NotesAgent:
    def save_note(self, content: str):
        return save_note_tool(content)

notes_agent = NotesAgent()