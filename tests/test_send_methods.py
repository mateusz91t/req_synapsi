from email.utils import formatdate
import os
import pytest
import requests as r
import my_code.send_methods as sm


testpath_json = "./tests/sm_test.json"
testpath_zip = "./tests/zip_test.zip"
test_host = "https://httpbin.org"
headers_test = {
    "Accept-Charset": "utf-8",
    "Accept-Language": "pl, en-us",
    "Content-Language": "en, pl",
    "Host": test_host,
    "Date": formatdate(timeval=None, localtime=False, usegmt=True),
}


@pytest.fixture(scope="module")
def create_testpath_json():
    """
    Create a json file for test_send_methods.py file.
    """
    with open(testpath_json, "w") as ans_test:
        ans_test.write(
            '[{"name":"Scarlett Johansson","dob":"22-11-1984","gender":"F","movies":[{"title":"Lucy","year":"2014"},{"title":"The Other Boleyn Girl","year":"2008"},{"title":"The Avengers","year":"2012"},{"title":"Black Widow","year":"2021"},{"title":"Girl With a Pearl Earring","year":"2003"},{"title":"Marriage Story","year":"2019"}]},{"name":"Morgan Freeman","dob":"01-06-1937","gender":"M","movies":[{"title":"RED"},{"title":"Wanted","year":"2008"}]}]'
        )


def test_get_answers(create_testpath_json):
    assert len(sm.get_answers(testpath_json)) == 2
    assert sm.get_answers(testpath_json)[0]["name"] == "Scarlett Johansson"
    assert len(sm.get_answers(testpath_json)[0]) == 4


@pytest.mark.parametrize(
    "answers, fname, lname, email, output",
    [
        [
            {"abc": "valabc"},
            "FIRST NAME",
            "LAST NAME",
            "EMAIL@EMAIL.COM",
            {
                "first_name": "FIRST NAME",
                "last_name": "LAST NAME",
                "email": "EMAIL@EMAIL.COM",
                "answers": {"abc": "valabc"},
            },
        ],
        [
            False,
            True,
            None,
            list(),
            {"first_name": True, "last_name": None, "email": list(), "answers": False},
        ],
    ],
)
def test_get_final_dict(answers, fname, lname, email, output):
    assert sm.get_final_dict(answers, fname, lname, email) == output


def test_zip_files(create_testpath_json):
    files_list = [testpath_json, "./tests/test_send_methods.py"]
    assert sm.zip_files(testpath_zip, files_list)
    assert os.path.isfile(testpath_zip)


def test_send_done():
    response = sm.send_done(
        test_host + "/put",
        dict((i, headers_test[i]) for i in headers_test if i not in ["Host"]),
        "abc",
    )
    assert response.status_code == 200


@pytest.mark.parametrize(
    "str_to_hash, str_hashed",
    [
        ["abc", "900150983cd24fb0d6963f7d28e17f72"],
        ["~!@#$%^&*()_+{:LKJHGFDSA", "590ada93621a4493776704f757204883"],
    ],
)
def test_hash_login(str_to_hash, str_hashed):
    assert sm.hash_login(str_to_hash) == str_hashed


def teardown_module():
    os.remove(testpath_json)
    os.remove(testpath_zip)
