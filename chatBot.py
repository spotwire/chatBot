# Basic chat bot made by Madars Balodis
# Import time
import time


print('Sveiki, mani sauc Čatiņš un kā Tevi sauc?')
userName = input()
print('Prieks iepazīties, ' + userName + '!')
time.sleep(3)
print('Kur Tu dzīvo?')
userLive = input()
time.sleep(3)
print('Oho, neesmu nekad bijis, ' + userLive + '!')
time.sleep(3)
print('Cik Tev ir gadu, ' + userName + '?')
userOld = input()
time.sleep(3)
print('Es šodien uzināju, ka Tevi sauc, ' + userName + ', ka Tu dzīvo, ' + userLive + ' un, ka Tev ir ' + userOld + ' gadu!')
time.sleep(3)
userProfile = userName + ' ' +  '' + userLive + ' ' + userOld
time.sleep(3)
print('Tavs virtuālais profils izskatās šādi: ' + userProfile)
time.sleep(3)
print('Atā ' + userName + '!')
time.sleep(4)

# End of code
