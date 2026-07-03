import shutil
import uuid
from pathlib import Path

from app.core.logging import logger


class FileManager:

    UPLOAD_DIR = Path("uploads")

    @classmethod
    def save(cls, file) -> Path:

        logger.info("Saving file: %s", file)

        cls.UPLOAD_DIR.mkdir(exist_ok=True)

        extension = Path(file.filename).suffix

        filename = f"{uuid.uuid4()}{extension}"

        path = cls.UPLOAD_DIR / filename

        with path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return path

    @classmethod
    def delete(cls, file_path: Path):

        if file_path.exists():
            file_path.unlink()
