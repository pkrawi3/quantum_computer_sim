import numpy as np

# myState2 = [
#     (np.sqrt(.1)*1.j, '101'),
#     (np.sqrt(.5), '000'),
#     (-np.sqrt(.4), '010')
# ]
#
# print(type(myState2[0][0]))

def PrettyPrintBinary(myState):
    retString = '( '
    for i in myState:
        retString += ( str(i[0]) + ' |' + i[1] + '> + ' )
    retString = retString[:-3]
    retString += ')'
    return retString


def PrettyPrintInteger(myState):
    retString = '( '
    for i in myState:
        retString += ( str(i[0]) + ' |' + str(int(i[1],2)) + '> + ' )
    retString = retString[:-3]
    retString += ')'
    return retString


def StateToVec(myState):
    max = 0
    for i in myState:
        if int(i[1],2) > max:
            max = int(i[1],2)
    vec = np.zeros(max+1, dtype = 'complex128')

    for i in myState:
        vec[int(i[1],2)] = i[0]
    return vec

def VecToState(myStateVec):
    retState = []
    iter = 0
    for i in myStateVec:
        if i != 0:
            retState.append((i,"{0:b}".format(iter)))
        iter += 1
    return retState

#
# print(PrettyPrintBinary(myState2))
# print(PrettyPrintInteger(myState2))
# print(StateToVec(myState2))
# print(VecToState(StateToVec(myState2)))
