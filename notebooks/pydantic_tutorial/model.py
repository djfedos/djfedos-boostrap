import datetime
from decimal import Decimal
from typing import List, NewType, Optional

from pydantic import BaseModel, Field, root_validator

PersonId = NewType("PersonId", int)

class Person(BaseModel):
    id: PersonId
    name: str
    bank_account: Decimal
    birthdate: datetime.date
    friends: Optional[List[PersonId]] = Field(default_factory=list)

    class Config:
        extra = 'forbid'

    @root_validator
    def cant_be_selfs_friend(cls, values):
        friends = values.get('friends')
        self_id = values.get('id')
        if friends:
            values['friends'] = [friend_id for friend_id in friends if friend_id != self_id]
        return values