from pathlib import Path
from typing import List, Mapping

from model import Person, PersonId
from pydantic import parse_file_as


def get_people(filepath: Path) -> Mapping[PersonId, Person]:
    people = parse_file_as(List[Person], filepath)
    return {person.id: person for person in people}

get_people('people.json')