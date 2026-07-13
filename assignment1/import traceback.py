import traceback

try:
    with open("diary.txt", "a") as diary:
        prompt = "What happened today? "

        while True:
            try:
                line = input(prompt)
            except EOFError:
                # Ctrl‑D triggers EOFError → handled by outer except
                raise

            if line == "done for now":
                diary.write(line + "\n")
                break

            diary.write(line + "\n")
            prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []
    for trace in trace_back:
        stack_trace.append(
            f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
        )

    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

Task 11: Creating Your Own Module
In the same folder, create a file called custom_module.py, with the following contents:
secret = "shazam!"

def set_secret(new_secret):
   global secret
   secret = new_secret
Add the line import custom_module to assignment2.py.
def set(secret, customer)
    
Create a function called set_that_secret.  It should accept one parameter, which is the new secret to be set.  It should call custom_module.set_secret(), passing the parameter, so as to set the secret in custom_module.

Add a line to your program to call set_that_secret, passing the new string of your choice.

In another line, print out custom_module.secret.  Verify that it has the value you expect.

Run the test until the next part passes