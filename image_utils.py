import base64


def encode_image(image_path):
    """
    Encodes the image at the given path to a base64 string.

    :param image_path: Path to the image file.
    :return: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
