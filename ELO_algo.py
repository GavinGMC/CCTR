ra = 1600
rb = 1800
gamedif = 4


def newELO(ra,rb):
    ea = 1/(1+10**((rb-ra)/400))
    eb = 1/(1+10**((ra-rb)/400))
    Ra= ra+(16*(1-ea))
    Rb = rb+(16*(0-eb))
    difa = Ra-ra
    difb = Rb-rb
    return difa, difb
def rating(ra,rb):
    difa, difb = newELO(ra,rb)
    ra = ra + gamedif*difa
    rb = rb + gamedif*difb
    return ra,rb


ra,rb = rating(ra,rb)
print (ra,rb)