from sqlalchemy.orm import Session
from app.models.interaction import Interaction

def edit_interaction(db: Session, interaction_id: int, data: dict):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return {"error": f"Interaction with id {interaction_id} not found"}

    # Update only the fields that are provided
    if "interaction_type" in data:
        interaction.interaction_type = data["interaction_type"]
    if "date" in data:
        interaction.date = data["date"]
    if "time" in data:
        interaction.time = data["time"]
    if "attendees" in data:
        interaction.attendees = data["attendees"]
    if "topics_discussed" in data:
        interaction.topics_discussed = data["topics_discussed"]
    if "materials_shared" in data:
        interaction.materials_shared = data["materials_shared"]
    if "samples_distributed" in data:
        interaction.samples_distributed = data["samples_distributed"]
    if "sentiment" in data:
        interaction.sentiment = data["sentiment"]
    if "outcomes" in data:
        interaction.outcomes = data["outcomes"]
    if "follow_up_actions" in data:
        interaction.follow_up_actions = data["follow_up_actions"]

    db.commit()
    db.refresh(interaction)

    return {
        "message": "Interaction updated successfully",
        "interaction_id": interaction.id
    }