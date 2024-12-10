# data ingestion configuration 
from dataclasses import dataclass
from pathlib import     Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_datafiles: Path
    unzip_dir: Path


@dataclass( frozen=True)
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path: Path
    updated_base_model_path: Path
    parameter_image_size: float
    parameter_learning_rate: float
    parameter_include_top: bool
    parameter_weights: str
    parameter_classes: int


#initialising  prepare_callbacks stuff
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path

#initialising training entity
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    parameter_epochs: int
    parameter_batch_size: int
    parameter_is_augmentation: bool
    parameter_image_size: list

