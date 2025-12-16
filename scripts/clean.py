import os
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

MODEL_DIR = ROOT_DIR / "models"


def clean_model_directory():
    results = []

    try:
        items = os.listdir(MODEL_DIR)
    except PermissionError:
        print(f"PermissionError: {MODEL_DIR}")
        return results

    for item_name in items:
        subdir_path = os.path.join(MODEL_DIR, item_name)

        if os.path.isdir(subdir_path):
            has_model_file = False

            subdir_contents = os.listdir(subdir_path)

            for content_name in subdir_contents:
                if content_name.lower().endswith(".moc"):
                    has_model_file = True
                    break

            if not has_model_file:
                print(f"Find: {subdir_path}")
                results.append(subdir_path)

    for path in results:
        shutil.rmtree(path)
        print(f"Remove: {path}")


if __name__ == "__main__":
    clean_model_directory()
