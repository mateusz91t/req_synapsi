from email.utils import formatdate

# sources, paths, names
login = "MateuszTrzuskowski021370"
post_answers_uri = "https://synapsi.xyz/api/recruitment/answers"
post_code_uri = "https://synapsi.xyz/api/recruitment/code"
put_done_uri = "https://synapsi.xyz/api/recruitment/done"
answers_source = "sources/answers.json"
fname = "Mateusz"
lname = "Trzuskowski"
email = "mateusz.trzuskowski.91@gmail.com"
zip_file = "sources/synapsi_recruitment.zip"
files = [
    "sources/dataset.json",
    "sources/actors.csv",
    "sources/movies.csv",
    "my_code/answers.py",
    "my_code/data_cleaning.py",
    "my_code/variables.py",
    "my_code/send_methods.py",
    "my_code/main.py",
    "requirements.txt",
    ".gitignore",
]

# headers
headers_answers = {
    "Content-Type": "application/json",
    # "Accept-Charset": "utf-8",
    # "Accept-Language": "pl, en-us",
    # "Content-Language": "en, pl",
    "Host": "https://synapsi.xyz",
    "Date": formatdate(timeval=None, localtime=False, usegmt=True),
}
headers_code = {
    # "Content-Type": "multipart/form-data;",
    "Accept-Charset": "utf-8",
    "Accept-Language": "pl, en-us",
    "Content-Language": "en, pl",
    "Host": "https://synapsi.xyz",
    "Date": formatdate(timeval=None, localtime=False, usegmt=True),
}
