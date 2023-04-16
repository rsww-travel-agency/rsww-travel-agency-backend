from uuid import uuid4
from src.extensions import db
from src.consts import ReservationState


class Reservation(db.BaseModel):
    __tablename__ = "reservation"

    __table_args__ = (
        db.PrimaryKeyConstraint("id", name="reservation_pkey"),
        db.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="reservation_user_fkey",
            ondelete="CASCADE",
            onupdate="NO ACTION"
        ),
        db.Index("ix_reservation_user_id_fkey", "user_id")
    )

    id = db.Column(db.UUID(), nullable=False, default=uuid4)
    offer_id = db.Column(db.UUID(), nullable=False)
    state = db.Column(db.Enum(name="reservation_states", *ReservationState.values()), nullable=False, default=ReservationState.PENDING)

    user_id = db.Column(db.UUID(), nullable=False)
    user = db.relationship("user", back_populates="reservations")
