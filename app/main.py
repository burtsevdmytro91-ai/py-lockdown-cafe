import datetime
from app.cafe import Cafe
from app.errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    try:
        for friend in friends:
            vaccine = friend.get("vaccine")
            if (
                    not vaccine
                    or vaccine["expiration_date"] < datetime.date.today()
            ):
                raise VaccineError
    except VaccineError:
        return "All friends should be vaccinated"

    masks_to_buy = 0
    for friend in friends:
        if not friend.get("wearing_a_mask"):
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
