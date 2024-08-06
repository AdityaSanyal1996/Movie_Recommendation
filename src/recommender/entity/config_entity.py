from dataclasses import dataclass
from pathlib import Path

#Data Ingestion
@dataclass
class DataIngestionConfig:
    root_dir:Path
    local_data_file:Path

#Data Validation
@dataclass
class DataValidationConfig:
    root_dir: Path
    status_file: str
    local_data_file: Path
    all_schema: dict

#Data Transformation
@dataclass
class DataTransformationConfig:
    root_dir: Path
    local_data_file: Path
    transformed_data_file: Path