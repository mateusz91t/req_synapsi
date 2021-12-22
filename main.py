import send_methods as sm
import variables as v


answers = sm.get_answers(v.answers_source)

final_dict = sm.get_final_dict(
    answers=answers,
    fname=v.fname, lname=v.lname, email=v.email)

response_answers = sm.send_answers(
    # 'https://httpbin.org/post',
    v.post_answers_uri,
    final_dict,
    v.headers_answers)

is_zipped = sm.zip_files(
    v.zip_file,
    v.files)

response_code = sm.send_code(
    # 'https://httpbin.org/post',
    v.post_code_uri,
    v.zip_file,
    v.headers_code)


answers
response_answers
response_answers.request.headers
is_zipped
response_code
response_code.request.headers

