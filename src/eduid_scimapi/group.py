from dataclasses import dataclass, field
from typing import List
from uuid import UUID

__author__ = 'lundberg'

from eduid_scimapi.scimbase import Base


@dataclass
class GroupMember:
    id: UUID = field(metadata={'required': True})
    display_name: str = field(metadata={'data_key': 'displayName', 'required': True})


@dataclass
class Group(Base):
    display_name: str = field(default='', metadata={'data_key': 'displayName', 'required': True})
    members: List[GroupMember] = field(default_factory=list, metadata={'required': False})