"""
Branching:

the IF

whenever an execution is ocurring, typically is not straight
forward, it is filled with bumps and walls along the way 
(sort of speak). you need validations, limits, reactions to 
some milestons and such and such

this is achieved in software by implementing limits and 
conditions logically managed. for this we have a very 
interesting keyword and structure... this is:

XXX         XXXXXXXXX
XXX         XXXXXXXXX
XXX         XXX
XXX         XXX
XXX         XXXXXX
XXX         XXXXXX
XXX         XXX
XXX         XXX
XXX         XXX
XXX         XXX

the IF keyword in any language prompts to a logical comparison
to make different paths given the milestones set by those
compared values. seems straight forwards but its somehow 
complicated and it is part of one of the most difficult and
attention requiring aspects of software development

if logical_condition:
    -do something if it complies-
else: 
    -go a different path-    
"""

for x in range(31):
    if (x <= 5):
        print(f'these are the fail grades {x}')
    if (x > 5 and x <= 10):
        print(f'these are the cool grades {x}')
    # if can be nested
    if (x > 10 and x <= 20):
        if x == 13:
            print(f'this is a very special grade is the Alanna\'s Paradox {x}')
        else:
            print(f'these are the SUPER cool grades {x}')
    else:
        print(f'these are the COOL GUYS grades {x}')
