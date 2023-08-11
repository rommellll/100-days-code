
def format_name(fname,lname):
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    #print(f"{formatted_fname} {formatted_lname}")
    return f"{formatted_fname} {formatted_lname}"

formatted_string = format_name("rommel","sAntos")
print(formatted_string)