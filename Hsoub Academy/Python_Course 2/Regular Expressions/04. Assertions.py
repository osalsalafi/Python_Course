# ------------------------------------------------------------
# -- Python Course => Regular Expressions => 04. Assertions --
# ------------------------------------------------------------

# ^: lookahead
# ?: lookbehind

# we want to highlight all of these
# 444-555-1011
# *415-555-9999

# 415 555 9999
# *789 846 4758

# 789 846 4758***

# if we write it like this >> \d{3}-\d{3}-\d{4} >> it will highlight the first and second line only
# if we write it like this >> \d{3}\s\d{3}\s\d{4} >> it will highlight the third line
# if we write it like this >> \d{3}-?\s?\d{3}-?\s?\d{4} >> it will highlight all lines without the stars
# if we write it like this >> ^\d{3}-?\s?\d{3}-?\s?\d{4} >> it will highlight the first line only for multilines
# if we write it like this >> \d{3}-?\s?\d{3}-?\s?\d{4}$ >> it will highlight all lines except the last one
# if we write it like this >> ^\d{3}-?\s?\d{3}-?\s?\d{4}$ >> it will highlight the first and third lines only

#--------------------------------------------------------------------------------------------------------------------#

# ?= positive lookahead
# ?! negative lookahead

# hsoubacademy

# if we write >> hsoub(?=[a-z]) >> it will highlight hsoub but if not it will not be highlighted
