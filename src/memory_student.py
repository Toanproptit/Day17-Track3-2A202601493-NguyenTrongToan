from __future__ import annotations

import re
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search

class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(
            thread_id=thread_id
        )
        context_block = getattr(user_context, "context", "") or ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        # Put compact, provenance-bearing facts first so the long-term budget
        # does not trim them away behind a verbose Context Block.
        return join_nonempty([fact_text, context_block], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )

        return render_graph_search(
            results,
            episode_char_cap=180,
        )

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        queries = [cap_query(query)]

        # A long natural-language question can dilute the important domain
        # terms. Add a compact lexical variant while keeping the original
        # query for normal semantic ranking.
        hint_words = {
            "async",
            "backend",
            "budget",
            "connection",
            "context",
            "delete",
            "deletion",
            "http",
            "incident",
            "memory",
            "payment",
            "playbook",
            "pooling",
            "privacy",
            "retry",
            "token",
        }
        salient = [
            word
            for word in re.findall(r"[a-z0-9-]+", query.casefold())
            if word in hint_words
        ]
        compact_query = " ".join(dict.fromkeys(salient))
        if compact_query and compact_query != queries[0]:
            queries.insert(0, compact_query)

        if len(query) > 400:
            tail_query = cap_query(query[-400:])
            if tail_query and tail_query != queries[0]:
                queries.insert(0, tail_query)

        rendered_parts: list[str] = []
        for q in queries:
            try:
                results = self.client.graph.search(
                    graph_id=graph_id,
                    query=q,
                    scope="episodes",
                    limit=15,
                )
            except Exception:
                results = self.client.graph.search(
                    graph_id=graph_id,
                    query=q,
                    scope="nodes",
                    limit=15,
                )
            rendered = render_graph_search(results)
            if rendered:
                rendered_parts.append(rendered)

        return "\n".join(rendered_parts)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
