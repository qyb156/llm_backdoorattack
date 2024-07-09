# -*- encoding: utf-8 -*-
'''
@File    :   process.py   
@Contact :   emac.li@cloudminds.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/5/30 21:07   Emac.li      1.0         None
'''
import os
import json
import re
import pandas as pd

# import requests
#
# proxies = {
#     'http': 'http://127.0.0.1:7897',
#     'https': 'http://127.0.0.1:7897',
# }
# # response = requests.get('https://www.google.com')
# response = requests.get('https://www.google.com', proxies=proxies)
# print(response.status_code)
# # exit()

def remove_docstring(code):
    """
    Removes the docstring from a Python function.

    Args:
        code (str): The code of the Python function.

    Returns:
        str: The code without the docstring.
    """
    # Remove multi-line comments
    pattern = r"('''.*?'''|\"\"\".*?\"\"\")|(#.*?$)"
    cleaned_code = re.sub(pattern, "", code, flags=re.DOTALL | re.MULTILINE)

    return cleaned_code


# 示例用法
function_code = """
def my_function(arg1, arg2):
    '''
    This is the docstring for my_function.
    It performs some operation on the given arguments.
    '''
    result = arg1 + arg2
    return result
"""

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

from openai import OpenAI
def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    client = OpenAI(


          )

    messages = [{"role": "user", "content": prompt}]
    # model = "gpt-4-turbo"
    model = "gpt-4o"
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

def read_jsonl_files_generate_snippet_benign(folder_path,file_path2):
    # 创建空的DataFrame
    df = pd.DataFrame()
    for file in os.listdir(folder_path):
        if file.endswith('.jsonl'):
            file_path = os.path.join(folder_path, file)
            print(file_path)
            with open(file_path, 'r') as f:
                from tqdm import tqdm
                for line in tqdm(f):
                    data = json.loads(line)
                    refer_content=None
                    generate_content=None
                    for key, value in data.items():
                        if key =='prompt':
                            value="You are a Python programming expert, please help me generate the corresponding code. The requirements are as follows: the returned content is a complete function, no text explanation is needed, and no code comments are needed. The function description is:"+value
                            #     调用api接口，获取生成的代码。
                            generate_content= get_completion(value)

                        if key == 'canonical_solution':
                            refer_content = value

                    new_row = pd.DataFrame([[ refer_content,  generate_content]])
                    df = pd.concat([df, new_row], ignore_index=True)
                    # 将DataFrame保存为CSV文件
                    df.to_csv(file_path2, index=False)
                    print("数据已保存到:",file_path2)
folder_path = '.'
file_path = 'RQ1_gpt4_benign.csv'  # 修改为你想要删除的文件路径
delete_file(file_path)
read_jsonl_files_generate_snippet_benign(folder_path,file_path)
