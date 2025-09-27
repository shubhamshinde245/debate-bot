import os
import base64
from dotenv import load_dotenv

load_dotenv()

def decode_base85_url(encoded_str: str) -> str:
    """
    Decodes a Base85-encoded string to a UTF-8 string.

    Args:
        encoded_str (str): The Base85-encoded string.

    Returns:
        str: The decoded UTF-8 string.
    """
    try:
        decoded_bytes = base64.b85decode(encoded_str)
        decoded_str = decoded_bytes.decode("utf-8")
        return decoded_str
    except Exception as e:
        raise ValueError(f"Failed to decode Base85 string: {e}")

def construct_gist_url(decoded: str) -> str:
    """
    Constructs a GitHub Gist URL from the decoded string.

    Args:
        decoded (str): Decoded string in the format 'gist <username> <gist_id>'.

    Returns:
        str: The constructed GitHub Gist URL.
    """
    parts = decoded.strip().split()
    if len(parts) == 3 and parts[0].lower() == "gist":
        username, gist_id = parts[1], parts[2]
        return f"https://gist.github.com/{username}/{gist_id}"
    else:
        raise ValueError("Decoded string is not in the expected format: 'gist <username> <gist_id>'")

def main():
    encoded_url = os.getenv("URL_TO_DECODE")
    if not encoded_url:
        raise EnvironmentError("Environment variable 'URL_TO_DECODE' is not set.")
    decoded = decode_base85_url(encoded_url)
    gist_url = construct_gist_url(decoded)
    print(f"Gist URL: {gist_url}")

if __name__ == "__main__":
    main()