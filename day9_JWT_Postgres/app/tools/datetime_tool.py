from datetime import datetime, timezone

from app.tools.base_tool import BaseTool


class DateTimeTool(BaseTool):

    name = "datetime"

    description = "Provides current date and time information."

    def execute(
        self,
        action: str = "datetime"
    ):

        now = datetime.now()

        utc_now = datetime.now(timezone.utc)

        action = action.lower()

        if action == "date":

            return {
                "success": True,
                "action": action,
                "result": now.strftime("%Y-%m-%d")
            }

        elif action == "time":

            return {
                "success": True,
                "action": action,
                "result": now.strftime("%H:%M:%S")
            }

        elif action == "datetime":

            return {
                "success": True,
                "action": action,
                "result": now.strftime("%Y-%m-%d %H:%M:%S")
            }

        elif action == "utc":

            return {
                "success": True,
                "action": action,
                "result": utc_now.strftime("%Y-%m-%d %H:%M:%S UTC")
            }

        elif action == "day":

            return {
                "success": True,
                "action": action,
                "result": now.strftime("%A")
            }

        elif action == "iso":

            return {
                "success": True,
                "action": action,
                "result": now.isoformat()
            }

        elif action == "timestamp":

            return {
                "success": True,
                "action": action,
                "result": int(now.timestamp())
            }

        else:

            return {
                "success": False,
                "error": f"Unknown action: {action}"
            }