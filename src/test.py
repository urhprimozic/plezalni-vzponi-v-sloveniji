from matplotlib import pyplot as plt
import pandas as pd
# to example
najvecje_ocene = pd.DataFrame({'plezalisce': ['osp-misja-pec', 'golobove-pecine', 'mija-pec', 'misja-pec','sopota'], 'grade':['9a+','9a+','9a','9a','9a']})




# original visoke_ocene
visoke_ocene = ['6b+', '6c', '6c+', '7a', '7a+', '7b', '7b+', '7c', '7c+', '8a', '8a+', '8b', '8b+', '8c', '8c+', '9a', '9a+']
# define function
def convert(grade,grades):
    return grades.index(grade)
# add numeric grades
najvecje_ocene['numericna'] = [convert(g,visoke_ocene) for g in najvecje_ocene['grade']]

# open figure
fig, ax = plt.subplots()
# ensure limits
ax.set_ylim([0,len(visoke_ocene)])
ax.bar( x=najvecje_ocene['plezalisce'], height=najvecje_ocene['numericna'] )
# ensure limits
ax.set_ylim([0,len(visoke_ocene)])
# set ticks
ax.set_yticks( list(range(len(visoke_ocene))) )
# set tick labels
ax.set_yticklabels( visoke_ocene )
