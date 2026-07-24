from app.ai.hybrid_search import hybrid_search
from app.ai.retriever import retrieve_context

from app.tools.base_tool import BaseTool


class DocumentSearchTool(BaseTool):

    name = "document_search"

    description = (
        "Searches the indexed knowledge base "
        "using the RAG retrieval pipeline."
    )

    def execute(
        self,
        query: str,
        top_k: int = 5
    ):

        try:

            context = retrieve_context(
                query,
                top_k=top_k
            )

            results = hybrid_search(
                query,
                top_k=top_k
            )

            documents = []

            for result in results:

                metadata = result.get("metadata") or {}

                documents.append({

                    "title": metadata.get("title"),

                    "source": metadata.get("source"),

                    "score": round(
                        result.get("final_score", 0),
                        3
                    )

                })

            return {

                "success": True,

                "query": query,

                "documents_found": len(documents),

                "documents": documents,

                "context": context

            }

        except Exception as e:

            return {

                "success": False,

                "query": query,

                "error": str(e)

            }