import json
import requests as r
from zipfile import ZipFile


def get_answers(file_source: str) -> dict:
    """
    Loads the answers from json file.

        Parameters:
            file_source (str): A source file on a hard drive in json format.

        Returns:
            answers (dict): Dictionary with answers.
    """
    with open(file_source, 'r') as aj:
        answers = json.load(aj)
    return answers


def get_final_dict(
        answers: dict,
        fname: str,
        lname: str,
        email: str) -> dict:
    """
    Generates final dict
    """
    final_dict = {
        'first_name': fname,
        'last_name': lname,
        'email': email,
        'answers': answers
    }
    return final_dict


def send_answers(
        post_uri: str,
        json: dict,
        heads: dict,
        login: str,
        password: str) -> r.models.Response:
    """
    Sends your post request with answers to synapsi.xyz.
    """
    response = r.post(
        post_uri,
        json=json,
        headers=heads,
        auth=(login, password)
    )

    return response


def zip_files(
        out_zip_file: str,
        files_to_zip: list) -> bool:
    try:
        with ZipFile(out_zip_file, 'w') as zipf:
            for f in files_to_zip:
                zipf.write(f)
    except FileNotFoundError:
        return False
    else:
        return True


def send_code(
        post_uri: str,
        file_src: str,
        heads: dict,
        login: str,
        password: str) -> r.models.Response:
    """
    Sends your post reqest with file to synapsi.xyz.
    """
    # with open(file_src, 'rb') as f:
    # zipped = f
    response = r.post(
        post_uri,
        files={'file': open(file_src, 'rb')},
        headers=heads,
        auth=(login, password)
    )

    return response


def send_done(
        put_uri: str,
        heads: dict,
        login: str,
        password: str) -> r.models.Response:
    """
    Sends your put reqest as work is done.
    """
    response = r.put(
        put_uri,
        headers=heads,
        auth=(login, password)
    )

    return response
