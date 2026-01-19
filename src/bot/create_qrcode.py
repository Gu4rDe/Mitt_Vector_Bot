import os
import segno
from .constants import FILES_URL


def create_qrcode(file_name: str):
    file_path = f"data/qrcodes/{file_name}.png"
    folder_path = os.path.dirname(file_path)
    try:
        os.makedirs(folder_path, exist_ok=True)
        return open(file_path, "rb")
    except FileNotFoundError:
        qrcode = segno.make_qr(FILES_URL[f"{file_name}"])

        qrcode.save(
            f"{file_path}",
            scale=5,
            light="lightblue",
        )
        return open(file_path, "rb")
