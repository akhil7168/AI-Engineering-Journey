from datetime import datetime


class PlannerMetadata:
    """
    Stores planner execution metadata.
    """

    @staticmethod
    def update(
        state,
        planner_type: str,
        planning_time: float,
        valid_tools: list,
        invalid_tools: list
    ):

        state.add_metadata(
            "planner_type",
            planner_type
        )

        state.add_metadata(
            "planning_time_ms",
            round(planning_time * 1000, 2)
        )

        state.add_metadata(
            "tool_count",
            len(valid_tools)
        )

        state.add_metadata(
            "valid_tools",
            valid_tools
        )

        state.add_metadata(
            "invalid_tools",
            invalid_tools
        )

        state.add_metadata(
            "timestamp",
            datetime.now().isoformat()
        )