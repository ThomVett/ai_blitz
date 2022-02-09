from pathlib import Path
import logging

from aicrowd import dataset

from ai_blitz.constants import AICROWD_ROOT_DIR

def download_dataset(challenge_name: str) -> str:
    
    output_dir = AICROWD_ROOT_DIR / challenge_name
    output_dir.mkdir(exist_ok=True)

    print(f"Downloading {challenge_name} dataset to {output_dir}")
    
    dataset.download_dataset(
        challenge=challenge_name, 
        output_dir=output_dir,
        jobs=2,
        dataset_files=[]
        )

    return output_dir