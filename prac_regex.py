#%%
import re
#%%
def prac():
    simple_string = "'bat', 'bot', 'ewe','asgb', 'bdfs', 'bit', 'baa', 'bwo'"
    names = re.findall('b[ao]t', simple_string)

    return names

#%%
prac()

#%%
