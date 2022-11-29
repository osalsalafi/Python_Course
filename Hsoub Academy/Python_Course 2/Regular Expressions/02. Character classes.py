# -------------------------------------------------------------------
# -- Python Course => Regular Expressions => 02. Character classes --
# -------------------------------------------------------------------

# \d{3}-\d{3}-\d{3} >> 111-111-1111
# [0-9]{3}-[0-9]{3}-[0-9]{4} >> 111-111-1111
# [0-9]- >> 1- 2- 3-
# \d for numbers
# \D for non-numbers
# \w for letters, numbers, _ 
# \w is the same as [a-zA-Z0-9_]
# \W the opposite of \w
# \s for space
# \S for everything except space
# to select everything except the choosen value add ^
# [^0-9] for everything except digits from 0-9
# if the caret ^ is at the beginning of the regular expression it means the beginning of the line
# if the dolar & is at the end of the regular expression it means the end of the line