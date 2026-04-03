from tools import create_task_tool

class TaskAgent:
    def create_task(self, task: str):
        return create_task_tool(task)

task_agent = TaskAgent()