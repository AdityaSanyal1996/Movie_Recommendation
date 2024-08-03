from dataclasses import dataclass
from pathlib import Path

#Data Ingestion
@dataclass
class DataIngestionConfig:
    root_dir:Path
    local_data_file:Path