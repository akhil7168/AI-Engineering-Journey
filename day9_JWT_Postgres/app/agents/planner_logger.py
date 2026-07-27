import json
import logging
import os


class PlannerLogger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        self.logger = logging.getLogger("planner")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            handler = logging.FileHandler(
                "logs/planner.log",
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s %(message)s"
            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

    def log(self, state):

        data = {

            "query": state.query,

            "planner_type":
                state.metadata.get("planner_type"),

            "planning_time_ms":
                state.metadata.get("planning_time_ms"),

            "tool_count":
                state.metadata.get("tool_count"),

            "planned_tools":
                state.planned_tools,

            "invalid_tools":
                state.metadata.get(
                    "invalid_tools",
                    []
                ),

            "status":
                state.status,

            "errors":
                state.errors

        }

        self.logger.info(

            json.dumps(
                data,
                ensure_ascii=False
            )

        )