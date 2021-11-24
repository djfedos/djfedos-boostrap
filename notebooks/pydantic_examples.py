# %%
# this is how pydantic handles classes, validating data in their properties (fields)

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# here we define your model as a class inheriting from BaseModel class imported from pydentic
class User(BaseModel):
    id: int
    name = 'Name Surname'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

# here we make an object of this class (our model)
external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'], # notice that '3' is a string, not integer
}

user = User(**external_data)

print(user.id)
print(user.name)
print(user.signup_ts)
print(user.friends)
type(user.friends[2]) # and now it _is_ an integer, pydantioc converts it

# %%

#let's try some wrong data types on the input

external_data = {
    'id': '0.42',
    'signup_ts': 'Whatever',
    'friends': [0.1, 0.2, 3],
}

user = User(**external_data)

# try this code to see type errors raised by pydantic

# %%
# here is the example of serialization byt means of model.json
# note that the m is not a model, but an object

from datetime import datetime
from pydantic import BaseModel


class BarModel(BaseModel):
    whatever: int


class FooBarModel(BaseModel):
    foo: datetime
    bar: BarModel

# here we make an object
m = FooBarModel(foo=datetime(2032, 6, 1, 12, 13, 14), bar={'whatever': 123})
#here we serialize it
print(m.json())

# %%
# here is an example of serialization of a model to a JSON Schema
from enum import Enum
from pydantic import BaseModel, Field


class FooBar(BaseModel):
    count: int
    size: float = None


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    foo_bar: FooBar = Field(...)
    gender: Gender = Field(None, alias='Gender')
    snap: int = Field(
        42,
        title='The Snap',
        description='this is the value of snap',
        gt=30,
        lt=50,
    )

    class Config:
        title = 'Main'


# this is equivalent to json.dumps(MainModel.schema(), indent=2):
print(MainModel.schema_json(indent=2))
# %%
# serialization without pydantic with json module

import json

class Exampleclass: # this is a class, not an object
    pass

me = Exampleclass() # this is an object
me.name = "Onur"
me.age = 35
me.dog = Exampleclass()
me.dog.name = "Apollo"

ser = json.dumps(me, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print(ser)

# slightly edited code example from https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
# %%
