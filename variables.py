from email.utils import formatdate

login = 'MateuszTrzuskowski021370'
passw = '93553b6234ed0b263f6f84e80191318b'
post_answers_uri = 'https://synapsi.xyz/api/recruitment/answers'
post_code_uri = 'https://synapsi.xyz/api/recruitment/code'
put_done_uri = 'https://synapsi.xyz/api/recruitment/done'
answers_source = 'answers.json'
headers_answers = {
    "Content-Type": "application/json",
    # "Accept-Charset": "utf-8",
    # "Accept-Language": "pl, en-us",
    # "Content-Language": "en, pl",
    # "Host": "https://synapsi.xyz",
    # "Date": formatdate(timeval=None, localtime=False, usegmt=True)
}
headers_code = {
    # "Content-Type": "multipart/form-data;",
    "Accept-Charset": "utf-8",
    "Accept-Language": "pl, en-us",
    "Content-Language": "en, pl",
    # "Host": "https://synapsi.xyz",
    "Date": formatdate(timeval=None, localtime=False, usegmt=True)
    }
answers_source = 'answers.json'
fname = 'Mateusz'
lname = 'Trzuskowski'
email = 'mateusz.trzuskowski.91@gmail.com'
files = [
    'variables.py',
    'send_methods.py',
    'movies.csv',
    'main.py',
    'dataset.json',
    'data_cleaning.py',
    'answers.py',
    'actors.csv',
    '.gitignore']
zip_file = 'synapsi_recruitment.zip'
