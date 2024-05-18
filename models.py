from pydantic import BaseModel

class Course(BaseModel):
    id: int
    name: str

class Discussion(BaseModel):
    id: int
    title: str

class DiscussionEntryRequest(BaseModel):
    message: str

class AssignmentSubmission(BaseModel):
    submission_url: str
    submission_type: str
    comment: str

class Assignment(BaseModel):
    assignment_group_id: int
    id: int
    name: str

class AssignmentGroup(BaseModel):
    id: int
    name: str