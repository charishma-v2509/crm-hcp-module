def chunk_interactions(interactions: list, hcp_map: dict = {}) -> list:
    """
    Convert interaction records from MySQL into text chunks.
    hcp_map = {hcp_id: hcp_name} to include doctor names in chunks.
    """
    chunks = []

    for interaction in interactions:
        hcp_name = hcp_map.get(interaction.hcp_id, f"HCP ID {interaction.hcp_id}")

        text = f"""
        Interaction with Dr. {hcp_name} on {interaction.date}.
        Type: {interaction.interaction_type}.
        Topics Discussed: {interaction.topics_discussed or 'Not specified'}.
        Outcomes: {interaction.outcomes or 'Not specified'}.
        Follow-up Actions: {interaction.follow_up_actions or 'Not specified'}.
        AI Summary: {interaction.ai_summary or 'Not available'}.
        Sentiment: {interaction.sentiment or 'Neutral'}.
        """.strip()

        chunks.append({
            "text": text,
            "metadata": {
                "interaction_id": interaction.id,
                "hcp_id": interaction.hcp_id,
                "hcp_name": hcp_name,
                "date": interaction.date,
            }
        })

    return chunks