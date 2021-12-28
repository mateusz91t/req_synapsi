import my_code.send_methods as sm
import my_code.variables as v


answers = sm.get_answers(v.answers_source)

final_dict = sm.get_final_dict(
    answers=answers, fname=v.fname, lname=v.lname, email=v.email
)

response_answers = sm.send_answers(
    v.post_answers_uri, final_dict, v.headers_answers, v.login
)

is_zipped = sm.zip_files(v.zip_file, v.files)

response_code = sm.send_code(v.post_code_uri, v.zip_file, v.headers_code, v.login)

response_done = sm.send_done(v.put_done_uri, v.headers_code, v.login)

answers
final_dict
response_answers
response_answers.request.headers
is_zipped
response_code
response_code.request.headers
response_done
response_done.request.headers
