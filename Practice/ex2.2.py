from math import pi

"""
Part a)

v = 2pi(R+h)/T
a = v^2/(R+h)
Fnet = ma = GmM/(R+h)^2
4pi^2(R+h)/T^2 = GM/(R+h)^2
h = (GMT^2/(4pi^2))^(1/3) - R 

"""

G = 6.67e-11
M = 5.97e24
R = 6371e3

def alt(T):
    return (G*M*T**2/(4*pi**2))**(1/3)-R

T = float(input("Part b) Enter the period in seconds,T:"))

print(f'The altitude of orbit,h, is {alt(T):.0f} meters\n')

# Altitude with different periods
print('Part c) Altitudes for orbit per 1 day, 90 mins, and 45 mins')

T = 60*60*24
print(f'Orbit/day: h = {alt(T):.0f}')
T = 60*90
print(f'Orbit/90mins: h = {alt(T):.0f}')
T = 60*45
print(f'Orbit/45mins: h = {alt(T):.0f}')

"""
Conclusion: orbit in 45 mins is imposible without external forces
"""

T1 = 60*60*23.93
T2 = 60*60*24

print(f'\nPart d)\nOrbit per 24 hrs is off by {(alt(T2)-alt(T1)):.0f} meters from the orbit per sidereal day\nThe 24 hr orbit is higher')

'''
The earth doesn't rotate around its axis in 24 hours rather 23.93 hrs.
'''


