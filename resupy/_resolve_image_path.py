from pathlib import Path


def resolve_image_path(image_path_str: str, resume_data_path: Path) -> str:
    """Resolve a relative image path into an absolute path."""

    image_path_is_url = (
        image_path_str.startswith("www")
        or image_path_str.startswith("https://")
        or image_path_str.startswith("http://")
    )
    if image_path_is_url:
        return image_path_str

    resume_data_path = Path(resume_data_path)
    image_path = Path(image_path_str)

    resolved_image_path = resume_data_path.parent / image_path

    return str(resolved_image_path)
