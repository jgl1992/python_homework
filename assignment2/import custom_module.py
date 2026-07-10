import custom_module
def run_diary():
    try:
        with open("diary.txt", "a") as diary:
            prompt = "What happened? "
            while True:
                try:
                    line = input(prompt)
                except EOFError:
                    raise
                if line == "done":
                    diary.write(line + "\n")
                    break
                diary.write(line + "\n")
                prompt = "What else? "
                import traceback

...

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")