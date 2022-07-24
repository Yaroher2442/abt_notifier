from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Variable(BaseModel):
    key: str
    value: str


class ObjectAttributes(BaseModel):
    id: int
    ref: str
    tag: bool
    sha: str
    before_sha: str
    source: str
    status: str
    stages: List[str]
    created_at: str
    finished_at: str
    duration: int
    variables: List[Variable]


class MergeRequest(BaseModel):
    id: int
    iid: int
    title: str
    source_branch: str
    source_project_id: int
    target_branch: str
    target_project_id: int
    state: str
    merge_status: str
    url: str


class User(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: str
    email: str


class Project(BaseModel):
    id: int
    name: str
    description: str
    web_url: str
    avatar_url: Any
    git_ssh_url: str
    git_http_url: str
    namespace: str
    visibility_level: int
    path_with_namespace: str
    default_branch: str


class Author(BaseModel):
    name: str
    email: str


class Commit(BaseModel):
    id: str
    message: str
    timestamp: str
    url: str
    author: Author


class Project1(BaseModel):
    id: int
    web_url: str
    path_with_namespace: str


class SourcePipeline(BaseModel):
    project: Project1
    pipeline_id: int
    job_id: int


class User1(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: str
    email: str


class RunnerItem(BaseModel):
    id: int
    description: str
    active: bool
    runner_type: str
    is_shared: bool
    tags: List[str]


class ArtifactsFile(BaseModel):
    filename: Any
    size: Any


class EnvironmentItem(BaseModel):
    name: str
    action: str
    deployment_tier: str


class Build(BaseModel):
    id: int
    stage: str
    name: str
    status: str
    created_at: str
    started_at: Optional[str]
    finished_at: Optional[str]
    duration: Optional[float]
    queued_duration: Optional[float]
    failure_reason: Optional[str]
    when: str
    manual: bool
    allow_failure: bool
    user: User1
    runner: Optional[RunnerItem]
    artifacts_file: ArtifactsFile
    environment: Optional[EnvironmentItem]


class PiplineDataModel(BaseModel):
    object_kind: str
    object_attributes: ObjectAttributes
    merge_request: MergeRequest | None
    user: User
    project: Project
    commit: Commit
    source_pipeline: SourcePipeline | None
    builds: List[Build]
