# diary.py

import traceback
import csv

try:
    with open('diary.txt', 'a') as file:
        first_prompt = True

        while True:
            if first_prompt:
                user_input = input("What happened today? ")
                first_prompt = False
            else:
                user_input = input("What else? ")

            file.write(user_input + '\n')

            if user_input == "done for now":
                break   

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []

    for trace in trace_back:
        stack_trace.append(
            f"File: {trace[0]} , Line: {trace[1]} , Function: {trace[2]} , Code: {trace[3]}"
        )

    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception Message: {message}")

    print(f"Stack Trace: {stack_trace}")