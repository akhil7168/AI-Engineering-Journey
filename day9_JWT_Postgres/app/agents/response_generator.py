from app.agents.agent_state import AgentState


class ResponseGenerator:
    """
    Combines outputs from multiple tools into a
    single natural language response.
    """

    def generate(
        self,
        state: AgentState
    ) -> str:

        sections = []

        # ---------------- Calculator ----------------

        if "calculator" in state.tool_outputs:

            output = state.tool_outputs["calculator"]

            if isinstance(output, dict):

                if output.get("success"):

                    result = output.get("output", {})

                    if isinstance(result, dict):

                        value = result.get("result", result)

                    else:

                        value = result

                    sections.append(
                        f"Calculation Result:\n{value}"
                    )

                else:

                    sections.append(
                        "Calculation failed."
                    )

        # ---------------- DateTime ----------------

        if "datetime" in state.tool_outputs:

            output = state.tool_outputs["datetime"]

            if isinstance(output, dict):

                if output.get("success"):

                    value = output.get("output")

                    sections.append(
                        f"Date & Time:\n{value}"
                    )

                else:

                    sections.append(
                        "Unable to retrieve date/time."
                    )

        # ---------------- Document Search ----------------

        if "document_search" in state.tool_outputs:

            output = state.tool_outputs["document_search"]

            if isinstance(output, dict):

                if output.get("success"):

                    value = output.get("output")

                    sections.append(
                        f"Knowledge Base:\n{value}"
                    )

                else:

                    sections.append(
                        "No relevant documents found."
                    )

        # ---------------- System Info ----------------

        if "system_info" in state.tool_outputs:

            output = state.tool_outputs["system_info"]

            if isinstance(output, dict):

                if output.get("success"):

                    value = output.get("output")

                    sections.append(
                        f"System Information:\n{value}"
                    )

                else:

                    sections.append(
                        "Unable to retrieve system information."
                    )

        # ---------------- Errors ----------------

        if state.errors:

            sections.append(

                "Errors:\n" +

                "\n".join(state.errors)

            )

        # ---------------- Empty ----------------

        if not sections:

            response = "No response generated."

        else:

            response = "\n\n".join(sections)

        state.set_response(response)

        return response

    def print_response(
        self,
        state: AgentState
    ):

        print()

        print("=" * 80)

        print("FINAL RESPONSE")

        print("=" * 80)

        print()

        print(state.final_response)

        print()

    def generate_markdown(
        self,
        state: AgentState
    ) -> str:

        response = self.generate(state)

        return f"""# AI Response

{response}
"""