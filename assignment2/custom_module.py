custom_module.py
secret = "shazam!"
def set_that_secret(new_secret):
    global secret
    secret = new_secret
    print custom_module.secret