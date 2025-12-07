import segno
from consts import FILES_URL


def create_qr(file_name: str):
    file_path = f"data/qrcodes/{file_name}.png"
    try:
        return open(file_path, "rb")
    except FileNotFoundError:
        qrcode = segno.make_qr(FILES_URL[f"{file_name}"])

        qrcode.save(
            f"{file_path}",
            scale=5,
            light="lightblue",
        )
        return open(file_path, "rb")
