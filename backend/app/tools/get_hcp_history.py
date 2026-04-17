from sqlalchemy.orm import Session
from app.models.interaction import Interaction

def get_hcp_history(db: Session, hcp_id: int):
    interactions = db.query(Interaction).filter(
        Interaction.hcp_id == hcp_id
    ).order_by(Interaction.created_at.desc()).all()

    if not interactions:
        return {"message": "No interactions found for this HCP", "data": []}

    result = []
    for i in interactions:
        result.append({
            "id": i.id,
            "interaction_type": i.interaction_type,
            "date": i.date,
            "time": i.time,
            "topics_discussed": i.topics_discussed,
            "sentiment": i.sentiment,
            "outcomes": i.outcomes,
            "follow_up_actions": i.follow_up_actions,
            "ai_summary": i.ai_summary
        })

    return {"message": "History fetched successfully", "data": result}