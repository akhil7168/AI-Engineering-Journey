import platform

import psutil

from app.tools.base_tool import BaseTool


class SystemInfoTool(BaseTool):

    name = "system_info"

    description = "Returns system information."

    def execute(self):

        return {

            "platform": platform.system(),

            "cpu_percent": psutil.cpu_percent(),

            "memory_percent": psutil.virtual_memory().percent
        }