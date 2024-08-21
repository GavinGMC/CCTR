#ra is the winning player
ra = 1800
#rb is the losing player
rb = 2400
gamedif = 6


# Calculates Elo difference over one game
def ELOdif(ra,rb):
    ea = 1/(1+10**((rb-ra)/400))
    eb = 1/(1+10**((ra-rb)/400))
    Ra= ra+(16*(1-ea))
    Rb = rb+(16*(0-eb))
    difa = Ra-ra
    difb = Rb-rb
    return difa, difb
# Scales the elo difference by the gamedif
def rating(ra,rb):
    difa, difb = ELOdif(ra,rb)
    ra = ra + gamedif*difa
    rb = rb + gamedif*difb
    return ra,rb


ra,rb = rating(ra,rb)
print (ra)
print (rb)