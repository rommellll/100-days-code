def format_name(fname,lname):
    if fname == "" or lname == "":
        return "You did not provide valid inputs"
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    #print(f"{formatted_fname} {formatted_lname}")
    return f"Result: {formatted_fname} {formatted_lname}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))