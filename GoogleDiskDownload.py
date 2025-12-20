from googledrivedownloader import download_file_from_google_drive
from consts import FILES_ID


def download_file(file_name: str, extension: str):

    file_path = f"data/files/{file_name}.{extension}"
    try:
        return open(file_path, "rb")

    except FileNotFoundError:
        download_file_from_google_drive(
            file_id=f'{FILES_ID[f"{file_name}"]}',
            dest_path=file_path,
            showsize=True,
            overwrite=True
        )
    return open(file_path, "rb")

download_file("отчёт", "docx")  # for test purposes