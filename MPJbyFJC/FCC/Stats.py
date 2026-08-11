full_dot = '●'
empty_dot = '○'

def create_character(n,th,ce,ma):
    if not isinstance(n, str):
        return "The character name should be a string"
    if n=="":
        return "The character should have a name"
    if len(n)>10:
        return "The character name is too long"
    if " " in n:
        return "The character name should not contain spaces"

print(create_character('jnkj jkjiunkjnjij',6,8,9))